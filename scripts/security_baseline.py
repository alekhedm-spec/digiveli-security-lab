#!/usr/bin/env python3
"""DigiVeli Security Lab: dependency-free, read-only repository hygiene checks.

This is NOT a comprehensive secret scanner or code security audit.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    '.github/workflows/security-baseline.yml',
    'scripts/security_baseline.py',
    'README.md',
    'SECURITY.md',
    'CONTRIBUTING.md',
    'docs/SCOPE_AND_AUTHORIZATION.md',
    'research/ai-harness-boundaries/PLAN.md',
}
TEXT_SUFFIXES = {'.md', '.py', '.yml', '.yaml', '.json', '.sh', '.toml', '.txt'}
FORBIDDEN_NAMES = {'id_rsa', 'id_ed25519', 'credentials.json', 'secrets.json', '.env'}
FORBIDDEN_SUFFIXES = {'.pem', '.p12', '.pfx', '.key'}
MAX_ERRORS = 30


def main() -> int:
    try:
        output = subprocess.check_output(
            ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
            cwd=ROOT,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f'FAIL: cannot enumerate repository files: {exc}', file=sys.stderr)
        return 2

    names = sorted(set(os.fsdecode(p) for p in output.split(b'\0') if p))
    failures: list[str] = []
    missing = sorted(REQUIRED - set(names))
    for name in missing:
        failures.append(f'MISSING_REQUIRED_FILE: {name}')

    for name in names:
        path = ROOT / name
        components = Path(name).parts
        if (any(p in {'private', 'secrets', 'credentials'} for p in components)
                or path.name in FORBIDDEN_NAMES
                or (path.name.startswith('.env.') and path.name != '.env.example')
                or path.suffix.lower() in FORBIDDEN_SUFFIXES):
            failures.append(f'RESTRICTED_PATH: {name}')
            continue
        if path.is_symlink():
            failures.append(f'SYMLINK_NOT_ALLOWED: {name}')
            continue
        if not path.is_file():
            failures.append(f'MISSING_LOCAL_FILE: {name}')
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name != '.gitignore':
            continue
        try:
            raw = path.read_bytes()
            data = raw.decode('utf-8')
        except UnicodeDecodeError:
            failures.append(f'INVALID_UTF8: {name}')
            continue
        if not raw.endswith(b'\n'):
            failures.append(f'MISSING_FINAL_NEWLINE: {name}')
        if b'\r' in raw:
            failures.append(f'CRLF_OR_CR: {name}')
        for number, line in enumerate(data.splitlines(), 1):
            if line.endswith((' ', '\t')):
                failures.append(f'TRAILING_WHITESPACE: {name}:{number}')
            if line.startswith(('<<<<<<< ', '>>>>>>> ')) or line == '=======':
                failures.append(f'MERGE_CONFLICT_MARKER: {name}:{number}')
            if len(failures) >= MAX_ERRORS:
                break
        if len(failures) >= MAX_ERRORS:
            break

    print(f'CHECKED_PATHS={len(names)}')
    print(f'FINDINGS={len(failures)}')
    for failure in failures:
        print(f'REVIEW_REQUIRED: {failure}')
    print(f'SECURITY_BASELINE={"FAIL" if failures else "PASS"}')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
