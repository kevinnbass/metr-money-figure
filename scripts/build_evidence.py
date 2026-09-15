"""Build research/EVIDENCE-10a-anthropic.txt: one block per row id cited on figure 10a-anthropic (claim / why it matters / source)."""
import re,csv,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; sys.path.insert(0,str(ROOT/'research'))
from evidence_significance import CLAIM,WHY,default_why
sys.path.insert(0,str(ROOT/'scripts')); from fig_common import strip_ids
h=open(ROOT/'figures/metr-01b-money-that-doesnt-show-up-with-anthropic.html').read()
ids=set()
for m in re.finditer(r'\b(ST|RW|IV|AP|TB|TO|M|G|J|K|S|B)(\d{2,3})(?:[–-](?:(ST|RW|IV|AP|TB|TO|M|G|J|K|S|B))?(\d{2,3}))?\b',h):
    p,a,p2,b=m.groups()
    if b and (not p2 or p2==p) and int(b)>=int(a) and int(b)-int(a)<40:
        for i in range(int(a),int(b)+1): ids.add(f'{p}{i:02d}')
    else: ids.add(f'{p}{int(a):02d}')
files={'ST':('stakes.csv','Anthropic equity, the donated stake, and the accounts that pay Coefficient\'s grants'),'IV':('investments.csv','Anthropic\'s funding rounds and named investors'),'M':('money_flows.csv','Money into METR\'s network'),'AP':('audacious-partners.csv','The Audacious Project and Canary'),'G':('budget.csv','METR\'s own budget statements'),'TB':('tarbell_funding.csv','Tarbell Center funding'),'TO':('tarbell_outlets.csv','Tarbell fellows\' articles by outlet'),'RW':('redwood.csv','Redwood Research and METR'),'J':('shared_donors.csv','Donors shared between METR and the labs'),'B':('board.csv','METR\'s board'),'K':('compute_inkind.csv','In-kind support from labs'),'S':('staff_origins.csv','Staff moves')}
def first(s,n=320):
    s=re.sub(r'\s+',' ',s or '').strip()
    if not s: return ''
    m=re.match(r'(.+?[.;])(\s|$)',s); t=m.group(1) if m and len(m.group(1))<n else s[:n]
    return t.strip()
def money(v):
    return ('$'+format(int(float(v)),',')) if re.fullmatch(r'[\d.]+',v or '') else (v or 'amount undisclosed')
def claim(p,i,r):
    if i in CLAIM: return CLAIM[i]
    if p=='M': return f"{r['from_entity']} → {r['to_entity']}: {money(r['amount_usd'])} ({r['measure']}), {r['date']}. {r['purpose']}"
    if p=='ST': return f"{r['investor']} — {r['value']}{(' '+r['unit']) if r['unit'] not in ('n/a','') else ''} ({r['date_of_source']}, {r['source_type']})"
    if p=='IV': return f"Anthropic {r['round']}, {r['date']}: {money(r['amount_usd'])} raised; post-money {money(r['post_money_valuation_usd'])}; named investors: {r['named_investors']}"
    if p=='AP': return f"{r['partner']}: {r['grant_to'] or 'no grant found'} {money(r['amount_usd']) if r['amount_usd'] else ''} {r['date']} — {r['purpose']}"
    if p=='G': return f"METR {r['measure']}: {r['value']} ({r['period']}), stated {r['date']}"
    if p=='TB': return f"{r['measure'].replace('_',' ')}: {r['organization']}, {r['title']}, {money(r['amount_usd'])}, {r['award_date']}"
    if p=='TO': return f"{r['outlet']}: {r['n_tarbell_ai']} articles by Tarbell fellows classified as AI, {r['window_min']} to {r['window_max']} (of {r['n_ai']} AI articles found in that window)"
    if p=='RW': return f"{r['date']} {r['fact_type']}: {r['subject']} — {first(r['detail'],260)}"
    if p=='J': return f"{r['donor']}: gives to METR — {r['gives_to_metr']}; gives to or invests in a lab — {r['gives_to_or_invests_in_lab']}"
    if p=='K': return f"{r['date']} {r['lab']}: {r['statement']} (quantified: {r['quantified']}; {r['value_or_volume']})"
    if p=='S': return f"{r['name']}, {r['metr_title']}, joined METR {r['joined']} from {r['prior_org']} ({r['prior_role']})"
    if p=='B': return f"{r['name']}: {r['metr_role']}; also {r['other_current_org']} ({r['other_org_role']})"
def url(r): return r.get('source_url') or r.get('url') or r.get('lab_source_url') or r.get('metr_source_url') or r.get('source_urls') or ''
out=["EVIDENCE — every fact cited on figure 10a-anthropic (metr-01b), one block per row id","Format: Claim / Why it matters / Source, one block per fact. A keyed copy maps each block to its row in the research tables, where the verbatim quote, full note and fetch date live. Built 2026-09-14; revised after audit 4.","",""]
n=0; missing=[]; keyed=list(out)
for p in ['ST','IV','M','AP','G','TB','TO','RW','J','B','K','S']:
    f,title=files[p]; rows={r['row_id']:r for r in csv.DictReader(open(ROOT/'research'/f,newline=''))}
    want=sorted((i for i in ids if re.match(r'[A-Z]+',i).group()==p and i in rows), key=lambda x:int(re.sub(r'\D','',x)))
    if not want: continue
    keyed+=[f"== {title} ({f}) ==",""]; out+=[f"== {title} ==",""]
    for i in want:
        r=rows[i]; n+=1
        w=WHY.get(i) or default_why(i,r)
        if not w: missing.append(i); w=first(r.get('notes') or r.get('note') or r.get('quote_verbatim') or r.get('quote') or '')
        keyed+=[f"{i}. Claim: {claim(p,i,r)}", f"Why it matters: {w}", f"Source: {url(r)}","",""]
        out+=[f"Claim: {strip_ids(claim(p,i,r))}", f"Why it matters: {strip_ids(w)}", f"Source: {url(r)}","",""]
open(ROOT/'research/EVIDENCE-10a-anthropic.txt','w').write("\n".join(out))
open(ROOT/'research/EVIDENCE-10a-anthropic-keyed.txt','w').write("\n".join(keyed))
print("blocks",n,"without hand-written significance:",missing)
