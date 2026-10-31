from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
for slug in ('inquiry','purpose-planning','toolcraft','judgment','discovery','contribution','reliability-by-construction'):
 p=root/'skills'/slug/'SKILL.md'
 assert p.exists() and p.read_text().startswith('---\n')
for p in (root/'schemas').glob('*.json'):json.loads(p.read_text())
example=json.loads((root/'examples'/'guffy-field-lab.json').read_text())
assert example['status']=='inconclusive' and example['leads']
try:
 import jsonschema
 jsonschema.validate(example,json.loads((root/'schemas'/'research-state.schema.json').read_text()))
 print('JSON schema: passed')
except ImportError:print('JSON schema library unavailable; JSON syntax checked')
print('Package structure: passed')
