import subprocess
import sys
import json
import time
from pathlib import Path

HERE = Path(__file__).parent
DETECTORS = [
    'detector_sql_injection.py',
    'detector_xss.py',
    'detector_auth_fraca.py',
    'detector_config_insegura.py',
]

report = {
    'generated_at': time.strftime('%Y-%m-%dT%H:%M:%S'),
    'results': []
}

for d in DETECTORS:
    path = HERE / d
    entry = {'name': d, 'path': str(path), 'started_at': time.strftime('%Y-%m-%dT%H:%M:%S'), 'duration': None, 'returncode': None, 'stdout': None, 'stderr': None}
    start = time.time()
    try:
        proc = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=15)
        entry['returncode'] = proc.returncode
        entry['stdout'] = proc.stdout.strip()
        entry['stderr'] = proc.stderr.strip()
    except subprocess.TimeoutExpired as e:
        entry['returncode'] = -1
        entry['stdout'] = ''
        entry['stderr'] = f'Timeout after {e.timeout} seconds'
    except Exception as e:
        entry['returncode'] = -2
        entry['stdout'] = ''
        entry['stderr'] = str(e)
    entry['duration'] = round(time.time() - start, 3)
    entry['finished_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    report['results'].append(entry)

out_path = HERE / 'report.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Report saved to {out_path}")
print(json.dumps({'summary': {r['name']: r['returncode'] for r in report['results']}}, ensure_ascii=False))
