from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
for slug in ('inquiry','purpose-planning','toolcraft','judgment','discovery','contribution','reliability-by-construction','performance-metric-integrity','institutional-intelligence'):
 p=root/'skills'/slug/'SKILL.md'
 assert p.exists() and p.read_text().startswith('---\n')
for p in (root/'schemas').glob('*.json'):json.loads(p.read_text())
example=json.loads((root/'examples'/'research-example.json').read_text())
assert example['status']=='inconclusive' and example['leads']
try:
 import jsonschema
 jsonschema.validate(example,json.loads((root/'schemas'/'research-state.schema.json').read_text()))
 print('JSON schema: passed')
except ImportError:print('JSON schema library unavailable; JSON syntax checked')
print('Package structure: passed')

metric_report=json.loads((root/'examples'/'metric-reconciliation.json').read_text(encoding='utf-8'))
metric_schema=json.loads((root/'schemas'/'metric-report.schema.json').read_text(encoding='utf-8'))
counts=metric_report['counts']
assert counts['received']==sum(counts[key] for key in ('verified_complete','incomplete','failed','excluded'))
assert metric_report['reconciled']==counts['verified_complete']/counts['received']
assert metric_report['reported']!=metric_report['reconciled']
print('Metric example arithmetic: passed')
try:
 import jsonschema
 jsonschema.Draft202012Validator.check_schema(metric_schema)
 jsonschema.validate(metric_report,metric_schema)
 print('Metric report schema: passed')
except ImportError:
 print('Metric report schema: JSON syntax checked; install jsonschema for schema validation')

goal_schema=json.loads((root/'schemas'/'goal-proposal.schema.json').read_text(encoding='utf-8'))
goal_examples=[json.loads((root/'examples'/name).read_text(encoding='utf-8')) for name in ('purpose-to-action-goal.json','purpose-to-action-no-goal.json')]
try:
 import jsonschema
 jsonschema.Draft202012Validator.check_schema(goal_schema)
 for goal_example in goal_examples:
  jsonschema.validate(goal_example,goal_schema)
 print('Goal proposal schemas: passed')
except ImportError:
 print('Goal proposal schemas: JSON syntax checked; install jsonschema for schema validation')
