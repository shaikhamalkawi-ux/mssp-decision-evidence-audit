#!/usr/bin/env python3
from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
d=json.loads((root/"evidence"/"anonymized_derived_evidence.json").read_text())
checks=[]
def ck(n,c): checks.append((n,bool(c)))
ck("51_to_25",(d["capabilities"],d["packages"])==(51,25))
ck("mapping_count",d["mapping_exact_names"]==51)
ck("status_sum",sum(d["status_counts"].values())==51)
ck("year_sum",sum(d["detailed_year_counts"])==51 and sum(d["package_year_counts"])==25)
ck("stage_sensitivity_sums",sum(d["all_components_sensitivity"])==25 and sum(d["broad_full_scope_sensitivity"])==25)
f=d["financial"]
ck("rank_free_dimensions",f["total_unknowns"]-f["total_equations"]==f["total_free_dimensions"]==45)
sc=d["scorecards"]; fw=sc["vectors"]["Managed Firewall Services"]
def dom(a,b): return all(x>=y for x,y in zip(a,b)) and any(x>y for x,y in zip(a,b))
ck("firewall_dominates_IAM",dom(fw,sc["vectors"]["Managed IAM & PAM"]))
ck("firewall_dominates_GRC",dom(fw,sc["vectors"]["Managed GRC, Risk and Compliance-as-a-Service"]))
ck("firewall_not_dominate_DSPM",not dom(fw,sc["vectors"]["DSPM / Data Privacy"]))
ck("firewall_not_dominate_Human",not dom(fw,sc["vectors"]["Managed Human Risk and AI Awareness"]))
ck("counterexample_soc",sc["vectors"]["DSPM / Data Privacy"][3]>fw[3])
ck("counterexample_demand",sc["vectors"]["Managed Human Risk and AI Awareness"][1]>fw[1])
ad=json.loads((root/"evidence"/"archive_admission_summary.json").read_text())
ck("archive_entry_disposition",ad["zip_entry_count"]==25 and ad["material_entries"]==23 and ad["export_error_entries"]==2 and ad["distinct_material_payloads"]==21 and ad["primary_analytical_payloads"]==9 and ad["contextual_approval_status_payloads"]==1)
ck("normalization", abs(sum(d["financial"]["ratios"]["annual_revenue_shares"])-1)<1e-10)
failed=[n for n,o in checks if not o]
print(json.dumps({"checks":len(checks),"passed":len(checks)-len(failed),"failed":failed},indent=2))
sys.exit(1 if failed else 0)
