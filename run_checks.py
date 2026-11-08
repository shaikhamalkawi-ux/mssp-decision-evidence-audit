"""Execute source-free checks with a single command; outputs are diagnostic."""
import subprocess, sys, pathlib
root=pathlib.Path(__file__).resolve().parent
cmds=[
 [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
 [sys.executable, 'code/verify_anonymized.py'],
 [sys.executable, 'code/check_casebook_v8.py'],
 [sys.executable, 'code/claim_gate_demo.py'],
]
for c in cmds:
 print('$',' '.join(c),flush=True)
 p=subprocess.run(c,cwd=root,check=False)
 if p.returncode: sys.exit(p.returncode)
print('PASS: source-free reproducibility checks; not raw-workbook or field validation.')
