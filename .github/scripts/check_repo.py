"""Fast repository checks run by CI before executing the notebook.

1. Every notebook is a valid nbformat 4 file (catches .ipynb files broken by a bad merge).
2. No git conflict markers are left in tracked text files.
3. No en dashes, em dashes, middle dots or minus signs in tracked text files (group writing rule).

Usage: python .github/scripts/check_repo.py
"""
import re
import subprocess
import sys

import nbformat

sys.stdout.reconfigure(encoding='utf-8')  # the Windows console is not UTF-8 by default

TEXT_EXT = ('.ipynb', '.md', '.txt', '.py', '.yml', '.yaml')
# Built with chr() so this file does not contain the characters it looks for
FORBIDDEN = {chr(0x2013): 'travessão (en dash)', chr(0x2014): 'travessão (em dash)',
             chr(0x00B7): 'ponto central', chr(0x2212): 'sinal de menos'}
CONFLICT = re.compile(r'^(<{7}|={7}|>{7})( |$)', re.M)

files = [f for f in subprocess.run(['git', 'ls-files'], capture_output=True, text=True,
                                   check=True).stdout.splitlines() if f.endswith(TEXT_EXT)]
errors = []

for path in files:
    text = open(path, encoding='utf-8').read()
    if path.endswith('.ipynb'):
        try:
            nbformat.validate(nbformat.reads(text, as_version=4))
        except Exception as exc:  # invalid JSON or schema
            errors.append(f'{path}: notebook inválido ({type(exc).__name__}: {str(exc)[:200]})')
    for m in CONFLICT.finditer(text):
        line = text.count('\n', 0, m.start()) + 1
        errors.append(f'{path}:{line}: marcador de conflito de merge')
    for lineno, line in enumerate(text.splitlines(), 1):
        for ch, name in FORBIDDEN.items():
            if ch in line:
                col = line.index(ch)
                errors.append(f'{path}:{lineno}: {name}: ...{line[max(0, col - 40):col + 20]}...')

print(f'{len(files)} ficheiros verificados')
if errors:
    print(f'{len(errors)} problema(s):')
    print('\n'.join(errors))
    sys.exit(1)
print('Sem problemas')
