#!/usr/bin/env python3
"""Demonstrate claim dispositions on sanitized, source-derived aggregates.
No corporate workbook is included or regenerated. Example-only consistency model.
"""
from pathlib import Path
import json, math
D=json.loads((Path(__file__).parents[1]/'evidence'/'anonymized_derived_evidence.json').read_text())

def classify_claim(*, evidence_role, joint_assertions=None, admissible_answers=None, observed_outcome=None):
    """Role-aware four-way claim disposition; values alone have no interpretation.

    joint_assertions: same unit, date, version and claim semantics, each with a value.
    admissible_answers: explicitly alternative interpretations, not simultaneous facts.
    observed_outcome: whether the demanded post-launch outcome record is present.
    No cross-version or cross-unit joining is performed by this demonstration.
    """
    if evidence_role == 'joint_source_assertions':
        if not joint_assertions: raise ValueError('joint assertions require scoped records')
        fields=('claim_unit','source_version','observation_time')
        scopes={tuple(r[field] for field in fields) for r in joint_assertions}
        if len(scopes)!=1: raise ValueError('cannot jointly assert different claim scopes')
        values=[r['value'] for r in joint_assertions]
        return 'SOURCE_CONFLICT' if len(set(values))>1 else 'IDENTIFIED_SOURCE_FACT'
    if evidence_role == 'admissible_alternatives':
        if admissible_answers is None: raise ValueError('alternative answers must be supplied')
        if not admissible_answers: return 'SOURCE_CONFLICT'  # inconsistent admitted model
        return 'IDENTIFIED_SOURCE_FACT' if len(set(admissible_answers))==1 else 'NOT_IDENTIFIED'
    if evidence_role == 'operational_outcome':
        if observed_outcome is None: raise ValueError('outcome observation state must be declared')
        if observed_outcome: raise ValueError('a present record still requires an outcome-specific verification rule')
        return 'OUTCOME_EVIDENCE_ABSENT'
    raise ValueError('unknown evidence role: '+str(evidence_role))

DRAFT3_SCOPE={'claim_unit':'detailed_capabilities','source_version':'Draft-3','observation_time':'planning'}
assert classify_claim(evidence_role='joint_source_assertions',joint_assertions=[
    {**DRAFT3_SCOPE,'value':49,'source':'source-authored total helper'},
    {**DRAFT3_SCOPE,'value':51,'source':'direct detailed-row enumeration'},
])=='SOURCE_CONFLICT'
assert classify_claim(evidence_role='admissible_alternatives',admissible_answers=[49,51])=='NOT_IDENTIFIED'
assert classify_claim(evidence_role='joint_source_assertions',joint_assertions=[
    {**DRAFT3_SCOPE,'value':51,'source':'row enumeration'}])=='IDENTIFIED_SOURCE_FACT'
assert classify_claim(evidence_role='admissible_alternatives',admissible_answers=[])=='SOURCE_CONFLICT'
assert classify_claim(evidence_role='operational_outcome',observed_outcome=False)=='OUTCOME_EVIDENCE_ABSENT'
try:
    classify_claim(evidence_role='joint_source_assertions',joint_assertions=[
        {**DRAFT3_SCOPE,'value':49},
        {**DRAFT3_SCOPE,'value':51,'source_version':'Draft-2'},
    ])
    raise AssertionError('version mismatch must fail')
except ValueError:
    pass
score=D['scorecards']['vectors']; fw=score['Managed Firewall Services']; dspm=score['DSPM / Data Privacy']; human=score['Managed Human Risk and AI Awareness']
assert fw[3]<dspm[3] and fw[1]<human[1]

def priority_winner(criterion_weights):
    assert len(criterion_weights)==5 and abs(sum(criterion_weights)-1)<1e-10
    value={k:sum(w*x for w,x in zip(criterion_weights,v)) for k,v in score.items()}
    maximum=max(value.values())
    return tuple(sorted(k for k,v in value.items() if abs(v-maximum)<1e-10))

criteria_witnesses={
    'equal_weights':priority_winner([0.2]*5),
    'SOC_only':priority_winner([0,0,0,1,0]),
    'demand_only':priority_winner([0,1,0,0,0]),
}
assert criteria_witnesses['equal_weights']==('Managed Firewall Services',)
assert criteria_witnesses['SOC_only']==('DSPM / Data Privacy',)
assert criteria_witnesses['demand_only']==('Managed Human Risk and AI Awareness',)
assert classify_claim(evidence_role='admissible_alternatives',admissible_answers=list(criteria_witnesses.values()))=='NOT_IDENTIFIED' # explicit alternative admissible scorecard rules
# Witnesses for distinct allocations conserving the same family total.
y,k=1.0,3
alloc_equal=[y/k]*k
alloc_unequal=[2*y/3]+[y/(3*(k-1))]*(k-1)
assert abs(sum(alloc_equal)-y)<1e-12 and abs(sum(alloc_unequal)-y)<1e-12
assert alloc_equal!=alloc_unequal and all(x>0 for x in alloc_unequal)
fin=D['financial']
assert fin['total_unknowns']==57 and fin['total_equations']==12 and fin['total_free_dimensions']==45
print(json.dumps({'result':'PASS','status_examples':['SOURCE_CONFLICT','IDENTIFIED_SOURCE_FACT','NOT_IDENTIFIED','OUTCOME_EVIDENCE_ABSENT'],
'witnesses':criteria_witnesses,'boundary':'derived evidence only; typed example semantics; no direct corporate source rerun'},indent=2))
