"""METR figures 10a-10l. Run: ~/.venvs/memes/bin/python scripts/generate.py [stem ...]
Every number traces to a row_id in research/*.csv."""
import sys, csv, json, math, re, traceback, datetime
from pathlib import Path
from fig_common import *
import fig_common as FC

RES = ROOT/'research'
SRC = 'Source: memes/ai-machine/10-metr/research/ (built 2026-09-14; second audit research/AUDIT-2.md applied)'

def rows(name):
    with open(RES/name, newline='') as f: return list(csv.DictReader(f))

def card(title, body, color=None, size=19):
    bar = f'border-left:6px solid {color};' if color else ''
    return f'<div style="background:#efece4;border-radius:10px;padding:14px 18px;{bar}"><div style="font-size:{size}px;font-weight:bold;line-height:1.25">{title}</div><div style="font-size:{size-2}px;color:{MUTED};line-height:1.35;margin-top:6px">{body}</div></div>'

# ---------------------------------------------------------------- 10i. RFI asks
def fig_rfi():
    W,H=2200,1380; STEM='metr-09-ask-the-regulator'
    R=[r for r in rows('rfi_asks.csv')]
    order=['R01','R03','R05','R04','R07','R06','R02','R08']
    R={r['row_id']:r for r in R}; R=[R[k] for k in order]
    col={'yes':AQUA,'partial':YELLOW,'context':BLUE,'no':GRAY}
    lab={'yes':'Overlaps METR\'s own methods or activity','partial':'Partly overlaps','context':'Empowers an agency then led by METR\'s parent-org founder','no':'No METR activity matches'}
    html='<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px 26px;margin-top:4px">'
    html+=f'<div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold">What METR asked the White House for (verbatim, p. of the PDF)</div><div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold">What METR already does</div>'
    for r in R:
        c=col[r['metr_supplies_it']]
        html+=f'<div style="background:#efece4;border-radius:10px;padding:14px 18px;border-left:7px solid {c}"><div style="font-size:15px;color:{MUTED};font-weight:bold;letter-spacing:1px">{r["row_id"]} · p.{r["pdf_page"]} · {esc(r["location"])}</div><div style="font-size:19px;line-height:1.3;margin-top:4px">“{esc(r["ask_verbatim"])}”</div></div>'
        html+=f'<div style="background:#efece4;border-radius:10px;padding:14px 18px;border-left:7px solid {c}"><div style="font-size:15px;color:{c if c!=YELLOW else WARNTXT};font-weight:bold;letter-spacing:1px;text-transform:uppercase">{esc(lab[r["metr_supplies_it"]])}</div><div style="font-size:18px;line-height:1.3;margin-top:4px;color:{INK}">{esc(r["matching_metr_activity"])}</div></div>'
    html+='</div>'
    body=legend([(AQUA,'Overlaps METR\'s own methods or activity'),(YELLOW,'Partly overlaps'),(BLUE,'Empowers an agency then led by the founder of METR\'s parent org'),(GRAY,'No METR activity matches')])+html
    foot=f'<b>Coverage:</b> All four "priority actions" in METR\'s summary plus the three body-text recommendations that name a verifier, and the one ask with no METR product (R08), so nothing is dropped. Quotes are verbatim from METR\'s March 15, 2025 response to the OSTP/NITRD Request for Information on the AI Action Plan (rows R01–R08, research/rfi_asks.csv; PDF in research/). Matching activities are METR\'s own published work as listed on metr.org; the overlap column is interpretation, graded per the Codex source audit 2026-09-14 (R02 no overlap, R07 partial: NIST, not METR, would write the standard). METR is a nonprofit and sells nothing; the response does not ask for money for METR and says none of its actions "requires restructuring of existing authorities." Asking government to standardize your own method is normal for a standards body; the figure shows the overlap, not a motive. {SRC}.'
    render(STEM, shell('Ask the regulator for what you do: METR\'s asks to the White House beside METR\'s own methods','Figure 10i · March 2025 RFI response','Every recommendation in METR\'s AI Action Plan comment beside the METR activity it overlaps with, if any.',body,foot,W,H),W,H)


def num(v):
    v=str(v).replace('$','').replace(',','')
    try: return float(v)
    except: pass
    if v.strip().lower().startswith('eur'): return 0.0
    nums=re.findall(r'\d+(?:\.\d+)?', v)
    return sum(float(n) for n in nums) if nums else 0.0

def wrap(s, n):
    """greedy word wrap to lines of <= n chars"""
    if FC.STRIP_IDS: s=FC._strip_ids_text(str(s))
    out=[]; cur=''
    for w in str(s).split():
        if len(cur)+len(w)+1>n and cur: out.append(cur); cur=w
        else: cur=(cur+' '+w).strip()
    if cur: out.append(cur)
    return out

def tspans(x,y,lines,size,fill,lh=None,anchor='start',weight='normal'):
    lh=lh or size*1.2
    if FC.STRIP_IDS: lines=[FC._strip_ids_text(str(l)) for l in lines]
    return ''.join(f'<text x="{x:.1f}" y="{y+i*lh:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{esc(l)}</text>' for i,l in enumerate(lines))

# ---------------------------------------------------------------- 10a. money that doesn't show up
def fig_money(anth=False):
    FC.STRIP_IDS=True; FC.STRIPPED_IDS.clear()
    W=2200; STEM='metr-01b-money-that-doesnt-show-up-with-anthropic' if anth else 'metr-01-money-that-doesnt-show-up'
    M=rows('money_flows.csv')
    def tot(ids): return sum(num(r['amount_usd']) for r in M if r['row_id'] in ids)
    coef_arc=tot({'M01','M02'}); coef_rand=tot({'M03'}); coef_long=tot({'M%02d'%i for i in range(4,15)}); coef_far=tot({'M%02d'%i for i in range(15,33)})
    sff_arc=tot({'M35','M36','M37'}); sff_metr=tot({'M38','M39'}); arc_metr=tot({'M63'})
    aud_canary=tot({'M57'}); aud_metr=tot({'M58'}); long_metr=tot({'M59'})
    daf_metr=tot({'M79','M83','M87'}); daf_arc=tot({'M77','M78','M80','M81','M82','M84','M85','M86','M88','M89','M90','M93','M94','M95','M96'})
    TB={r['row_id']:r for r in rows('tarbell_funding.csv')}; coef_tarbell=sum(num(TB[k]['amount_usd']) for k in ('TB02','TB03','TB04'))
    L,Mx,R,MW=(700,1280,1760,290) if anth else (330,1060,1700,330); s=[]; pipes=[]
    def node(x,y,w,h,name,sub,c):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}" opacity="0.13"/><rect x="{x}" y="{y}" width="8" height="{h}" rx="3" fill="{c}"/>'
                + tspans(x+22,y+34,[name],min(24,int((w-36)/(0.6*len(name)))),INK,weight='bold') + tspans(x+22,y+62,wrap(sub,34),17,MUTED,lh=21))
    def bez(x1,y1,x2,y2,t):
        mid=(x1+x2)/2
        bx=lambda: (1-t)**3*x1+3*(1-t)**2*t*mid+3*(1-t)*t**2*mid+t**3*x2
        by=lambda: (1-t)**3*y1+3*(1-t)**2*t*y1+3*(1-t)*t**2*y2+t**3*y2
        return bx(),by()
    def pw(amt): return max(6, 6+amt/1e6*1.4)   # one linear scale, no cap: 1.4 px per $1M
    def flow(x1,y1,x2,y2,amt,label,c,w=None,dash=False,t=0.3,dy=-12,anchor='middle'):
        w = w or pw(amt)
        mid=(x1+x2)/2
        d=f'M{x1},{y1} C{mid},{y1} {mid},{y2} {x2},{y2}'
        extra=' stroke-dasharray="14 10"' if dash else ''
        px,py=bez(x1,y1,x2,y2,t)
        if '@@PIPES@@' not in s: s.append('@@PIPES@@')
        pipes.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w:.1f}"{extra}/>')
        return tspans(px,py-w/2+dy,[label],17,INK,anchor=anchor,weight='bold')
    # funders column: Moskovitz bracket around Coefficient + Good Ventures
    s.append(f'<rect x="{L-320}" y="60" width="340" height="555" rx="14" fill="{BLUE}" opacity="0.06"/><rect x="{L-320}" y="60" width="340" height="555" rx="14" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="6 6" opacity="0.6"/>')
    s.append(tspans(L-300,96,['Dustin Moskovitz'],28,INK,weight='bold')+tspans(L-300,110,wrap('and Cari Tuna: Good Ventures Foundation and the funding partners that pay what Coefficient recommends',46),13,MUTED,lh=15))
    s.append(node(L-300,148,300,215,'Coefficient Giving','Formerly Open Philanthropy. Recommends grants; Coefficient Giving Advisors or its funding partners, Good Ventures Foundation and accounts at SVCF and NPT, approve and pay. The account principals are not public (ST105, ST109)',BLUE))
    s.append(node(L-300,410,300,190,'Good Ventures Foundation','Moskovitz and Tuna\'s $10.1B endowment (Jun 2025, ST100); Coefficient\'s named funding partner (ST105, ST111); $10M to Open Philanthropy Advisors, now Coefficient Giving Advisors, FY2024 (ST140)',BLUE))
    s.append(f'<path d="M{L-150},410 L{L-150},379" fill="none" stroke="{BLUE}" stroke-width="12" opacity="0.5"/><path d="M{L-162},385 L{L-150},367 L{L-138},385 Z" fill="{BLUE}" opacity="0.7"/>')
    s.append(tspans(L-138,396,['the money'],13,BLUE,weight='bold'))
    s.append(node(L-300,635,300,110,'Jaan Tallinn / SFF','Anthropic Series A lead, board observer by his own account (IV01, ST41)' if anth else 'Recommends grants through SFF; his personal ledger is public (M35–M39)',BLUE))
    s.append(node(L-300,775,300,300,'The Audacious Project','TED-run funding collective: donors pool multi-year commitments to chosen projects and pay grantees directly. Its 2024 cohort funded Canary (RAND + METR). Filed payments found: Valhalla → RAND $10.0M, High Tide → RAND $333K; none to METR in the filings read. Good Ventures joined the partner list after Canary was announced; none traced.',GRAY))
    s.append(node(L-300,1090,300,215,'DAFs and regrantors','Donor-advised funds and regrantors. Founders Pledge grants match Tallinn\'s ledger to the dollar, SVCF within $450. Vanguard, Effective Ventures, Every.org, AEF, Fidelity: donor unnamed.',YELLOW))
    # intermediaries
    s.append(node(Mx-150,50,340,125,'Alignment Research Center','METR\'s parent until Dec 2023 (Christiano); handed METR $4.55M at the spin-out',ORANGE))
    s.append(node(Mx-150,240,340,185,'RAND Corporation','METR\'s partner in Canary, the Audacious-funded joint project (~$38M: ~$21M RAND, ~$17M METR; METR later: "a bit under $16m" over 3 years, G14)',ORANGE))
    s.append(node(Mx-150,460,340,110,'Longview Philanthropy','METR\'s pooled-fund donor; regrants to METR',ORANGE))
    s.append(node(Mx-150,660,340,110,'FAR AI','Founder Adam Gleave sits on METR\'s board (B05)',ORANGE))
    s.append(node(Mx-150,860,340,170,'Redwood Research','Worked with METR on the OpenAI investigation (RW31–RW34); Redwood says its staff are subcontracted by METR on the Anthropic one, terms undisclosed (RW36, RW58)' if anth else 'Worked with METR on the OpenAI investigation; Redwood says its staff are subcontracted by METR on the current one, terms undisclosed (RW31–RW36, RW58)',ORANGE))
    s.append(node(Mx-150,1060,340,110,'Constellation','The Berkeley office METR works from',ORANGE))
    s.append(node(R,380,MW,180,'METR','Model Evaluation and Threat Research. Says it takes no money from frontier labs or their staff.',AQUA))
    # Coefficient flows (labels near source, staggered)
    s.append(flow(L,200,Mx-150,110,coef_arc,money(coef_arc)+' 2022 → ARC',BLUE,t=0.25,dy=-10))
    s.append(flow(L,200,Mx-150,300,coef_rand,money(coef_rand)+' 2025 "AI Evaluation and Testing" → RAND',BLUE,t=0.5,dy=-14))
    s.append(flow(L,200,Mx-150,510,coef_long,money(coef_long)+' 2022–25 → Longview',BLUE,t=0.55,dy=-14))
    s.append(flow(L,200,Mx-150,710,coef_far,money(coef_far)+' 2021–25 → FAR AI',BLUE,t=0.5,dy=-16))
    s.append(flow(L,690,Mx-150,110,sff_arc,money(sff_arc)+' 2022–24 SFF recs → ARC / ARC Evals',BLUE,t=0.42,dy=22))
    # Tallinn → METR: routed under Longview, not across it
    wsm=pw(sff_metr)
    pipes.append(f'<path d="M{L},690 C{L+250},690 {Mx-300},625 {Mx},625 C{Mx+280},625 {Mx+320},470 {R},470" fill="none" stroke="{BLUE}" stroke-width="{wsm:.1f}"/>'); s.append(tspans(Mx,600,[money(sff_metr)+' SFF recs 2024–25 → METR incl. conditional match'],17,INK,anchor='middle',weight='bold'))
    coef_redwood=70e6; sff_redwood=1274000+1098000; coef_const=3000000+3200000+16750000; svcf_const=10e6
    s.append(flow(L,920,Mx-150,335,aud_canary,money(aud_canary)+' Audacious commitment to Canary (RAND + METR), 2024 (grey pipe)',GRAY,t=0.08,dy=-72,anchor='start'))
    s.append(flow(L,200,Mx-150,915,coef_redwood,'$70M+ 2026 recommendation → Redwood (M120)',BLUE,t=0.93,dy=-14,anchor='end'))
    s.append(flow(L,690,Mx-150,940,sff_redwood,money(sff_redwood)+' SFF recs 2022–23 → Redwood',BLUE,t=0.82,dy=22,anchor='end'))
    s.append(flow(L,200,Mx-150,1110,coef_const,'$22.95M 2023–24 → Constellation',BLUE,t=0.92,dy=-2,anchor='end'))
    s.append(flow(L,1195,Mx-150,1130,svcf_const,money(svcf_const)+' 2024 SVCF → Constellation (ST107)',YELLOW,t=0.5,dy=22))
    s.append(flow(Mx+190,915,R,530,0,'contractor on the OpenAI investigation; Anthropic per Redwood; terms undisclosed' if anth else 'contractor on METR\'s lab investigations; terms undisclosed',ORANGE,w=6,dash=True,t=0.35,dy=-10))
    s.append(flow(Mx+190,1110,R,548,0,'office; no grant on record',ORANGE,w=6,dash=True,t=0.38,dy=-10))
    s.append(flow(L,1195,Mx-150,150,daf_arc,money(daf_arc)+' 2022–25 → ARC; $4.2M matches Tallinn\'s ledger',YELLOW,t=0.04,dy=-132,anchor='start'))
    s.append(flow(L,1195,R,540,daf_metr,money(daf_metr)+' → METR 2024–25: Vanguard $4.0M (donor unnamed); FP $184K + SVCF $20K match Tallinn\'s ledger',YELLOW,t=0.9,dy=78,anchor='end'))
    s.append(flow(Mx+190,400,R,520,aud_metr,'~$17M committed to METR',GRAY,t=0.25,dy=-30,anchor='start'))
    s.append(flow(Mx+190,110,R,420,arc_metr,money(arc_metr)+' spin-out transfer, Apr 2024 (ARC 990)',ORANGE,t=0.45,dy=-18))
    s.append(flow(Mx+190,510,R,480,long_metr,'$220K recommended 2023 (GWWC)',ORANGE,t=0.5,dy=16)+tspans((Mx+190+R)/2,527,['+ pooled fund, undisclosed'],14,INK,anchor='middle',weight='bold'))
    s.append(flow(Mx+190,710,R,510,0,'board seat (Gleave); no grant on record',ORANGE,w=6,dash=True,t=0.62,dy=16,anchor='start'))
    SVGH=1260
    if anth:
        SVGH=1890
        # Tarbell branch, bottom right: pipe runs down the channel, then across under Constellation
        TX,TY=R-330,1190
        wt=pw(coef_tarbell)
        pipes.append(f'<path d="M{L},200 C{L+130},200 {L+130},1255 {L+240},1255 L{TX-60},1255 C{TX-30},1255 {TX-30},1255 {TX},1255" fill="none" stroke="{BLUE}" stroke-width="{wt:.1f}"/>')
        s.append(tspans(L+160,1240,[money(coef_tarbell)+' Coefficient awards 2024–25 → Tarbell Center (TB02–TB04)'],17,INK,weight='bold')+tspans(L+160,1284,['SFF recommended $1.3M more, 2024–25, incl. a $200K conditional match (TB05–TB06)'],13,MUTED))
        s.append(node(TX,TY,300,150,'Tarbell Center for AI Journalism','Fellowship whose reporters work at outlets. Coefficient-funded. Fellows\' AI articles found in each outlet\'s captured window →',ORANGE))
        TO=rows('tarbell_outlets.csv'); chips=[('TIME','TO01'),('The Verge','TO02'),('MIT Tech Review','TO03'),('Lawfare','TO04'),('The Guardian','TO05'),('LA Times','TO06')]
        cnt={r['row_id']:r['n_tarbell_ai'] for r in TO}
        for i,(nm,rid) in enumerate(chips):
            cx=TX+320+(i%2)*150; cy=TY+8+(i//2)*46
            s.append(f'<path d="M{TX+300},{TY+70} C{TX+310},{TY+70} {cx-10},{cy+18} {cx},{cy+18}" fill="none" stroke="{ORANGE}" stroke-width="3" opacity="0.6"/>')
            s.append(f'<rect x="{cx}" y="{cy}" width="140" height="36" rx="8" fill="{ORANGE}" opacity="0.15"/>'+tspans(cx+10,cy+24,[f'{nm} · {cnt[rid]}'],14,INK,weight='bold'))
        # Anthropic panel
        IV={r['row_id']:r for r in rows('investments.csv')}
        AX,AW,AY,AH=30,200,60,1310
        s.append(f'<rect x="{AX}" y="{AY}" width="{AW}" height="{AH}" rx="10" fill="{RED}" opacity="0.10"/><rect x="{AX}" y="{AY}" width="8" height="{AH}" rx="3" fill="{RED}"/>')
        s.append(tspans(AX+20,AY+34,['Anthropic'],24,INK,weight='bold'))
        lines=['The lab METR evaluates and now investigates.','','Series H, May 2026: $965B post-money (IV10). WSJ: IPO target ~$2T (IV11). Board observers, by their own account: Moskovitz and Tallinn (ST118, ST41).','','Investors among METR\'s funders:','','Moskovitz: named Series A investor 2021; under 0.8% (Forbes); donated in 2025 to what he calls "our foundation"; Good Ventures Foundation\'s return to Jun 2025 shows no such gift; Coefficient\'s CEO: "not to us"; the recipient account is not public (IV01, ST89–ST118)','','Tallinn: Series A lead, Series B; "we do not announce percentages" (IV01–IV02, ST98)','','Schmidt: Series A; his family vehicle Hillspire bought 20% of D.E. Shaw in 2015 (Forbes), and D.E. Shaw\'s venture arm is in Series H; Schmidt Sciences is a named METR supporter (IV01, ST26, ST49, J08)','','Jane Street, the firm: $100M for 3.3M shares at ~$30 in the FTX estate sale, Mar 2024; then Series E–H, undisclosed. METR names "individuals from Jane Street" (IV05–IV10, M75)','','McClave: Series A and B; BEMC is not a METR donor in the filings checked (IV01–IV02, J02)','','CERR / Macroscopic: Series A and B; funds Redwood and Longview, holds Apollo and Halcyon\'s venture arm (ST54, M139–M142)','','Good Ventures\' own book, Jun 2025: TSMC $509M, SK Hynix $400M, Broadcom $290M, Vistra, Micron, Vertiv; its manager launched VAR AI Fund in Mar 2025, $4.35B sold to 116 investors by Jun 2026; at least one of the manager\'s two charitable clients is an LP, which one is not stated; the manager\'s co-owner sits on the board of METR\'s former parent ARC (ST100–ST102, ST125, ST127)']
        yy=AY+62
        for ln in lines:
            if ln=='' : yy+=8; continue
            for w in wrap(ln,25): s.append(tspans(AX+20,yy,[w],13,MUTED if not ln.startswith(('Moskovitz','Tallinn','Schmidt','Jane','McClave','Series H','CERR','Good Ventures')) else INK,weight='bold' if ln.startswith(('Moskovitz','Tallinn','Schmidt','Jane','McClave','CERR','Good Ventures')) else 'normal')); yy+=16
        # the equity band: Anthropic → the Moskovitz bracket. 1/30 of the grant-pipe scale.
        BAND=int(pw(7.7e9)/30)   # ≈360 px
        by0=95
        s.append(f'<rect x="{AX+AW}" y="{by0}" width="{L-320-AX-AW}" height="{BAND}" fill="{RED}" opacity="0.32"/>')
        s.append(tspans(AX+AW+(L-320-AX-AW)/2,by0+BAND/2-6,['≤ $7.7B'],26,INK,anchor='middle',weight='bold'))
        s.append(tspans(AX+AW+(L-320-AX-AW)/2,by0+BAND/2+18,['stake, donated'],14,INK,anchor='middle',weight='bold'))
        s.append(tspans(AX+AW+(L-320-AX-AW)/2,by0+BAND/2+36,['drawn at 1/30 scale'],11,INK,anchor='middle'))
        # dashed: Tallinn (undisclosed) and DAF accounts (the same stake, if it sits there)
        for (y1,y2,lab,ly) in [(690,AY+600,'Tallinn: Series A lead; percentage undisclosed (ST98)',765),(1195,AY+1000,'or in a DAF account at SVCF/NPT: a possible route no source confirms; NPT took in $1.18B of closely held stock in 19 gifts in FY2025, donor and issuer unattributed (ST104, ST121)',1323)]:
            pipes.append(f'<path d="M{L-300},{y1} C{L-340},{y1} {AX+AW+40},{y2} {AX+AW},{y2}" fill="none" stroke="{RED}" stroke-width="8" stroke-dasharray="14 10"/>')
            s.append(tspans(L-300,ly,wrap(lab,60),12,RED,weight='bold',lh=14))
        s.append(tspans(R+MW,604,['Frontier AI companies, unnamed by METR → METR: free tokens, unquantified (K01).','Joe Benton, Anthropic alignment staff → METR, announced Sep 2 2026 (S13).'],12,MUTED,lh=14,anchor='end'))
        # bottom: bar chart (left) and two quote cards (right)
        VY=1400; s.append(f'<line x1="{AX}" y1="{VY-20}" x2="{R+MW}" y2="{VY-20}" stroke="{AXIS}"/>')
        s.append(tspans(AX,VY+14,['Two published bounds on the donated stake, at different dates'],20,INK,weight='bold'))
        s.append(tspans(AX,VY+38,wrap('Forbes\' Nov 2025 estimate for a stake it says moved in early 2025, vs the ceiling implied by "less than 0.8%" at the Series H valuation (ST32–ST33, ST92, IV10). No filing checked states the number of shares.',125),14,MUTED,lh=18))
        base=VY+380; maxh=300; vals=[('$500M',500e6,'early 2025 transfer','Forbes estimate, published Nov 2025, for the stake moved into "a nonprofit vehicle" (ST32–ST33)'),('≤ $7.7B',7.7e9,'ceiling at the May 2026 valuation','0.8% × $965B Series H post-money = $7.72B, a ceiling with no floor (ST92, IV10); "already skyrocketed in value" (Forbes)')]
        for i,(lab,v,when,sub) in enumerate(vals):
            bx=AX+120+i*420; bh=maxh*v/7.7e9; bw=220
            s.append(f'<rect x="{bx}" y="{base-bh:.0f}" width="{bw}" height="{bh:.0f}" rx="6" fill="{RED}" opacity="{0.45 if i else 0.75}"/>')
            s.append(tspans(bx+bw/2,base-bh-14,[lab],34,RED,anchor='middle',weight='bold'))
            s.append(tspans(bx+bw/2,base+26,[when],17,INK,anchor='middle',weight='bold'))
            for j,w in enumerate(wrap(sub,40)): s.append(tspans(bx+bw/2,base+48+j*16,[w],13,MUTED,anchor='middle'))
        s.append(f'<line x1="{AX+100}" y1="{base}" x2="{AX+900}" y2="{base}" stroke="{AXIS}"/>')
        s.append(tspans(AX+560,base-maxh*500e6/7.7e9-40,['≈15× at the ceiling, not measured growth'],14,MUTED,anchor='middle'))
        CX=1040; CW=320
        cards=[('Forbes, Nov 7 2025 (ST32–ST33)','"Their Anthropic stake (worth an estimated $500 million) was moved into a nonprofit vehicle in early 2025 so they could invest any \'significant financial return\' back into philanthropy and \'dispel any perception of conflict of interest,\' she says."','Phoebe Liu, Forbes, quoting Cari Tuna. The vehicle is not named. Forbes\' Apr 2026 reranking adds the only percentage bound found, "less than 0.8%" (ST92), which sets the $7.7B ceiling.'),
               ('Moskovitz on Bluesky, Mar 30, Apr 11 and Apr 12 2026 (ST110, ST112, ST113)','"Our Anthropic shares are entirely in our foundation - no personal benefit." · "all Anthropic holdings are in the foundation, dedicated to charity" · "we have about $20B more in the foundation … The foundation is invested in Anthropic as well." · next day: "not all (but still most) of the $20B is in the foundation"','Good Ventures Foundation\'s return to June 2025 lists two contributors and no direct gift of private stock (ST78–ST79); Coefficient\'s CEO: "not to us" (ST89). Which account holds them is unattributed.'),
               ('Moskovitz to Stratechery, Oct 20 2025 (ST118); elsewhere in the same interview: "I\'m a board observer at Anthropic"','"I\'m a chair of at Open Philanthropy and I\'m a business guy and I\'m also in the boardroom in at Anthropic and I know all the players. I\'m sure I\'m naive in some ways, but I think the collection of people is not quite that naive …"','Board observer, not a director, by his own account; Tallinn says the same of himself (ST41). Coefficient, on whose Board of Managers he sits (Tuna chairs it, ST124), makes grants to METR\'s parent, joint-project partner, pooled donor and contractor for their own programs. No motive is asserted.')]
        for i,(hd,q,sub) in enumerate(cards):
            cx=CX+i*(CW+15); cy=VY+2
            s.append(f'<rect x="{cx}" y="{cy}" width="{CW}" height="480" rx="12" fill="{RED}" opacity="0.08"/><rect x="{cx}" y="{cy}" width="6" height="480" rx="3" fill="{RED}"/>')
            hl=wrap(hd,34); s.append(tspans(cx+20,cy+28,hl,13,RED,weight='bold',lh=16))
            ql=wrap(q,32); qy=cy+28+len(hl)*16+14; s.append(tspans(cx+20,qy,ql,15,INK,lh=20,weight='bold'))
            s.append(tspans(cx+20,qy+len(ql)*20+12,wrap(sub,40),12,MUTED,lh=15))
    # the zero: dashed line above everything
    s.append(f'<path d="M{L},148 C{L+370},148 {L+970},220 {R+160},372" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="6 8"/>')
    s.append(tspans(L+20,42,['Direct: none found. No METR-named grant in Coefficient\'s 2,911-row index (Sep 11 2026) or Good Ventures\' 990-PFs to Jun 2025' if anth else 'Direct: none found. No METR-named grant in Coefficient\'s index or Good Ventures\' 990-PFs to Jun 2025'],18 if anth else 14,RED,weight='bold',anchor='start'))
    s=[('<g opacity="0.55">'+''.join(pipes)+'</g>') if x=='@@PIPES@@' else x for x in s]
    body=legend(([(RED,'Anthropic equity held by a funder: solid band = Moskovitz\'s donated stake, drawn at 1/30 of the grant-pipe scale; dashed = undisclosed or unattributed')] if anth else [])+[(BLUE,'Coefficient / Open Philanthropy awards (approved and paid by Coefficient\'s funding partners: Good Ventures Foundation, or accounts at SVCF and NPT whose principals are not public) and SFF / Tallinn recommendations, labelled as such (width: 6 px + 1.4 px per $1M)'),(GRAY,'Audacious Project commitment'),(YELLOW,'Grants booked in donor-advised funds\' and regrantors\' filings; donor inferred only where Tallinn\'s public ledger matches'),(ORANGE,'Relationship to METR: parent, partner, pooled donor, board, contractor, office (dashed: no grant on record)')])+f'<svg width="{W-44}" height="{int(SVGH*(W-44)/(W-120))}" viewBox="0 0 {W-120} {SVGH}">{"".join(s)}</svg>'
    idl=f'M01–M{len(M):02d} (research/money_flows.csv; Coefficient M01–M34, SFF M35–M48, Audacious M57–M58, Longview M59–M60, ARC transfer M63)'
    anth_note=(' Anthropic panel: investment facts are from Anthropic\'s own round announcements and court-supervised FTX estate sales (rows IV01–IV11, research/investments.csv, copied from the anthropic-investors pack); Moskovitz, Tallinn and Schmidt are named Series A investors with undisclosed amounts; Jane Street the firm bought $100M of shares in 2024 and joined four later rounds, while METR names "individuals from Jane Street" as donors, not the firm; no individual\'s current stake is public. Equity band: Moskovitz\'s stake is bounded only by Forbes\' "less than 0.8%" (ST92); 0.8% of the $965B Series H post-money is $7.7B, so the band is a ceiling, not a valuation, and it is drawn at 1/30 of the grant-pipe scale because at 1.4 px per $1M it would be about 10,800 px wide, five canvases. Forbes\' $500M is an estimate it published in Nov 2025 for a stake it says moved in early 2025 (ST32–ST33). Bar chart: same two rows. Anthropic named Moskovitz personally as the Series A investor; Coefficient\'s CEO says Coefficient never invested (ST89); the purchasing vehicle and the recipient of the donated shares are undisclosed. Moskovitz says the stake was donated (Berger: "not to us", ST89) and is "entirely in our foundation" (ST110, ST112–ST113), while Good Ventures Foundation\'s FY2025 990-PF lists every gift and none is private stock (ST78–ST79); Coefficient\'s own page names Good Ventures Foundation and accounts at the Silicon Valley Community Foundation and the National Philanthropic Trust as external funding partners that approve its grants, without naming the account principals (ST105), those accounts pay Coefficient\'s awards to the dollar (ST109), SVCF granted NPT $1.59B in 2024 (ST107) and NPT received $1.18B of closely held stock in 19 gifts in the year covering early 2025 and held $1B more at year-end (ST104, ST106), unattributed; Vanguard Charitable\'s posted FY2025 Schedule B names no issuer and its largest private-equity line in that window is $130M, so it is unresolved rather than excluded (ST133). Moskovitz (Stratechery, Oct 2025) and Tallinn (Postimees, 2026) each describe themselves as Anthropic board observers (ST118, ST41). CERR/Macroscopic, a Series A and B investor, lists Redwood and Longview as grantees and Apollo and Halcyon Venture Partners as investments (M139–M142). Good Ventures\' public book at Jun 30 2025 is an AI-infrastructure portfolio and its manager, Value Aligned Research Advisors, launched VAR AI Fund LP in March 2025 (ST100–ST102). Schmidt\'s Hillspire owns 20% of D.E. Shaw & Co. per Forbes, whose venture arm is a Series H investor (ST49, ST26). Tarbell: Coefficient awards of $816,000 (Nov 2024), $2,888,000 (Mar 2025) and $1,587,930 (Jul 2025) to the Tarbell Center for AI Journalism (TB02–TB04, research/tarbell_funding.csv), plus SFF recommendations of $520,000 (2024) and $783,000 (2025, incl. a conditional match; TB05–TB06); outlet chips count articles by Tarbell fellows classified as AI, by publisher tag where the outlet has one and otherwise by the bylines pack\'s title/slug keyword fallback, in each outlet\'s captured window; TIME, Lawfare and most of the others rest mainly on the keyword fallback, and most windows are partial, so the counts are not comparable full-year shares (TO01–TO06, research/tarbell_outlets.csv, which states the method and window per outlet). Tarbell fellowship rows establish affiliation and bylines, not editorial control. The per-share price strip that this panel used to carry now lives only in the share_ladder rows (LD01–LD22).' if anth else '')
    foot=(f'<b>Coverage:</b> Every number cites a row id in research/*.csv of the figure repo; money types are never summed: blue = Coefficient awards (index snapshot 2026-09-11) and SFF recommendations, grey = the Audacious commitment, yellow = grants filed by DAF sponsors and regrantors, orange = relationships. Pipe width is 6 px + 1.4 px per $1M, no cap. '+('The equity band is a ceiling, 0.8% × the $965B Series H valuation, drawn at 1/30 of the pipe scale; the SVCF/NPT accounts and the location of the donated stake are unattributed. ' if anth else '')+f'"None found" negatives are bounded to the sources named. Full notes, every source file, the e-files and four independent audits: github.com/kevinnbass/metr-money-figure (NOTES.md). {SRC}.')
    H=(2560 if anth else 1840)
    _raw=body+foot; body=strip_ids(body); foot=strip_ids(foot); _EXTRA={'M%02d'%i for i in list(range(1,34))+list(range(35,40))+[47,48,57,58,59,60,63]+list(range(77,97))+[104,117,118,119,126,127,128,143]}|{'AP46','AP47','AP48','AP49','ST107'}|({'TO0%d'%i for i in range(1,7)} if anth else set()); _ids=sorted(set(FC.STRIPPED_IDS)|set(collect_ids(_raw))|_EXTRA); foot=foot+'<!-- rows: '+' '.join(_ids)+' -->'; FC.STRIP_IDS=False
    render(STEM, shell((strip_ids('Funders that reach METR through ARC, RAND, Longview and pooled funds include Anthropic\'s Series A investors, two of them its board observers by their own account; Moskovitz donated a stake worth up to $7.7B at Anthropic\'s May 2026 valuation, a ceiling, to what he calls "our foundation", and no filing checked shows where it sits; no METR grant appears in Coefficient\'s index or Good Ventures\' filings to June 2025' if anth else 'Good Ventures Foundation, advised by Coefficient, has no METR grant on its books. Its grants reached METR\'s parent, partner, pooled donor and a board member\'s organization; ARC handed METR $4.55M at the spin-out, not attributable to any one ARC funder')),('Figure 10a (with Anthropic) · Funders → intermediaries → the evaluator, and the lab → the funders' if anth else 'Figure 10a · Funders → intermediaries → the evaluator'),strip_ids(('Dustin Moskovitz and Cari Tuna\'s philanthropy is the money: Good Ventures Foundation, their $10.1B endowment, and Coefficient\'s other funding partners, accounts at SVCF and NPT whose principals are not public, pay what Coefficient Giving recommends. No METR grant appears in Coefficient\'s index or the foundation\'s returns to June 2025; its grants went to METR\'s parent, joint-project partner, pooled-fund donor, a board member\'s organization, and the Tarbell Center, whose fellows write for TIME, The Verge and others. Moskovitz and Jaan Tallinn, both Anthropic board observers by their own account, bought into the 2021 Series A; Moskovitz donated his stake, under 0.8% of Anthropic, in 2025 to what he calls "our foundation". Forbes estimated it at $500M in Nov 2025; at the $965B Series H valuation of May 2026 the same bound is $7.7B, a ceiling, and no filing checked shows where it sits.' if anth else 'Good Ventures Foundation, Dustin Moskovitz and Cari Tuna\'s $10.1B endowment, is the money; Coefficient Giving recommends its grants, which the foundation or its funding partners pay. No METR-named grant appears in Coefficient\'s index or the foundation\'s returns to June 2025. Coefficient awarded ARC $1.5M; ARC, which had several funders, transferred $4.55M of evaluation-program assets to METR at the spin-out; Coefficient also funds METR\'s joint-project partner, pooled-fund donor and a board member\'s organization.')),body,foot,W,H,extra_css='body{padding:28px 22px 16px}.subtitle{max-width:2100px}'),W,H)

def fig_money_anth(): return fig_money(anth=True)

# ---------------------------------------------------------------- 10b. evaluated by the people you fund
def fig_evals():
    E=rows('evals.csv'); E=[r for r in E if r['lab']]
    shared={'E29','E30','E31','E32'}  # one Frontier Risk Report engagement, split by lab
    labs=['OpenAI','Anthropic','Google DeepMind','Amazon','Meta','xAI','DeepSeek','other']
    def lab_key(l):
        for k in labs:
            if k.lower() in l.lower(): return k
        return 'other'
    by={k:[] for k in labs}
    for r in E: by[lab_key(r['lab'])].append(r)
    by={k:v for k,v in by.items() if v}
    n=len(E); rowh=46; H=max(1100, 520+ n*rowh + 60*len(by)); W=2200; STEM='metr-02-evaluated-by-the-people-you-fund'
    tcol={'pre-deployment evaluation':BLUE,'post-release evaluation':BLUE250,'lab used METR tasks':AQUA,'external review of lab risk report':ORANGE,'incident investigation':RED,'not a partnership':GRAY,'none found':LGRAY}
    s=[]; y=40; L=60
    hdr=[('Date',L),('Model',L+130),('Engagement',L+560),('Cites METR',L+1000),('Quote from the lab document',L+1200),('METR report',L+1800)]
    for t,x in hdr: s.append(tspans(x,y,[t],16,MUTED,weight='bold'))
    y+=20
    for lab,items in by.items():
        y+=30; s.append(f'<rect x="{L-10}" y="{y-24}" width="{W-120}" height="36" rx="6" fill="#e9e5db"/>'); s.append(tspans(L,y,[f'{lab} · {len(items)} engagements'],21,INK,weight='bold')); y+=36
        for r in sorted(items,key=lambda r:r['date']):
            c=tcol.get(r['engagement_type'].strip().lower(),GRAY)
            s.append(f'<circle cx="{L+540}" cy="{y-7}" r="9" fill="{c}"/>')
            s.append(tspans(L,y,[r['date']],17,MUTED)); s.append(tspans(L+130,y,[r['model'][:36]+('…' if len(r['model'])>36 else '')],19,INK,weight='bold'))
            s.append(tspans(L+560,y,[r['engagement_type'][:48]+(' · shared FRR engagement' if r['row_id'] in shared else '')],17,INK))
            cites=r['lab_doc_cites_metr'].strip().lower()
            cc={'yes':AQUA,'no':RED,'unknown':GRAY}.get(cites,GRAY); ct={'yes':'✓ cites METR','no':'✗ no METR','unknown':'? not checked'}.get(cites,'?')
            s.append(tspans(L+1000,y,[ct],17,cc,weight='bold'))
            if r.get('quote'): s.append(tspans(L+1200,y,[('“'+r['quote'][:66]+'…”') if len(r['quote'])>66 else '“'+r['quote']+'”'],14,MUTED))
            s.append(tspans(L+1800,y,['published' if r['metr_report_url'].strip() else 'none public'],17,INK if r['metr_report_url'].strip() else MUTED))
            s.append(tspans(W-130,y,[r['row_id']],13,MUTED,anchor='end'))
            y+=rowh
    shared={'E29','E30','E31','E32'}  # one Frontier Risk Report engagement, split by lab
    noneng=[r for r in E if r['engagement_type'].strip().lower() in ('none found','not a partnership')]
    eng=[r for r in E if r not in noneng]; distinct=len(eng)-(len([r for r in eng if r['row_id'] in shared])-1)
    pre_rows=[r for r in eng if 'pre-deployment' in r['engagement_type'].lower()]; pre=len(pre_rows)-(len([r for r in pre_rows if r['row_id'] in shared])-1)
    yes=sum(1 for r in E if r['lab_doc_cites_metr'].strip().lower()=='yes'); docs=yes-1  # E26 and E29 cite the same Anthropic risk report
    kp=f'<div class="kpis"><div class="kpi"><div class="l">Distinct engagements</div><div class="v">{distinct}</div><div class="d">from {n} rows: the May 2026 Frontier Risk Report is one engagement across four labs (E29–E32); {len(noneng)} rows record no engagement</div></div><div class="kpi"><div class="l">Pre-deployment</div><div class="v">{pre}</div><div class="d">distinct engagements where METR saw a model before the public did</div></div><div class="kpi"><div class="l">Lab documents citing METR</div><div class="v">{docs}</div><div class="d">{yes} rows; E26 and E29 cite the same Anthropic risk report</div></div></div>'
    body=kp+legend([(BLUE,'Pre-deployment evaluation'),(BLUE250,'Post-release evaluation'),(AQUA,'Lab used METR tasks'),(ORANGE,'External review of lab risk report'),(RED,'Incident investigation'),(GRAY,'Not a partnership'),(LGRAY,'No engagement found')])+f'<svg width="{W-120}" height="{y+10}" viewBox="0 0 {W-120} {y+10}">{"".join(s)}</svg>'
    foot=f'<b>Coverage:</b> Every lab engagement located on metr.org/research, metr.org/blog, the 2024 annual report and Wikipedia, checked against the lab\'s own system card or risk document where one exists (rows E01–E{n:02d}, research/evals.csv; Codex source audit 2026-09-14). Rows are per lab; the Frontier Risk Report is one engagement drawn in four lanes and counted once. "Cites METR" was determined by searching the lab document text; "not checked" means the document could not be fetched or identified; E30\'s "yes" is a generic link to METR\'s frontier-safety page, not a citation of the report. METR is paid by none of these labs; they supply free tokens and pre-release access (metr.org/about). Labs cite METR in their own safety documents, and METR now investigates the same labs\' incidents. {SRC}.'
    render(STEM, shell('Evaluated by the people you cite: every METR engagement with a frontier lab, and whether the lab\'s own document names METR','Figure 10b · 2023–2026','METR tests the labs\' models before release on the labs\' free tokens; the labs quote METR in system cards; METR now audits the labs\' incidents.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10c. Christiano's hats
def fig_christiano():
    W=2200; STEM='metr-03-christianos-hats'
    C=[r for r in rows('christiano.csv') if not r['role'].lower().startswith('spouse')]; E=rows('evals.csv')
    def ym(s):
        s=(s or '').strip()
        if len(s)>=7: y,m=s[:7].split('-')[:2]; return int(y)+(int(m)-1)/12
        if len(s)>=4 and s[:4].isdigit(): return int(s[:4])+0.0
        return None
    t0,t1=2017.0,2026.95; L,R=460,W-140; x=lambda t:L+(R-L)*(t-t0)/(t1-t0)
    types=[('lab','Frontier lab'),('funder','Funder'),('safety org','ARC / METR'),('lab governance','Lab governance'),('government','Government'),('lab foundation','Lab foundation')]
    col={'lab':RED,'funder':BLUE,'safety org':ORANGE,'lab governance':RED,'government':AQUA,'lab foundation':RED}
    # assign one sub-row per role, grouped by type
    order=[]; 
    for k,name in types:
        items=[r for r in C if (r['org_type'].strip().lower() if r['org_type'].strip().lower() in col else 'safety org')==k]
        items.sort(key=lambda r: ym(r['start']) or 0)
        order.append((k,name,items))
    rowh=78; y0=110; s=[]; y=y0; lane_y={}
    for k,name,items in order:
        if not items: continue
        top=y; 
        for r in items:
            lane_y[r['row_id']]=y; y+=rowh
        s.append(f'<rect x="{L-440}" y="{top-30}" width="{R-L+440}" height="{y-top-14}" rx="8" fill="{col[k]}" opacity="0.06"/>')
        s.append(tspans(L-420,top+8,[name],20,INK,weight='bold'))
    Hsvg=y+120
    for yr in range(2017,2027):
        X=x(yr); s.append(f'<line x1="{X:.1f}" y1="{y0-40}" x2="{X:.1f}" y2="{y}" stroke="{GRID}"/>'+tspans(X,y0-52,[str(yr)],17,MUTED,anchor='middle'))
    for r in C:
        k=r['org_type'].strip().lower(); k=k if k in col else 'safety org'; c=col[k]
        a=ym(r['start']); b=ym(r['end']); openended=b is None
        if a is None: continue
        if b is None: b = t1 if a>=2026 else a+1.0
        if r['end'].strip() and len(r['end'].strip())==4: b=int(r['end'])+0.99
        Y=lane_y[r['row_id']]
        dash=' stroke-dasharray="8 6" stroke="'+INK+'" stroke-width="2" fill-opacity="0.35"' if (openended and a<2026) else ''
        s.append(f'<rect x="{x(a):.1f}" y="{Y-14}" width="{max(10,x(b)-x(a)):.1f}" height="30" rx="7" fill="{c}" opacity="0.9"{dash}/>')
        lab=f'{r["role"].split("(")[0].strip()}, {r["organization"].split("(")[0].strip()}'+(' · end not public' if (openended and a<2026) else '')
        if x(a) > R-700: s.append(tspans(x(b),Y-22,[lab[:80]],16,INK,anchor='end',weight='bold'))
        else: s.append(tspans(x(a),Y-22,[lab[:80]],16,INK,weight='bold'))
        s.append(tspans(x(a)-8,Y+8,[r['row_id']],13,MUTED,anchor='end'))
    Yt=y+40
    s.append(f'<line x1="{L}" y1="{Yt}" x2="{R}" y2="{Yt}" stroke="{AXIS}"/>'+tspans(L-16,Yt+6,['METR evaluates OpenAI / Anthropic'],17,INK,anchor='end',weight='bold'))
    for r in E:
        t=ym(r['date'])
        if t is None or not any(k in r['lab'] for k in ('OpenAI','Anthropic')): continue
        c=RED if 'OpenAI' in r['lab'] else BLUE
        s.append(f'<line x1="{x(t):.1f}" y1="{Yt-14}" x2="{x(t):.1f}" y2="{Yt+14}" stroke="{c}" stroke-width="3"/>')
    H=Hsvg+430
    body=legend([(RED,'OpenAI roles and OpenAI-related bodies / red ticks: OpenAI evals'),(BLUE,'Funder role / blue ticks: Anthropic evals'),(ORANGE,'ARC, which incubated METR'),(AQUA,'Government')])+f'<svg width="{W-120}" height="{Hsvg}" viewBox="0 0 {W-120} {Hsvg}">{"".join(s)}</svg>'
    n=len(rows('christiano.csv'))
    foot=f'<b>Coverage:</b> One person\'s roles from public announcements, org pages and press (rows C01–C{n:02d}, research/christiano.csv); dates to the month where sources give them, else to the year; dashed bars have no public end date and are drawn one year long. The Sep 2023 spin-out post said Christiano had declined a planned METR board seat; METR\'s own team pages then listed him as technical advisor and board member from at least Dec 28 2023 to Mar 3 2024 and dropped him by Mar 24 2024 (Wayback copies in research/wayback-metr-team/), three weeks before his US AISI appointment was announced, so C06 is drawn Dec 2023 to Mar 2024. Each role is its own bar, so overlaps are visible; overlap is a fact about dates, not an allegation about conduct. The CAISI step-back is bracketed by Transformer\'s 16 Jul 2026 reference to him as head of AI safety, Veronica Irwin\'s 3 Aug report that he had moved to a part-time advisor role, and his own 4 Aug post "Returning to ARC", whose footnote says he continues "as a special government employee one day a week" (C08, C13, IF114–IF115). His 9 Sep OpenAI Foundation board announcement (2.8M views, IF116) came two hours before Anthropic named METR its investigator (D-rows). Ticks are METR and ARC Evals engagements with OpenAI and Anthropic from research/evals.csv. {SRC}.'
    render(STEM, shell('Paul Christiano\'s hats: OpenAI, Open Phil adviser, ARC founder, Anthropic trustee, US safety chief, ARC again, OpenAI Foundation','Figure 10c · 2017–2026','The founder of the organization that became METR has held a seat at nearly every table METR\'s work touches. On Aug 26 2026 METR and Redwood published their investigation of OpenAI\'s Hugging Face incident; on Sep 9 OpenAI seated Christiano on the OpenAI Foundation board (E35, C11). One bar per role; ticks are METR evaluations of OpenAI and Anthropic models.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10d. the evaluator's board
def fig_board():
    B=[r for r in rows('board.csv') if 'supplement' not in r['name']]; n=len(B); W=2200; H=max(1000, 500+math.ceil(n/4)*400); STEM='metr-04-the-evaluators-board'
    html='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:6px">'
    for r in B:
        role=r['metr_role']; c=BLUE if 'Board' in role or 'board' in role else (AQUA if role in ('CEO','President','Chief Scientist','CTO') else GRAY)
        html+=f'<div style="background:#efece4;border-radius:10px;padding:16px 20px;border-top:6px solid {c}"><div style="font-size:15px;color:{MUTED};font-weight:bold;letter-spacing:1px;text-transform:uppercase">{esc(role)} · {r["row_id"]}</div><div style="font-size:26px;font-weight:bold;margin:4px 0 6px">{esc(r["name"])}</div>'
        html+=f'<div style="font-size:17px;line-height:1.35"><b>Came from:</b> {esc(r["prior_affiliations"])}</div>'
        if r['other_current_org'].strip(): html+=f'<div style="font-size:17px;line-height:1.35;margin-top:6px"><b>Also:</b> {esc(r["other_org_role"])}, {esc(r["other_current_org"])}</div>'
        if r['other_org_funders'].strip(): html+=f'<div style="font-size:17px;line-height:1.35;margin-top:6px;color:{BLUE}"><b>That org\'s funders:</b> {esc(r["other_org_funders"])}</div>'
        if r['other_org_lab_ties'].strip(): html+=f'<div style="font-size:17px;line-height:1.35;margin-top:6px;color:{RED}"><b>Lab ties:</b> {esc(r["other_org_lab_ties"])}</div>'
        html+='</div>'
    html+='</div>'
    body=legend([(AQUA,'Officer'),(BLUE,'Board member'),(GRAY,'Advisor')])+html
    foot=f'<b>Coverage:</b> Second pass 2026-09-14 (B15–B17, M132–M138): board member Rajiv Dattani\'s AIUC sells certification and liability insurance whose standard requires certified companies to "appoint expert third parties to evaluate" their systems quarterly, took a $15M seed round that included Anthropic co-founder Ben Mann, and lists Halcyon Futures as having "invested in every round"; board member Adam Gleave\'s FAR.AI counts the Frontier Model Forum\'s AI Safety Fund, supported by Anthropic, Google, Microsoft and OpenAI, among its principal supporters and did 80 hours of paid-or-unpaid red-teaming for OpenAI\'s GPT-5; advisor Marco Mascorro left a16z between April and September 2026 while metr.org still calls him a partner, having led a16z\'s $2B seed in Thinking Machines, where advisor Alec Radford advises. Everyone listed under leadership, board and advisors on metr.org/about as of 2026-09-13, officers and directors in the FY2024 Form 990, and the former advisors and board members that metr.org keeps on its former-team pages (B10–B14) (rows B01–B{n:02d}, research/board.csv). Christiano\'s seat (B11) is dated from Wayback copies of METR\'s team pages, Dec 2023 to Mar 2024, after the Sep 2023 post that said he had declined it. Prior affiliations are from the person\'s own METR page, org bios and press. Funder amounts for other organizations are Coefficient awards from the index snapshot 2026-09-11 and SFF recommendations, to those organizations, not to the person. A board seat at an evaluator and a stake in a business that depends on evaluation is a structural overlap; the figure records it and states no motive. {SRC}.'
    render(STEM, shell('The evaluator\'s board: where METR\'s officers, directors and advisors came from and what else they run','Figure 10d · metr.org/about, Sep 2026','Each card is one person on METR\'s leadership, board or advisor list, with their prior lab or funder, their other organization, and who funds that organization.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10e. free tokens are not free
def fig_tokens():
    W,H=2200,1150; STEM='metr-05-free-tokens-are-not-free'
    F=rows('finances.csv'); K=rows('compute_inkind.csv'); G=rows('budget.csv')
    def get(measure,fy=None):
        for r in F:
            if measure in r['measure'].lower() and (fy is None or str(r['fiscal_year']).startswith(str(fy))): return num(r['value_usd']), r['row_id']
        return 0,''
    rev,rid=get('total revenue',2024); exp,eid=get('total expenses',2024); con,cid=get('contributions',2024)
    quant=[r for r in K if r['quantified'].strip().lower()=='yes']
    s=[]; L=380; base=760; scale=lambda v: v/ max(rev,1) * 520
    bars=[('Cash revenue FY2024',rev,BLUE,rid),('Cash expenses FY2024',exp,BLUE250,eid),('Free lab tokens + pre-release access',None,RED,','.join(r['row_id'] for r in K))]
    for i,(name,v,c,idx) in enumerate(bars):
        X=L+i*520
        if v is not None:
            h=scale(v); s.append(f'<rect x="{X}" y="{base-h:.1f}" width="360" height="{h:.1f}" rx="8" fill="{c}"/>'+tspans(X+180,base-h-16,[money(v)],30,INK,anchor='middle',weight='bold'))
        else:
            s.append(f'<rect x="{X}" y="{base-520}" width="360" height="520" rx="8" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="14 10"/>'+tspans(X+180,base-260,['?'],120,c,anchor='middle',weight='bold')+tspans(X+180,base-150,['no annual value disclosed by METR or any lab','only figure: ~$400K OpenAI API credits','for one six-day investigation (K05)'],18,MUTED,anchor='middle'))
        s.append(tspans(X+180,base+36,[name],20,INK,anchor='middle',weight='bold')+tspans(X+180,base+62,[idx],14,MUTED,anchor='middle'))
    s.append(f'<line x1="{L-40}" y1="{base}" x2="{L+3*520}" y2="{base}" stroke="{AXIS}"/>')
    q=[r for r in K if r['statement'].strip()][:4]
    html='<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px 26px;margin-top:8px">'+''.join(card(f'{esc(r["lab"])} · {esc(r["date"])} · {r["row_id"]}',f'“{esc(r["statement"])}”',RED if r["quantified"].strip().lower()!="yes" else AQUA,18) for r in q)+'</div>'
    body=f'<svg width="{W-120}" height="840" viewBox="0 0 {W-120} 840">{"".join(s)}</svg>'+html
    foot=f'<b>Coverage:</b> Cash figures are Form 990 FY2024 lines (rows {rid}, {eid}, {cid}, research/finances.csv). The third bar is deliberately empty: METR says frontier companies "provide a significant amount of free tokens for our evaluations, research, and engineering" and lists pre-release model access, but neither METR nor any lab publishes a dollar value or token volume (rows in research/compute_inkind.csv; the ~$400K estimate is K05, the data volumes OpenAI supplied are K04; {len(quant)} quantified statements found). A Form 990 does not require in-kind API access to be booked. "Not free" here means the input is supplied by the parties being evaluated; it is not a claim that the tokens have influenced a result. {SRC}.'
    render(STEM, shell('Free tokens are not free: METR\'s cash is public, the labs\' in-kind compute is not','Figure 10e · FY2024 Form 990 vs. undisclosed in-kind','METR reports its donations to the IRS. The tokens and pre-release access it gets from the companies it evaluates have no published value.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10f. same day, three moves
def fig_sep9():
    W,H=2200,2000; STEM='metr-06-same-day-three-moves'
    D0=[r for r in rows('sep9.csv') if r['utc_time'].strip()]
    dateline=[r for r in D0 if r['utc_time'].strip().endswith('00:00:00') or not r['utc_time'].startswith('2026-09-09')]
    D=[r for r in D0 if not r['utc_time'].strip().endswith('00:00:00') and r['utc_time'].startswith('2026-09-09')]
    def sec(t):
        h,m,s_=t.strip()[11:19].split(':'); return int(h)*3600+int(m)*60+int(s_)
    D=sorted(D,key=lambda r:sec(r['utc_time']))
    t0=min(sec(r['utc_time']) for r in D)-600; t1=max(sec(r['utc_time']) for r in D)+900
    L,R,top=280,W-180,200; x=lambda t:L+(R-L)*(t-t0)/(t1-t0)
    lanes=[('Coefficient','Coefficient Giving'),('Dwarkesh','Dwarkesh Patel'),('Anthropic','Anthropic'),('METR','METR and METR-bound'),('other','Others')]
    def lane(r):
        a=r['actor'].lower(); aff=r['actor_affiliation'].lower()
        if 'coefficient' in a or 'oehlsen' in a or aff.startswith('coefficient giving'): return 'Coefficient'
        if 'dwarkesh' in a: return 'Dwarkesh'
        if 'metr' in a or 'metr' in aff: return 'METR'
        if a.strip().startswith('anthropic'): return 'Anthropic'
        return 'other'
    ly={k:top+90+i*215 for i,(k,_) in enumerate(lanes)}
    col={'Coefficient':BLUE,'Dwarkesh':GRAY,'Anthropic':RED,'METR':AQUA,'other':GRAY}
    s=[]
    for hh in range(t0//3600, t1//3600+1, 2):
        T=hh*3600
        if t0<=T<=t1: s.append(f'<line x1="{x(T):.1f}" y1="{top}" x2="{x(T):.1f}" y2="{top+1120}" stroke="{GRID}"/>'+tspans(x(T),top+1150,[f'{hh:02d}:00 UTC'],17,MUTED,anchor='middle'))
    for k,name in lanes:
        Y=ly[k]; s.append(f'<line x1="{L}" y1="{Y}" x2="{R}" y2="{Y}" stroke="{AXIS}"/>'+tspans(L-16,Y+6,[name],19,INK,anchor='end',weight='bold'))
    def clean(t):
        t=re.sub(r'\s*\((?:[^()]*(?:Wayback|curl|jina|timestamp|payload|API|conversation_id|same second|not a reply|page shows)[^()]*)\)','',t)
        return re.sub(r'\s+',' ',t).strip(' ;:')
    # merge same-second posts in the same lane into one label
    merged=[]; skip=set()
    for i,r in enumerate(D):
        if r['row_id'] in skip: continue
        twins=[q for q in D[i+1:] if lane(q)==lane(r) and q['utc_time']==r['utc_time']]
        for q in twins: skip.add(q['row_id'])
        merged.append((r,twins))
    last={}
    for r,twins in merged:
        k=lane(r); X=x(sec(r['utc_time'])); Y=ly[k]; c=col[k]
        s.append(f'<circle cx="{X:.1f}" cy="{Y}" r="12" fill="{c}" stroke="{BG}" stroke-width="2"/>')
        idx=last.get(k,0); last[k]=idx+1
        dy=[-52,44,-104,96,-150][idx%5]
        v=fmt_views(r['views'])+' views' if num(r['views']) else ''
        anc='end' if X>R-760 else 'start'; tx=X-16 if anc=='end' else X+16
        ev=wrap(clean(r['event']),78)[:2]
        lines=[f'{r["utc_time"][11:16]} · {ev[0]}']+ev[1:]
        s.append(tspans(tx,Y+dy,lines,16,INK,weight='bold',anchor=anc,lh=19))
        tw=(' · +'+', '.join(f'{q["row_id"]} same second, {fmt_views(q["views"])} views' for q in twins)) if twins else ''
        s.append(tspans(tx,Y+dy+19*len(lines),[f'{r["actor"]}{(" · "+v) if v else ""} · {r["row_id"]}{tw}'],14,MUTED,anchor=anc))
    box='<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px 24px;margin-top:4px">'+''.join(card(f'{esc(r["actor"])} · {"same day, time not published" if r["utc_time"].startswith("2026-09-09") else "not Sep 9 UTC: "+r["utc_time"][:16]+" UTC"} · {r["row_id"]}',esc((lambda t: t if len(t)<=330 else t[:330].rsplit('. ',1)[0]+'.')(clean(r["event"].split(". Native-IP")[0]))),GRAY,17) for r in dateline)+'</div>'
    body=legend([(BLUE,'Coefficient Giving'),(RED,'Anthropic'),(AQUA,'METR and METR-bound'),(GRAY,'Others')])+f'<svg width="{W-120}" height="{top+1180}" viewBox="0 0 {W-120} {top+1180}">{"".join(s)}</svg>'+box
    foot=f'<b>Coverage:</b> Every Sep 9, 2026 post and page located (rows D01–D{len(rows('sep9.csv')):02d}, research/sep9.csv; five accounts searched and not found are listed there too). Timestamps are fxtwitter payload created_at values for posts and page metadata or first Wayback capture for web pages, all UTC; views as fetched 2026-09-13. Same-day sequence is a fact about the calendar. No document links Coefficient\'s Tailwind launch to Anthropic\'s announcement, and Dwarkesh Patel\'s post quote-posted Tailwind, not Anthropic. Two further Coefficient-staff posts that day are drawn from the G12 lane: Anuja Uppuluri at 15:34 ("After leaving Anthropic, I\'ve been working on Tailwind", D21) and Catherine Brewer at 21:17 ("metr just can\'t stop winning", D22). {SRC}.'
    render(STEM, shell('Same day, four moves: Coefficient launches a founder fund, a podcaster names METR "the evaluator", Anthropic hands METR the investigation, OpenAI seats METR\'s founding patron','Figure 10f · September 9, 2026, hour by hour','One Tuesday, UTC. Coxon\'s resignation post at 00:04, Coefficient\'s Project Tailwind at 15:03 (its initiatives list asks for incident investigators and independent auditors, naming METR), Dwarkesh Patel\'s "tap a blade on each of METR\'s shoulders" at 15:24, Anthropic\'s assessment at 19:02, METR\'s confirmation at 19:15. Below: same-day items with no published time.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10g. who gets ordained
def fig_finra():
    P=rows('finra_proposals.csv'); n=len(P); W=2200; H=max(1000, 400+n*100); STEM='metr-07-who-gets-ordained'
    s=[]; y=30; L=60
    for t,xx in [('Date',L),('Who',L+150),('Proposal',L+620),('Supervisor',L+1120),('Who examines the models',L+1450),('Names METR?',L+1900)]: s.append(tspans(xx,y,[t],16,MUTED,weight='bold'))
    y+=34
    for r in sorted(P,key=lambda r:r['date']):
        nm=r['names_metr'].strip().lower(); c={'yes':AQUA,'no':RED}.get(nm,GRAY)
        s.append(f'<rect x="{L-10}" y="{y-26}" width="{W-120}" height="88" rx="8" fill="#efece4"/>')
        s.append(tspans(L,y,[r['date']],17,MUTED)+tspans(L,y+24,[r['row_id']],13,MUTED))
        s.append(tspans(L+150,y,wrap(r['author_or_body'],34)[:2],19,INK,weight='bold',lh=22)+tspans(L+150,y+48,wrap(r['affiliation'],40)[:2],15,MUTED,lh=18))
        s.append(tspans(L+620,y,wrap(r['title'],42)[:3],17,INK,lh=21))
        s.append(tspans(L+1120,y,wrap(r['proposed_supervisor'],28)[:3],17,INK,lh=21))
        s.append(tspans(L+1450,y,wrap(r['proposed_examiner'],38)[:3],17,INK,lh=21))
        s.append(f'<circle cx="{L+1920}" cy="{y-6}" r="11" fill="{c}"/>'+tspans(L+1940,y,[{'yes':'yes','no':'no'}.get(nm,'n/a')],18,c,weight='bold'))
        y+=100
    yes=sum(1 for r in P if r['names_metr'].strip().lower()=='yes')
    body=legend([(AQUA,'Names METR'),(RED,'Does not name METR'),(GRAY,'Not a proposal (commentary)')])+f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}">{"".join(s)}</svg>'
    foot=f'<b>Coverage:</b> Every 2026 "FINRA for AI" proposal, framework, report or bill located (rows F01–F{n:02d}, research/finra_proposals.csv), read in full for the sentence that says who examines the models. {yes} of {n} name METR: Dwarkesh Patel (F15) presumes it, Amodei (F16) proposes embedding evaluators "such as METR", Sacks (F19) rejects it as not independent, and the Examiner report (F20) relays Sacks. No institutional proposal, bill or framework names any examiner. Incumbency is inferred by readers and by two CEOs, not asserted by any proposal. {SRC}.'
    render(STEM, shell('Who gets ordained: 22 documents on a "FINRA for AI", and the only ones that say METR are a podcaster, Dario Amodei and David Sacks','Figure 10g · July–September 2026','Each row is one proposal for a self-regulatory body over frontier AI, with the body it would answer to, who it says would run the evaluations, and whether it names METR.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10h. revolving door into the referee
def fig_staff():
    S=rows('staff_origins.csv'); W=2200; STEM='metr-08-revolving-door-into-the-referee'
    col={'frontier lab':RED,'funder':BLUE,'safety nonprofit':ORANGE,'government':AQUA,'other company':GRAY,'academia':GRAY,'other nonprofit':YELLOW}
    allin=[r for r in S if r['prior_org'].strip().upper()!='METR' and not r['metr_title'].startswith('(reverse)')]
    nonstaff=[r for r in allin if any(k in r['metr_title'] for k in ('Advisor','Collaborator','Contractor'))]
    into=[r for r in allin if r not in nonstaff]
    outof=[r for r in S if r['metr_title'].startswith('(reverse)')]
    def ptype(r):
        t=r['prior_org_type'].strip().lower(); return t if t in col else 'other company'
    order=['frontier lab','funder','safety nonprofit','government','other nonprofit','other company','academia']
    groups={k:[r for r in into if ptype(r)==k] for k in order}
    # three columns: labs+funder | safety+gov | other+academia ; fourth: reverse
    cols=[['frontier lab','funder','government'],['safety nonprofit','other nonprofit'],['other company','academia']]
    colw=500; gap=30; L=60; rowh=40; s=[]; maxy=0
    def first(org): return org.split(';')[0].split('(')[0].strip()
    for ci,ks in enumerate(cols):
        x=L+ci*(colw+gap); y=30
        for k in ks:
            items=sorted(groups[k],key=lambda r:(first(r['prior_org']),r['name'])); c=col[k]
            if not items: continue
            h=len(items)*rowh+50
            s.append(f'<rect x="{x-10}" y="{y-24}" width="{colw}" height="{h}" rx="8" fill="{c}" opacity="0.08"/><rect x="{x-10}" y="{y-24}" width="8" height="{h}" rx="3" fill="{c}"/>')
            s.append(tspans(x+10,y+4,[{'frontier lab':'From a frontier lab','funder':'From a funder','safety nonprofit':'From a safety nonprofit','government':'From government','other company':'From another company','academia':'From academia','other nonprofit':'From another nonprofit'}[k]+f' · {len(items)}'],20,INK,weight='bold')); y+=40
            for r in items:
                s.append(tspans(x+10,y,[r['name']],17,INK,weight='bold')+tspans(x+215,y,[first(r['prior_org'])[:30]],16,MUTED)+tspans(x+colw-20,y,[r['row_id']],12,MUTED,anchor='end'))
                y+=rowh
            y+=30
        maxy=max(maxy,y)
    # reverse column
    x=L+3*(colw+gap); y=30; c=INK
    h=len(outof)*62+50
    s.append(f'<rect x="{x-10}" y="{y-24}" width="{W-120-x+10}" height="{h}" rx="8" fill="{INK}" opacity="0.06"/><rect x="{x-10}" y="{y-24}" width="8" height="{h}" rx="3" fill="{INK}"/>')
    s.append(tspans(x+10,y+4,[f'Left METR for a lab or government · {len(outof)}'],20,INK,weight='bold')); y+=40
    for r in sorted(outof,key=lambda r:r['joined']):
        dest=r['metr_title'].replace('(reverse) ','').split('->')[-1].strip()
        s.append(tspans(x+10,y,[r['name']],17,INK,weight='bold')+tspans(x+10,y+20,[('→ '+dest)[:52]],14,MUTED)+tspans(x+10,y+36,[f'{r["joined"] or "date n/a"} · {r["row_id"]}'],12,MUTED)); y+=62
    maxy=max(maxy,y)
    named=[r for r in into if not r['prior_org'].strip().startswith('(')]; n=len(named); labs=len(groups['frontier lab']); fund=len(groups['funder']); safe=len(groups['safety nonprofit'])
    H=460+maxy
    kp=f'<div class="kpis"><div class="kpi"><div class="l">Staff with a named prior employer</div><div class="v">{n}</div><div class="d">current and former staff records ({len(into)-n} without a named employer); {len(nonstaff)} advisor, contractor and collaborator rows shown separately (S29, S42, S43)</div></div><div class="kpi"><div class="l">From frontier labs</div><div class="v">{labs}</div><div class="d">OpenAI, Anthropic, Google DeepMind</div></div><div class="kpi"><div class="l">From the funders</div><div class="v">{fund}</div><div class="d">Open Philanthropy / Coefficient, Longview</div></div><div class="kpi"><div class="l">From funder-backed safety orgs</div><div class="v">{safe}</div><div class="d">Redwood, MIRI, MATS, CAIS, GovAI, FHI, CLR, Transluce</div></div></div>'
    body=kp+legend([(RED,'Frontier lab'),(BLUE,'Funder'),(ORANGE,'Safety nonprofit'),(AQUA,'Government'),(YELLOW,'Other nonprofit'),(GRAY,'Other company or academia')])+f'<svg width="{W-120}" height="{maxy+10}" viewBox="0 0 {W-120} {maxy+10}">{"".join(s)}</svg>'
    foot=f'<b>Coverage:</b> Only people whose prior employer is stated on metr.org, in METR\'s 2024 annual report, in the FY2024 Form 990 or in press (rows S01–S{len(S):02d}, research/staff_origins.csv), current and former staff; the advisor, contractor and collaborator rows (S29, S42, S43) are excluded from the staff count. METR publishes no staff list with histories, so this is a floor, not a census, and a mixed current-and-former set is not comparable to the current headcount of ~35–38. Organization types per the Codex source audit 2026-09-14. The first listed prior employer is shown; several people had earlier lab or safety-org roles listed second. The right column is the door the other way: former METR staff and advisors now at a lab or in government. Leaving a lab for its evaluator is the direction METR itself advertises. Names are already public in those sources. {SRC}.'
    render(STEM, shell('The revolving door into the referee: where METR\'s named staff worked before, and where its alumni went','Figure 10h · 2022–2026','Every METR person whose previous employer is on the public record, grouped by that employer\'s type, and the six who left METR for a lab, a lab foundation or a government post.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10j. Barnes in TIME by a Tarbell fellow
def fig_time():
    T=rows('time_metr.csv'); W=2200; H=max(950, 420+len(T)*62); STEM='metr-10-barnes-in-time-by-a-tarbell-fellow'
    s=[]; y=30; L=60
    for t,xx in [('Date',L),('Outlet',L+130),('Headline',L+330),('Byline',L+1180),('Tarbell fellow',L+1480),('Discloses',L+1720)]: s.append(tspans(xx,y,[t],16,MUTED,weight='bold'))
    y+=34
    for r in sorted(T,key=lambda r:r['date']):
        tf=r['tarbell_fellow'].strip().lower()=='yes'; dl=r['disclosure_line'].strip().lower()
        c=BLUE if tf else GRAY
        s.append(f'<rect x="{L-10}" y="{y-24}" width="{W-120}" height="52" rx="8" fill="{"#e6eefb" if tf else "#efece4"}"/>')
        s.append(tspans(L,y,[r['date']],16,MUTED)+tspans(L+130,y,[r['outlet'][:18]],17,INK)+tspans(L+330,y,[r['title'][:78]],18,INK,weight='bold')+tspans(L+1180,y,[r['byline'][:26]],17,INK))
        s.append(f'<circle cx="{L+1490}" cy="{y-6}" r="10" fill="{c}"/>'+tspans(L+1510,y,['Tarbell fellow' if tf else 'no'],16,c,weight='bold'))
        s.append(tspans(L+1720,y,[{'yes':'yes','no':'no disclosure'}.get(dl,'?')],16,RED if dl=='no' else INK)+tspans(W-130,y,[r['row_id']],13,MUTED,anchor='end'))
        y+=62
    tfn=sum(1 for r in T if r['tarbell_fellow'].strip().lower()=='yes'); nd=sum(1 for r in T if r['tarbell_fellow'].strip().lower()=='yes' and r['disclosure_line'].strip().lower()=='no')
    kp=f'<div class="kpis"><div class="kpi"><div class="l">Coefficient → Tarbell Center</div><div class="v">$6.29M</div><div class="d">four awards 2023–25 (TB01–TB04); SFF recommended $1.3M more (TB05–TB06)</div></div><div class="kpi"><div class="l">Articles about METR or Barnes</div><div class="v">{len(T)}</div><div class="d">TIME, The Verge, Platformer, 2024–26</div></div><div class="kpi"><div class="l">By Tarbell fellows</div><div class="v">{tfn}</div><div class="d">roster: 01-tarbell-bylines/research/roster.csv</div></div><div class="kpi"><div class="l">Without a Tarbell line</div><div class="v">{nd}</div><div class="d">of the {tfn} fellow-written pieces</div></div></div>'
    body=kp+f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}">{"".join(s)}</svg>'
    foot=f'<b>Coverage:</b> Articles located by site search and author pages at TIME, The Verge and Platformer that mention METR or Beth Barnes, Sep 2024–Sep 2026 (rows T01–T{len(T):02d}, research/time_metr.csv); not a census of all coverage; as a denominator, Harry Booth\'s TIME author page lists 38 articles in the window, of which 3 plus the two Barnes profiles mention METR. "Tarbell fellow" means the byline appears on the Tarbell Center roster; Booth is listed as a 2024–25 fellow placed at TIME (01-tarbell-bylines/research/roster.csv, row for Harry Booth). Tarbell\'s funders: Coefficient $6.29M in four awards 2023–25, SFF recommendations of $520K (2024) and $783K (2025), plus FLI, EA Infrastructure Fund and Longview listed without amounts (research/tarbell_funding.csv TB01–TB06). Tarbell says its donors have no editorial control; a fellow profiling the head of an evaluator funded by the same donor network is a disclosure question, not a claim the profile is wrong. Extends coxon-09. {SRC}.'
    render(STEM, shell('Both TIME100 AI profiles of METR\'s CEO were written by a fellow of a journalism program that Coefficient funds; neither told readers so','Figure 10j · 2024–2026 · a disclosure gap, not a claim about the profiles','The chain: Coefficient Giving, the funder behind METR\'s parent, partners and pooled funds, gave $6.29M to the Tarbell Center, which places fellows at outlets including TIME. Tarbell fellow Harry Booth wrote TIME\'s 2024 and 2026 TIME100 AI profiles of Beth Barnes; six of nine METR articles at three outlets were by Tarbell fellows. None carried a disclosure line. Tarbell says its donors have no editorial control, and nothing here says the profiles are wrong.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10k. same donors both sides
def fig_donors():
    J=rows('shared_donors.csv'); W=2200; STEM='metr-11-same-donors-both-sides-of-the-table'
    def cls(r):
        t=r['gives_to_or_invests_in_lab'].lower()
        if t.startswith('none of these') or t.startswith('no '): return 'none'
        if t.startswith('indirect'): return 'aff'
        if 'board member of evaluator' in t or 'evaluator-network' in t: return 'evl'
        if any(k in t for k in ('series a','series b','series e','series f','investor','secondary')): return 'inv'
        if any(k in t for k in ('affiliation','funded largely','not researched','employee')): return 'aff'
        return 'none'
    col={'inv':RED,'aff':YELLOW,'evl':ORANGE,'none':GRAY}; rank={'inv':0,'aff':1,'evl':2,'none':3}
    drawn=[r for r in J if cls(r)!='none']; rest=[r for r in J if cls(r)=='none']; H=max(1000, 520+len(drawn)*96)
    s=[]; y=30; L=60
    s.append(tspans(L,y,['Donor'],16,MUTED,weight='bold')+tspans(L+520,y,['Gives to METR'],16,MUTED,weight='bold')+tspans(L+900,y,['Money in a frontier lab'],16,MUTED,weight='bold')); y+=36
    for r in sorted(drawn,key=lambda r:(rank[cls(r)], r['donor'])):
        k=cls(r); c=col[k]; tie=r['gives_to_or_invests_in_lab'].strip()
        s.append(f'<rect x="{L-10}" y="{y-26}" width="{W-120}" height="84" rx="8" fill="#efece4"/>')
        s.append(tspans(L,y,wrap(r['donor'],30)[:2],20,INK,weight='bold',lh=24)+tspans(L,y+50,[r['row_id']],13,MUTED))
        s.append(tspans(L+520,y,wrap(r['gives_to_metr'],30)[:3],16,INK,lh=20))
        s.append(f'<circle cx="{L+880}" cy="{y-6}" r="10" fill="{c}"/>'+tspans(L+900,y,wrap(tie or 'no lab tie found',70)[:3],17,INK if k!='none' else MUTED,lh=21))
        y+=96
    n=sum(1 for r in J if cls(r)=='inv'); na=sum(1 for r in J if cls(r)=='aff')
    body=legend([(RED,'Donor is an investor in a frontier lab'),(YELLOW,'Affiliation or indirect tie, not an investment'),(ORANGE,'Tie to another evaluator, not a lab')])+f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}">{"".join(s)}</svg>'+f'<div style="font-size:15px;color:{MUTED};line-height:1.4;margin-top:6px"><b style="color:{INK}">Also checked, no direct lab tie found in public records:</b> '+'; '.join(esc(r['donor'].split('(')[0].strip())+' ('+r['row_id']+')' for r in sorted(rest,key=lambda r:r['donor']))+'. Investor lists omit unnamed limited partners, so absence is a bounded result.</div>'
    foot=f'<b>Coverage:</b> Every funder and named individual on metr.org/about, plus Moskovitz and BEMC as controls, checked against the Anthropic funding-round and investor records in memes/anthropic-investors and public 990 full-text search (rows J01–J{len(J):02d}, research/shared_donors.csv). {n} of {len(J)} are documented investors in Anthropic (Tallinn, Schmidt, Moskovitz, McClave, Jane Street the firm); {na} have an affiliation or indirect tie only. Jane Street\'s Anthropic stakes belong to the firm, while METR names "individuals from Jane Street"; the two are not the same and are shown together only because METR does not name the individuals. BEMC (McClave) is an Anthropic investor but no METR gift was found on its 990-PFs. METR\'s ban covers donations "made by or at the direction of frontier AI company employees"; it does not cover lab investors. "No direct lab tie found" means exact-name searches of public sources found none (Codex audit 2026-09-14); Anthropic\'s rounds name leads and some participants only, so absence is bounded, not proven. {SRC}.'
    render(STEM, shell('Same donors, both sides of the table: METR\'s funders who also hold a piece of the labs it evaluates','Figure 10k · metr.org/about donor list vs. lab cap tables','METR refuses lab money and lab-employee money. Its rule says nothing about lab investors, and its two earliest patrons led and joined Anthropic\'s Series A. Every named funder was checked; the ones with no tie found are listed below the chart.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10l. $10M to $71M
def fig_budget():
    W,H=2200,1460; STEM='metr-12-ten-million-to-seventy-one'
    G={r['row_id']:r for r in rows('budget.csv')}; E={r['row_id']:r for r in rows('evals.csv')}; F={r['row_id']:r for r in rows('finra_proposals.csv')}; I={r['row_id']:r for r in rows('independence_fight.csv')}
    def ym(d):
        y,m=int(d[:4]),int(d[5:7]); dd=int(d[8:10]) if len(d)>=10 and d[8:10].isdigit() else 15
        return y+(m-1)/12+(dd-1)/365
    t0,t1=ym('2025-10-01'),ym('2026-09-20'); L,R=120,W-140; x=lambda t:L+(R-L)*(t-t0)/(t1-t0)
    top=40; lanes={'money':top+90,'policy':top+300,'incident':top+470}; s=[]
    months=['2025-10','2025-11','2025-12','2026-01','2026-02','2026-03','2026-04','2026-05','2026-06','2026-07','2026-08','2026-09']
    for mo in months:
        X=x(ym(mo+'-01')); s.append(f'<line x1="{X:.1f}" y1="{top}" x2="{X:.1f}" y2="{lanes["incident"]+90}" stroke="{GRID}"/>'+tspans(X+6,top-8,[mo[5:]+('/'+mo[:4] if mo.endswith('-01') or mo=='2025-10' else '')],14,MUTED))
    # money lane: commitments window
    xa,xb=x(ym('2026-02-14')),x(ym('2026-08-14')); Y=lanes['money']
    s.append(f'<rect x="{xa:.1f}" y="{Y-60}" width="{xb-xa:.1f}" height="120" rx="10" fill="{RED}" opacity="0.14"/><rect x="{xa:.1f}" y="{Y-60}" width="{xb-xa:.1f}" height="120" rx="10" fill="none" stroke="{RED}" stroke-width="3"/>')
    s.append(tspans((xa+xb)/2,Y-12,['$71M of commitments raised in these six months'],26,INK,anchor='middle',weight='bold')+tspans((xa+xb)/2,Y+18,['"In the last 6 months, METR raised commitments of around $71 million" · Aug 14 2026 · G03'],15,MUTED,anchor='middle'))
    s.append(f'<circle cx="{xb:.1f}" cy="{Y}" r="10" fill="{RED}"/>')
    s.append(tspans(L,Y-72,['MONEY'],15,MUTED,weight='bold'))
    s.append(tspans(x(ym('2025-10-01'))+6,Y+52,['For scale: 2024 budget $10M (G01), 2025 target $15M (G02), FY2024 revenue $13.6M incl. $4.5M from ARC (G05)'],14,MUTED))
    # policy lane
    Yp=lanes['policy']; s.append(tspans(L,Yp-90,['THE SEAT BEING DRAFTED'],15,MUTED,weight='bold')+f'<line x1="{L}" y1="{Yp}" x2="{R}" y2="{Yp}" stroke="{AXIS}"/>')
    pol=[('2026-05-19','Frontier Risk Report: four labs let METR test internal models','E29'),('2026-06-03','OpenAI blueprint: CAISI plus independent assessments','F03'),('2026-06-10','Anthropic Advanced AI Framework: "at least one qualified independent evaluator"','F05'),('2026-07-14','Hassabis: FINRA-style Frontier AI Standards Body','F07'),('2026-07-17','Bloomberg: White House reviewing a FINRA-like watchdog','F09'),('2026-07-23','FRONTIER Act: licensed independent verification organizations','F10'),('2026-07-30','Lawfare: "Designing a FINRA for Frontier AI"','F12'),('2026-09-09','Dwarkesh: "ordain METR the evaluator"','F15'),('2026-09-12','Amodei essay: embedded evaluators "such as METR"','F16'),('2026-09-13','Sacks: "Stop pretending METR is independent"','F19')]
    plist=[]
    for i,(d,lab,rid) in enumerate(pol):
        X=x(ym(d)); Yc=Yp-(38 if i%2 else 0)-18
        after=ym(d)>ym('2026-08-14')
        s.append(f'<line x1="{X:.1f}" y1="{Yp}" x2="{X:.1f}" y2="{Yc+13}" stroke="{AXIS}"/><circle cx="{X:.1f}" cy="{Yc}" r="14" fill="{BG if after else BLUE}" stroke="{BLUE}" stroke-width="3"/>'+tspans(X,Yc+5,[str(i+1)],14,BLUE if after else '#fff',anchor='middle',weight='bold')+f'<circle cx="{X:.1f}" cy="{Yp}" r="6" fill="{BLUE}"/>')
        plist.append(f'<span style="display:inline-flex;align-items:flex-start;gap:8px"><i style="display:inline-flex;flex:none;width:24px;height:24px;border-radius:50%;background:{BLUE};color:#fff;font-size:13px;font-weight:bold;align-items:center;justify-content:center;font-style:normal">{i+1}</i><span><b>{d[5:]}</b> · {esc(lab)} <span style="color:{MUTED}">{rid}</span></span></span>')
    # incident lane
    Yi=lanes['incident']; s.append(tspans(L,Yi-80,['INCIDENT WORK'],15,MUTED,weight='bold')+f'<line x1="{L}" y1="{Yi}" x2="{R}" y2="{Yi}" stroke="{AXIS}"/>')
    inc=[('2026-01-27','Amazon Nova 2.0 Lite risk review','E21'),('2026-03-12','Review of Anthropic\'s Sabotage Risk Report','E25'),('2026-03-25','Red-team of Anthropic\'s agent monitoring','E26'),('2026-07-30','OpenAI Hugging Face investigation agreed','E35'),('2026-08-26','Hugging Face report published','E35'),('2026-09-09','Anthropic incident investigation agreed','E38')]
    for i,(d,lab,rid) in enumerate(inc):
        X=x(ym(d)); dy=[-62,-28,28,62][i%4]; before=ym(d)<ym('2026-08-14')
        s.append(f'<line x1="{X:.1f}" y1="{Yi}" x2="{X:.1f}" y2="{Yi+dy+(6 if dy<0 else -14)}" stroke="{AXIS}"/><circle cx="{X:.1f}" cy="{Yi}" r="9" fill="{GRAY}"/>')
        anc='end' if X>R-460 else 'start'; tx=X-12 if anc=='end' else X+12
        s.append(tspans(tx,Yi+dy,[f'{d[5:]} · {lab}'],15,INK,anchor=anc)+tspans(tx,Yi+dy+16,[rid],11,MUTED,anchor=anc))
    s.append(f'<line x1="{xb:.1f}" y1="{top}" x2="{xb:.1f}" y2="{Yi+70}" stroke="{RED}" stroke-width="2" stroke-dasharray="6 6"/>'+tspans(xb-8,Yi+88,['$71M announced'],13,RED,anchor='end',weight='bold'))
    howto=(f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:2px 0 10px">'
        +card('1 · The money','METR says it raised about $71M of commitments between mid-February and mid-August 2026 (G03). That is seven times its 2024 budget (G01). Who committed what, and when inside the window, is not public.',RED,16)
        +card('2 · The seat','In the same months, the industry and Washington drafted the job METR now holds: the Frontier Risk Report, OpenAI\'s and Anthropic\'s frameworks calling for independent evaluators, Hassabis\'s FINRA-style body, the White House review and the FRONTIER Act (markers 1–7). The three proposals that name METR came after the money was announced (8–10).',BLUE,16)
        +card('3 · The incidents','The OpenAI investigation was agreed July 30, two weeks before the announcement; the Anthropic investigation on September 9, after it. So the money cannot have followed the incidents. It arrived while the seat was being designed. Whether donors were funding the seat is an inference; the dates are not.',GRAY,16)+'</div>')
    body=howto+legend([(RED,'Fundraising window and announcement'),(BLUE,'Proposals for a mandated evaluator (hollow: after the announcement)'),(GRAY,'METR\'s incident reviews and investigations')])+f'<svg width="{W-120}" height="{Yi+110}" viewBox="0 0 {W-120} {Yi+110}">{"".join(s)}</svg>'+f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px 30px;font-size:15px;line-height:1.3;margin-top:4px">{"".join(plist)}</div>'
    body+=f'<div style="background:#efece4;border-radius:10px;padding:14px 20px;font-size:18px;line-height:1.45;margin-top:8px">The six-month raise ran from mid-February to mid-August 2026. Inside that window came the Frontier Risk Report, both labs\' governance frameworks calling for independent evaluators, Hassabis\'s FINRA proposal, the White House review and the FRONTIER Act. The two incident investigations were agreed on July 30 and September 9, at the end of and after the window; the routine risk-report reviews in March were already happening before any of it. The three posts that name METR as the evaluator came after the announcement. What the commitments were for is not public; the sequence rules out the incidents as the cause and is consistent with, but does not prove, the money anticipating the seat.</div>'
    foot=f'<b>Coverage:</b> Fundraising window is METR\'s own statement, "the last 6 months" to Aug 14 2026 (G03, research/budget.csv); the earlier budget, target and revenue figures (G01, G02, G05) are for scale and are different measures, never summed. Policy markers are the proposals in research/finra_proposals.csv and the Frontier Risk Report (E29); incident marks are METR\'s lab engagements typed as reviews or investigations in research/evals.csv. Commitment dates within the window are not public, so the figure shows the window, not a curve. Commitments are pledges, not cash received, and are never summed with the budget or revenue figures. Sequence is a fact about dates; any reading of what the commitments anticipated is interpretation, stated as such in the box. {SRC}.'
    render(STEM, shell('METR raised $71M in the six months the evaluator\'s seat was being designed; the investigations came after the money, not before it','Figure 10l · October 2025 – September 2026 · three things in one window','Read it in three steps: the money, the seat, the incidents. Six of nine proposals for a mandated evaluator fell inside the fundraising window; the two incident investigations were agreed at its end and after it. The overlap is at six-month resolution because METR does not date its commitments.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10m. the subcontractor
def fig_redwood():
    W,H=2200,1560; STEM='metr-13-the-subcontractor'
    R={r['row_id']:r for r in rows('redwood.csv')}
    grants=[('RW01','2021-11',9.42e6),('RW02','2022-08',10.7e6),('RW03','2023-06',5.3e6),('RW04','2025-05',1.1e6),('RW05','2025-11',36.566e6)]
    rev=[('RW38',2021,13904248),('RW39',2022,12049894),('RW40',2023,10036347),('RW41',2024,22060)]
    total=sum(g[2] for g in grants)
    kp=f'<div class="kpis"><div class="kpi"><div class="l">Coefficient grants to Redwood</div><div class="v">{money(total)}</div><div class="d">five awards 2021–25 (RW01–RW05)</div></div><div class="kpi"><div class="l">Redwood revenue, 2024</div><div class="v">$22K</div><div class="d">6 employees after the Constellation spin-out (RW41)</div></div><div class="kpi"><div class="l">Then, Nov 2025 and 2026</div><div class="v">$36.6M · then $70M+</div><div class="d">largest single award (RW05); then "more than $70 million over the next two years" recommended, per Coefficient\'s Sep 9 2026 post (RW42)</div></div><div class="kpi"><div class="l">Staff moved</div><div class="v">4 → METR · 3 → Anthropic</div><div class="d">RW18–RW21, RW29–RW30</div></div></div>'
    board=[('Paul Christiano','Secretary and director, 2021 – Jun 2023','Then: US AISI head of AI safety; ARC executive director; OpenAI Foundation board (Sep 9 2026)','RW13',RED),
           ('Holden Karnofsky','Treasurer and director, 2021 – Nov 2023','Co-CEO of Open Philanthropy at the Nov 2021 and Aug 2022 Redwood grants; on leave, with Berger acting sole CEO, at the Jun 2023 grant; back as Director of AI Strategy from Jul 2023. Then: Anthropic (Jan 2025)','RW14',BLUE),
           ('Ajeya Cotra','Director, 2023 – Aug 2024','Then: Open Philanthropy; METR technical staff (Jan 2026); co-author of the Aug 26 OpenAI report with Redwood\'s Greenblatt. METR bio does not mention the seat','RW15',AQUA),
           ('Buck Shlegeris','Co-founder; CEO and director from 2023','Ex-MIRI','RW10',GRAY),
           ('Nate Thomas','Co-founder; board chair from 2023','','RW09',GRAY),
           ('Ammon Bartram','Director (2024 filing)','Triplebyte co-founder','RW12',GRAY),
           ('Ryan Greenblatt','Chief Scientist (staff, not board)','Employee-level model access at Anthropic for the alignment-faking paper (Dec 2024); lead on the Aug 26 OpenAI report','RW11',ORANGE)]
    left='<div style="display:flex;flex-direction:column;gap:10px">'+f'<div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold">Redwood\'s board and chief scientist, per its Form 990s</div>'
    for n,role,then,rid,c in board:
        left+=f'<div style="background:#efece4;border-radius:10px;padding:10px 14px;border-left:6px solid {c}"><div style="font-size:20px;font-weight:bold">{esc(n)} <span style="font-size:13px;color:{MUTED};font-weight:normal">{rid}</span></div><div style="font-size:16px;line-height:1.3">{esc(role)}</div>'+(f'<div style="font-size:15px;line-height:1.3;color:{MUTED};margin-top:3px">{esc(then)}</div>' if then else '')+'</div>'
    left+='</div>'
    t0,t1=2021.4,2026.9; L,Rr,top,base=70,720,40,470; x=lambda t:L+(Rr-L)*(t-t0)/(t1-t0); vmax=40e6; yv=lambda v: base-(base-top)*v/vmax
    sv=[]
    for yr in range(2022,2027): sv.append(f'<line x1="{x(yr):.1f}" y1="{top}" x2="{x(yr):.1f}" y2="{base}" stroke="{GRID}"/>'+tspans(x(yr),base+24,[str(yr)],15,MUTED,anchor='middle'))
    for v in (10e6,20e6,30e6): sv.append(f'<line x1="{L}" y1="{yv(v):.1f}" x2="{Rr}" y2="{yv(v):.1f}" stroke="{GRID}"/>'+tspans(L-8,yv(v)+5,[money(v)],13,MUTED,anchor='end'))
    for rid,yr,v in rev:
        X=x(yr+0.5); sv.append(f'<rect x="{X-16:.1f}" y="{yv(v):.1f}" width="32" height="{base-yv(v):.1f}" rx="4" fill="{AQUA}" opacity="0.8"/>'+tspans(X,yv(v)-6,[money(v) if v>1e5 else '$22K'],13,INK,anchor='middle',weight='bold'))
    for rid,d,v in grants:
        y,m=d.split('-'); t=int(y)+(int(m)-1)/12; X=x(t)
        sv.append(f'<rect x="{X-10:.1f}" y="{yv(v):.1f}" width="20" height="{base-yv(v):.1f}" rx="4" fill="{BLUE}"/>'+tspans(X,yv(v)-6,[money(v)],13,INK,anchor='middle',weight='bold'))
    for rid,d,lab in [('RW31','2026-07','Jul 30'),('RW32','2026-08','Aug 26'),('RW35','2026-09','Sep 9'),('RW36','2026-09','Sep 12')]:
        y,m=d.split('-'); t=int(y)+(int(m)-1)/12; X=x(t)
        sv.append(f'<line x1="{X:.1f}" y1="{top}" x2="{X:.1f}" y2="{base}" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="6 6"/>')
    sv.append(tspans(x(2026.4)-6,top-8,['METR joint work, Jul–Sep 2026'],14,ORANGE,anchor='end',weight='bold'))
    mid=f'<div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold;margin-bottom:6px">Money in: Coefficient awards (blue) vs. Redwood revenue by year (aqua)</div><svg width="740" height="510" viewBox="0 0 740 510">{"".join(sv)}</svg>'
    mid+=f'<div style="font-size:15px;color:{MUTED};line-height:1.35;margin-top:4px">Revenue fell to $22K in 2024 after Redwood spun Constellation out ($4.34M cash plus $554K non-cash transferred in 2023, and $250K cash plus $430K leasehold in 2024, RW40–41). The $36.6M award came eleven months later (RW05), and on Sep 9 2026 Coefficient said its grantmakers had recommended more than $70M over two years to Redwood, citing Greenblatt\'s OpenAI investigation (RW42); a recommendation, not summed with awards. SFF/Tallinn added $2.4M in recommendations 2022–23 (RW06–RW08), not summed here.</div>'
    flows=[('Redwood → METR',AQUA,['Daniel Ziegler (OpenAI → Redwood → METR → Anthropic) RW18','Lawrence Chan RW19','Haoxing Du RW20','Seraphina Nix RW21','Beth Barnes attended Redwood\'s MLAB bootcamp RW22']),
           ('Redwood → Anthropic',RED,['Fabien Roger (Jul 2024) RW29','Kshitij Sachan (Nov 2023) RW30','Daniel Ziegler (Jun 2024) RW18']),
           ('Lab ties',ORANGE,['Alignment-faking paper with Anthropic, Dec 2024 RW23','Greenblatt: employee-level access at Anthropic RW24','Eight joint papers with Anthropic 2025–26, Joe Benton on all eight, now at METR RW52','LinuxArena used in the Mythos Preview system card RW53','Advises Google DeepMind and Anthropic (own site) RW26']),
           ('The 2025–26 bench: from a lab, the funder, and funded orgs (Grok G2)',YELLOW,['Keshav Shenoy ← Anthropic Alignment Science G2 RP02', 'Lukas Finnveden ← Coefficient Giving (Jul 2025, per The Org, unverified) G2 RP07', 'Alex Kastner ← AI Futures Project bylines G2 RP03', 'Alexa Pan ← Forecasting Research Institute (2025; own page says research intern) G2 RP04', 'Aghyad Deeb ← Redwood intern G2 RP08', 'Julian Stastny ← Center on Long-Term Risk G2 RP05', 'Alek Westover ← MIT (2025) G2 RP09', 'Emery Cooper ← Carnegie Mellon (2026) G2 RP01', 'Caspar Oesterheld ← Carnegie Mellon (2026) G2 RP12']),
           ('Joint work with METR',BLUE,['Jul 30 2026: OpenAI Hugging Face incident, 252K views RW31','Aug 26: report; Greenblatt "contracting with METR", 6 days on site RW32','Sep 12: "Several staff from Redwood have been subcontracted by METR" 96K views RW36'])]
    right='<div style="display:flex;flex-direction:column;gap:10px">'
    for name,c,items in flows:
        right+=f'<div style="background:#efece4;border-radius:10px;padding:10px 14px;border-left:6px solid {c}"><div style="font-size:17px;font-weight:bold;margin-bottom:4px">{esc(name)}</div>'+''.join(f'<div style="font-size:15px;line-height:1.35">{esc(i)}</div>' for i in items)+'</div>'
    right+='</div>'
    body=kp+f'<div style="display:grid;grid-template-columns:620px 760px 1fr;gap:26px;margin-top:4px">{left}<div>{mid}</div>{right}</div>'
    foot=f'<b>Coverage:</b> On Sep 13 2026 METR edited its Aug 26 OpenAI report post to disclose that Ryan Greenblatt, the Redwood staff member contracting with METR on that investigation and now on the Anthropic team, "is the domestic partner of Beth Barnes, METR\'s CEO", adding that Barnes "was not involved in the decision to engage" him (RW59, IF149; who made the decision is not stated). Redwood also founded Constellation Research Center in 2023 to take over its co-working programme; Constellation (EIN 93-2465256) received $22.95M in three Coefficient grants 2023–24, reported $12.6M revenue and 23 employees for 2024, and is the "shared research center" METR says it works from alongside "some AI lab staff" (RW57, M126–M128, DR28). Redwood Research Group (EIN 87-1702255) Form 990s TY2021–TY2024 for board, officers, pay and revenue; redwoodresearch.org for current roles; Coefficient index snapshot 2026-09-11 for awards; SFF round pages and Tallinn\'s ledger for recommendations; fxtwitter payloads for post views (rows RW01–RW{len(rows("redwood.csv")):02d}, research/redwood.csv; 2025–26 hires from research/grok-out/G2-redwood-people.csv). Board seats are dated by the 990 "thru" notes. No page names which Redwood staff are subcontracted or on what terms, and Anthropic\'s Sep 9 announcement has no subcontractor language (RW35). Overlap of funder, funded, evaluator and evaluated is a fact about the filings; the figure states no motive. {SRC}.'
    render(STEM, shell('The investigator\'s subcontractor: Redwood\'s board held the funder\'s co-CEO, Anthropic\'s future trustee and METR\'s future staffer','Figure 10m · Redwood Research, 2021–2026','On Sep 12 Redwood said its staff were subcontracted onto METR\'s investigation of Anthropic. Redwood holds $63M in Coefficient awards, with a further $70M+ recommended in 2026; its directors have included Karnofsky (now Anthropic), Christiano (now OpenAI Foundation) and Cotra (now METR).',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10n. the independence fight
def fig_independence():
    W,H=2200,2640; STEM='metr-14-the-independence-fight'
    I=rows('independence_fight.csv'); A=rows('x_amplifiers.csv')
    posts=[r for r in I if r['venue'].strip().lower().startswith('x post') and num(r['views'])>0 and r['utc'][:10]>='2026-09-11' and not ('reply layer' in r['notes'] and num(r['views'])<10000)]
    def tsec(u):
        d,t=u[:10],u[11:16]; base={'2026-09-11':0,'2026-09-12':24,'2026-09-13':48,'2026-09-14':72,'2026-09-15':96,'2026-09-16':120}[d]; h,m=t.split(':'); return base+int(h)+int(m)/60
    posts.sort(key=lambda r:tsec(r['utc']))
    rowh=40; L=60; s=[]; y=28
    for t,xx in [('UTC',L),('Who',L+150),('Views (log scale)',L+520),('Names METR',L+1020),('What it said',L+1200)]: s.append(tspans(xx,y,[t],15,MUTED,weight='bold'))
    y+=28
    vmaxlog=math.log10(7e7)
    for r in posts:
        v=num(r['views']); w=440*(math.log10(max(v,1000))-3)/(vmaxlog-3)
        nm=r['names_metr'].strip().lower()=='yes'; c=RED if nm else GRAY
        actor=r['actor'].split('(')[0].strip()
        s.append(f'<rect x="{L-10}" y="{y-24}" width="{W-120}" height="{rowh-4}" rx="6" fill="#efece4"/>')
        s.append(tspans(L,y,[r['utc'][5:16].replace('-','/').replace('T',' ')],15,MUTED)+tspans(L+150,y,[actor[:32]],17,INK,weight='bold'))
        s.append(f'<rect x="{L+520}" y="{y-16}" width="{max(3,w):.1f}" height="20" rx="4" fill="{c}"/>'+tspans(L+528+max(3,w),y,[fmt_views(v)],14,INK,weight='bold'))
        s.append(f'<circle cx="{L+1035}" cy="{y-6}" r="8" fill="{c}"/>'+tspans(L+1052,y,['yes' if nm else 'no'],14,c,weight='bold'))
        s.append(tspans(L+1200,y,[r['event'][:88]],14,INK)+tspans(W-130,y,[r['row_id']],11,MUTED,anchor='end'))
        y+=rowh
    svg=f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}">{"".join(s)}</svg>'
    dario=[r for r in I if r['row_id']=='IF09'][0]; sacks=[r for r in I if r['row_id']=='IF28'][0]; none=[r for r in I if r['row_id']=='IF44'][0]
    cards='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:6px">'
    cards+=card('Dario Amodei, "We Must Pace the Frontier", Sep 12 · IF09',f'“{esc(dario["metr_language"][:260])}”',RED,17)
    cards+=card('David Sacks, Sep 13 03:14 UTC · 7.1M views · IF28',f'“{esc(sacks["metr_language"][:260])}”',RED,17)
    cards+=card('METR, Beth Barnes, Chris Painter · IF44',esc(none['event'][:300]),GRAY,17)
    cards+='</div>'
    press=[r for r in I if r['venue'].strip().lower()=='press']; py=sum(1 for r in press if r['names_metr'].strip().lower()=='yes')
    agg={}
    for a in A: k=a['affiliation']; agg.setdefault(k,[0,0]); agg[k][0]+=1; agg[k][1]+=int(a['views'] or 0)
    order=sorted(agg,key=lambda k:-agg[k][1]); tot=sum(v[1] for v in agg.values()); n=len(A)
    col={'commentator/anon':GRAY,'unknown':LGRAY,'frontier lab staff':RED,'METR or Redwood staff':AQUA,'AI industry other':GRAY,'investor or VC':YELLOW,'journalist':BLUE250,'AI safety advocate or org':ORANGE,'SFF/Coefficient-funded org staff':BLUE,'politician or official':YELLOW}
    bar=f'<div style="display:flex;height:34px;border-radius:8px;overflow:hidden;margin:8px 0 6px">'+''.join(f'<div title="{esc(k)}" style="width:{100*agg[k][1]/tot:.2f}%;background:{col.get(k,GRAY)}"></div>' for k in order)+'</div>'
    leg='<div style="display:flex;flex-wrap:wrap;gap:8px 22px;font-size:15px">'+''.join(f'<span><i class="sw" style="background:{col.get(k,GRAY)};vertical-align:-3px;margin-right:6px"></i>{esc(k)}: {agg[k][0]} accounts, {fmt_views(agg[k][1])} views</span>' for k in order)+'</div>'
    funded=sum(agg[k][0] for k in ('SFF/Coefficient-funded org staff','METR or Redwood staff') if k in agg)
    lower=f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:26px;margin-top:14px"><div><div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold">Who carried the Sep 9 announcement: {n} quote-posts and replies over 1,000 views, share of views by account type</div>{bar}{leg}<div style="font-size:15px;color:{MUTED};margin-top:6px">{funded} of {n} accounts are staff of METR, Redwood or an SFF/Coefficient-funded organization (rows X01–X{n}, research/x_amplifiers.csv).</div></div><div><div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{MUTED};font-weight:bold">Press, Sep 12–13</div><div class="kpis" style="margin-top:8px"><div class="kpi" style="min-width:200px"><div class="l">Press records</div><div class="v">{len(press)}</div></div><div class="kpi" style="min-width:200px"><div class="l">Name METR</div><div class="v">{py}</div></div><div class="kpi" style="min-width:200px"><div class="l">Discuss METR\'s funding</div><div class="v">1</div><div class="d">a blog fact-check (IF27); rows, not unique articles: IF25, IF40, IF130 and IF131 each summarise several</div></div></div><div style="font-size:15px;color:{MUTED};line-height:1.35">Bloomberg, Washington Post, Axios, CNBC, NBC, Reuters, Semafor and The Verge covered the essay and the Trump response without naming METR; the outlets that did name it repeated Sacks\'s sentence and did not describe who funds METR (IF21–IF42); of five New York Times and four Wall Street Journal pieces read from Kevin\'s PDFs (IF140–IF148), one Times story names METR and Redwood once, as organizations critics said Anthropic had "too many ties" to, with a Bill Gurley quote and no funder (IF140); the other eight, including both papers\' first-day stories on the essay and the Journal\'s Trump-and-Sacks piece, name no evaluator and, where they quote Sacks, omit his METR sentence; a second sweep to Sep 14 07:35 UTC found nine more outlets carrying the sentence, none naming a funder or reporting a METR comment (IF131, research/press_sweep.csv PR01–PR56), and Altman\'s Sep 14 follow-up post naming no evaluator (IF128).</div></div></div>'
    SK=rows('sacks_thread.csv'); top=SK[:6]
    sk='<div style="margin-top:14px"><div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:'+MUTED+';font-weight:bold">Sacks\'s thread: who answered, and who from the network did not</div><div class="kpis" style="margin-top:8px"><div class="kpi" style="min-width:240px"><div class="l">Quotes and replies over 1,000 views</div><div class="v">'+str(len(SK))+'</div><div class="d">Grok X-API pull; not a census of 2,203 quotes / 2,807 replies</div></div><div class="kpi" style="min-width:240px"><div class="l">From METR, Redwood or Coefficient accounts</div><div class="v">0</div><div class="d">search of 58 named handles with no threshold found none (research/grok-out/G1-sacks-census.csv); a search result, not a census</div></div><div class="kpi" style="min-width:240px"><div class="l">From SFF-funded org accounts</div><div class="v">2</div><div class="d">quote-posts by Kokotajlo (AI Futures) and Soares (MIRI), both conceding Sacks\'s point (IF60, IF58)</div></div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px 20px">'+''.join(card(f'{esc(x["name"])} · {fmt_views(x["views"])} · {x["row_id"]}',f'“{esc(x["text_200"][:150])}”',GRAY,15) for x in top)+'</div></div>'
    body=legend([(RED,'Post names METR'),(GRAY,'Post does not name METR')])+svg+cards+lower+sk
    foot=f'<b>Coverage:</b> Every X post, essay, press item and government statement located for Sep 11–14 2026 on the Amodei essay, Altman\'s and Sacks\'s replies and reactions to METR being named, plus the highest-view posts mentioning METR from Grok\'s X-API keyword pull (rows IF01–IF{len(I):02d}, research/independence_fight.csv; research/sacks_thread.csv); views are fxtwitter values at fetch 2026-09-13; a refetch of the 611 unique post ids behind 627 row references (agent S2, 2026-09-14 ~07:07 UTC) returned 610 successes and one 404 (Matt Stoller\'s post, IF33, kept from its archived payload; a 404 is not proof of deletion) and no author or date mismatches (research/agents-2026-09-14/S2-fx-recheck/). The essay names METR once, as an example ("such as METR"). Sacks names no funder. No METR, Barnes, Painter or Wijk response was located by the 2026-09-14 07:13 UTC snapshot (IF44; per-handle searches of 16 METR accounts since Sep 13, Grok G10 and G13), but X search caps at ten hits per query, so this is a negative with stated coverage, not a finding of silence. The amplifier panel is Grok\'s X-API pull of quotes and replies over 1,000 views on the Sep 9 Anthropic and METR posts, not a full census (586 quotes, 737 replies exist); classification from fxtwitter bios and local rosters. The Sacks-thread check of 58 named METR, Redwood, Coefficient, SFF-org and lab handles ran with no threshold and located no reply in the thread, a capped search result rather than a census; Kokotajlo and Soares quote-posted Sacks; Painter\'s only related post asked Tim Hwang to define "independent" (IF64); Anthropic\'s Drake Thomas argued in replies that METR\'s leverage is that "there are few options" and "if METR is the only credible game in town, nothing the labs can do about it" (IF62–IF63). The share of funded-org accounts is small, and the figure says so. Reply-layer posts located by the Grok G6 lane (research/grok-out/G6-insiders.csv, 324 rows, refetched via fxtwitter 2026-09-14 05:23 UTC) and the Grok G9 lane (research/grok-out/G9-thousand-metrs.csv, 788 rows) are drawn above only when their snapshot views are at least 10,000, an editorial selection that keeps the earlier low-view rows IF62–IF64 and drops Alexander Barry\'s and Kei Nishimura-Gasparian\'s replies from the chart; the full set, including the METR-affiliated accounts that carried the defense in replies (Alexander Barry, an Epoch AI statistician listed on metr.org/about as a METR research collaborator, five posts; Kei Nishimura-Gasparian, METR technical staff, one post), is rows IF67–IF113, scored against the ledger in Figure 10r, with the security-community threads and the founder call in Figure 10t. {SRC}.'
    render(STEM, shell('"Stop pretending METR is independent": Amodei names it, Altman signs on, Sacks objects, no METR reply found','Figure 10n · September 11–14, 2026','Three days on X, one row per post, bars on a log scale of views. Dario Amodei\'s post announcing his essay, which offered embedded evaluators "such as METR", drew 67M views; David Sacks\'s reply drew 7M (post views at the 2026-09-13 snapshot, not readers). Below: the two sentences, the search for a METR reply, who carried the Sep 9 announcement, and what the press said.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10o. the candidates
def fig_candidates():
    E=[r for r in rows('evaluators.csv') if r['row_id'] not in ('EV21','EV22','EV23','EV24')]; W=2200; STEM='metr-15-the-candidates'  # EV21 Halcyon (incubator), EV22 AIUC (insurer), EV24 LMArena (leaderboard) are not evaluators; EV23 duplicates EV09
    def short(o):
        for k,v in [('RAND','RAND (Canary)'),('METR','METR'),('Apollo','Apollo Research'),('Epoch','Epoch AI'),('EquiStamp','EquiStamp'),('Redwood','Redwood Research'),('Transluce','Transluce'),('Irregular','Irregular (ex-Pattern Labs)'),('Nemesys','Nemesys Insights'),('FAR','FAR.AI'),('SaferAI','SaferAI'),('UK AI Security','UK AISI'),('US Center','US CAISI'),('EU AI Office','EU AI Office (buyer)'),('Stanford','Stanford NLP'),('Hugging Face','Hugging Face Open Alignment'),('Scale AI','Scale AI / SEAL'),('MLCommons','MLCommons'),('Palisade','Palisade Research'),('Alignment Research Center','ARC')]:
            if o.startswith(k): return v
        return o[:26]
    def lm(t):
        t=t.lower()
        if t.startswith('no'): return ('refuses',AQUA)
        if t.startswith('yes, capped') or 'may accept' in t[:40]: return ('takes, with a cap or disclosure',YELLOW)
        if t.startswith('yes'): return ('takes lab money',RED)
        return ('no policy found',GRAY)
    E=sorted(E,key=lambda r:-(num(r['coefficient_total_usd'])+num(r['sff_total_usd'])))
    rowh=52; L=60; s=[]; y=30
    for t,xx in [('Candidate',L),('Type',L+330),('Coefficient awards (log)',L+520),('SFF recs',L+1000),('Frontier-lab money',L+1110),('Government work',L+1400),('Proposed as evaluator, Sep 9–13',L+1720)]: s.append(tspans(xx,y,[t],15,MUTED,weight='bold'))
    y+=30; cmax=math.log10(1e8)
    for r in E:
        c=num(r['coefficient_total_usd']); sf=num(r['sff_total_usd']); pol,pc=lm(r['lab_money'])
        nmv=r['named_in_sep_2026'].strip(); named=bool(nmv) and not nmv.lower().startswith(('none','no'))
        s.append(f'<rect x="{L-10}" y="{y-26}" width="{W-120}" height="{rowh-6}" rx="6" fill="{"#e6eefb" if named else "#efece4"}"/>')
        nmw=wrap(short(r['org']),22)[:2]
        s.append(tspans(L,y-(7 if len(nmw)>1 else 0),nmw,17,INK,weight='bold',lh=18)+tspans(L+260,y+17,[r['row_id']],11,MUTED))
        s.append(tspans(L+330,y,[r['type'].split('(')[0].strip()[:20]],14,MUTED))
        if c>0:
            w=300*(math.log10(c)-5)/(cmax-5) if c>1e5 else 8
            scope={'EV18':'institution-wide; $10.0M evaluation-specific','EV14':'NLP-PI subset of $53.4M institution-wide'}.get(r['row_id'],'')
            s.append(f'<rect x="{L+520}" y="{y-16}" width="{max(8,w):.1f}" height="20" rx="4" fill="{BLUE}" opacity="{0.45 if scope else 1}"/>'+tspans(L+528+max(8,w),y,[money(c)+(f' ({r["coefficient_grants_n"]})' if r['coefficient_grants_n'].strip() else '')],14,INK,weight='bold')+(tspans(L+520,y+17,[scope],11,MUTED) if scope else ''))
        else: s.append(tspans(L+520,y,['none in index'],14,MUTED))
        s.append(tspans(L+1000,y,[money(sf) if sf>0 else '—'],14,INK if sf>0 else MUTED))
        s.append(f'<circle cx="{L+1118}" cy="{y-6}" r="7" fill="{pc}"/>'+tspans(L+1132,y,[pol],14,INK))
        g=r['gov_contracts'].strip(); g=g if g and not g.lower().startswith('none') else 'none found'
        gw=wrap(g,44); gl=gw[:2]
        if len(gw)>2: gl[1]=gl[1][:41].rstrip()+'…'
        s.append(tspans(L+1400,y-(6 if len(gl)>1 else 0),gl,12,MUTED,lh=15))
        nm=nmv if named else '—'; nw=wrap(nm,40); nl=nw[:2]
        if len(nw)>2: nl[1]=nl[1][:37].rstrip()+'…'
        s.append(tspans(L+1720,y-(6 if len(nl)>1 else 0),nl,12,INK if named else MUTED,lh=15,weight='bold' if named else 'normal'))
        y+=rowh
    H=y+660
    n_named=sum(1 for r in E if r['named_in_sep_2026'].strip() and not r['named_in_sep_2026'].lower().startswith(('none','no')))
    n_coef=sum(1 for r in E if num(r['coefficient_total_usd'])>0); n_ref=sum(1 for r in E if lm(r['lab_money'])[0]=='refuses' and r['type'].startswith('nonprofit'))
    kp=f'<div class="kpis"><div class="kpi"><div class="l">Candidate evaluators</div><div class="v">{len(E)}</div><div class="d">nonprofits, companies, governments, academics</div></div><div class="kpi"><div class="l">With Coefficient awards</div><div class="v">{n_coef}</div><div class="d">in the 2,911-row index (RAND and Stanford institution-wide)</div></div><div class="kpi"><div class="l">Nonprofits that refuse lab money</div><div class="v">{n_ref}</div><div class="d">METR only; FAR.AI caps it, Transluce discloses it, Epoch takes it</div></div><div class="kpi"><div class="l">Put forward Sep 9–13</div><div class="v">{n_named}</div><div class="d">METR (Dwarkesh, Amodei), Stanford NLP (Manning), Hugging Face (Delangue)</div></div></div>'
    body=kp+legend([(BLUE,'Coefficient / Open Philanthropy awards, log scale'),(AQUA,'Refuses frontier-lab money'),(YELLOW,'Takes it with a cap or disclosure'),(RED,'Takes it'),(GRAY,'No policy found'),('#e6eefb','Proposed as an evaluator this week')])+f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}" style="flex-shrink:0">{"".join(s)}</svg>'
    foot=f'<b>Coverage:</b> Every organization proposed, contracted or plausibly positioned as a frontier-AI evaluator in Sep 2026: the three named on X that week, the six EU AI Office lot winners (TED 864574-2025), Anthropic\'s and Amazon\'s commercial assessors, the UK and US institutes, and the established safety nonprofits (rows EV01–EV{len(E):02d}, research/evaluators.csv). Coefficient totals are awards in the index snapshot 2026-09-11 matched by organization name; RAND\'s and Stanford\'s are institution-wide and not evaluation-specific; METR\'s ARC-era $1.5M sits on the ARC row. SFF figures are recommendations including matching pledges. Lab-money column quotes each org\'s own policy where one exists; "inferred" cases are commercial assessors. Transluce reports 38% of FY2025 revenue from OpenAI and Anthropic employees\' personal gifts. Coefficient\'s Sep 9 2026 post adds a $68M three-year renewal recommended to Epoch and more than $70M over two years to Redwood (money_flows M120–M121), recommendations not yet in the awards index; the same post puts Coefficient\'s technical AI safety commitments at $168M in 2024, $351M in 2025 and "on track" for over $1B in 2026 (M122). Coefficient\'s Project Tailwind, launched Sep 9 2026, lists "AI incident investigations", "Independent AI auditors" and a "Control red team" among the organizations it wants founded, naming METR as the alternative to founding and citing METR\'s David Rein "inside Anthropic\'s systems" (money_flows M123; verified first-hand 2026-09-14 from the page\'s decoded iframe text and a browser save). Being funded by the same donors is a fact about the field, not a finding about any evaluation. {SRC}.'
    render(STEM, shell('The candidates: of twenty possible evaluators, nine hold Coefficient awards, one refuses lab money, and the three put forward this week were METR, Stanford and Hugging Face','Figure 10o · Who could be "the evaluator", and who funds each','Every organization that could fill the seat Amodei described, with its Coefficient and SFF money, its stated policy on frontier-lab money, its government work, and whether anyone proposed it between Sep 9 and 13.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10p. METR's megaphone
def fig_megaphone():
    W,H=2200,1640; STEM='metr-16-metrs-megaphone'
    P=rows('metr_posts.csv'); LM=rows('lab_mentions.csv'); AR=rows('arrivals.csv'); OM=rows('officials_mentions.csv')
    from collections import defaultdict
    bym=defaultdict(lambda:[0,0])
    for x in P: bym[x['utc'][:7]][0]+=1; bym[x['utc'][:7]][1]+=int(x['views'] or 0)
    months=[]; y0,m0=2024,1
    while (y0,m0)<=(2026,9): months.append(f'{y0}-{m0:02d}'); m0+=1; (y0,m0)=(y0+1,1) if m0==13 else (y0,m0)
    L,R,top,base=140,W-160,70,560; bw=(R-L)/len(months); xm=lambda i:L+i*bw
    yv=lambda v: base-(base-top)*(math.log10(max(v,1e3))-3)/(7-3)
    s=[]
    for v in (1e4,1e5,1e6,1e7): s.append(f'<line x1="{L}" y1="{yv(v):.1f}" x2="{R}" y2="{yv(v):.1f}" stroke="{GRID}"/>'+tspans(L-10,yv(v)+5,[fmt_views(v)],14,MUTED,anchor='end'))
    for i,mo in enumerate(months):
        n,v=bym.get(mo,[0,0])
        if mo.endswith('-01') or i==0: s.append(tspans(xm(i)+bw/2,base+24,[mo[:4]],15,MUTED,anchor='middle',weight='bold'))
        if n: s.append(f'<rect x="{xm(i)+3:.1f}" y="{yv(v):.1f}" width="{bw-6:.1f}" height="{base-yv(v):.1f}" rx="4" fill="{AQUA}"/>'+tspans(xm(i)+bw/2,base+42,[str(n)],11,MUTED,anchor='middle'))
        else: s.append(tspans(xm(i)+bw/2,base-4,['·'],14,GRAY,anchor='middle'))
    s.append(tspans(L,base+42,['posts:'],11,MUTED,anchor='end'))
    tops=sorted(P,key=lambda x:-int(x['views'] or 0))[:6]
    labels={'1902384481111322929':'Time-horizon paper (Mar 2025)','2092692175452803393':'OpenAI Hugging Face report (Aug 2026)','2002203627377574113':'Opus 4.5 time horizon (Dec 2025)','2019169900317798857':'GPT-5.2 time horizon (Feb 2026)','2052896621760004602':'Mythos Preview evaluation (May 2026)','2070584331068969336':'GPT-5.6 Sol early access (Jun 2026)'}
    toplist=[]
    for j,x in enumerate(tops,1):
        mo=x['utc'][:7]; i=months.index(mo); v=bym[mo][1]; X=xm(i)+bw/2; Y=yv(v)-16
        s.append(f'<circle cx="{X:.1f}" cy="{Y}" r="12" fill="{INK}"/>'+tspans(X,Y+5,[str(j)],13,'#fff',anchor='middle',weight='bold'))
        toplist.append(f'<span><i style="display:inline-flex;width:22px;height:22px;border-radius:50%;background:{INK};color:#fff;font-size:13px;font-weight:bold;align-items:center;justify-content:center;font-style:normal;margin-right:6px">{j}</i>{esc(labels.get(x["id"],x["text_200"][:30]))} · <b>{fmt_views(x["views"])}</b> <span style="color:{MUTED}">{x["row_id"]}</span></span>')
    Y2=base+100; s.append(f'<line x1="{L}" y1="{Y2}" x2="{R}" y2="{Y2}" stroke="{AXIS}"/>'+tspans(L-10,Y2+5,['A lab says "METR"'],14,INK,anchor='end',weight='bold'))
    col={'AnthropicAI':RED,'OpenAI':ORANGE,'jackclarkSF':BLUE}
    for x in LM:
        mo=x['utc'][:7]
        if mo not in months: continue
        i=months.index(mo); d=int(x['utc'][8:10]); X=xm(i)+bw*(d/31); c=col.get(x['handle'],GRAY); v=int(x['views'] or 0)
        s.append(f'<circle cx="{X:.1f}" cy="{Y2}" r="{max(6,min(22,6+4*math.log10(max(v,1e3)/1e3))):.1f}" fill="{c}" opacity="0.8"/>')
    Y3=Y2+70; s.append(f'<line x1="{L}" y1="{Y3}" x2="{R}" y2="{Y3}" stroke="{AXIS}"/>'+tspans(L-10,Y3+5,['"Joining METR" posts'],14,INK,anchor='end',weight='bold'))
    for x in AR:
        mo=x['utc'][:7]
        if mo not in months: continue
        i=months.index(mo); d=int(x['utc'][8:10]); X=xm(i)+bw*(d/31); v=int(x['views'] or 0)
        s.append(f'<circle cx="{X:.1f}" cy="{Y3}" r="{max(6,min(22,6+4*math.log10(max(v,1e3)/1e3))):.1f}" fill="{AQUA}" opacity="0.8"/>')
    who={'ajeya_cotra':'Ajeya Cotra, from Coefficient','JoeJBenton':'Joe Benton, from Anthropic','JoshAEngels':'Josh Engels, from Google DeepMind','ChaseHasbrouck':'Chase Hasbrouck, from US Army','ArfurGrok':'Thomas Kwa leaves for OpenAI (third-party post)','_NathanCalvin':'Kwa leaves (Nathan Calvin post)'}
    lmrows=''.join(f'<div style="display:flex;gap:10px;font-size:14px;line-height:1.3"><span style="color:{MUTED};min-width:78px">{x["utc"][:10]}</span><i class="sw" style="background:{col.get(x["handle"],GRAY)};width:12px;height:12px;margin-top:4px"></i><span style="min-width:96px;font-weight:bold">{esc(x["handle"])}</span><span style="min-width:50px">{fmt_views(x["views"])}</span><span style="color:{MUTED}">{esc(x["text_200"][:70])} · {x["row_id"]}</span></div>' for x in LM)
    arrows=''.join(f'<div style="display:flex;gap:10px;font-size:14px;line-height:1.3"><span style="color:{MUTED};min-width:78px">{x["utc"][:10]}</span><span style="min-width:300px;font-weight:bold">{esc(who.get(x["handle"],x["handle"]))}</span><span style="min-width:50px">{fmt_views(x["views"])}</span><span style="color:{MUTED}">{x["row_id"]}</span></div>' for x in AR)
    tables=f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-top:6px"><div><div style="font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};font-weight:bold;margin-bottom:4px">Six biggest METR posts</div><div style="display:flex;flex-direction:column;gap:5px;font-size:14px">{"".join(toplist)}</div></div><div><div style="font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};font-weight:bold;margin-bottom:4px">Every lab-account post containing "METR"</div>{lmrows}</div><div><div style="font-size:14px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};font-weight:bold;margin-bottom:4px">Arrivals and departures on X</div>{arrows}</div></div>'
    svg=f'<svg width="{W-120}" height="{Y3+40}" viewBox="0 0 {W-120} {Y3+40}">{"".join(s)}</svg>'+tables
    tot=sum(v[1] for v in bym.values()); n=len(P)
    kp=f'<div class="kpis"><div class="kpi"><div class="l">@METR_Evals posts recovered</div><div class="v">{n}</div><div class="d">Feb 2024 – Sep 2026, {fmt_views(tot)} views in total</div></div><div class="kpi"><div class="l">Biggest post</div><div class="v">8.8M</div><div class="d">the time-horizon paper, Mar 19 2025 (MP{[x["row_id"] for x in P if x["id"]=="1902384481111322929"][0][2:]})</div></div><div class="kpi"><div class="l">Retrieved lab-account posts saying "METR"</div><div class="v">{len(LM)}</div><div class="d">since 2023 across ten accounts: Anthropic 4, OpenAI 2, Jack Clark 4; Altman, Amodei, Musk, Hassabis: 0 retrieved</div></div><div class="kpi"><div class="l">Retrieved official posts saying "METR"</div><div class="v">{len(OM)}</div><div class="d">Sacks, Sep 13 2026 (OM01); nine named official accounts searched, no other hit</div></div></div>'
    body=kp+legend([(AQUA,'Monthly views of METR\'s own posts (log scale; number of posts under each bar)'),(RED,'Anthropic'),(ORANGE,'OpenAI'),(BLUE,'Jack Clark (Anthropic co-founder), personal account')])+svg
    foot=f'<b>Coverage:</b> Grok X-API pull of @METR_Evals since 2024-01-01 (rows MP001–MP{n:03d}, research/metr_posts.csv); views are fxtwitter values at 2026-09-14 05:15 UTC. Not a full census: X search returns at most 10 posts per query window, and 2024-01, 04, 06, 07, 12 and 2025-09 came back empty, so quiet months may be under-counted rather than silent. Lab mentions are every retrieved post by the ten lab and lab-CEO accounts listed that contains the string "METR" (rows LM01–LM{len(LM):02d}), and the official count is the one retrieved post across nine named official accounts (research/officials_mentions.csv); retrieval is capped, so both are floors. In the retrieved set Amodei and Altman say "third-party evaluators" and never the name. Arrivals are first-party "joining" posts plus the two third-party posts on Kwa\'s departure (research/arrivals.csv). Reach is a measure of attention, not of correctness. {SRC}.'
    render(STEM, shell('METR\'s megaphone: one post drew 8.8M views, ten retrieved lab posts say its name, one official\'s does','Figure 10p · @METR_Evals reach, Feb 2024 – Sep 2026','Monthly views of METR\'s own X posts, every retrieved post in which one of ten frontier-lab or lab-CEO accounts wrote "METR", and the arrivals from Coefficient, Anthropic and DeepMind announced on X. Retrieval is capped, so these are floors.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10q. the Vanguard channel
def fig_vanguard():
    W,H=2200,1340; STEM='metr-17-the-vanguard-channel'
    V=rows('vanguard-ai-cluster.csv'); A=[x for x in V if x['tier'].startswith('A-') and 'borderline' not in x['tier']]
    import collections
    tot=collections.defaultdict(float); n=collections.Counter()
    for x in A: tot[x['fiscal_year']]+=num(x['amount']); n[x['fiscal_year']]+=1
    yrs=['FY2023','FY2024','FY2025']; win={'FY2023':'Jul 2022–Jun 2023','FY2024':'Jul 2023–Jun 2024','FY2025':'Jul 2024–Jun 2025'}
    L,base,top=200,520,80; vmax=70e6; yv=lambda v: base-(base-top)*v/vmax; s=[]
    for v in (20e6,40e6,60e6): s.append(f'<line x1="{L}" y1="{yv(v):.1f}" x2="{L+900}" y2="{yv(v):.1f}" stroke="{GRID}"/>'+tspans(L-10,yv(v)+5,[money(v)],14,MUTED,anchor='end'))
    for i,y in enumerate(yrs):
        X=L+60+i*280; v=tot[y]
        metr=sum(num(x['amount']) for x in A if x['fiscal_year']==y and x['canonical_name'].strip()=='METR')
        arc=sum(num(x['amount']) for x in A if x['fiscal_year']==y and 'Alignment Research' in x['canonical_name'])
        s.append(f'<rect x="{X}" y="{yv(v):.1f}" width="180" height="{base-yv(v):.1f}" rx="8" fill="{BLUE}" opacity="0.85"/>')
        if metr: s.append(f'<rect x="{X}" y="{yv(metr):.1f}" width="180" height="{base-yv(metr):.1f}" fill="{AQUA}"/>'+f'<line x1="{X+180}" y1="{(yv(metr)+base)/2:.1f}" x2="{X+196}" y2="{(yv(metr)+base)/2:.1f}" stroke="{AQUA}" stroke-width="2"/>'+tspans(X+200,(yv(metr)+base)/2+5,[f'METR {money(metr)}'],14,AQUA,weight='bold'))
        if arc:
            ya,yb=yv(metr+arc),yv(metr); yl=(ya+yb)/2-(22 if metr else 0)
            s.append(f'<rect x="{X}" y="{ya:.1f}" width="180" height="{yb-ya:.1f}" fill="{ORANGE}"/>'+f'<line x1="{X+180}" y1="{yl:.1f}" x2="{X+196}" y2="{yl:.1f}" stroke="{ORANGE}" stroke-width="2"/>'+tspans(X+200,yl+5,[f'ARC {money(arc)}'],14,ORANGE,weight='bold'))
        s.append(tspans(X+90,yv(v)-14,[money(v)],24,INK,anchor='middle',weight='bold')+tspans(X+90,base+26,[y],17,INK,anchor='middle',weight='bold')+tspans(X+90,base+46,[win[y]+f' · {n[y]} grantees'],13,MUTED,anchor='middle'))
    # tender / match annotations
    s.append(tspans(L+60,base+80,['Anthropic employee tender offer #1: May 2025 at $61.5B (inside FY2025). Anthropic donation match: 3:1 to 2024, 1:1 from 2025.'],14,MUTED))
    chart=f'<svg width="1120" height="{base+100}" viewBox="0 0 1120 {base+100}">{"".join(s)}</svg>'
    topl=sorted([x for x in A if x['fiscal_year']=='FY2025'],key=lambda x:-num(x['amount']))[:14]
    rowsh=''.join(f'<div style="display:flex;gap:10px;font-size:15px;line-height:1.35"><span style="min-width:90px;text-align:right;font-weight:bold">{money(num(x["amount"]))}</span><span style="min-width:330px">{esc(x["canonical_name"][:44])}</span><span style="color:{MUTED}">{esc(x["overlaps_known_portfolios"][:40]) or "—"} · {x["row_id"]}</span></div>' for x in topl)
    right=f'<div style="font-size:15px;letter-spacing:1.5px;text-transform:uppercase;color:{MUTED};font-weight:bold;margin-bottom:6px">FY2025 AI-safety and EA-infrastructure grantees at Vanguard Charitable, largest first (overlap with Tallinn, Coefficient, SFF portfolios)</div>{rowsh}'
    body=legend([(BLUE,'AI-safety and EA-infrastructure grants from Vanguard Charitable donor-advised funds (tiers A, borderline excluded)'),(AQUA,'of which METR'),(ORANGE,'of which ARC')])+f'<div style="display:grid;grid-template-columns:1140px 1fr;gap:26px">{chart}<div>{right}</div></div>'
    body+=f'<div style="background:#efece4;border-radius:10px;padding:14px 20px;font-size:17px;line-height:1.45;margin-top:10px">Vanguard Charitable pools thousands of donor-advised accounts and reports one line per grantee per year with the same purpose text on every row, so no grant can be tied to a donor. What the filing shows is a population: the FY2025 grantee list is the SFF and Coefficient recipient set, and it grew eight-fold in the year that contained Anthropic\'s first employee tender offer. Transluce, the second-largest line, separately reports 38% of its FY2025 revenue as personal gifts from OpenAI and Anthropic employees (EV06); Sentinel Bio lists individual EA donors and "donor advised funds" as its funders. METR\'s rule bars donations "made by or at the direction of frontier AI company employees"; a DAF grant directed by an employee would fall under it, and nothing here shows one did.</div>'
    foot=f'<b>Coverage:</b> Vanguard Charitable Endowment Program (EIN 23-2888152) Schedule I for FY2023–FY2025, parsed in full (21,268 / 24,269 / 27,221 grant rows; research/vanguard-fy20xx-schedule-i.csv) and classified into an AI-safety / EA-infrastructure tier by recipient name (rows VG001–VG{len(V):03d}, research/vanguard-ai-cluster.csv; NOTES-vanguard.md). Amounts are fiscal-year totals per grantee and may bundle several account holders. The tender-offer and match-program dates are context, not attribution: the filing cannot show whether any Anthropic or OpenAI employee\'s account is among the donors, and METR\'s $4.0M donor remains unidentified (M87). Tallinn, Moskovitz, Schmidt, Sijbrandij and McClave are excluded as the METR donor by their known vehicles. {SRC}.'
    render(STEM, shell('The Vanguard channel: donor-advised money to the AI-safety cluster grew from $8M to $66M in the year of Anthropic\'s first tender offer, and no filing says whose it is','Figure 10q · Vanguard Charitable Schedule I, FY2023–FY2025','METR\'s largest identifiable grant, $4.0M, came through Vanguard Charitable in FY2025. The same sponsor\'s grants to the AI-safety and EA-infrastructure cluster went from '+money(tot['FY2023'])+' to '+money(tot['FY2024'])+' to '+money(tot['FY2025'])+'. The donor-advised structure hides every donor.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10r. the argument vs the ledger
def fig_ledger():
    W,H=2200,1800; STEM='metr-18-the-argument-vs-the-ledger'
    I={r['row_id']:r for r in rows('independence_fight.csv')}
    VER={'contradicted':(RED,'Contradicted by the ledger'),'confirmed':(AQUA,'Confirmed by the ledger'),'incomplete':(YELLOW,'True as stated, incomplete'),'unchecked':(GRAY,'Not checkable from the ledger'),'narrower':(BLUE,'Narrower fact holds; claim as worded not checkable')}
    def claim(ids,quote,who,verdict,ledger):
        c,lab=VER[verdict]; v=sum(num(I[i]['views']) for i in ids)
        return (f'<div style="background:#efece4;border-radius:10px;padding:12px 16px;border-left:6px solid {c};display:flex;flex-direction:column;gap:6px">'
                f'<div style="font-size:17px;line-height:1.3;font-weight:bold">“{esc(quote)}”</div>'
                f'<div style="font-size:14px;color:{MUTED}">{esc(who)} · {fmt_views(v)} views · {", ".join(ids)}</div>'
                f'<div style="font-size:14px;line-height:1.35"><span style="display:inline-block;padding:1px 8px;border-radius:6px;background:{c};color:#fff;font-weight:bold;font-size:12px;letter-spacing:1px;text-transform:uppercase;margin-right:6px">{esc(lab)}</span>{ledger}</div></div>')
    crit=[
        claim(['IF83'],'Coefficient, itself closely tied to Anthropic, pays their bills','SE Gyges, anonymous commentator','narrower','No direct grant from Coefficient to METR in the 2,911-row awards index (M33) or in the Coefficient 990 checked (M105); RAND\'s FY2023–25 990s show no Schedule I line to METR and METR is not among RAND\'s five named contractors, with 47–61 contractors unnamed each year (M124). "Pays their bills", as a claim about all funding routes, is not checkable from filings.'),
        claim(['IF83'],'their entire senior staff are ~all old friends of Anthropic\'s senior staff','SE Gyges','unchecked','"All", "senior" and "old friends" are in no row. What METR said itself in May 2026: "some METR staff have strong social ties to employees of AI companies", "at least 6" of the staff on its Frontier Risk Report "have close personal relationships with AI company staff", it works out of Constellation, a centre founded by Redwood in 2023 and funded with $22.95M of Coefficient grants, which "hosts some AI lab staff" and whose 2023–24 returns list Coefficient program officer Eli Rose as a director (RW57, RW62, M126–M128), and it had no personnel conflict-of-interest policy when that report began (DR28, DR30, AE23). Two ties are on the record by name, both disclosed by METR itself in a Sep 13 edit to its Aug 26 report post (IF149): co-author Ajeya Cotra is married to Paul Christiano, who joined OpenAI\'s Safety and Security Committee fourteen days after publication (C12, C11), and co-author Ryan Greenblatt of Redwood "is the domestic partner of Beth Barnes, METR\'s CEO" (RW59). The roster: 5 of 49 roster records (staff, advisors, contractors, one duplicate) came from a frontier lab (S01–S49); Christiano was listed as advisor and board member on captures from Dec 28 2023 to Feb 22 2024 (C06); Karnofsky was listed as advisor through Dec 3 2024 and is now at Anthropic (B12).'),
        claim(['IF14'],'a "voluntary" third-party auditor that is not only ideologically and financially tied','Heidy Khlaaf, AI Now Institute chief AI scientist','narrower','Documented relations, each separately: METR\'s page says it has not accepted funding from AI companies (N57); it uses free lab tokens it does not book (K01, K04–K05); it names "individuals from Jane Street" as donors while the firm, not those individuals, holds Anthropic stock (M75, J01). "Ideologically tied" is not a ledger question.'),
        claim(['IF75'],'pretty bad for a senior anthropic employee to be involved in early funding/advising for an "independent" auditing org','Yafah Edelman, Epoch AI chief strategy officer, on Logan Graham\'s offer','narrower','The offer is on the record, whether it was improper is a judgment, and no row shows any organization accepted it: Anthropic\'s Frontier Red Team head wrote "Happy to help w/ advice/connections/maybe $!" (IF69) and replied "something I\'m sensitive to" (IF76). METR\'s own rule bars donations "made by or at the direction of frontier AI company employees" (N57).'),
        claim(['IF72'],'Must be independent and not indirectly funded by the labs or those enriched by their growth','Talia Goldberg, Bessemer partner','unchecked','A proposed standard, not a checkable claim. Under a textual rule, 4 of the 15 donor lines that give to METR record a firm investment, a named investment or a historical lab affiliation (J01 Jane Street the firm, J08 Schmidt, J12 Tallinn/SFF, J07 Farhi) and 2 to 3 an indirect organizational relationship (J03 Founders Pledge and SVCF routing, J15 Audacious via Good Ventures membership, J14 Longview\'s Coefficient funding). These are lines, not distinct donors, and several aggregate entities (J01–J17, Figure 10k).'),
        claim(['IF77','IF79'],'the suggestion that METR be treated as an authority is dangerous, deceptive, and morally corrupt / METR is corrupt','Greg Linares and Robert Graham, security researchers','unchecked','Neither post makes a checkable financial claim. Linares\'s is the largest post in the security panel of Figure 10t, not the largest critical post located (Julia Turc\'s IF49 has more views). No reply from Graham to Barry\'s request to specify (IF80) was located in the fetched payload.'),
    ]
    dfn=[
        claim(['IF85','IF90','IF61'],'METR has never accepted any funding from them (or when they were known as open philanthropy)','Alexander Barry (Epoch AI; METR research collaborator), Kei Nishimura-Gasparian (METR staff), Kelsey Piper','narrower','No direct grant found in the checked index and filing (M33, M105); "never" as a lifetime claim is not checkable. Left out of the sentence: ARC, which held $1.5M of Coefficient grants (M01–M02) and $5.6M of SFF recommendations (M35–M37), transferred $4,553,935 of assets to METR at the April 2024 spin-out (M63), a program transfer that does not identify whose money it contained; Coefficient\'s $10M "AI Evaluation and Testing" award went to RAND, METR\'s partner in the Canary program, with no traced payment onward (M03, M57).'),
        claim(['IF68','IF74'],'They also take no funding from the labs (beyond API credits) and don\'t accept donations from individuals whose source of wealth is from working at the labs','Alexander Barry','narrower','METR\'s current rule bars donations "made by or at the direction of frontier AI company employees" (N57), narrower than "anyone whose wealth came from a lab"; the no-lab-funding statement is METR\'s own. The credits are unbooked in-kind support: the FY2024 990 records no non-cash contribution (N02) and METR valued one six-day OpenAI allotment at about $400K (K05).'),
        claim(['IF84'],'RAND reports their grants and contractor spends - no METR','Jai (@Laneless_), says they have worked closely with METR','incomplete','RAND\'s FY2023–25 990s list no Schedule I grant to METR and METR is not among the five named contractors each year, but 53, 47 and 61 contractors over $100K are unnamed, so a subcontract below the fifth-largest ($987K, $1.15M, $965K) cannot be excluded (M124).'),
        claim(['IF87'],'CG giving $10m to a $38m RAND/METR collaboration (of which METR got $17m) ... They received $71m in the last 6 months alone','Charles (@CharlesD353), Arb Research','narrower','The amounts match the rows with their measure labels: Audacious committed about $38M to Canary with about $17M allocated to METR, Oct 2024 (M57, M58); Coefficient\'s $10M award to RAND is dated Sep 2025 and is not a traced METR payment (M03); METR reported $71M of commitments, not cash received, in the six months to Aug 2026 (G03).'),
        claim(['IF87'],'METR is mostly funded by a handful of very rich EAs at Jane Street','Charles','unchecked','METR names "individuals from Jane Street" with no names or amounts (M75); no 990 identifies them. Jane Street the firm bought Anthropic stock in 2024 and 2025 (J01).'),
        claim(['IF70','IF89'],'today is a great day to apply to METR / all the third party evaluators should not be financially supported by the labs','Drake Thomas, Anthropic staff','confirmed','Confirmed as statements and affiliation only: an Anthropic staffer recruited for METR on Sep 12 (30K views) and argued against lab funding of evaluators; the same account said METR\'s leverage is that "there are few options" (IF62–IF63). Not a verdict on any evaluator\'s independence.'),
    ]
    col=lambda title,items,c: f'<div><div style="font-size:17px;letter-spacing:2px;text-transform:uppercase;color:{c};font-weight:bold;margin-bottom:8px">{title}</div><div style="display:flex;flex-direction:column;gap:10px">{"".join(items)}</div></div>'
    grid=f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:4px">{col("What critics said, Sep 12–13",crit,RED)}{col("What defenders said, Sep 12–13",dfn,AQUA)}</div>'
    kp=('<div class="kpis">'
        '<div class="kpi" style="min-width:250px"><div class="l">Direct Coefficient grant to METR found</div><div class="v">none</div><div class="d">in the 2,911-row awards index and the Coefficient 990 checked (M33, M105)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">ARC → METR, spin-out</div><div class="v">$4.55M</div><div class="d">assets transferred Apr 2024, ARC FY2024 990 (M63)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Coefficient → RAND, evaluation</div><div class="v">$10M</div><div class="d">"AI Evaluation and Testing", Sep 2025 (M03)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">RAND → METR named in RAND\'s 990s</div><div class="v">none</div><div class="d">FY2023–25 Schedule I and five named contractors; 47–61 unnamed each year (M124)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Lab cash to METR</div><div class="v">none</div><div class="d">per METR\'s own statement, not independently verified; tokens are unbooked (N57, K01, K05)</div></div></div>')
    body=kp+legend([(RED,'Contradicted by the ledger'),(AQUA,'Confirmed by the ledger'),(YELLOW,'True as stated, but incomplete'),(BLUE,'Narrower fact holds; claim as worded not checkable'),(GRAY,'Not checkable from the ledger')])+grid
    foot=f'<b>Coverage:</b> The Sep 12–14 reply threads on METR\'s independence pulled whole by the Grok G6 lane (Hwang, Edelman, Gyges/Laneless, corsaren threads plus every post by lab- and evaluator-affiliated accounts on the terms; research/grok-out/G6-insiders.csv, 324 rows) and refetched through fxtwitter at 2026-09-14 05:23 UTC (research/fx-lane6/); rows IF67–IF91 in research/independence_fight.csv, with IF11, IF14 and IF61 from the earlier pull. Each claim is scored only against rows in research/: "contradicted" means a row records the opposite; "incomplete" means the sentence is accurate and a related row is missing from it; "narrower" means a narrower fact is in the rows while the claim as worded (all funding routes, lifetime, everyone, improper) is not; "not checkable" means the claim is about friendship, motive, a proposed standard or undisclosed amounts. Labels were re-derived in the Codex second audit (research/AUDIT-2.md, findings 6–11) and no card is now scored "contradicted": a missing positive record is not a record of the opposite. Money types are never added together: M63 is a transfer of assets, M03 and M01–M02 are grants, M35–M37 and G03 are recommendations and commitments, K05 is in-kind. Alexander Barry\'s METR affiliation appears in one of his ten located posts (IF80) and on metr.org/about (N58). Who is right about "independence" is a judgment the rows do not settle; the figure records what each side asserted and what the filings show. Nothing here establishes motive, routing of any particular dollar, or wrongdoing. {SRC}.'
    render(STEM, shell('No direct Coefficient grant to METR appears in the checked index and filings; both sides argued over one anyway. The filings do show an ARC program transfer and a Coefficient award to METR\'s RAND partner','Figure 10r · The reply threads, scored against the research ledger','After Sacks, the fight moved into replies. Critics said Coefficient "pays their bills"; METR-affiliated accounts said METR "never accepted any funding" from it. Neither claim, as worded, can be settled from filings. What the filings do record: a $4.55M ARC program transfer at the spin-out, a $10M Coefficient award to METR\'s RAND partner, unbooked lab tokens, and donor lines with lab ties on record.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10s. the rule and the donor
def fig_rule():
    W,H=2200,1560; STEM='metr-19-the-rule-and-the-donor'
    D={r['row_id']:r for r in rows('donor_rule.csv')}
    L,R=170,W-150; top=120
    def xd(d):
        y,m,dd=(d+'-01-01')[:10].split('-')[:3]; y=int(y); m=int(m); dd=int(dd[:2]) if dd else 1
        t=y+(m-1)/12+(dd-1)/365; t0=2024+3/12; t1=2026+9/12
        return L+(R-L)*(t-t0)/(t1-t0)
    s=[]
    for y in (2024,2025,2026):
        for m in range(1,13):
            d=f'{y}-{m:02d}'
            if (y,m)<(2024,4) or (y,m)>(2026,9): continue
            x=xd(d); s.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+880}" stroke="{GRID}"/>')
            if m in (1,7): s.append(tspans(x,top-14,[('Jan ' if m==1 else 'Jul ')+str(y)],14,MUTED,anchor='middle',weight='bold'))
    Y1=top+200; Y2=Y1+430
    s.append(f'<line x1="{L}" y1="{Y1}" x2="{R}" y2="{Y1}" stroke="{AXIS}" stroke-width="2"/>'+tspans(L-12,Y1+5,["METR's rule"],16,INK,anchor='end',weight='bold'))
    s.append(f'<line x1="{L}" y1="{Y2}" x2="{R}" y2="{Y2}" stroke="{AXIS}" stroke-width="2"/>'+tspans(L-12,Y2+5,['David Farhi'],16,INK,anchor='end',weight='bold'))
    OFF={'an':-92,'af':-184,'bn':34,'bf':126}
    def mark(Y,d,t,rid,c,lvl,anchor='start'):
        x=xd(d); yy=Y+OFF[lvl]; lines=[d]+wrap(t,50)[:3]
        tip = yy+16*len(lines)+2 if lvl[0]=='a' else yy-16
        s.append(f'<line x1="{x:.1f}" y1="{Y}" x2="{x:.1f}" y2="{tip}" stroke="{c}" stroke-width="2"/><circle cx="{x:.1f}" cy="{Y}" r="9" fill="{c}"/>')
        tx=x+(6 if anchor=='start' else -6)
        s.append(tspans(tx,yy,lines,13,INK,anchor=anchor,lh=16)+tspans(tx,yy+16*len(lines),[rid],11,MUTED,anchor=anchor))
    mark(Y1,'2024-04-23','No lab-money rule on the site','DR02',GRAY,'an')
    mark(Y1,'2025-04-18','"not accepted compensation from AI companies for the evaluations" (present by Apr 18, absent Apr 1)','DR07',YELLOW,'bn')
    mark(Y1,'2025-08-01','"not accepted funding from AI companies"','DR08',YELLOW,'an')
    mark(Y1,'2025-09-27','Barnes: "open to taking donations from individual lab employees ... excluding senior decision-makers, <50% of our funding"','DR10',ORANGE,'bf')
    mark(Y1,'2026-05-19','"not accepting cash payments or donations from AI companies and AI lab executives"','DR15',ORANGE,'af','end')
    mark(Y1,'2026-07-19','"cannot accept donations made by or at the direction of frontier AI company employees" (after Jul 14 20:05, by Jul 19 17:12 UTC)','DR19',RED,'bn','end')
    mark(Y1,'2026-08-14','"we do not accept donations made by or at the direction of their staff"','DR22',RED,'an','end')
    mark(Y2,'2024-12-21','OpenAI o1 system card credit; o1 contributions page: "Supporting Leadership"','DR29',BLUE,'bn')
    mark(Y2,'2025-07-15','arXiv 2507.11473: "David Farhi, OpenAI"','DR29',BLUE,'an')
    mark(Y2,'2025-12-16','First named on metr.org/about: "individuals directly, such as David Farhi"','DR12',RED,'bn')
    mark(Y2,'2026-04-12','Computer History Museum profile (not an OpenAI page): "Technical Lead, OpenAI"','DR13',GRAY,'af','end')
    mark(Y2,'2026-07-15','WIRED reports he left OpenAI in summer 2025, with a statement from him','DR36',ORANGE,'an')
    mark(Y2,'2026-07-19','Still named on the Jul 19 page that adds the employee ban, and in the Aug 14 funding update that restates it','DR19, DR22',RED,'bf','end')
    x=xd('2026-08-14'); s.append(f'<circle cx="{x:.1f}" cy="{Y2}" r="9" fill="{RED}"/>')
    mark(Y2,'2026-09-14','About page live: still named; CHM profile unchanged','DR26',RED,'bn','end')
    x0,x1=xd('2025-12-16'),xd('2026-09-14'); s.append(f'<rect x="{x0:.1f}" y="{Y2-8}" width="{x1-x0:.1f}" height="16" fill="{RED}" opacity="0.18"/>')
    x2=xd('2026-07-19'); s.append(f'<rect x="{x2:.1f}" y="{Y1-8}" width="{R-x2:.1f}" height="16" fill="{RED}" opacity="0.18"/>')
    svg=f'<svg width="{W-120}" height="{Y2+230}" viewBox="0 0 {W-120} {Y2+230}">{"".join(s)}</svg>'
    cards='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:0">'
    cards+=card('Sep 27 2025, Barnes on the EA Forum · DR10','“We are open to taking donations from individual lab employees (subject to some constraints, e.g. excluding senior decision-makers, constituting &lt;50% of our funding).”',ORANGE,16)
    cards+=card('May 19 2026, METR Frontier Risk Report · DR15, DR28, DR30','“METR did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project ... some METR staff have strong social ties to employees of AI companies, and METR currently works out of a shared research center (Constellation) which hosts some AI lab staff.” Table A.1: “Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff.” Figure 10u has the full self-assessment.',ORANGE,16)
    cards+=card('What the rows do not establish · DR36–DR37','When Farhi gave, how much, whether the September 2025 "senior decision-maker" constraint applied to him, and his exact departure date: WIRED reported on Jul 15 2026 that he left OpenAI in summer 2025 (DR36); an FEC itemized receipt of Jun 16 2026 lists his employer as "SELF EMPLOYED" and his occupation as "RESEARCH MANAGER" (DR37), the only employer record in his own hand; the Computer History Museum profile still calls him "Technical Lead, OpenAI" (DR13, DR26). A donor acknowledgement does not disclose gift timing or establish a breach of any applicable rule. No conflict is asserted.',GRAY,16)
    cards+='</div>'
    body=legend([(GRAY,'No rule on the page'),(YELLOW,'Says no company money taken'),(ORANGE,'Employee gifts allowed with limits / executives excluded'),(RED,'Employee gifts barred'),(BLUE,'OpenAI credit on a paper or page (historical)'),(GRAY,'Third-party profile'),(ORANGE,'Departure reported'),(RED,'Named as a METR supporter')])+svg+cards
    foot=f'<b>Coverage:</b> Wayback captures of metr.org/donate (monthly Apr 2024–Sep 2026) and metr.org/about (monthly from Dec 2024, plus Apr 2024), with unique-digest captures around each wording change (search coverage, not a manifest of every intervening state), METR\'s 2024 annual report, the May 19 2026 Frontier Risk Report, the Aug 14 2026 funding update, Barnes\'s Sep 2025 X thread and EA Forum quick take, the Sep 11 2026 Business Insider interview, arXiv author search for Farhi, D (12 papers, none announced in 2026), OpenAI 2026 system cards, and the Computer History Museum profile (rows DR01–DR29, research/donor_rule.csv; located by the Grok G8 lane, refetched first-hand (research/fr-verify/, agent S1) and re-derived in the Codex second audit (research/AUDIT-2.md findings 12–17). The "compensation" footnote is present from the Apr 18 2025 capture and absent on Apr 1; the employee-ban sentence appears between the Jul 14 20:05 and Jul 19 17:12 UTC about captures and by the Aug 4 donate capture; Farhi is named on all 76 recovered about captures from Dec 16 2025 to Sep 13 2026 (three digests unrecovered). The dated statements differ in scope (compensation for evaluations, company funding, employee gifts, executive gifts) and are not four demonstrated tightenings of one rule. The rule\'s dates and Farhi\'s credits are facts about pages; the overlap is a sequence, not a finding that any gift broke a rule. {SRC}.'
    render(STEM, shell('METR\'s wording on lab-employee gifts went from "open to" them (Sep 2025) to "cannot accept" them (Jul 2026); it kept naming David Farhi, whom WIRED reports left OpenAI in summer 2025, as a supporter throughout','Figure 10s · METR\'s lab-money statements, 2024–2026, against one named donor','METR\'s public statements on lab money changed in dated steps. David Farhi, credited on OpenAI papers through July 2025 and titled "Technical Lead, OpenAI" on a Computer History Museum profile, was first named a METR supporter in December 2025 and is still named; WIRED reported in July 2026 that he left OpenAI in summer 2025. Gift date and amount are not public.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10t. the security revolt and the founder call
def fig_revolt():
    W,H=2200,2260; STEM='metr-20-the-security-revolt-and-the-founder-call'
    I={r['row_id']:r for r in rows('independence_fight.csv')}; AR={r['row_id']:r for r in rows('arrivals.csv')}
    sec=[('IF77','against'),('IF14','against'),('IF103','against'),('IF99','against'),('IF98','against'),('IF100','for'),('IF113','against'),('IF110','against'),('IF101','against'),('IF79','against'),('IF102','against'),('IF104','against'),('IF107','mixed'),('IF105','against'),('IF109','mixed'),('IF108','mixed'),('IF106','against'),('IF111','against'),('IF112','mixed')]
    col={'against':RED,'for':AQUA,'mixed':YELLOW}
    L=40; y=30; rowh=44; ss=[]
    for t,xx in [('UTC',L),('Who',L+120),('Views (log)',L+430),('What it said',L+720)]: ss.append(tspans(xx,y,[t],14,MUTED,weight='bold'))
    y+=26; vmax=math.log10(4e5)
    for rid,st in sorted(sec,key=lambda k:-num(I[k[0]]['views'])):
        r=I[rid]; v=num(r['views']); w=200*(math.log10(max(v,100))-2)/(vmax-2); c=col[st]
        el=wrap(r['event'],74)[:4]; rh=rowh+ (len(el)-1)*15
        ss.append(f'<rect x="{L-10}" y="{y-24}" width="1250" height="{rh-4}" rx="6" fill="#efece4"/>')
        ss.append(tspans(L,y,[r['utc'][5:16].replace('-','/').replace('T',' ')],13,MUTED)+tspans(L+120,y,[r['actor'].split('(')[0].strip()[:24]],15,INK,weight='bold'))
        ss.append(f'<rect x="{L+430}" y="{y-15}" width="{max(3,w):.1f}" height="18" rx="4" fill="{c}"/>'+tspans(L+438+max(3,w),y,[fmt_views(v)],13,INK,weight='bold'))
        ss.append(tspans(L+720,y,el,12,INK,lh=15)+tspans(L+1232,y,[rid],10,MUTED,anchor="end"))
        y+=rh
    left_svg=f'<svg width="1300" height="{y}" viewBox="0 0 1300 {y}">{"".join(ss)}</svg>'
    n_sec=len(sec); n_for=sum(1 for _,st in sec if st=='for')
    left=(f'<div><div style="font-size:16px;letter-spacing:2px;text-transform:uppercase;color:{RED};font-weight:bold;margin-bottom:6px">Security professionals and their amplifiers on METR, Sep 12–13</div>'+left_svg+
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px">'+
          card('Linares\'s bill of particulars · IF105','“The lack of evidence presented even when respected members of cybersecurity requested for it publicly. The failure to use any industry recognized Incident response firm ... The negligent test scenarios and invalid sandbox environment ... refusal to include any of the cybersecurity [community] to review, replicate, or validate any finding.”',RED,14)+
          card('The answers · IF71, IF100, AR11',f'Anthropic\'s red-team head: “The 3 METR investigators aren\'t cyber experts and they did a phenomenal job!” (1.2K views). Joshua Saxe, ex-Meta security: “many at METR gave up generational wealth to work there ... Security people should go work there” (14K). Sep 13 21:00 UTC: a retiring Army Cyber Command forensics lead announces he is joining METR as an advisor (17K).',AQUA,14)+'</div></div>')
    chain=[('1','Sep 12 19:45 · Anthropic\'s Frontier Red Team head','IF69','“Let a thousand METRs bloom ... Happy to help w/ advice/connections/maybe $!” (114K)',RED),
           ('2','20:43–20:46 · Mike McCormick, Halcyon Futures, and Graham\'s reply','IF139, IF94, IF92, IF93, M125, M131','20:43 McCormick: “We need 10 more METRs” (3K). 20:44, replying to Graham: “Would gladly support these!” (2K). 20:45 Graham: “Mike is person #1 I think of” (3K). 20:46 McCormick: “I\'d love to fund / launch more eval and audit orgs (and companies)” (24K). Halcyon: nonprofit seed grants up to $1M; FY2024 revenue $2.1M, $611K grants paid, of which $185K to three named organizations including $65K to Clarity AI Research, Transluce\'s legal entity. Largest funder among identified records: Good Ventures, Coefficient\'s principal donor, $902,880 paid in FY2024 and $527,870 approved, not paid (990-PF).',ORANGE),
           ('3','21:16 · A MATS fellow','IF97','“I am proposing for this now with CG through MATS. Would you be willing to connect re the proposed org? Directly relates to your role at A\\” (149)',BLUE),
           ('4','21:39 · Anuja Uppuluri, Coefficient Tailwind staff, ex-Anthropic by her own account','IF96, IF132, IF133','“There is a LOT of money my team and I at Coefficient Giving want to give out via Tailwind, LOCK IN” (10K), linking Graham\'s post while quote-posting her own Sep 9 announcement: “After leaving Anthropic, I\'ve been working on Tailwind ... there could be $200 million dollars waiting for the right ambitious idea” (23K). Her Dec 2025 post credits work on Opus 4.5 (105K).',BLUE),
           ('5','Sep 13 01:08 and 01:52 · The objection and the reply','IF75, IF76','Epoch\'s chief strategy officer: “pretty bad for a senior anthropic employee to be involved in early funding/advising for an \'independent\' auditing org” (13K). Graham: “something I\'m sensitive to — if I can help bootstrap and pass off, cool” (1K).',GRAY),
           ('C','Context, Sep 9–13 · Coefficient\'s grantmakers on METR (not a step in the chain)','IF135, D20, IF134, IF136, IF138','Sep 9: Catherine Brewer “metr just can\'t stop winning” (1K); Jake Mendel “welcome to the metr golden age” (3K). Sep 10: McCormick says Halcyon\'s own RFP would be “hard to beat CG / Tailwind” (2K). Sep 12: managing director Luke Muehlhauser, “A lot of high-skill, high-context people should be applying to METR right now” (21K). Sep 13: Alex Lawsen points Graham to Tailwind\'s “independent AI auditors” initiative (2K).',LGRAY)]
    right=f'<div><div style="font-size:16px;letter-spacing:2px;text-transform:uppercase;color:{BLUE};font-weight:bold;margin-bottom:6px">The founder call, in UTC order, with per-post snapshot views</div><div style="display:flex;flex-direction:column;gap:8px">'
    for n,who,rid,q,c in chain:
        right+=f'<div style="background:#efece4;border-radius:10px;padding:10px 14px;border-left:6px solid {c};display:flex;gap:12px"><div style="font-size:26px;font-weight:bold;color:{c};min-width:30px">{n}</div><div><div style="font-size:14px;color:{MUTED}">{esc(who)} · {rid}</div><div style="font-size:15px;line-height:1.3;margin-top:3px">{esc(q)}</div></div></div>'
    right+=f'</div><div style="margin-top:10px;font-size:14px;color:{MUTED};line-height:1.4">Who answered: 22 tagged posts from 19 handles, a mixture of offers, proposals, existing projects (Continuation Observatory, Oktsec, Bluejay, LlmStats, FideAILabs) and commentary; none was independently assessed, and none named a funder other than Halcyon or Coefficient (G9-thousand-metrs.csv, new_org_named column). Anthropic\'s Drake Thomas told applicants it was "a great day to apply to METR" (IF70, 30K views).</div></div>'
    kp=(f'<div class="kpis"><div class="kpi" style="min-width:230px"><div class="l">Selected posts / accounts</div><div class="v">{n_sec} / 16</div><div class="d">security-community accounts and amplifiers, Sep 12–13, any view count; Linares four times</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Explicit defenses in this selection</div><div class="v">{n_for}</div><div class="d">Joshua Saxe, ex-Meta (IF100); four more rows are mixed</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Largest post in this panel</div><div class="v">{fmt_views(num(I["IF77"]["views"]))}</div><div class="d">Greg Linares, "dangerous, deceptive, and morally corrupt" (snapshot views)</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Sources of offered money</div><div class="v">3</div><div class="d">Graham "maybe $"; Halcyon seed grants up to $1M (M125, M131); Coefficient Tailwind tiers $200K–$200M+ (M123). Offers and ceilings, not pools of cash</div></div></div>')
    body=kp+legend([(RED,'Against METR'),(AQUA,'For METR'),(YELLOW,'Mixed or procedural'),(BLUE,'Coefficient-side post'),(ORANGE,'Incubator post'),(LGRAY,'Context, not a step')])+f'<div style="display:grid;grid-template-columns:1300px 1fr;gap:26px">{left}{right}</div>'
    foot=f'<b>Coverage:</b> Grok G9 lane, no view threshold: every reply and quote-post of Graham\'s and Thomas\'s Sep 12 posts, the full Linares, Robert Graham and Khlaaf threads, and a keyword sweep for "new METR", "another METR", "independent auditor" and "Tailwind" from Sep 12 (research/grok-out/G9-thousand-metrs.csv, 788 rows including off-topic keyword hits; Graham\'s post advertised ~110 replies and Linares\'s ~86, and Grok\'s recovery of each is partial, so counts are lower bounds). Every post drawn was refetched through fxtwitter at 2026-09-14 06:40 UTC (research/fx-lane9/); rows IF92–IF113 plus IF14, IF69–IF71, IF75–IF77, IF79 in research/independence_fight.csv; Halcyon\'s 990s in research/halcyon-990-*.xml (M125). "Security professional" follows the account\'s own bio or public page; the panel is a selection, not a census of a profession, and stance colours are the author\'s reading of each full post. Charles Dardaman\'s claim of a marital tie between a METR investigator and an OpenAI board member (IF112) matches public record already in the ledger: Ajeya Cotra, co-author of the Aug 26 report, is married to Paul Christiano, who joined the OpenAI Foundation board on Sep 9 (C12, E35, C11); the appointment post-dates the report. On Sep 13 METR itself added that disclosure to the report post, together with one nobody on X had raised: co-author Ryan Greenblatt "is the domestic partner of Beth Barnes, METR\'s CEO" (IF149, RW59). The chain on the right is public posts in UTC order with each post\'s own snapshot views; it shows who offered money and who linked whom, not an agreement between them. McCormick\'s first offer (20:44) precedes Graham\'s naming him (20:45). Codex second audit: research/AUDIT-2.md findings 18–24 and 34. Coefficient itself has no grant to Halcyon in the index, but Good Ventures, the Moskovitz foundation that is Coefficient\'s principal donor, paid Halcyon $902,880 in FY2024 with $527,870 more approved for later payment (990-PF Part XV, M131); other funders listed by CauseIQ and philanthropy.org (Fidelity Charitable, DAFgiving360, American Endowment Foundation, Secure AI Future) were not refetched. Halcyon\'s FY2023 return was amended from $3.57M to $2.14M revenue. McCormick\'s Jul 23 offer of “$250k career transition grant or a $1m pre-seed check” for “AI control, verification, oversight” (164K views, IF137) pre-dates the essay by seven weeks. {SRC}.'
    render(STEM, shell('Sixteen security-community accounts called METR unqualified or conflicted and one defended it; the "thousand METRs" call ran from Anthropic\'s red team to a Good Ventures-funded incubator to Coefficient\'s Tailwind within two hours','Figure 10t · September 12–13, 2026: two threads the Sacks census missed','Left: a selection of security researchers and their amplifiers said METR lacks the expertise or independence to judge the Hugging Face and Anthropic incidents; the largest post in the selection out-drew its one explicit defense. Right: Anthropic\'s red-team head invited founders to build rival auditors and named the funder to call; that incubator\'s largest identified backer is Good Ventures, and a Coefficient Tailwind staffer who says she left Anthropic linked his post to advertise Tailwind.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10u. METR grades itself
def fig_aef1():
    W,H=2200,2260; STEM='metr-21-metr-grades-itself'
    A=rows('aef1.csv'); D={r['row_id']:r for r in rows('donor_rule.csv')}
    P={'1':'Secure sufficient access and resources','2':'Minimized conflicts of interest','3':'Evaluator autonomy','4':'Disclosure of results','5':'Security and responsible disclosure'}
    def colour(f):
        f=f.strip().lower()
        if f.startswith('yes'): return AQUA
        if f.startswith('not requested'): return GRAY
        if f.startswith('partial'): return YELLOW
        if f.startswith('no'): return RED
        if f.startswith('see notes'): return ORANGE
        return GRAY
    main=[r for r in A if r['kind'] in ('Requirement','Recommendation')]
    subs=[r for r in A if r['principle_no']=='2' and r['item_no'].startswith('2.4.')]
    acc=[r for r in A if r['item_no'].startswith('1.1.')]
    L=40; y=34; rowh=46; s=[]
    for t,xx in [('Item',L),('Kind',L+80),('METR\'s answer',L+250),('Text and METR\'s note',L+430)]: s.append(tspans(xx,y,[t],14,MUTED,weight='bold'))
    y+=26; cur=None
    for r in main:
        if r['principle_no']!=cur:
            cur=r['principle_no']; y+=10
            s.append(tspans(L,y,[f'{cur}. {P[cur]}'],17,INK,weight='bold')); y+=30
        f=r['fulfilled'].strip(); c=colour(f); req=r['kind']=='Requirement'
        flip=f.lower().startswith(('no','see notes')) and req
        s.append(f'<rect x="{L-10}" y="{y-24}" width="1270" height="{rowh-4}" rx="6" fill="{"#fbe9e7" if flip else "#efece4"}"/>')
        s.append(tspans(L,y,[r['item_no']],14,INK,weight='bold')+tspans(L+80,y,[('required' if req else 'recommended')],13,RED if req else MUTED))
        s.append(f'<rect x="{L+250}" y="{y-16}" width="150" height="22" rx="5" fill="{c}"/>'+tspans(L+325,y,[f[:16]],13,'#fff' if c not in (YELLOW,GRAY) else INK,anchor='middle',weight='bold'))
        txt=r['item_text'].replace('The evaluator ','').replace('The system provider ','Provider ')
        note=r['notes_evidence'].strip()
        s.append(tspans(L+430,y-6,[txt[:118]+('…' if len(txt)>118 else '')],13,INK)+tspans(L+430,y+11,[note[:140]+('…' if len(note)>140 else '')] if note else [''],11,MUTED)+tspans(L+1252,y,[r['row_id']],10,MUTED,anchor='end'))
        y+=rowh
    svg=f'<svg width="1320" height="{y}" viewBox="0 0 1320 {y}">{"".join(s)}</svg>'
    n_req=sum(1 for r in main if r['kind']=='Requirement'); n_req_no=sum(1 for r in main if r['kind']=='Requirement' and r['fulfilled'].strip().lower().startswith(('no','see notes')))
    n_yes=sum(1 for r in main if r['fulfilled'].strip().lower().startswith('yes'))
    q=lambda rid: esc(D[rid]['quote_or_fact'])
    right='<div style="display:flex;flex-direction:column;gap:12px">'
    right+='<div><div style="font-size:15px;letter-spacing:2px;text-transform:uppercase;color:'+MUTED+';font-weight:bold;margin-bottom:6px">The six disclosure questions under 2.4</div><div style="display:flex;flex-direction:column;gap:5px">'
    for r in subs:
        f=r['fulfilled'].strip(); good=f.lower().startswith('no'); c=AQUA if good else RED
        txt=r['item_text'].replace('the system provider','the lab').replace('its direct competitor','a rival')
        lab='no' if good else 'disclosed'
        right+=f'<div style="display:flex;gap:10px;align-items:flex-start;background:#efece4;border-radius:8px;padding:7px 10px"><span style="display:inline-block;min-width:36px;text-align:center;padding:2px 6px;border-radius:5px;background:{c};color:#fff;font-weight:bold;font-size:12px">{lab}</span><div style="font-size:13px;line-height:1.3">{esc(txt[:150])}'+(f'<div style="color:{MUTED};margin-top:2px">“{esc(f[:220])}”</div>' if not good else '')+f'<div style="color:{MUTED};font-size:11px">{r["row_id"]}</div></div></div>'
    right+='</div></div>'
    right+=card('What METR asked for, and got · AE02–AE09, AE13','Query access: yes (AE02). Intermediate states, i.e. chains of thought: yes (AE05). Other elicitation tools: yes (AE08). Scaffolding access: partial (AE03). Safeguard exemptions: partial (AE04). Fine-tuning, weights, user data: not requested. Legal safe harbor: not requested (AE13). "Companies were not required to authorize" third-party monitoring of outputs.',YELLOW,14)
    right+=card('The exit door · DR32',q('DR32')[:330],ORANGE,14)
    right+=card('The incentive METR names · DR31',q('DR31')+' (AE19, AE25)',ORANGE,14)
    right+=card('The preamble · DR28, DR30','“METR did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project, and as such we did not run a formal recusal or disclosures process. Given this, this pilot was not compliant with all of the requirements of the AEF-1 standard.” ... “Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff.”',RED,14)
    right+='</div>'
    kp=(f'<div class="kpis"><div class="kpi" style="min-width:220px"><div class="l">AEF-1 items</div><div class="v">{len(main)}</div><div class="d">{n_req} requirements, {len(main)-n_req} recommendations</div></div>'
        f'<div class="kpi" style="min-width:220px"><div class="l">Answered "Yes"</div><div class="v">{n_yes}</div><div class="d">of 26, by METR\'s own grading; 4.1 notes methodological sufficiency is "not determinable by METR alone"</div></div>'
        f'<div class="kpi" style="min-width:220px"><div class="l">Requirements answered "No"</div><div class="v">2</div><div class="d">2.3 published conflict-of-interest policy; 5.4 responsible-disclosure policy. One more, 4.6 redaction authority, answered "See notes" (silent exit)</div></div>'
        f'<div class="kpi" style="min-width:220px"><div class="l">Staff with "close personal relationships" to lab staff</div><div class="v">≥6</div><div class="d">METR\'s own count for this pilot (AE23)</div></div></div>')
    body=kp+legend([(AQUA,'Yes'),(YELLOW,'Partial'),(RED,'No'),(ORANGE,'See notes'),(GRAY,'Not requested / N/A'),('#fbe9e7','A requirement answered No or See notes')])+f'<div style="display:grid;grid-template-columns:1320px 1fr;gap:24px">{svg}{right}</div>'
    foot=f'<b>Coverage:</b> Table A.1 of METR\'s Frontier Risk Report, May 19 2026, which grades the report\'s own operating conditions against AEF-1, a voluntary standard of the AI Evaluator Forum of which METR is a member (rows AE01–AE40, research/aef1.csv, extracted verbatim from research/fr-verify/risk-report-20260519.html; preamble in research/aef1_preamble.txt; quotes DR28, DR30–DR33 in research/donor_rule.csv). The 26 numbered items are drawn; the eight access sub-items under 1.1 and the six disclosure questions under 2.4 are summarised at right. "No" on a 2.4 disclosure question is the favourable answer and is coloured green; the prose answer to the sixth question is marked "disclosed". The answers are METR\'s; the colour categories and the row shading for "See notes" are this figure\'s presentation, and the report says its methodological sufficiency is not determinable by METR alone (AE30). Redaction and silent-exit provisions belong to this voluntary pilot and are not projected onto the Sep 2026 investigation. The pilot covered Anthropic, Google, Meta and OpenAI models shared between Feb 16 and Mar 16 2026 under agreements that let any participant exit silently before approving non-public information, which METR says means the participant list "may not represent the full set of companies who began engaging". Nothing here concerns the Sep 2026 Anthropic incident investigation, whose terms are not yet published. {SRC}.'
    render(STEM, shell('METR graded its own independence in May 2026: two requirements answered "No", no conflict-of-interest policy, "at least 6" staff and collaborators with close personal ties to lab employees','Figure 10u · METR\'s AEF-1 self-assessment, Frontier Risk Report, May 19 2026','Four months before Amodei proposed it as the embedded evaluator, METR published a compliance table against its own industry\'s standard. It answered Yes on 21 of 26 items, said it had no personnel conflict-of-interest policy, named the incentive that free tokens create, and disclosed that participants could leave the pilot without anyone knowing.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10v. where the sentence went
def fig_transmission(lean=False):
    W,H=2200,(2160 if lean else 1900); STEM='metr-22b-where-the-sentence-went-with-lean' if lean else 'metr-22-where-the-sentence-went'
    T=rows('transmission.csv'); I={r['row_id']:r for r in rows('independence_fight.csv')}
    LN={r['outlet_match']:r for r in rows('lean.csv')}
    def lean_of(o):
        for k,r in LN.items():
            if k!='(unrated)' and o.startswith(k): return r
        return None
    def lean_badge(o):
        r=lean_of(o)
        if not r: return f'<span style="display:inline-block;padding:1px 6px;border-radius:5px;background:{LGRAY};color:{MUTED};font-size:10px;font-weight:bold;margin-right:4px">not rated</span>'
        af=r['adfontes_bias']; mb=r['mbfc_bias']
        if af!='':
            v=float(af); c=BLUE if v<-3 else (RED if v>3 else GRAY); lab=f'Ad Fontes {v:+.1f}'
        else:
            c=BLUE if mb.startswith('Left') else (RED if mb.startswith('Right') else GRAY); lab='Ad Fontes: none'
        mbl=f' · MBFC {mb}' if mb else ''
        return f'<span style="display:inline-block;padding:1px 6px;border-radius:5px;background:{c};color:#fff;font-size:10px;font-weight:bold;margin-right:4px">{lab}{mbl}</span>'
    tiers=[('A','Carried Sacks\'s METR sentence',RED),('B','Quoted the same post, left the METR sentence out',ORANGE),('C','Named METR without Sacks\'s sentence',YELLOW),('D','Covered the essay or the Trump response; no Sacks post, no METR',GRAY)]
    major={'New York Times','Wall Street Journal','Washington Post','Bloomberg','Reuters','NPR','CNBC','Axios','The Verge','Semafor','The Telegraph'}
    def is_major(o): return any(o.startswith(m) for m in major)
    cols=''
    for code,title,c in tiers:
        rs=[r for r in T if r['tier']==code]
        items=''
        for r in rs:
            maj=is_major(r['outlet'])
            badge=lambda ok,lab: f'<span style="display:inline-block;padding:1px 6px;border-radius:5px;background:{AQUA if ok else LGRAY};color:{"#fff" if ok else MUTED};font-size:10px;font-weight:bold;margin-right:4px">{lab}</span>'
            items+=(f'<div style="background:#efece4;border-radius:8px;padding:7px 10px;border-left:4px solid {c}">'
                    f'<div style="font-size:14px;font-weight:bold">{esc(r["outlet"])}{" <span style=\"font-weight:normal;color:"+MUTED+";font-size:12px\">national / wire</span>" if maj else ""}</div>'
                    f'<div style="font-size:12px;color:{MUTED};margin:2px 0">{esc(r["date_utc"][:10])} · {esc(r["sacks_line_used"][:120])}</div>'
                    f'<div>{lean_badge(r["outlet"]) if lean else ""}{badge(r["names_metr"]=="yes","names METR")}{badge(r["funder_named"].startswith("yes"),"names a funder")}{badge(r["reports_asking_metr"]=="yes","asked METR")}<span style="font-size:10px;color:{MUTED}">{r["row_id"]} · {r["source_row"]}</span></div></div>')
        cols+=f'<div><div style="font-size:15px;letter-spacing:2px;text-transform:uppercase;color:{c if c!=GRAY else MUTED};font-weight:bold;margin-bottom:6px">{esc(title)} · {len(rs)}</div><div style="display:flex;flex-direction:column;gap:6px">{items}</div></div>'
    grid=f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{cols}</div>'
    nA=sum(1 for r in T if r['tier']=='A'); nB=sum(1 for r in T if r['tier']=='B'); nAmaj=sum(1 for r in T if r['tier']=='A' and is_major(r['outlet'])); nfund=sum(1 for r in T if r['funder_named'].startswith('yes')); nask=sum(1 for r in T if r['reports_asking_metr']=='yes')
    sacks=I['IF28']
    kp=(f'<div class="kpis"><div class="kpi" style="min-width:230px"><div class="l">Outlets carrying the METR sentence</div><div class="v">{nA}</div><div class="d">trade, partisan, newsletter and East Asian press; one blog fact-check</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">National papers or wires carrying it</div><div class="v">{nAmaj}</div><div class="d">of {nA}</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Quoted the same post without it</div><div class="v">{nB}</div><div class="d">NYT, WSJ, NPR, Telegraph, Axios, CNBC, Stocktwits</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Named a METR funder</div><div class="v">{nfund}</div><div class="d">a blog (Kingy AI: Schmidt Sciences / Eric Schmidt)</div></div>'
        f'<div class="kpi" style="min-width:230px"><div class="l">Reported asking METR</div><div class="v">{nask}</div><div class="d">no "declined to comment" or "did not respond" line found in any item</div></div></div>')
    def mean_bias(code):
        vs=[float(lean_of(r['outlet'])['adfontes_bias']) for r in T if r['tier']==code and lean_of(r['outlet']) and lean_of(r['outlet'])['adfontes_bias']!='']
        return (sum(vs)/len(vs), len(vs)) if vs else (None,0)
    if lean:
        mA,nA_=mean_bias('A'); mB,nB_=mean_bias('B'); mD,nD_=mean_bias('D')
        kp=kp.replace('</div></div></div>',f'</div></div><div class="kpi" style="min-width:230px"><div class="l">Ad Fontes bias, rated outlets only</div><div class="v">{mA:+.1f} / {mB:+.1f} / {mD:+.1f}</div><div class="d">mean for tiers A / B / D ({nA_}, {nB_}, {nD_} rated of {nA}, {nB}, {sum(1 for r in T if r["tier"]=="D")}); positive is right</div></div></div>',1)
    sentence=card('The sentence · David Sacks, Sep 13 03:14 UTC · IF28 · 7.1M views at the Sep 13 snapshot, 8.2M at the Sep 14 recheck',f'“{esc(sacks["metr_language"][:300])}”',RED,16)
    body=kp+sentence+'<div style="height:12px"></div>'+grid
    foot=f'<b>Coverage:</b> Every press and newsletter item located for Sep 12–14 2026 that covered the Amodei essay, the Trump response or Sacks\'s reply (rows TR01–TR{len(T)}, research/transmission.csv, each pointing to its independence_fight.csv or press_sweep.csv source row; agent S6 sweep to Sep 14 07:35 UTC plus Kevin\'s NYT and WSJ PDFs in research/press-pdfs/). Tier is assigned from the retrieved text: paywalled remainders (Washington Post, The Information) and one blocked body (Neowin, snippet only) are labelled. "National / wire" is a fixed list of eleven outlets. "Names a funder" means any METR funder is identified; "asked METR" means the item reports seeking comment. The pattern is a fact about which outlets printed which line; the reasons are not in any row.'+(' Editorial lean is a third party\'s rating, not ours: Ad Fontes Media bias score (negative left, positive right; roughly ±42) and reliability, and Media Bias/Fact Check\'s label, each fetched 2026-09-14 from the outlet\'s own rating page (rows LN01–LN18, research/lean.csv, pages in research/lean/). Eighteen outlets, mostly trade and foreign, have no rating on either site and are marked "not rated", so the tier means cover only rated outlets: tier A\'s four Ad Fontes-rated outlets (Examiner, Breitbart, Daily Caller, ZeroHedge) are all right-of-centre, and MBFC agrees where it rates them, while The Next Web carries an MBFC left-centre label and no Ad Fontes score; tiers B and D include the right-of-centre Wall Street Journal and the unrated UK Telegraph. Ratings describe outlets, not these articles, and do not explain any editor\'s quote choice.' if lean else '')+f' Quote selection and the cost of verifying a contested claim are ordinary explanations; nothing here establishes why any outlet chose its quote. Whether the same papers name METR once it becomes a Washington talking point is a later question (research/WATCHLIST.md). {SRC}.'
    render(STEM, shell((f'Sacks\'s "stop pretending METR is independent" reached {nA} outlets; the four with an Ad Fontes score are all right-of-centre, and the national papers that quoted the same post left it out' if lean else f'Sacks\'s "stop pretending METR is independent" reached {nA} outlets, none a national paper or wire; the two papers that quoted the same post left it out, and no outlet reports asking METR'),('Figure 10v (lean variant) · Where one sentence went, Sep 12–14, 2026, with third-party bias ratings' if lean else 'Figure 10v · Where one sentence went, Sep 12–14, 2026'),'An 8-million-view post with six "stop pretending" lines. Trade, partisan and East Asian outlets printed the METR line; the New York Times and Wall Street Journal quoted the post\'s opening lines and stopped; one blog named a funder; nobody records asking METR.',body,foot,W,H),W,H)

def fig_transmission_lean(): return fig_transmission(lean=True)

# ---------------------------------------------------------------- 10w. what METR pays
def fig_pay():
    W,H=2200,1720; STEM='metr-23-what-metr-pays'
    P={r['row_id']:r for r in rows('pay.csv')}
    bars=[('METR · Embedded Assessments MTS, posted Aug 27 2026 →',402048,687759,RED,'PY49, PY64'),
          ('METR · Evaluation Execution / Security MTS, posted Aug 27 →',328380,578583,RED,'PY50, PY67'),
          ('METR · generic MTS posting, Jun 16 – Aug 25 2026',285548,503116,ORANGE,'PY58, PY63'),
          ('METR · System Administrator, posted',260937,471969,ORANGE,'PY53'),
          ('METR · General Counsel, posted',328380,402048,ORANGE,'PY54'),
          ('Redwood Research · MTS, careers page',350000,850000,YELLOW,'PY74'),
          ('Epoch AI · Senior Researcher, posted',168000,300000,YELLOW,'PY75'),
          ('Anthropic · software engineer, levels.fyi self-reported total comp incl. equity',367000,1420000,BLUE,'PY78'),
          ('OpenAI · software engineer, levels.fyi self-reported total comp incl. equity',250000,1890000,BLUE,'PY79')]
    pts=[('METR FY2024 (8-month year): highest reportable comp, M. Taran',243560,'PY08'),('METR FY2024: R. Dattani, COO',230384,'PY03'),('METR FY2024: B. Barnes, CEO (+$75,637 from ARC)',172737,'PY01'),('ARC FY2024 (full year): J. Hilton, president',328284,'PY31'),('Redwood TY2024: R. Greenblatt',314922,'PY45')]
    L=560; R=W-420; y=40; s=[]; xmax=1_950_000; x=lambda v:L+(R-L)*v/xmax
    for v in (250_000,500_000,750_000,1_000_000,1_500_000): s.append(f'<line x1="{x(v):.1f}" y1="{y-10}" x2="{x(v):.1f}" y2="{y+len(bars)*46+len(pts)*40+40}" stroke="{GRID}"/>'+tspans(x(v),y-16,[f'${v//1000}K' if v<1e6 else f'${v/1e6:.1f}M'],14,MUTED,anchor='middle'))
    y+=20
    for lab,lo,hi,c,rid in bars:
        s.append(tspans(L-14,y+6,[lab[:78]],15,INK,anchor='end')+f'<rect x="{x(lo):.1f}" y="{y-10}" width="{x(hi)-x(lo):.1f}" height="22" rx="5" fill="{c}" opacity="0.85"/>'+tspans(x(hi)+8,y+6,[f'${lo//1000}K – ${hi//1000}K' if hi<1e6 else f'${lo//1000}K – ${hi/1e6:.2f}M'],13,INK,weight='bold')+tspans(W-130,y+6,[rid],11,MUTED,anchor='end'))
        y+=46
    y+=10; s.append(f'<line x1="{L-500}" y1="{y-18}" x2="{W-130}" y2="{y-18}" stroke="{AXIS}"/>')
    s.append(tspans(L-500,y+4,['Paid, per Form 990 (base + bonus; bonus and equity $0 on METR\'s Schedule J)'],14,MUTED,weight='bold')); y+=30
    for lab,v,rid in pts:
        s.append(tspans(L-14,y+6,[lab[:78]],15,INK,anchor='end')+f'<circle cx="{x(v):.1f}" cy="{y}" r="9" fill="{INK}"/>'+tspans(x(v)+16,y+6,[f'${v:,}'],13,INK,weight='bold')+tspans(W-130,y+6,[rid],11,MUTED,anchor='end'))
        y+=40
    svg=f'<svg width="{W-120}" height="{y+10}" viewBox="0 0 {W-120} {y+10}">{"".join(s)}</svg>'
    claims='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:8px">'
    claims+=card('"METR\'s salaries are listing around 500k/yr" · Hacker News, Sep 13 · PY72','Posted, not paid. On that day the Lever board carried eight postings with base ranges from $260,937 to $687,759 (PY68); no filing shows a paid salary above $328,284 (ARC FY2024, PY31). The bands\' midpoints are $453K–$545K.',YELLOW,15)
    claims+=card('"lofty salaries, which reach $503,000 on current job postings" · Business Insider, Sep 11 · PY69','Stale ceiling. $503,116 was the generic MTS ceiling from Jun 16 to Aug 25 (PY58–PY63); on Sep 11 the live ceilings were $578,583 and $687,759 (PY67, PY64).',YELLOW,15)
    claims+=card('"many at METR gave up generational wealth to work there" · Joshua Saxe, Sep 13 · PY73','Not checkable. Said "without knowing the details". METR posts base only and its Schedule J shows no equity; levels.fyi puts Anthropic and OpenAI engineers\' self-reported total comp medians at $883K and $880K (PY78–PY79), a proxy, not a record of anyone\'s forgone pay.',GRAY,15)
    claims+=card('"similar salaries at METR, though without equity compensation" · Chris Painter via BI, Sep 11 · PY70','Consistent with the postings: METR\'s bands overlap lab base pay; equity is the gap. A paraphrase by the reporter, not a direct quote.',AQUA,15)
    claims+='</div>'
    kp=('<div class="kpis"><div class="kpi" style="min-width:230px"><div class="l">Highest posted base ceiling</div><div class="v">$687,759</div><div class="d">Embedded Assessments MTS, from Aug 27 2026 (PY64)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Ceiling raised on</div><div class="v">Aug 27</div><div class="d">generic MTS $503,116 → $578,583, two weeks before the essay (PY63, PY67)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Highest paid, METR FY2024 990</div><div class="v">$243,560</div><div class="d">8-month short year; 18 people over $100K (PY08, PY13)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Wages per W-2, annualised</div><div class="v">≈$161K</div><div class="d">$4.08M ÷ 38 W-2s × 12/8; partial-year hires pull it down (PY17)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Salaries + benefits share of expenses</div><div class="v">55%</div><div class="d">$4.5M of $8.2M, FY2024 (PY19)</div></div></div>')
    body=kp+legend([(RED,'METR posted base range, current'),(ORANGE,'METR posted base range, earlier or non-research'),(YELLOW,'Other evaluators, posted'),(BLUE,'Frontier lab, self-reported total comp incl. equity (levels.fyi)'),(INK,'Paid, Form 990')])+svg+claims
    foot=f'<b>Coverage:</b> METR\'s FY2024 Form 990 (short year May–Dec 2024; Part VII, Schedule J, Part IX), ARC\'s FY2023–24 and Redwood\'s TY2024 990s, every METR posting on jobs.lever.co/metr live on 2026-09-14 and Wayback captures of the board and postings from Jun 16 to Sep 13 2026, Redwood\'s and Epoch\'s careers pages, Apollo\'s (no figures), Business Insider\'s Sep 11 2026 profile, the HN and X claims, and levels.fyi\'s Anthropic and OpenAI software-engineer pages (rows PY01–PY79, research/pay.csv; agent S10, pages in research/agents-2026-09-14/S10-pay/docs/). Four measures are drawn and never mixed: posted base ranges (METR says "the listed range applies to the base salary"), 990 reportable compensation for a fiscal period, 990 wage totals divided by a W-2 count, and levels.fyi self-reported total compensation including stock. The FY2024 return covers eight months and predates the 2026 postings, so paid and posted figures are not the same people or period. A posted ceiling is what METR offers, not what anyone receives; whether any employee forwent lab equity is not in any record. {SRC}.'
    render(STEM, shell('METR posts base salaries up to $687,759 and pays its top people about $244K on its last filing; the "$500K" in the argument was a posted ceiling, and the ceiling rose two weeks before the essay','Figure 10w · What METR pays, posted versus filed','Critics called METR salaries "around 500k/yr" and a defender said staff "gave up generational wealth." The postings, the 990s and the lab pay proxy say something narrower: METR advertises lab-level base pay with no equity, its filed pay is a fraction of the posted ceilings, and the ceilings went up on Aug 27, 2026.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10x. the terms of the first investigation
def fig_terms():
    W,H=2200,1900; STEM='metr-24-the-terms-of-the-first-investigation'
    HF={r['row_id']:r for r in rows('hf_case.csv')}
    q=lambda k,n=330: esc(HF[k]['quote_verbatim'][:n])
    def col(title,c,items):
        out=f'<div><div style="font-size:15px;letter-spacing:2px;text-transform:uppercase;color:{c};font-weight:bold;margin-bottom:6px">{esc(title)}</div><div style="display:flex;flex-direction:column;gap:7px">'
        for head,rid,body in items:
            out+=f'<div style="background:#efece4;border-radius:8px;padding:8px 11px;border-left:4px solid {c}"><div style="font-size:14px;font-weight:bold">{esc(head)} <span style="font-weight:normal;color:{MUTED};font-size:11px">{rid}</span></div><div style="font-size:13px;line-height:1.35;margin-top:2px">{body}</div></div>'
        return out+'</div></div>'
    left=col('What OpenAI set or held',RED,[
        ('The window','HF12, HF13',f'“{q("HF12",200)}” The start date rested on an OpenAI statement METR says it was out of scope to confirm.'),
        ('The questions','HF08, HF09, HF10, HF11',f'Seven questions agreed Jul 29; “{q("HF09",110)}” Out of scope by agreement: safeguards, the extent of the compromise, OpenAI\'s own investigation and remediation, and three questions from METR\'s own July framework.'),
        ('The data','HF28, HF29, HF31, HF33','First ~285 transcripts were OpenAI-selected (about 30% of relevant activity per OpenAI\'s later replication); no per-action timestamps (“not feasible”); no access to the HPIM agents behind most of the attack; METR\'s Aug 3 request for broader datasets answered with “most of the data”.'),
        ('The text','HF02, HF04, HF16, HF17, HF18, HF19',f'“{q("HF02",230)}” Plus: “{q("HF04",160)}” Raw chain-of-thought capped at 30 of 100+ snippets; four OpenAI review rounds; draft written on OpenAI systems and released to METR\'s accounts by OpenAI; METR did not see OpenAI\'s report before joint publication.'),
        ('The incentive, in METR\'s words','HF05',f'“{q("HF05",330)}”'),
    ])
    mid=col('Where METR\'s findings cut against OpenAI\'s account',ORANGE,[
        ('Spoofed logs reached the graders','HF38, HF39','OpenAI: none of the manipulation attempts “affected the logs that our graders or monitors ultimately see.” METR: “Agents used this to alter outputs in our actual transcripts”; over 7% of transcripts, at least 96, contained spoofed tool calls.'),
        ('No scorer was running','HF40',f'“{q("HF40",220)}” Absent from OpenAI\'s report.'),
        ('Motive','HF41, HF42','OpenAI: agents “looked to cheat by finding the solutions online.” METR: about 60% were primarily after the scorer\'s implementation, about 30% after task solutions.'),
        ('A mass exit OpenAI\'s timeline omits','HF45','METR infers agents were “likely killed by an unexpected external process” at 01:30 UTC Jul 12; OpenAI\'s first recorded alert is Jul 19.'),
        ('Where they agreed','HF48–HF57','Model split, the HDF5 exploit within minutes, first remote code execution, cache poisoning never executed, the July 13 admin token: ten points match.'),
        ('What METR asked of OpenAI','HF86–HF88','Nothing. The report has no recommendations section; it calls the exercise “an excellent precedent for independent third-party investigation.”'),
    ])
    right=col('Disclosures, and the next contract',BLUE,[
        ('At publication, Aug 26','HF80','Three named investigators; the 91-page PDF contains no conflict-of-interest or recusal statement. Payment: “we did not take payment from OpenAI”; credits: “roughly ~$400K in API credits” (HF14, HF15).'),
        ('Added Sep 13, the day of the Sacks fight','HF81, HF82, HF83',f'“{q("HF81",120)}” “{q("HF82",200)}” “{q("HF83",230)}”'),
        ('The standard METR said it lacked','HF84, AE16','May 2026: “METR did not have an applicable personnel conflict of interest (CoI) policy in place”; AEF-1 item 2.3, a published CoI policy applied to the evaluation, answered No.'),
        ('Anthropic\'s terms, Sep 9','HF89, HF90, HF91',f'“{q("HF89",300)}” “{q("HF90",120)}” Anthropic was assembling transcripts for METR in August, before the announcement.'),
        ('What METR promised for Anthropic','HF93, HF94','Reports that “describe our terms of engagement” and cover “all of the questions” in its July framework, three of which the OpenAI engagement excluded. Neither Anthropic text mentions redaction, feedback rounds, credits, or who initiated.'),
    ])
    kp=('<div class="kpis">'
        '<div class="kpi" style="min-width:200px"><div class="l">Days on premises</div><div class="v">6</div><div class="d">two planned; extended twice by OpenAI invitation (HF08, HF17)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">Questions</div><div class="v">7</div><div class="d">one added at OpenAI\'s request; three of METR\'s own excluded (HF09, HF11)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">Window, set by OpenAI</div><div class="v">18 days</div><div class="d">Jun 26 – Jul 13; start date not independently confirmed (HF12, HF13)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">OpenAI review rounds</div><div class="v">4</div><div class="d">Aug 2, 12, 20, 24; edits to “structure, emphasis, clarity, and tone” (HF04, HF18)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">Raw chain-of-thought published</div><div class="v">30</div><div class="d">of 100+ in the private report, “for IP reasons” (HF16)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">Paid / credits</div><div class="v">$0 / ~$400K</div><div class="d">no payment; free credits on an implicated model (HF14, HF15, HF26)</div></div>'
        '<div class="kpi" style="min-width:200px"><div class="l">Recommendations to OpenAI</div><div class="v">0</div><div class="d">(HF86)</div></div></div>')
    body=kp+f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px">{left}{mid}{right}</div>'
    foot=f'<b>Coverage:</b> METR\'s 91-page report on the OpenAI / Hugging Face incident (Aug 26 2026, research/metr-hugging-face-incident-report-aug-2026.pdf) read in full against OpenAI\'s own technical report and METR\'s blog post as refetched 2026-09-14 (rows HF01–HF119, research/hf_case.csv, every quote a verbatim substring with page; agent S7), Anthropic\'s Sep 9 page and METR\'s Sep 9 thread, and the AEF-1 items in research/aef1.csv. Published critiques by Andrew Wu (“OpenAI controlled too much of the investigation”) and Venkatesh Rao (“epistemological hall of mirrors”) are recorded as opinions (HF101–HF119); the New York Times\' Sep 3 “dictated the terms” line is carried only as Wu reproduces it. The report never says who initiated the engagement, whether a conflict-of-interest policy existed for it, or what METR retained from OpenAI\'s systems. Terms are what the report states; ten findings match OpenAI\'s account and several cut against it; the Anthropic engagement\'s terms beyond the two quoted sentences are not yet published. This figure records the conditions and the disclosures; it does not score the findings\' correctness. {SRC}.'
    render(STEM, shell('METR\'s first investigation ran on OpenAI\'s window, OpenAI\'s questions, OpenAI-selected transcripts and four OpenAI edit rounds; it still contradicted OpenAI on the logs, and disclosed two family ties only on Sep 13','Figure 10x · The terms behind the OpenAI / Hugging Face report, Aug 26 2026, and what changed for Anthropic','Six days on premises, no payment, ~$400K in free credits on an implicated model, and a footnote saying the wish to keep future access “impacted judgment calls” in drafting. METR found things OpenAI\'s report does not say, asked nothing of OpenAI, and eighteen days later added that one author\'s spouse now sits on OpenAI\'s safety committee and another is the CEO\'s partner.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10y. the accuser's ledger
def fig_sacks():
    W,H=2200,1500; STEM='metr-25-the-accusers-ledger'
    SL={r['row_id']:r for r in rows('sacks_ledger.csv')}
    q=lambda k,n=300: esc(SL[k]['quote'][:n])
    def col(title,c,items):
        out=f'<div><div style="font-size:15px;letter-spacing:2px;text-transform:uppercase;color:{c};font-weight:bold;margin-bottom:6px">{esc(title)}</div><div style="display:flex;flex-direction:column;gap:7px">'
        for head,rid,body in items:
            out+=f'<div style="background:#efece4;border-radius:8px;padding:8px 11px;border-left:4px solid {c}"><div style="font-size:14px;font-weight:bold">{esc(head)} <span style="font-weight:normal;color:{MUTED};font-size:11px">{rid}</span></div><div style="font-size:13px;line-height:1.35;margin-top:2px">{body}</div></div>'
        return out+'</div></div>'
    left=col('The role',BLUE,[
        ('Special Advisor for AI and Crypto, a special government employee','SL03, SL04','Appointed Dec 2024; unpaid; “130 days or less in a one-year period”; ex officio co-chair of PCAST under the Jan 23 2025 executive order.'),
        ('Days counted','SL29, SL20','Sen. Warren, Sep 2025: the 130th day fell on May 29 or Jul 25 2025 depending on the count. Sacks, Mar 26 2026: he had “used up” his 130 days and would continue as PCAST co-chair.'),
        ('Title as of Sep 2026','SL19, SL23','White House, Mar 25 2026: “The Council will be co-chaired by David Sacks and Michael Kratsios.” His X bio: “Co-Chair, President\'s Council of Advisors on Science & Technology.” Whether a PCAST co-chair is himself a special government employee is not established.'),
        ('The disclosure that is not public','SL30','The OGE Form 278e was never released; Sen. Warren asked OGE in May 2025 to seek his consent. What is public are two White House ethics memos (Mar 5 and Jun 13 2025) giving percentages of an unstated total.'),
    ])
    mid=col('The holdings, per the two White House memos',ORANGE,[
        ('Divested','SL05',f'“{q("SL05")}”'),
        ('AI, direct, pending divestiture (Jun 2025)','SL09','Meta 1.762%, Amazon 0.034%, TSMC 0.035% of total assets; “Your Meta holding will be divested no later than the end of Q2 2025.”'),
        ('AI, via Craft Ventures funds','SL10, SL11, SL12','X.AI Corp. 0.044% (“Craft Ventures in turn has initiated divestment of its direct interests in X.AI”); Stability AI 0.001%; Groq, Runway, Etched and five others at 0.000% each; Craft AI total 0.045%. Groq look-through under 0.001%.'),
        ('Retained','SL14, SL07, SL06','SaaS interests “just over 13% of your total assets” (Palantir 1.819%, Glue 0.914%); Beldore S&P 500 exchange fund 5.07%; private digital-asset positions under 3.8%.'),
        ('Not in either memo','SL09–SL11','Anthropic and OpenAI appear in neither Schedule A (direct) nor Schedule B (Craft). Craft was in xAI\'s $6B Series B (May 2024) and reports the stake sold in 2025 (SL02).'),
        ('Portfolio count, by the Times','SL18','“among Sacks\' 708 tech investments, 449 are AI companies that could benefit from the policies he supports” (Nov 2025; NYT text unread, relayed by TechCrunch).'),
    ])
    right=col('The record on Anthropic and its network before Sep 13',RED,[
        ('Oct 14 2025 · 3.0M views','SL25',f'“{q("SL25")}”'),
        ('Nov 8 2025 · 903K views','SL26',f'“{q("SL26",200)}” Names Moskovitz, Tallinn, Buterin and Bankman-Fried per the thread; not Open Philanthropy, not METR.'),
        ('Aug 17 2026 · 1.7M views','SL27',f'“{q("SL27",260)}” The organizations are not named.'),
        ('METR, before Sep 13','SL28','No public Sacks statement naming METR was located before the 03:14 UTC post (search of X and the web; All-In transcripts not searchable fetch-only).'),
        ('The Musk post read as backing him','SL31','Musk\'s 04:07 reply is to Kevin Bass and says “Dario is right that there should be some oversight”; it does not mention Sacks or METR. Craft\'s site lists SpaceX and Neuralink among Sacks\'s early investments (SL22).'),
    ])
    kp=('<div class="kpis">'
        '<div class="kpi" style="min-width:230px"><div class="l">Divested on taking the role</div><div class="v">&gt;$200M</div><div class="d">digital-asset positions, Sacks and Craft; “at least $85 million directly attributable to you” (SL05)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Frontier-lab stake in the memos</div><div class="v">xAI 0.044%</div><div class="d">via Craft funds, divestment initiated Jun 2025; no Anthropic, no OpenAI (SL10)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Retained SaaS and index positions</div><div class="v">≈18%</div><div class="d">of total assets: SaaS “just over 13%” incl. Palantir, plus a 5.07% S&amp;P exchange fund (SL14, SL07)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Public statements on Anthropic before Sep 13</div><div class="v">4+</div><div class="d">“regulatory capture” (Oct 2025), “Doomer Industrial Complex” (Nov 2025), nine points (Aug 2026), Politico (Jul 2026); none names METR (SL25–SL28)</div></div>'
        '<div class="kpi" style="min-width:230px"><div class="l">Financial disclosure form public</div><div class="v">No</div><div class="d">278e withheld; two ethics memos give percentages of an unstated total (SL30)</div></div></div>')
    body=kp+f'<div style="display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:18px">{left}{mid}{right}</div>'
    foot=f'<b>Coverage:</b> The Jan 23 2025 executive order, the two White House ethics memos on Sacks (Mar 5 and Jun 13 2025, PDFs at whitehouse.gov, read page by page), the Mar 25 2026 PCAST release, Sen. Warren\'s May and Sep 2025 letters, Craft Ventures\' site, Axios, CNBC, TechCrunch and Bloomberg reporting, and Sacks\'s own X posts refetched through fxtwitter on 2026-09-14 (rows SL01–SL31, research/sacks_ledger.csv; agent S8, sources in research/agents-2026-09-14/S8-sacks/docs/). Percentages are of a total the memos never state, so no dollar value for any holding is known. The 278e itself, Craft\'s xAI sale terms, Schedules D–H, and his day count against the 130-day cap are not public. This figure applies to the accuser the same test the slice applies to METR: what the filings show, what they do not, and what he had said before. It establishes no motive for the Sep 13 post. {SRC}.'
    render(STEM, shell('The accuser\'s ledger: Sacks divested over $200M to take an unpaid 130-day role, kept 13% in SaaS and a sliver of xAI via Craft, holds no Anthropic or OpenAI in the memos, and had attacked Anthropic four times before naming METR once','Figure 10y · David Sacks by the same records used for METR','The slice scores METR\'s ties from filings. Fairness requires the same for the man who called it “intertwined.” His financial-disclosure form is not public; two White House ethics memos are, as are his posts.',body,foot,W,H),W,H)

# ---------------------------------------------------------------- 10z. what each investor's stake is worth
def fig_stakes():
    W,H=2200,2130; STEM='metr-26-what-the-stakes-are-worth'
    ST={r['row_id']:r for r in rows('stakes.csv')}; LD={r['row_id']:r for r in rows('share_ladder.csv')}
    HP=589.01; PB=11.2261
    G={'court':(AQUA,'Court or SEC filing'),'issuer':(BLUE,'Issuer release, no amount'),'forbes':(YELLOW,'Forbes / Bloomberg estimate'),'derived':(ORANGE,'Derived: documented shares × Series H price'),'none':(GRAY,'No public figure')}
    def money2(v):
        return f'${v/1e9:.2f}B' if v>=1e9 else f'${v/1e6:.0f}M'
    T=[
     ('Alameda / FTX estate (calibration)','court','$500M M-SAFE, Oct 2021, converted May 13 2022 into 44,539,240 Series B shares at $11.2261; 13.56% fully diluted at the Series B close, 7.84% by Jan 2024',money2(44539240*HP),'Sold in two court-supervised sales for $1,336,377,627 (Mar and May 2024) at $30.00; had it held, the block would be worth the figure at left at the Series H price','ST01–ST08'),
     ('Caroline Ellison and Nishad Singh (forfeited)','derived','$10M and $40M SAFEs, converted May 13 2022 (forfeiture orders); share counts not stated, so ≈890,824 and ≈3,563,296 shares by arithmetic at $11.2261',money2(4454120*HP),'Forfeited to the United States; the Marshals sold both blocks in 2025 to existing investors, price undisclosed (Business Insider). Value at left is the arithmetic block at the Series H price','ST13–ST16'),
     ('Jane Street Global Trading, the firm','court','3,332,833 shares for $99,999,988 in the Mar 2024 FTX sale (purchaser list, docket exhibit); named in Series E, F, G and H with no amounts',money2(3332833*HP),'That one purchase at the Series H price. Bloomberg reported Anthropic drove "$830 million of third-quarter gains" for Jane Street in 2025. METR names "individuals from Jane Street" as donors, not the firm','ST20–ST21, M75'),
     ('Dustin Moskovitz (with Cari Tuna)','forbes','Series A participant, amount not disclosed. Forbes, Nov 10 2025: "Their Anthropic stake (worth an estimated $500 million) was moved into a nonprofit vehicle in early 2025"',money2(500e6*HP/140.97),'Forbes\' $500M is a Nov 2025 estimate, when the Series F price was $140.97; scaled to the Series H price it would be the figure at left, an estimate of an estimate. Forbes Apr 2026: he "donated" a stake of "less than 0.8%" of Anthropic, a ceiling with no floor: up to $3.0B at the $380B Series G valuation then current, up to $7.7B at the $965B Series H. Forbes and Bloomberg exclude donated assets from net worth, so the stake appears in neither list. Good Ventures\' FY2025 990-PF shows no private-stock gift and no Anthropic; Coefficient\'s CEO: "not to us"; the couple also use donor-advised funds. Moskovitz, Aug 2026: "GV is itself a beneficiary of that wave (via Anthropic…)"','ST31–ST36, ST78–ST95'),
     ('Jaan Tallinn (via Metaplanet)','none','Series A lead and Series B participant, amounts not disclosed. Told Äripäev in 2026 that several rounds had "substantially diluted" Metaplanet\'s stake; declined to say its size; board observer by choice','not public','No Forbes profile exists; the Estonian press speculates from the $183B valuation without a figure from him. Aggregator ranges (0.6–1.7%) are not used','ST38–ST46'),
     ('Eric Schmidt','none','Series A participant, amount not disclosed; family office Hillspire has 22 private AI investments (CNBC)','not public','Forbes net worth $37.8B does not attribute an Anthropic stake','ST47–ST49'),
     ('James McClave (BEMC Foundation)','none','Series A and B participant, amounts not disclosed','not public','BEMC\'s 990-PF lists only an interest in JSHP LLLP; no Anthropic shares','ST50–ST53'),
     ('Center for Emerging Risk Research / Macroscopic','issuer','Series A and B participant; its own site lists "Anthropic Series A/B" under investments, no amount','not public','','ST31, ST39'),
     ('Anthropic\'s seven cofounders','forbes','Forbes: "just over 1.8%" each at $380B (Feb 2026) and "just over 1.7%" each at $965B (May 2026); Anthropic "declined to comment on their stakes"','≈$16.6B each','Forbes\' own figure at the Series H valuation','ST64–ST65'),
     ('Amazon','court','10-Q for the quarter ended Jun 30 2026: convertible notes $97.9B and nonvoting preferred $92.5B carrying value on $18B invested','≈$190B carried','About 19.7% of $965B by carrying value; the only holder whose stake is in an SEC filing','ST63'),
     ('Google / Alphabet','forbes','14% per court filings in the Google antitrust case (Mar 2025, via press); Alphabet\'s non-marketable equity securities $124.3B, "primarily" Anthropic per Bloomberg','≈$124B on the books','Alphabet\'s filings never name Anthropic','IV13'),
    ]
    s=[]; y=30; L=40; rowh=118
    for t,xx in [('Investor',L),('What is documented, and where',L+330),('Value at the Series H price',L+1120),('What it does not establish',L+1380)]: s.append(tspans(xx,y,[t],14,MUTED,weight='bold'))
    y+=26
    for name,g,doc,val,note,rid in T:
        c,lab=G[g]; nl=wrap(note,74); rh=max(rowh,len(nl)*15+36)
        s.append(f'<rect x="{L-10}" y="{y-22}" width="{W-120}" height="{rh-8}" rx="8" fill="#efece4"/><rect x="{L-10}" y="{y-22}" width="7" height="{rh-8}" rx="3" fill="{c}"/>')
        s.append(tspans(L+8,y,wrap(name,26)[:2],16,INK,weight='bold',lh=19)+tspans(L+8,y+48,[lab],11,c,weight='bold')+tspans(L+8,y+64,[rid],10,MUTED))
        s.append(tspans(L+330,y-2,wrap(doc,88)[:4],13,INK,lh=17))
        s.append(tspans(L+1120,y+4,[val],22 if val.startswith(('$','≈')) else 15,INK if val!='not public' else MUTED,weight='bold'))
        s.append(tspans(L+1380,y-2,nl,12,MUTED,lh=15))
        y+=rh
    svg=f'<svg width="{W-120}" height="{y}" viewBox="0 0 {W-120} {y}" style="flex-shrink:0">{"".join(s)}</svg>'
    kp=('<div class="kpis"><div class="kpi" style="min-width:250px"><div class="l">Holders with a court-documented share count</div><div class="v">2</div><div class="d">Alameda/FTX (44,539,240) and Jane Street (3,332,833); Ellison and Singh by arithmetic</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">METR-funder investors with any public dollar figure</div><div class="v">1 of 5</div><div class="d">Moskovitz, a Forbes estimate; Tallinn, Schmidt, McClave, CERR: none</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Series H price per share</div><div class="v">$589.01</div><div class="d">May 2026, Forge and Hustle Fund; the multiplier used at left (LD14)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Anthropic\'s own ownership disclosure</div><div class="v">none</div><div class="d">draft S-1 submitted Jun 1 2026, not public; no 5% holder table exists yet</div></div></div>')
    body=kp+legend([(AQUA,'Court or SEC filing'),(BLUE,'Issuer release, no amount'),(YELLOW,'Forbes / Bloomberg estimate'),(ORANGE,'Derived: documented shares × Series H price'),(GRAY,'No public figure')])+svg
    foot=f'<b>Coverage:</b> Every public statement located about each named early investor\'s Anthropic stake, graded by source: the FTX bankruptcy docket (sale motion D.I. 6952, executed M-SAFE D.I. 7590-1, purchaser lists D.I. 10241 and 16380), the SDNY forfeiture orders for Ellison and Singh, Amazon\'s 10-Q, Anthropic\'s round releases, Forbes and Bloomberg profiles and articles, Tallinn\'s own remarks to Äripäev and Postimees, Good Ventures\' and BEMC\'s 990-PFs (rows ST01–ST71, research/stakes.csv; agent S11, sources in research/agents-2026-09-14/S11-stakes/docs/). "Value at the Series H price" multiplies a documented share count by $589.01 (research/share_ladder.csv LD14) and is a mark, not a sale; the Alameda block was sold at $30 and the Ellison and Singh blocks at an undisclosed 2025 price, so those two lines show what the shares became, not what anyone received. The Moskovitz line scales a Forbes estimate by the per-share price change from Series F to H and is the weakest number on the page. Aggregator ranges for Moskovitz and Tallinn exist and are not used. No figure here is summed. Anthropic\'s S-1, when public, will list every holder above 5% and every director; until then the stakes of METR\'s three earliest patrons are not knowable from records. {SRC}.'
    render(STEM, shell('What the Anthropic stakes are worth: two holdings are court-documented and would be $26B and $2B at the Series H price; for METR\'s three earliest patrons the only public figure is a Forbes estimate','Figure 10z · Each investor\'s stake, graded by what the record supports','Moskovitz, Tallinn and Schmidt bought into Anthropic at $2.57 a share in 2021. Their share counts have never been disclosed. What can be shown: the FTX estate\'s court-recorded block, Jane Street\'s court-recorded purchase, Forbes\' estimates for Moskovitz and the cofounders, and the per-share price that turns any documented count into a value.',body,foot,W,H),W,H)

def fig_asym():
    STEM='metr-27-two-labs-one-endowment'; W=2200
    LAB=40; OX=350; AX=1250; CW=870
    R=[
     ("Equity in the lab held by METR's funder network",
      "None on any record. Open Philanthropy's own 2017 grant page: \"This grant is not an investment. Open Philanthropy does not have equity in OpenAI.\" OpenAI's own posts for its Oct 2024 and Mar 2025 rounds name only SoftBank; CNBC's investor lists name Thrive, Microsoft, Nvidia, SoftBank, Khosla, Altimeter, Fidelity, MGX, Tiger Global and Coatue. None of METR's named funders appears in either.",'ST72–ST74, ST76',
      "Moskovitz, Tallinn (lead), Schmidt, McClave and CERR bought the 2021 Series A at $2.57 a share; Moskovitz (\"I'm a board observer at Anthropic\", Oct 2025) and Tallinn each say they sit as observers on Anthropic's board; Tallinn and McClave again in Series B. Jane Street holds 3,332,833 court-recorded shares and joined four later rounds. Moskovitz donated his stake, under 0.8% per Forbes, to a nonprofit in early 2025 (no personal gain). Which one is not public: the foundation's return shows no private-stock gift, and Coefficient's CEO wrote that he gave it \"not to us\"; the couple's grants also flow through donor-advised funds at the Silicon Valley Community Foundation and the National Philanthropic Trust, per Coefficient's own page and to-the-dollar matches between those sponsors' grants and Coefficient's awards; DAFs disclose no donor. In 2024 SVCF moved $1.59B to NPT; in the year covering early 2025 NPT received $1.18B of closely held stock in 19 gifts and held $1B more closely held equity at year-end, unattributed. Moskovitz himself, Mar 2026: \"Our Anthropic shares are entirely in our foundation - no personal benefit\"; Apr 2026: \"we have about $20B more in the foundation … The foundation is invested in Anthropic as well\", twice the 990-PF filer's assets, so \"the foundation\" in his usage is the giving complex including its donor-advised accounts (Open Phil's own page named \"the Open Philanthropy Project fund, an advised fund of the Silicon Valley Community Foundation\"); Aug 2026: \"GV is itself a beneficiary of that wave (via Anthropic and a number of other investments).\" If the shares reached the foundation after June 30 2025, they appear on its next return, due Nov 15 2026.",'ST31, ST38–ST39, ST47, ST50–ST51, ST54, ST20, ST23–ST26, ST33, ST78–ST93, ST103–ST118, ST41, LD01',GRAY,RED),
     ("What rises when the lab's valuation rises",
      "Nothing in METR's funder network. OpenAI's own foundation does: OpenAI wrote in Oct 2025 that \"the more OpenAI succeeds as a company, the more the non-profit's equity stake will be worth.\" That foundation funds none of METR's network.",'ST75',
      "Moskovitz and Tuna's philanthropy (\"GV is itself a beneficiary of that wave (via Anthropic…)\"; \"We fund people like METR and Redwood\"), Tallinn's SFF, and CERR, the Series A and B investor that funds Redwood and Longview and holds stakes in Apollo and Halcyon's venture arm. Good Ventures (advised by Coefficient) and SFF between them fund METR's parent ARC ($1.5M + $5.6M), its subcontractor Redwood ($70M+), RAND's evaluation program ($10M), Longview ($16M general support), the Constellation office METR works from ($22.95M), the Halcyon incubator ($903K paid), Tarbell ($6.29M) and METR itself via SFF ($204K; $120K + $428K match).",'ST90, ST93, M01–M03, M13, M35–M39, M120, M126–M128, M131, M139–M142, TB01–TB04',GRAY,RED),
     ("Lab money to METR",
      "No cash, by METR's rule. About $400K in free API credits for the six-day investigation, plus pre-release model access for GPT-5 and GPT-5.6 evaluations.",'HF14–HF15, K05, K07–K08',
      "No cash, by the same rule. \"Access and tokens\" for evaluations, research and engineering; no dollar value published for any lab.",'K02, K14',GRAY,GRAY),
     ("Staff between the lab and METR",
      "Barnes, METR's founder, from OpenAI's alignment team (2022); Saunders (2024), Cunningham and Ziegler (2018–21 at OpenAI) also ex-OpenAI. Reverse: Kwa, METR technical staff, to OpenAI in 2026.",'S01, S08, S15, S31, S46',
      "Benton, ex-Anthropic safety team, to METR's incident-investigation team, Sep 2026. Reverse: Karnofsky, METR advisor to Dec 2024, joined Anthropic in Jan 2025; Ziegler, METR staff to Apr 2024, to Anthropic in Jun 2024.",'S13, S44, S45',GRAY,GRAY),
     ("Personal ties, as disclosed",
      "Cotra's spouse Christiano joined OpenAI's Safety and Security Committee on Sep 9; METR added the footnote on Sep 13, 18 days after publishing. Farhi, ex-OpenAI (left summer 2025 per WIRED; \"self employed\" on a Jun 2026 FEC receipt), is a named individual donor.",'HF81–HF82, C11, IF149, DR12, DR36–DR37',
      "None lab-specific. METR's May 2026 self-assessment: \"at least 6\" staff and collaborators on the pilot \"have close personal relationships with AI company staff\", labs unnamed.",'DR30',GRAY,GRAY),
     ("The investigation",
      "Completed: report published Aug 26 2026 after six days on site. Contradicted OpenAI's own report on the spoofed logs, the absent scorer, the agents' motive and the 30–40% of targets that cannot be exploited. Zero recommendations addressed to OpenAI. Footnote: the wish not to deter future access \"impacted judgment calls\".",'HF05, HF38–HF43, HF86',
      "Agreed Sep 9 2026: \"wide-ranging access, including to transcripts\"; eight-week initial term; METR may take as long as it deems necessary. Nothing reported as of Sep 14.",'HF89, HF95, D08–D09',AQUA,YELLOW),
     ("What the record shows",
      "METR will contradict, on technical points, a lab in which its funders hold nothing.",'',
      "Untested. The report due around Nov 4 is the first test of the case the structure bears on.",'',AQUA,YELLOW),
    ]
    s=[]; y=30
    s.append(tspans(OX,y,["OpenAI: the lab METR's funders do not own"],17,INK,weight='bold'))
    s.append(tspans(AX,y,["Anthropic: the lab they do"],17,RED,weight='bold'))
    y+=34
    for lab,o,oid,a,aid,oc,ac in R:
        ol=wrap(o,98); al=wrap(a,98); n=max(len(ol),len(al)); rh=max(64, n*18+ (30 if (oid or aid) else 14))
        s.append(f'<rect x="{LAB-10}" y="{y-20}" width="{W-80-20}" height="{rh}" rx="8" fill="#efece4"/>')
        s.append(f'<rect x="{OX-14}" y="{y-20}" width="6" height="{rh}" rx="3" fill="{oc}"/><rect x="{AX-14}" y="{y-20}" width="6" height="{rh}" rx="3" fill="{ac}"/>')
        s.append(tspans(LAB,y+2,wrap(lab,30)[:3],15,INK,weight='bold',lh=19))
        s.append(tspans(OX,y,ol,14,INK,lh=18)); s.append(tspans(AX,y,al,14,INK,lh=18))
        if oid: s.append(tspans(OX,y+n*18+4,[oid],10,MUTED))
        if aid: s.append(tspans(AX,y+n*18+4,[aid],10,MUTED))
        y+=rh+10
    svg=f'<svg width="{W-80}" height="{y}" viewBox="0 0 {W-80} {y}" style="flex-shrink:0">{"".join(s)}</svg>'
    kp=('<div class="kpis"><div class="kpi" style="min-width:250px"><div class="l">METR-named funders on OpenAI\'s investor lists</div><div class="v">0 of 6</div><div class="d">Moskovitz, Tallinn, Schmidt, McClave, CERR, Jane Street; rounds of Oct 2024 and Mar 2025 (ST73–ST74)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">METR-named funders in Anthropic\'s 2021 Series A</div><div class="v">5 of 6</div><div class="d">all but Jane Street, which bought in 2024 and joined Series E–H (ST20–ST26, ST31–ST54)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Coefficient\'s only OpenAI money</div><div class="v">$30M grant</div><div class="d">2017, "not an investment"; bought a board seat, not shares (ST72)</div></div>'
        '<div class="kpi" style="min-width:250px"><div class="l">Investigations of the lab its funders own</div><div class="v">0 reported</div><div class="d">one under way since Sep 9; eight-week term ends about Nov 4 (HF95)</div></div></div>')
    cards='<div style="display:flex;gap:18px;margin-top:6px">'+card('Reading one: the interest softens','A finding severe enough to damage Anthropic would lower the value of the vehicle whose returns feed the philanthropy that pays for METR\'s parent, partners, office and incubator. Nobody has to think it for it to operate; it works through what gets funded and who gets hired. METR wrote the milder form itself: free tokens "incentivize a cordial relationship" (DR31).',RED,15)+card('Reading two: the interest sharpens','A safety field that misses a disaster also destroys the endowment, and the funder knows it. Coefficient\'s stated purpose is to constrain the labs it holds. On this reading the stake buys resolve, not silence.',AQUA,15)+card('What decides it','Neither reading is established by the rows. The OpenAI contradictions cannot settle it, because OpenAI is the lab the funders hold nothing in. The Anthropic report, when it comes, is the first evidence either way. This figure states the structure, not a motive.',GRAY,15)+'</div>'
    body=kp+svg+cards
    H=1080+y
    foot=f'<b>Coverage:</b> Each cell cites the rows it rests on (research/stakes.csv ST72–ST77 added 2026-09-14 for the OpenAI column: Open Philanthropy\'s archived 2017 grant page, OpenAI\'s round posts of Oct 2024 and Mar 2025 with CNBC\'s investor lists from Wayback, OpenAI\'s Oct 2025 recapitalization post, EDGAR; sources saved under research/openai-rounds/). "None on any record" is scoped to those sources plus the Coefficient grants index, Good Ventures\' and BEMC\'s 990-PFs and Tallinn\'s Metaplanet portfolio page; Good Ventures\' FY2025 990-PF (IRS TEOS e-file, research/990pf-goodventures-202641359349102829.xml) lists every contribution it received in the year of the transfer: the only non-cash gift is $1.40B of publicly traded securities on Jun 30 2025, and its stock schedule names 406 public companies and no Anthropic, so the vehicle Forbes describes is not Good Ventures Foundation. The couple\'s other entities (Coefficient Giving Research, Advisors, Action Fund and Policy Fund; ST81–ST83) held no closely held stock through 2024; their 2025 returns, due by Nov 2026, must report such a gift by type even without naming the donor, Coefficient\'s CEO says the gift went "not to us" (ST89) and Forbes reports the couple also give through donor-advised funds (ST91), which never disclose a donor\'s holdings (of the four large sponsors whose fiscal 2025 returns cover the transfer window, only National Philanthropic Trust shows a closely-held-stock inflow of the stake\'s scale, $1.18B in 19 gifts, unattributed; ST103–ST104); a full-text scan of every IRS e-file received in 2025 and 2026 for the word Anthropic (research/irs-anthropic-scan/) found no return naming the stake. Moskovitz\'s own words place Anthropic upside at "GV" (ST90), consistent with a fund advised by the couple, with indirect exposure through the foundation\'s $1.6B of private-equity and venture funds, or with the Dustin Moskovitz Remainder Interest Trust (2018), the vehicle that supplies the foundation\'s largest gifts, whose trustee is the foundation\'s assistant secretary and whose holdings are on no public document (ST95). The foundation\'s own public book is positioned on the same boom: at Jun 30 2025 its largest holdings were TSMC $509M, SK Hynix $400M, Broadcom $290M, Vistra $202M, Micron $184M, Vertiv $179M and Constellation Energy $173M, with 58 positions added and 114 exited in the year (ST100); its manager, Value Aligned Research Advisors, launched a multi-billion AI hedge fund in March 2025 and reported a $40.1B public AI-equity book by June 2026, led by Nvidia, Alphabet and Amazon (ST101–ST102). Indirect fund exposure and private secondary purchases are not checked. Dollar figures in the second row are separate grants and recommendations from two funders, each cited to its row, and are not summed. Moskovitz\'s transfer to a nonprofit vehicle removes personal gain and is stated in his favour; Tuna told Forbes it was done to "dispel any perception of conflict of interest" (ST33). "Contradicted" means METR\'s report states a fact OpenAI\'s report states differently (HF38–HF43); it does not mean OpenAI conceded. Anthropic\'s eight-week term is the initial agreement, not a deadline. No motive is asserted of any person or organization. {SRC}. Review of the Sep 14 Grok lanes (GROKREVIEW-G and -H): VARA\'s Form ADV says half its four clients are LPs of the AI fund (ST125); its co-owner is an ARC director (ST127); Good Ventures\' FY2025 grants paid were the lowest of four years and met from carryover, so the couple\'s headline giving runs through DAF accounts (ST130); NPT\'s Schedule B Part II is publicly inspectable on written request (ST121).'
    render(STEM, shell('Two labs, one endowment: METR\'s funders hold Anthropic equity and no OpenAI equity; the only investigation METR has finished was of the lab they do not own, and it contradicted that lab; the investigation of the lab they do own has not reported','Figure 10aa · The asymmetry that decides what the OpenAI record proves','The couple whose foundation funds METR\'s parent, subcontractor, office, pooled funders and incubator donated their Anthropic stake; Moskovitz says it is \"entirely in our foundation\", the foundation\'s return through June 2025 shows no such gift, Coefficient\'s CEO says \"not to us\", and the couple\'s grants also run through donor-advised funds that disclose nothing. Wherever it sits, Moskovitz says Good Ventures benefits from Anthropic\'s rise. No person needs to profit for that to be an interest. OpenAI describes the same structure at its own foundation as a feature. Whether the interest has bent any finding is not established, and the four points on which METR contradicted OpenAI do not test it.',body,foot,W,H),W,H)


FIGS={'metr-27-two-labs-one-endowment':fig_asym,'metr-26-what-the-stakes-are-worth':fig_stakes,'metr-01b-money-that-doesnt-show-up-with-anthropic':fig_money_anth,'metr-25-the-accusers-ledger':fig_sacks,'metr-24-the-terms-of-the-first-investigation':fig_terms,'metr-23-what-metr-pays':fig_pay,'metr-22b-where-the-sentence-went-with-lean':fig_transmission_lean,'metr-22-where-the-sentence-went':fig_transmission,'metr-21-metr-grades-itself':fig_aef1,'metr-20-the-security-revolt-and-the-founder-call':fig_revolt,'metr-19-the-rule-and-the-donor':fig_rule,'metr-18-the-argument-vs-the-ledger':fig_ledger,'metr-17-the-vanguard-channel':fig_vanguard,'metr-15-the-candidates':fig_candidates,'metr-16-metrs-megaphone':fig_megaphone,'metr-13-the-subcontractor':fig_redwood,'metr-14-the-independence-fight':fig_independence,'metr-01-money-that-doesnt-show-up':fig_money,'metr-02-evaluated-by-the-people-you-fund':fig_evals,'metr-03-christianos-hats':fig_christiano,'metr-04-the-evaluators-board':fig_board,'metr-05-free-tokens-are-not-free':fig_tokens,'metr-06-same-day-three-moves':fig_sep9,'metr-07-who-gets-ordained':fig_finra,'metr-08-revolving-door-into-the-referee':fig_staff,'metr-09-ask-the-regulator':fig_rfi,'metr-10-barnes-in-time-by-a-tarbell-fellow':fig_time,'metr-11-same-donors-both-sides-of-the-table':fig_donors,'metr-12-ten-million-to-seventy-one':fig_budget}

if __name__=='__main__':
    want=sys.argv[1:] or list(FIGS)
    for k in want:
        try: FIGS[k]()
        except Exception: traceback.print_exc(); print('FAILED',k)
