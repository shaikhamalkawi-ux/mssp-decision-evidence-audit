#!/usr/bin/env python3
"""Self-contained finite-condition check for claim-class interpretation.

Uses anonymized group sizes and normalized group totals (not original corporate
amounts). Checks the sharp sum-of-group-extrema formula against scipy.linprog.
This is a mathematical regression test and NOT a new industrial measurement.
"""
import argparse, csv, json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

def load_groups(filename):
    with open(filename, newline='') as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==12
    sizes=[int(r['active_package_count']) for r in rows]
    totals=[float(r['normalized_total']) for r in rows]
    assert sum(sizes)==57 and all(n>1 for n in sizes)
    assert all(y>0 for y in totals)
    return sizes, totals

def verify(csv_file):
    sizes, totals=load_groups(csv_file)
    groups=[];st=0
    for n in sizes: groups.append(list(range(st,st+n)));st+=n
    A=np.zeros((len(groups),sum(sizes)))
    for g,idx in enumerate(groups):A[g,idx]=1.
    rank=np.linalg.matrix_rank(A)
    assert rank==12
    y=np.asarray(totals)
    rng=np.random.default_rng(104)
    targets=[]
    for g,idx in enumerate(groups):
        c=np.zeros(sum(sizes));c[idx]=1.
        targets.append((f'group_{g+1:02d}',c,True))
    for j in range(sum(sizes)):
        c=np.zeros(sum(sizes));c[j]=1.
        targets.append((f'coordinate_{j+1:02d}',c,False))
    for k in range(20):
        coeff=rng.normal(size=len(groups))
        c=A.T@coeff
        targets.append((f'full_group_linear_combination_{k:02d}',c,True))
    for k in range(20):
        c=rng.normal(size=sum(sizes))
        targets.append((f'mixed_linear_claim_{k:02d}',c,False))

    worst_gap=0.
    for label,c,expect_identified in targets:
        lows=sum(y[g]*min(c[idx]) for g,idx in enumerate(groups))
        ups=sum(y[g]*max(c[idx]) for g,idx in enumerate(groups))
        nonconstant=any(np.ptp(c[idx])>1.e-11 for idx in groups)
        if label.startswith('full_group') or label.startswith('group_'):
            nonconstant=False
        assert expect_identified==(not nonconstant),label
        lo=linprog(c,A_eq=A,b_eq=y,bounds=(0,None),method='highs')
        hi=linprog(-c,A_eq=A,b_eq=y,bounds=(0,None),method='highs')
        assert lo.success and hi.success,label
        gap=max(abs(lo.fun-lows),abs(-hi.fun-ups))
        worst_gap=max(worst_gap,gap)
        assert gap<1.e-8,(label,gap)
        if expect_identified: assert ups-lows<1.e-8
        else: assert ups-lows>1.e-8
    return {'status':'PASS', 'evidence_role':'normalized derived group-size mathematics; not original company amount replay',
      'groups':len(groups),'coordinates':sum(sizes),'rank':int(rank),'nullity':sum(sizes)-int(rank),
      'linear_targets_verified':len(targets),'identified_group_totals':12,'unidentified_coordinates':57,
      'identified_group_linear_combinations':20,'nonidentified_mixed_linear_claims':20,
      'maximum_analytic_vs_LP_endpoint_difference':float(worst_gap),
      'assumptions':'Y_g normalized to 1, strictly positive and disjoint nonnegative allocations; sharp bounds'
    }

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--groups',default='DERIVED_GROUP_SIZES_FOR_LINEAR_CLAIM_TEST.csv')
    p.add_argument('--output',default='V36R1_LINEAR_CLAIM_CLASS_QA.json'); args=p.parse_args()
    x=verify(args.groups)
    Path(args.output).write_text(json.dumps(x,indent=2)+'\n')
    print('PASS',x['linear_targets_verified'],'linear claims; max endpoint LP error',x['maximum_analytic_vs_LP_endpoint_difference'])
