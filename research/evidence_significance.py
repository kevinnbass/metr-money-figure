# Hand-written claim overrides and significance lines for the rows cited on figure 10a-anthropic. Edit here, then rebuild EVIDENCE with scripts/build_evidence.py.
CLAIM={
"ST26":"Anthropic's Series H release (May 28 2026) names Jane Street and D.E. Shaw Ventures among the investors; individual amounts are not disclosed.",
"ST41":"Jaan Tallinn told Postimees (Feb 2026) that he is an Anthropic board observer rather than a director.",
"ST49":"Forbes reports that Eric Schmidt's family office, Hillspire, bought 20% of D.E. Shaw & Co.; Schmidt's Forbes profile does not mention Anthropic.",
"ST54":"Anthropic's Series A release names the Center for Emerging Risk Research (now Macroscopic Ventures) as an investor; its Series B release names it again. Amounts undisclosed.",
"ST32":"Forbes (Nov 7 2025, Phoebe Liu) put the Moskovitz–Tuna Anthropic stake at \"an estimated $500 million\".",
"ST33":"Forbes, quoting Cari Tuna: the stake \"was moved into a nonprofit vehicle in early 2025\" to \"dispel any perception of conflict of interest\". The vehicle is not named.",
}
WHY={
"ST26":"Fixes the Series H investor list that the panel and the $965B valuation rest on, and shows the firm-level Jane Street link to the lab whose staff METR names as donors.",
"ST32":"The only published dollar estimate of the donated stake; it is the left bar of the chart and the '$500M' in the title.",
"ST33":"Establishes that the stake was donated in early 2025 and that Tuna gave conflict-of-interest as the reason; the vehicle is unnamed, which is the question the rest of the stakes rows try to close.",
"ST41":"Tallinn, METR's other large early funder through SFF, is an Anthropic board observer by his own account; the figure says 'observer', never 'director'.",
"ST49":"Links Schmidt, a Series A investor and METR supporter through Schmidt Sciences, to D.E. Shaw, whose venture arm joined Series H; the figure uses Forbes' exact 20%.",
"ST54":"CERR/Macroscopic is both an Anthropic Series A and B investor and a funder of Redwood and Longview, two of METR's intermediaries.",
"ST78":"Good Ventures Foundation's own FY2025 Schedule B lists two contributors and one non-cash gift of publicly traded securities; no private stock. So the shares had not reached the 990-PF filer by June 2025.",
"ST79":"The foundation's investment schedules name 406 public issuers and no Anthropic holding; indirect exposure through funds cannot be excluded.",
"ST89":"Coefficient's CEO says the stake was donated and 'not to us', so Coefficient's own entities are out; the recipient is still unnamed.",
"ST90":"Moskovitz says Good Ventures is 'itself a beneficiary' of the coming wave of AI wealth 'via Anthropic', i.e. the giving complex expects to gain when Anthropic gains.",
"ST91":"Forbes says the couple give through Good Ventures Foundation 'plus more in donor-advised funds', which is why the DAF route is on the figure.",
"ST92":"Forbes' 'less than 0.8%' is the only percentage bound found; 0.8% of the $965B Series H valuation is the $7.7B ceiling on the figure.",
"ST93":"Moskovitz's own words that his giving funds METR and Redwood.",
"ST94":"A full-text scan of every IRS e-file received in 2025 and 2026 finds no return naming Anthropic stock held by a Moskovitz or Tuna vehicle; a bounded negative.",
"ST95":"Identifies the family trust that makes the foundation's largest gifts; its holdings are on no public document.",
"ST96":"The NYT's investor-base reporting gives no percentage for any METR-named funder; nothing in the press resolves the stake.",
"ST97":"The WSJ confirms Jane Street's Anthropic position came partly from the FTX estate sale but gives no current share count.",
"ST98":"Tallinn declines to state his Anthropic percentage, so his dashed link is 'undisclosed'.",
"ST99":"Lists the entities through which Moskovitz holds reporting-company shares; none is shown holding Anthropic.",
"ST100":"Good Ventures' public book at June 2025 is concentrated in AI-infrastructure stocks (TSMC, SK Hynix, Broadcom, Vistra, Micron, Vertiv); the endowment is positioned on the same boom as the lab.",
"ST101":"The foundation's investment manager launched an AI hedge fund in March 2025; $4.35B sold to 116 investors by June 2026.",
"ST102":"The manager's reported public book grew from $4.7B to $40.1B in a year, led by Nvidia, Alphabet and Amazon; no Anthropic, which a 13F would not show.",
"ST103":"The sweep of DAF sponsors' closely-held-stock intake that narrows where a private-stock gift could have landed; corrected after audit to note line 11 and the 18 e-files on disk.",
"ST104":"NPT, one of Coefficient's two named DAF partners, took in $1.18B of closely held stock in 19 gifts in the year covering early 2025. Unattributed; a signal, not an identification.",
"ST105":"Coefficient's own page names Good Ventures Foundation, SVCF and NPT as the external funding partners that approve its grants, without naming the account principals.",
"ST106":"NPT's closely-held equity held at year-end rose by $996M in the same year; unattributed.",
"ST107":"SVCF granted NPT $1.59B in 2024 and Constellation $10M; the account family behind Coefficient's grants moved from SVCF to NPT.",
"ST108":"NPT's grants to METR's network (RAND $61.6M, Founders Pledge, FAR, Effective Ventures, Epoch, Longview, Redwood) jump in FY2025; NPT has no METR or ARC line.",
"ST109":"Exact-amount matches prove Coefficient's awards are paid from accounts at SVCF and NPT; 18 matches after audit. Proves the routing, not who owns the accounts.",
"ST110":"Moskovitz: 'Our Anthropic shares are entirely in our foundation - no personal benefit.' His most direct statement; 'foundation' is his word, not a legal entity.",
"ST111":"The thread root names Good Ventures as the funder surging Coefficient's budgets ahead of 'the anticipated wave of new funders'.",
"ST112":"Second statement in four minutes placing all Anthropic holdings 'in the foundation, dedicated to charity'.",
"ST113":"'About $20B more in the foundation … invested in Anthropic as well', double the 990-PF filer's assets, so 'the foundation' covers more than Good Ventures Foundation.",
"ST114":"Open Philanthropy's own page said grants were recommended to 'the Open Philanthropy Project fund, an advised fund of SVCF', naming the DAF account by name.",
"ST115":"The IRS split-interest-trust file has no Moskovitz, Tuna or CTF trust, so the trust route is private and cannot be read.",
"ST116":"NPT paid $50M to Coefficient Giving Advisors and $146.9M in Coefficient-pattern grants in FY2025; the DAF sponsor is a live channel for the giving complex.",
"ST117":"Blue Owl's 2021 S-1 shows the family's private vehicles (Moskovitz Investments LLC, the CTF Trust) and Good Ventures Foundation side by side as holders; a precedent for the foundation holding private units in its own name.",
"ST118":"Moskovitz, in his own words: 'I'm a board observer at Anthropic' and 'in the boardroom in at Anthropic and I know all the players'. Card 3.",
"ST121":"NPT's Schedule B is publicly inspectable on request and must list every contributor above $303M with the asset class, value and date of non-cash gifts; the route that could still settle the sponsor.",
"ST124":"Cari Tuna chairs both Good Ventures Foundation and Coefficient's Board of Managers; Moskovitz is a manager, not chair, which is how card 3 words it.",
"ST125":"VARA's Form ADV shows at least one of its two charitable clients is an LP in the AI fund; which one is not stated.",
"ST127":"The AI fund's co-owner sits on the board of ARC, METR's parent; a join between the endowment's manager and the evaluator's parent.",
"ST133":"Vanguard Charitable's posted Schedule B names no issuer; its largest private-equity line in the window is $130M. Unresolved, not excluded.",
"ST140":"The foundation's $10M FY2024 grant to Open Philanthropy Advisors (now Coefficient Giving Advisors), the line on the Good Ventures node.",
"IV01":"The 2021 Series A: Tallinn led; Moskovitz, Schmidt, McClave and CERR joined. The origin of every equity link on the figure.",
"IV02":"The Series B: Alameda/FTX's ~$500M plus the same early investors; Jane Street later bought the FTX estate's shares.",
"IV05":"The court-supervised FTX estate sale at ~$30 a share, where Jane Street bought 3,332,833 shares for $99,999,988.",
"IV06":"The second estate sale at the same price; fixes the 2024 per-share mark.",
"IV07":"Series E at $61.5B post-money, March 2025, the valuation in force when the stake was donated.",
"IV08":"Series F at $183B, September 2025.",
"IV09":"Series G at $380B, February 2026; D.E. Shaw Ventures appears.",
"IV10":"Series H at $965B, May 2026: the valuation behind the $7.7B ceiling.",
"IV11":"WSJ's reported IPO target of ~$2T; reporting, not a transaction, and labelled so.",
"M75":"METR names 'individuals from Jane Street' as donors, not the firm; the figure keeps that distinction.",
"M120":"Coefficient's grantmakers recommended more than $70M over two years for Redwood, METR's contractor; a recommendation, not a paid grant.",
"M139":"Macroscopic, an Anthropic investor, lists Redwood among its grantees.",
"M140":"Macroscopic lists two Longview programs among its grants; Longview is METR's pooled-fund donor.",
"M141":"Macroscopic holds Apollo Research, another evaluator, as an impact investment.",
"M142":"Macroscopic holds Halcyon Venture Partners, the venture arm beside METR's incubator, as an investment.",
"G14":"METR's own later figure for its Audacious money: 'a bit under $16m' over three years, against the ~$17M announced.",
"TB02":"First Coefficient award to the Tarbell Center; part of the $5.29M on the Tarbell pipe.",
"TB03":"Third Coefficient award to the Tarbell Center.",
"TB04":"Largest Coefficient award to the Tarbell Center.",
"TB05":"SFF's 2024 recommendation for the Tarbell Fellowship, paid via Players Philanthropy Fund; a recommendation, kept separate from awards.",
"TB06":"SFF's 2025 recommendation for the Tarbell Center, including a $200K conditional match.",
"RW31":"METR announced its OpenAI investigation 'with Redwood Research'.",
"RW32":"METR's OpenAI report names a Redwood staff member contracting with METR.",
"RW33":"OpenAI's own technical report names METR and Redwood as the third-party assessors.",
"RW34":"Redwood cross-posted the investigation under Greenblatt's byline.",
"RW36":"Redwood's own post: 'Several staff from Redwood have been subcontracted by METR to work on this investigation', the Anthropic one. Terms undisclosed.",
"RW58":"Search closure: no page names the subcontracted staff or terms; Anthropic's announcement names only METR.",
"J02":"McClave is a Series A and B investor; his BEMC Foundation is not a METR donor on any checked filing.",
"J08":"Schmidt Sciences is a named METR supporter; Schmidt is a Series A investor.",
"B05":"Adam Gleave, FAR AI's CEO, sits on METR's board; FAR AI received $59.3M of Coefficient awards.",
"K01":"METR says it takes no money from AI companies but receives 'significant free tokens' from unnamed frontier companies; unbooked and unquantified.",
"S13":"Joe Benton left Anthropic's alignment team to join METR's incident-investigation staff in September 2026, the month METR began investigating Anthropic.",
}
for k,v in {"TO01":"TIME","TO02":"The Verge","TO03":"MIT Technology Review","TO04":"Lawfare","TO05":"The Guardian","TO06":"the Los Angeles Times"}.items():
    WHY[k]=f"Count behind the {v} chip on the Tarbell branch: Coefficient-funded fellows' AI articles found in the captured window. Counts mix publisher tags and a keyword fallback and windows are partial, so they are not comparable full-year shares."

# ---- audit-4 (2026-09-14) corrections: claim/why overrides per research/AUDIT-4.md failures table ----
CLAIM.update({
"ST41":"Postimees reported in February 2026 that Jaan Tallinn is an Anthropic board observer and quoted his earlier explanation, given to Äripäev radio in January 2026, for declining a board seat.",
"ST49":"Forbes' Schmidt profile says his family's investment vehicle bought 20% of D.E. Shaw & Co. in May 2015; the profile does not mention Anthropic.",
"ST54":"Anthropic's Series A release names the Center for Emerging Risk Research (now Macroscopic Ventures) as an investor, and its Series B release names it again; amounts undisclosed. (Series B: anthropic.com/news/anthropic-series-b; grants: macroscopic.org/grants.)",
"ST91":"Forbes (Nov 2025, US original) says the couple give through Good Ventures Foundation \"plus more in donor-advised funds\"; the article's examples of large foundation holdings do not name Anthropic. Saved copy: Wayback 20251107132055.",
"ST94":"A full-text scan of the 2025 and 2026 IRS e-file batches for the word \"Anthropic\", completed Sep 14 2026, found 11 matching return records; none identifies a Moskovitz or Tuna vehicle holding Anthropic stock.",
"ST99":"The reviewed Asana and Kodiak ownership filings do not list the 2018 Remainder Interest Trust as a holder; Moskovitz's reporting-company shares sit in the trusts and entities his SEC filings name. None of the saved filings shows an Anthropic purchase vehicle.",
"ST100":"Good Ventures Foundation's FY2025 990-PF (total assets $10,107,955,038 at Jun 30 2025) lists 406 public issuers; its largest are TSMC $509M, SK Hynix $400M, Broadcom $290M, Vistra $202M, Micron $184M, Vertiv $179M. The listed public holdings include substantial AI-infrastructure exposure (analysis).",
"ST101":"Value Aligned Research Advisors, Good Ventures Foundation's investment manager ($5,264,377 fee, FY2025), runs VAR AI Fund LP: its initial Form D of Mar 21 2025 reported first sale yet to occur and $0 sold; the Jun 15 2026 amendment reports $4,346,290,561 sold to 116 investors.",
"ST102":"VARA's three 13F-HR filings report portfolio values of $4,734,560,970 (72 table entries, Jun 2025), $9,944,995,059 (86, Dec 2025) and $40,111,386,090 (123, Jun 2026), led by Nvidia, Alphabet, Amazon and TSMC. Saved: research/sec-filings/vara-13f-hr-*.xml.",
"ST103":"Schedule M line 10 (closely held stock) from 18 saved DAF-sponsor e-files, FY2023–FY2025: NPT FY2025 19 gifts / $1,183,079,981 is the only line of that shape; Fidelity, Vanguard and Schwab are far smaller. Line 10 does not cover every form of private-stock exposure; partnership and trust interests are reported on line 11.",
"ST104":"National Philanthropic Trust's FY2025 Form 990 (IRS object 202601289349302480) reports 19 closely-held-stock contributions worth $1,183,079,981, a new preferred-stock/crypto category of $162.7M, and 52 appraisals; NPT's policy is to liquidate complex assets quickly.",
"ST107":"SVCF's 2024 Schedule I reports $1,591,322,838 in grants to NPT and $10,000,000 to Constellation; the originating accounts, donors and any connection to the Anthropic stake are not identified.",
"ST109":"18 temporally compatible same-recipient, same-amount matches between Coefficient's award index and the SVCF and NPT Schedule I filings (e.g. Epoch $4,132,488; Redwood $1,100,000; Obelus $1,134,769) are consistent with the documented external-partner payment arrangement.",
"ST116":"NPT's FY2025 Schedule I lists seven Coefficient-pattern grants totalling $146,860,783, including $50,000,000 to Coefficient Giving Advisors; these identify recipient payments, not the underlying donors.",
"ST124":"Good Ventures Foundation's FY2025 990-PF lists Cari Tuna as president, board chair and director; Coefficient's governance page names her Chair of the Board of Managers and lists Dustin Moskovitz as a manager.",
"ST127":"Benjamin Hoskin, co-owner of Value Aligned Research Advisors, appears as a board member in the Alignment Research Center's FY2024 filing; ARC is METR's former parent.",
"ST140":"Good Ventures Foundation paid $10,000,000 general support to Open Philanthropy Advisors Inc (now Coefficient Giving Advisors) in FY2024 (Jul 2023–Jun 2024). Saved source: research/990pf-goodventures-202501349349105365.xml, IRS object 202501349349105365.",
"IV01":"Anthropic's Series A, May 28 2021: $124M; Jaan Tallinn led, with Dustin Moskovitz, Eric Schmidt, James McClave and the Center for Emerging Risk Research. Anthropic did not disclose a post-money valuation.",
"IV02":"Anthropic's Series B, announced Apr 29 2022: $580M; Sam Bankman-Fried, Caroline Ellison, Nishad Singh, Jaan Tallinn, James McClave and CERR participated. FTX bankruptcy filings later put Alameda's stake at about $500M.",
"IV05":"FTX estate secondary sale reported March 2024: about $884M of estate proceeds, not capital raised by Anthropic. The court exhibit (D.I. 10241-1) totals $884,109,327 for 29,465,891 shares; Jane Street Global Trading's line is 3,332,833 shares for $99,999,988.",
"IV06":"The FTX estate's sale of its remaining Anthropic shares, reported Jun 1 2024, generated over $450M for about 15M shares at about $30; G Squared bought 4.5M shares for $135M.",
"IV07":"Anthropic's Series E, Mar 3 2025: $3.5B at a $61.5B post-money valuation; Jane Street among the named investors. The exact date of the Moskovitz stake transfer is not established.",
"IV11":"WSJ reported on Sep 12 2026 that a prospective Anthropic IPO could raise up to $100B at around a $2T valuation; this is reporting, not a completed financing.",
"S13":"On Sep 2 2026 Joe Benton announced he had left Anthropic's alignment team the previous week to join METR for embedded AI-risk assessment; NBC reported the move on Sep 10.",
"RW58":"The reviewed METR and Redwood web pages did not name the full subcontracted staff or the terms as of Sep 14 2026; Greenblatt publicly identified his participation, and Anthropic's announcement names only METR.",
"J02":"James McClave is a named Anthropic Series A and B investor; his BEMC Foundation was not found as a METR donor in the checked records (metr.org/about and the BEMC filings read).",
"J08":"Schmidt Sciences is named on metr.org/about as a METR supporter; Eric Schmidt is a named Anthropic Series A investor.",
"TB05":"SFF recommended $520,000 in 2024 for the Tarbell Fellowship, with Players Philanthropy Fund listed as the receiving charity; disbursement is not established.",
})
WHY.update({
"ST32":"Forbes' November 2025 estimate supplies the chart's $500M bar and card 1; it is not a transfer-date valuation. US original Nov 7 2025 (Wayback 20251107132055), Australian reprint Nov 10.",
"ST41":"The source distinguishes the reporter's characterization from Tallinn's own quotation; both make him an observer, not a director.",
"ST49":"Links Schmidt, a Series A investor and METR supporter through Schmidt Sciences, to D.E. Shaw, whose venture arm joined Series H; a dated acquisition, not a claim about unchanged 2026 ownership.",
"ST78":"Good Ventures Foundation's FY2025 Schedule B reports one non-cash gift, described as publicly traded securities, and no direct gift described as Anthropic or private stock. This does not identify the recipient of the donated stake or exclude indirect exposure.",
"ST89":"Berger says the donated stake went \"not to us\". This is Coefficient's CEO's statement, not an independently established exclusion of every affiliated entity or account.",
"ST90":"Moskovitz says \"GV\" benefits through Anthropic and other investments; the post does not identify the legal entity, account, or direct versus indirect exposure.",
"ST91":"Puts donor-advised funds on the map in the couple's own giving, as reported by Forbes; it names no sponsor or account.",
"ST92":"Applying Forbes' Apr 20 2026 estimated bound of less than 0.8% to the May 28 2026 $965B round gives a conditional ceiling below $7.72B (about $7.7B), not a measured stake value. Saved: Wayback 20260421043155.",
"ST94":"A negative within the scanned files, not all filed or future returns. Records: research/irs-anthropic-scan/hits.csv and context files.",
"ST95":"Identifies the family trust that makes the foundation's largest gifts and its disclosed Meta holding; no Anthropic holding for it was identified in the reviewed records.",
"ST96":"This September 2026 NYT article gives no percentage for the METR-linked early funders and does not resolve their stakes. Saved: research/press-pdfs/nyt-2026-09-03-anthropic-ipo-investors.pdf.",
"ST99":"Lists the vehicles through which Moskovitz holds reporting-company shares, from dated filings saved under research/sec-filings/; none is shown holding Anthropic.",
"ST100":"The endowment is positioned on the same AI boom as the lab. Sources: the two saved 990-PF e-files (IRS objects 202501349349105365 and 202641359349102829).",
"ST101":"The foundation's manager launched an AI hedge fund; the figure separates the March 2025 launch from the June 2026 amount sold. Saved Form Ds: research/audit3-evidence/sec/vara-form-d-*.xml.",
"ST102":"The manager's reported public book grew from $4.7B to $40.1B in a year; a 13F does not show private stock, so Anthropic's absence is expected.",
"ST103":"The sweep that narrows where a private-stock gift of the stake's scale could have landed; it is a line-10 test only, and only for the 18 returns saved.",
"ST104":"NPT, one of Coefficient's two named DAF partners, took in $1.18B of closely held stock in 19 gifts in the year covering early 2025. The aggregate is unattributed and does not identify an Anthropic gift or a Moskovitz/Tuna account.",
"ST107":"These are sponsor-level payment records; they do not establish account migration or ownership. They show SVCF paying NPT $1.59B and Constellation $10M in 2024.",
"ST108":"No METR- or ARC-named grantee appears in the reviewed NPT FY2023–FY2025 Schedule I lists; the listed network grants are NPT's, without assigned donor accounts.",
"ST109":"The matches identify sponsor accounts as the payers of Coefficient-recommended grants; they do not identify the account principals or prove each transaction's attribution. Sources: the saved Sep 11 2026 index and the saved SVCF/NPT e-files.",
"ST111":"The thread root, quoted here, names Good Ventures as the funder surging Coefficient's budgets ahead of \"the anticipated wave of new funders\".",
"ST113":"'About $20B more in the foundation … invested in Anthropic as well', corrected the next day: not all, though still most, of the $20B is in the foundation. The statements do not specify a legal entity or establish the location of the Anthropic stake.",
"ST114":"Open Philanthropy's own page (Wayback capture Sep 27 2024) said grants were recommended to 'the Open Philanthropy Project fund, an advised fund of SVCF', naming the DAF account; it does not locate the donated stake.",
"ST115":"No identified Dustin Moskovitz / Cari Tuna family trust was found in the checked 2022 IRS split-interest-trust extract (two unrelated Moskovitz name matches). That does not determine the trust's legal form, other-year filings, or current holdings.",
"ST116":"The DAF sponsor is a live channel for Coefficient's programme; the $50M is included in the $146.9M total, not additional to it.",
"ST117":"The 2021 Blue Owl selling-stockholder table names these family vehicles and Good Ventures Foundation; it does not identify the purchaser or recipient of the Anthropic stake. Saved S-1: research/audit3-evidence/sec/st117-blue-owl-s1.html.",
"ST121":"NPT's public-inspection copy must list every contributor above $303,073,355.54 (first whole dollar $303,073,356) when the special rule applies; names, addresses and other identifying information may be withheld, and asset class, value and date do not guarantee an issuer name. The route that could still narrow the sponsor.",
"ST124":"Card 3 words the governance line from this row: Tuna chairs Coefficient's Board of Managers; Moskovitz is a manager.",
"ST127":"A join between the endowment's manager and the evaluator's former parent. Sources: the saved ADV and ARC's FY2024 return.",
"ST140":"The line on the Good Ventures node; the filing names the historical entity.",
"IV01":"The 2021 Series A: the origin of every equity link on the figure. The issuer names the investors, not their purchasing vehicles.",
"IV02":"The Series B: Alameda/FTX's stake plus three of the Series A investors; Jane Street later bought the FTX estate's shares.",
"IV05":"The court-supervised estate sale at about $30 a share, where Jane Street bought 3,332,833 shares. Primary: the CourtListener exhibit cited in ST20–ST21.",
"IV06":"The second estate sale at the same price. Saved article: research/agents-2026-09-14/S11-stakes/docs/wb-theblock-ftx-sale2.txt.",
"IV07":"The valuation in force in March 2025, the quarter Forbes says the stake moved; the transfer date itself is unknown.",
"IV11":"WSJ's reported IPO ambition; labelled as reporting on the figure. Saved: research/press-pdfs/wsj-2026-09-12-anthropic-boss-warns-slow-the-pace.txt.",
"M120":"Coefficient's grantmakers recommended more than $70M over two years for Redwood, METR's contractor; a recommendation, not a paid grant. Post: coefficientgiving.org/research/were-urgently-scaling-our-work-on-ai-and-biosecurity/.",
"TB02":"First Coefficient award to the Tarbell Center; with TB03 and TB04 it makes the $5,291,930 on the Tarbell pipe. Grant pages now 404; amounts and dates from the saved Sep 11 2026 index (bylines pack rows F002–F004).",
"TB03":"Third Coefficient award to the Tarbell Center; saved index record.",
"TB04":"Largest Coefficient award to the Tarbell Center; saved index record.",
"TB05":"A recommendation, kept separate from awards; the receiving charity differs from TB06's.",
"RW58":"Search closure for the subcontract's terms; a bounded negative, not proof no page exists.",
"J02":"McClave is a Series A and B investor; the negative is bounded to the records checked.",
"K01":"METR reports significant free tokens from unnamed frontier AI companies; the quoted statement gives no quantity or dollar value.",
"S13":"Benton's move from Anthropic's alignment team to METR's incident-investigation staff was announced the week METR began investigating Anthropic. Primary: his own Sep 2 2026 post.",
"ST105":"Coefficient's own page names Good Ventures Foundation, SVCF and NPT as the external funding partners that approve its grants; it does not name the account principals. This is why the figure calls them funding partners, not the couple's accounts.",
"ST106":"NPT's closely-held equity held at year-end rose by $996M in the same year; unattributed.",
"ST110":"Moskovitz: 'Our Anthropic shares are entirely in our foundation - no personal benefit.' His most direct statement; 'foundation' is his word, not a legal entity.",
"ST112":"Second statement in four minutes placing all Anthropic holdings 'in the foundation, dedicated to charity'.",
"ST118":"Moskovitz, in his own words: 'I'm a board observer at Anthropic' and 'in the boardroom in at Anthropic and I know all the players'. Card 3; the passage continues after 'naive', marked with an ellipsis. Saved transcript: Wayback 20251020103508.",
"ST125":"VARA's Form ADV shows at least one of its two charitable clients is an LP in the AI fund; the filing does not say which. Saved ADV PDF under research/audit3-evidence/sec/.",
"ST133":"Vanguard Charitable's posted Schedule B names no issuer; its largest private-equity line in the window is $130M. Unresolved, not excluded.",
})
def default_why(i,r):
    n=int(''.join(c for c in i if c.isdigit())); p=''.join(c for c in i if c.isalpha())
    if p=='M':
        if 1<=n<=2: return "One of the two Coefficient awards to ARC (2022) that make the $1.5M Coefficient → ARC pipe."
        if n==3: return "The $10.0M 'AI Evaluation and Testing' award to RAND (Sep 2025): the Coefficient → RAND pipe. An award to RAND for its own programme, not a payment routed to METR."
        if 4<=n<=14: return "One of eleven Coefficient awards to Longview (2022–25) that sum to the $26.3M Coefficient → Longview pipe; Longview's own programmes, not METR money."
        if 15<=n<=32: return "One of eighteen Coefficient awards to FAR AI (2021–25) that sum to the $59.3M Coefficient → FAR AI pipe; FAR AI's CEO sits on METR's board."
        if n==33: return "The bounded negative behind 'Direct: none found': no METR-named grant in Coefficient's 2,911-row index snapshot of Sep 11 2026."
        if 35<=n<=37: return "One of three SFF recommendations to ARC / ARC Evals (2022–24) that make the $5.6M SFF → ARC pipe; recommendations, not paid grants."
        if 38<=n<=39: return "One of two SFF recommendations to METR (2024–25) that make the $752K SFF → METR pipe, including a $428K conditional match."
        if 47<=n<=48: return "One of two SFF recommendations to Redwood (2022–23) that make the $2.4M SFF → Redwood pipe."
        if n==57: return "The ~$38M Audacious commitment to Canary, per RAND's Oct 9 2024 release: the grey pipe. A commitment, not a payment."
        if n==58: return "METR's own Oct 9 2024 statement that ~$17M of the Audacious commitment would support METR; the grey pipe into METR. Later revised by Barnes to 'a bit under $16m'."
        if n==59: return "Giving What We Can reports that Longview recommended a $220K grant to METR in 2023: the Longview → METR pipe. A reported recommendation, not a confirmed disbursement."
        if n==60: return "Longview's undisclosed pooled-fund support for METR, confirmed by both organizations without an amount."
        if n==63: return "ARC's FY2024 Schedule I transfer of the evaluation programme's assets to METR ($4,477,169 cash + $76,766 non-cash, Apr 30 2024): the ARC → METR pipe. Not attributable to any one ARC funder."
        if 77<=n<=96:
            if n in (79,83,87): return "One of the three filed DAF/regrantor grants to METR (Vanguard $4.0M, Founders Pledge $184K, SVCF $20K) that make the $4.2M yellow pipe into METR; the Founders Pledge and SVCF lines match Tallinn's public ledger."
            if n in (91,92): return "Good Ventures' filed payment counterpart of a Coefficient award to ARC (M01–M02); excluded from the yellow total to avoid double counting."
            return "One of the filed DAF/regrantor grants to ARC (2022–25) that sum to the $10.8M yellow pipe; donor named only where Tallinn's ledger matches."
        if n==104: return "The bounded negative behind 'Direct: none found': no METR grantee in Good Ventures Foundation's 990-PFs FY2022–FY2025 (to June 2025)."
        if n==117: return "Good Ventures is a listed Audacious partner today but was absent from the partner list on the day Canary was announced; no Canary payment traced through June 2025."
        if n==118: return "TED Foundation's own 990-PF Part XV (TY2021–TY2024) lists no Canary, RAND or METR grant; Audacious says partners fund grantees directly, so this says nothing about partner payments."
        if n==119: return "Valhalla Foundation's filed $10M 'Project Canary' payment to RAND, one of two filed Canary payments found."
        if 126<=n<=128: return "One of three Coefficient awards to Constellation (2023–24) that sum to the $22.95M Coefficient → Constellation pipe; Constellation is the Berkeley office METR works from."
        if n==143: return "High Tide Foundation's filed $333,334 'PROJECT CANARY' payment to RAND, the second filed Canary payment found."
    if p=='AP':
        return {46:"High Tide Foundation's filed Canary payment, missed by the first partner census.",47:"The Wayback diff showing Good Ventures joined the Audacious partner list after Canary was announced.",48:"Sea Grape Foundation, named by RAND as a Canary-center funder, has no filer of that name found; a lead, not a fact on the figure.",49:"Coverage note for the Audacious partner census: two filed Canary payments found, both to RAND, none to METR, in the filings read."}.get(n,"")
    if p=='ST' and n==107: return WHY['ST107']
    return ""
