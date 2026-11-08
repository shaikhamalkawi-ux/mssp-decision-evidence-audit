#!/usr/bin/env python3
"""Executable source-derived casebook checks. No protected corporate data."""
from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[1]
w=json.loads((root/'evidence/package_label_witness_v8.json').read_text())
b=json.loads((root/'evidence/claim_decision_casebook_v8.json').read_text())
d=json.loads((root/'evidence/anonymized_derived_evidence.json').read_text())
C=[]
def ck(tag,x): C.append((tag,bool(x)))
allowed={'Provided','Provided / Expandable'}
s=w['cases'];pred=lambda item: all(x in allowed for x in item['component_statuses'])
ck('label_same',w['status_label']=='Provided / Expandable' and len(s)==2)
ck('status_difference',s[0]['component_statuses']!=s[1]['component_statuses'])
ck('predicate_zero_one',[pred(x) for x in s]==[False,True])
ck('source_witness_values',all(pred(x)==x['strict_value'] for x in s))
ck('profiles_source_status_count',sum(d['status_counts'].values())==51)
ck('casebook_schema',len(b['claims'])==8 and all(all(k in c for k in b['admission_fields']) for c in b['claims']))
ck('four_distinct_dispositions',set(c['status'] for c in b['claims'])==set(b['decision_states']))
ck('source_conflict_case', next(c['status'] for c in b['claims'] if c['id']=='C2')=='SOURCE_CONFLICT')
ck('missing_operational_outcome_case', next(c['status'] for c in b['claims'] if c['id']=='C11')=='OUTCOME_EVIDENCE_ABSENT')
ck('distinct_missing_vs_notidentified', next(c['status'] for c in b['claims'] if c['id']=='C8')=='NOT_IDENTIFIED')
ck('casebook_current_version',b['version']=='V8')
vec=d['scorecards']['vectors']; vF=vec['Managed Firewall Services']
for tag,weights,winner in [('equal',[.2]*5,'Managed Firewall Services'),('SOC',[0,0,0,1,0],'DSPM / Data Privacy'),('demand',[0,1,0,0,0],'Managed Human Risk and AI Awareness')]:
    xs={k:sum(a*t for a,t in zip(weights,v)) for k,v in vec.items()}
    ck('witness_'+tag,list(k for k,q in xs.items() if abs(q-max(xs.values()))<1e-9)==[winner])
f=b['financial_illustrative']
ck('financial_identical_total',all(abs(sum(v)-1)<1e-12 and all(x>0 for x in v) for v in (f['allocation_a'],f['allocation_b'])))
ck('financial_distinct',f['allocation_a']!=f['allocation_b'])
ck('conditional_rank_nullity',f['unknowns_total']==57 and f['independent_group_totals']==12 and f['nullspace_dimension']==45)
ck('bounded_release',b['publication_state'].startswith('HOLD'))
failed=[n for n,t in C if not t]
print(json.dumps({'checks':len(C),'pass':len(C)-len(failed),'failed':failed,'scope':'derived status and algebra witnesses only'},indent=2))
sys.exit(bool(failed))
