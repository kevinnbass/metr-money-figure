# STATE — what 10-metr knows, what is open, what has been tried (as of 2026-09-14 ~08:00 UTC)

One entry per question. **Status**: SETTLED (figure-ready, rows cited), PARTIAL (rows exist, a named gap remains), OPEN (no rows settle it). "Tried" lists every route already used so nobody repeats it. "Closes it" names the single document or event that would settle the question. Lane reviews GROKREVIEW-A..D (research/agents-2026-09-14/) are folded in under each question as they land.

Rules that apply to every entry: each number traces to a row id; money types are never summed; footnotes state coverage; no motive asserted; only public people named; fetch-only; @kevinnbass posts are never sources.

---

## Part 1 — The questions

### Q1. Where does METR's money come from, and does any of it come from Anthropic's investors?  — SETTLED (10a, 10a-anthropic, 10k, 10l, 10q)
- Rows: money_flows M01–M138; finances N01–N58; shared_donors J01–J17; vanguard-ai-cluster VG001–VG106; audacious-partners AP01–AP45; tarbell_funding TB01–TB06.
- Established: Coefficient has no direct METR grant in its 2,911-row index (M33); ARC, seeded by Coefficient $1.5M and SFF $5.6M, transferred $4.55M to METR at the Apr 2024 spin-out (N rows); SFF/Tallinn to METR $204K (2024) and $120K + $428K match (2025) (M38–M39); Vanguard Charitable → METR $4.0M FY2025 (VG rows; donor unknown); "individuals from Jane Street" (M75); Farhi (DR12); Constellation office $22.95M Coefficient (M126–M128); Halcyon $902,880 + $527,870 Good Ventures (M131); Redwood $70M+ Coefficient (M120); RAND $10M (M03); Longview $16M (M13).
- Open inside Q1: identity of the Vanguard Charitable donor (lanes G77/G78 run 2026-09-15 in Codex: recipient acknowledgments, portfolio matching and named-donor vehicles all checked; no source names the adviser; Dylan Field's Nov 2025 and Aug 2026 Figma-share gifts to an unnamed DAF make him a candidate for Vanguard's FY2026 line, not FY2025; NOTES-vanguard.md items 11–17); Audacious Project cohort funders (AP rows are partial); the Feb–Aug 2026 $71M commitments by donor. → G25 (pending review B).
- Tried: Coefficient Algolia index (local snapshot 2026-09-11); SFF round pages; jaan.info ledger (identical to copy); gt990datalake 990s for ARC, METR, Redwood, RAND, Halcyon, Vanguard Charitable (FY2023–25 Schedule I, 72K rows); ProPublica renders; Audacious site.

### Q2. Which nonprofit holds Moskovitz's Anthropic stake?  — OPEN, narrowed (10aa, 10z)
- What is known: bought personally in the May 2021 Series A at $2.57/share (ST31, LD01); Forbes (Phoebe Liu, Nov 7 2025) quotes Tuna: moved "into a nonprofit vehicle in early 2025", est. $500M (ST32–ST33); Forbes Apr 20 2026: "donated his early investment ... an estimated stake of less than 0.8%" (ST92); Coefficient's CEO Berger, Dec 18 2025: "He's since donated his stake (and not to us)" (ST89); Moskovitz, Aug 26 2026: "GV is itself a beneficiary of that wave (via Anthropic and a number of other investments)" (ST90); Forbes: the couple give through the foundation "plus more in donor-advised funds" (ST91); Moskovitz, Sep 11 2026: "We fund people like METR and Redwood" (ST93).
- Excluded on the record: Good Ventures Foundation (FY2025 Schedule B: no private stock; 406-name stock schedule, no Anthropic; ST78–ST79); the four Coefficient entities by Berger's statement and by their 2023–24 returns (ST81–ST82, ST89); Policy Fund (990-N, ST84); Beneficial AI Foundation (Tegmark's, ST80); Outlier Projects Fund and Train Family Foundation (formed 2026, ST86); every other Apercen-administered entity (ST88).
- Moskovitz, Mar 30 2026, to a critic citing his "financial incentives": "Our Anthropic shares are entirely in our foundation - no personal benefit" (ST110, verified from the Bluesky API). Jul 23 2026: the "wave" is "the anticipated wave of new funders next year" (ST111).
- Candidate 0 (new, simplest): Good Ventures Foundation itself, received after 2025-06-30. Reconciles "entirely in our foundation" (ST110), Forbes' "last year he donated" (ST92), Berger's "not to us" (ST89) and the clean FY2025 Schedule B (ST78) at once; conflicts only with Tuna's "early 2025" (ST33). Closes with the FY2026 990-PF (Jul 2025–Jun 2026; due 2026-11-15, ext. 2027-05-15) or the FYE-2026 CA renewal. If true, "GV is itself a beneficiary … via Anthropic" (ST90) is literal, and NPT's FY2025 closely-held inflow (ST104) belongs to someone else.
- Review E adds (verified from the API): Mar 30 2026 "all Anthropic holdings are in the foundation, dedicated to charity" (ST112); Apr 11 2026 "we have about $20B more in the foundation … The foundation is invested in Anthropic as well" (ST113) — $20B is twice Good Ventures Foundation's assets, so "the foundation" in his usage is the giving complex (foundation + donor-advised accounts). Open Phil's own how-to-apply page named "the Open Philanthropy Project fund, an advised fund of the Silicon Valley Community Foundation" (ST114). NPT's FY2025 account also paid Coefficient Giving Advisors $50M (ST116). The IRS split-interest-trust file has no Moskovitz trust, so the Remainder Interest Trust is a private trust and is demoted (ST115). Blue Owl's 2021 S-1 names "Moskovitz Investments LLC" and "THE CTF TRUST UAD 122712" as his selling holders; the LLC is an unsearched candidate for the 2021 Anthropic purchaser (ST117). Anthropic's bylaws require Board approval of transfers and ban SPVs, so an S-1 selling-stockholder table would name the vehicle at any size.
- Moskovitz is an Anthropic board observer by his own account (Stratechery Oct 2025: "I'm a board observer at Anthropic"; "I'm also in the boardroom at Anthropic and I know all the players"; ST118, verified from Wayback), as is Tallinn (ST41). Both chair or run the funders of METR's network. → 10aa, 10k, 10z.
- Reading that fits every statement: the shares were donated (Forbes, Berger, Moskovitz) into the couple's giving complex, which Moskovitz calls "the foundation"; the 990-PF filer's return shows they did not enter it by June 2025; the donor-advised accounts at SVCF ("Open Philanthropy Project fund") and NPT are where a completed gift that never touches the 990-PF filer would sit; NPT's FY2025 return carries a closely-held-stock inflow and retained holding of the right scale. Tests: §6104(d) request to NPT for FY2025 Schedule B Part II (now; ST121); Good Ventures FY2026 990-PF (Nov 2026) for a post-June-2025 arrival; the Anthropic S-1 selling-stockholder table; SVCF CY2025 Schedule M (Nov 2026, weaker: ST119).
- Remaining candidates, both genuine donations and both undisclosed. Three sources say "donated" (Forbes Nov 2025 via Tuna: "nonprofit vehicle"; Berger Dec 2025; Forbes Apr 2026), which excludes a plain private trust for his or heirs' benefit. (1) A donor-advised fund: a completed gift to a public-charity sponsor; Forbes confirms the couple use DAFs (ST91); a sponsor never discloses per-donor holdings but its Schedule M line 10 shows the year's closely-held-stock total by amount. (2) The Dustin Moskovitz Remainder Interest Trust dated March 10 2018 (Meta 2020 proxy: trustee Tom van Loben Sels, Apercen Partners and Good Ventures' assistant secretary; 6,830,855 Meta Class B shares in 2020, the remainder of a 2008 GRAT; ST95), but only if it is a charitable remainder trust: tax-exempt, files Form 5227 not 990-PF (consistent with its absence from every IRS index), Good Ventures its remainder beneficiary (which makes "GV is itself a beneficiary … via Anthropic", ST90, literal); a CRT pays its grantor an income stream, so "no personal gain" would then need qualifying. Nothing on record states the trust's type. Neither vehicle has passed Anthropic shares to the foundation: the trust's gifts were public stock (ST78), and Moskovitz's own gifts stopped after FY2024.
- Coefficient's own grantmaking page names the Silicon Valley Community Foundation and the National Philanthropic Trust as the "external funding partners" that approve its recommended grants, alongside Good Ventures Foundation (ST105; page live since 2022): the couple's DAFs sit at SVCF and NPT.
- Sponsor sweep 2026-09-14 (ST103–ST104, ST106): of the June-year sponsors whose FY2025 returns cover early 2025, National Philanthropic Trust is the only one with a closely-held-stock inflow of the right scale ($1.18B in 19 gifts vs $280M in 186 the year before; new "preferred stock" category $162.7M at year-end; NPT liquidates complex assets quickly). Fidelity ($464M in 306 gifts), Vanguard Charitable ($96.7M in 12), Schwab ($14.4M in 29) show nothing comparable; SVCF, AEF, Goldman, Tides file calendar-2025 returns due Nov 16. NPT's closely-held equity held at year-end rose $996M in the same year (ST106). Exact-amount matches (ST109) prove Coefficient's grants are paid from DAF accounts at SVCF (2023–24) and NPT (FY2023, FY2025); SVCF granted $1,591,322,838 to NPT in 2024 (ST107); NPT's FY2025 network grants (RAND $61.6M, Founders Pledge $78.8M, FAR $14.4M, EV $11.6M, Epoch, Longview, Redwood; ST108) dwarf its earlier years. NPT is therefore the leading specific candidate for the vehicle: one of the couple's two named sponsors, and the only sponsor whose return for the window carries an inflow and a retained holding of the stake's scale. Unattributed; a signal, not an identification. SVCF's calendar-2025 return (due Nov 16) is a weaker test than first thought: SVCF's 2024 audit dates the account family's move to NPT to calendar 2024 ($1.667B out to other sponsors, 95% of it the NPT grant; SVCF's own private stock fell) (ST119). Review H 2026-09-14 also corrected the sweep: LLC/LP-wrapped private stock sits on Schedule M line 11, not line 10, so Vanguard Charitable (line 11 $753.8M FY2025) is not excluded (ST120). Review J (2026-09-14) narrowed the June-year field further: Vanguard Charitable's FY2025 Schedule B is already posted and excludes any single-donor block above $115.0M in the window (ST133); Fidelity's posted Schedule B lists one $680M 'PRIVATE SECURITY' entity interest dated 2024-12-31 that fits neither the size nor the couple's named sponsors (ST134); SVCF's posted 2024 Schedule B dates its largest gift, $1,607,194,500 of publicly traded stock, to 2024-01-24, 99.0% of the SVCF→NPT grant (ST135, unattributed). Posted Part II lines never name an issuer (ST136), so the NPT request can count and size the >$303M blocks, not print 'Anthropic'. The foundation has held pre-listing partnership units in its own name before (Blue Owl, ST138), so Candidate 0 is structurally ordinary. Single best public route: a written §6104(d) request to NPT for its FY2025 Form 990 with Schedule B Parts I–II, names redacted — every contributor above $303.07M is listed, Part II carries the noncash description, FMV and date, and IRS instructions make those public (ST121). Vanguard, Fidelity and SVCF already post their copies for the years in hand and may answer a letter with a URL (ST136); revised draft in grok-out/G73-6104d-letters.md. Tax law does not constrain either reading: a <0.8% stake is de minimis under §4943 at a foundation or a DAF (ST123).
- Closes it: a statement naming the sponsor; the sponsor's CY2025 990 Schedule M "closely held stock" line if the sponsor is small; Form 5227 via Form 4506-A; Good Ventures' FY2026 990-PF (Jul 2025–Jun 2026) if shares arrive after June 2025; the running full-text scan of every 2025–26 e-file for "Anthropic" (research/irs-anthropic-scan/).
- Tried and exhausted: see Part 2 plus ProPublica, IRS TEOS API (all EINs, 50+ PDFs), IRS EO BMF national sweep, CA registry FY2024 RRF-1s, Candid balance sheet, Forbes US/AU/Apr 2026, Coefficient site, Wayback CDX, X (Berger thread), Bluesky (Moskovitz feed, partial walk ~1,500 of 8,250 posts; GROKREVIEW-A L3), Politico 2023, Semafor Sep 3 2026.
- Manual (Kevin): CA portal Good Ventures record → Filings for FYE 6/30/2025 and any "Audited Financial Statements"; Correspondence tab. Form 4506-A for the trust.

### Q2b. Good Ventures' endowment and its manager  — NEW (10aa footnote)
- The foundation's public book at 2025-06-30 is an AI-infrastructure portfolio (TSMC, SK Hynix, Broadcom, Vistra, Micron, Vertiv, Constellation Energy, GE Vernova, Amazon, Celestica, Nebius; Nvidia sold, Microsoft/ASML/Alphabet cut; no Meta; ST100). Its manager Value Aligned Research Advisors (Princeton; $5.26M fees) launched VAR AI Fund LP in March 2025, $4.35B from 116 investors by June 2026, plus an offshore fund (ST101); the foundation's hedge-fund line rose $470M that year. Whether Anthropic sits anywhere in this structure is unknown. → G56, G64.

### Q2c. Review F (lanes G35–G37, G40–G48, G58, G63) — headline facts, to ingest as rows
- Intercept's founding post: "We are further supported by Coefficient Giving" — Coefficient co-funds Intercept with Anthropic and the OpenAI Foundation (Q4).
- RSP §3.6: the financial-interest bar for external reviewers was in v3.0 (Feb 24 2026); LTBT approval of reviewers first in v3.2 (Apr 29 2026); nothing from Anthropic, METR or the LTBT calls the Sep 9 investigation a §3.6 review; METR's Mar 12 2026 Sabotage Risk Report review is the only §3.6-class product. Karnofsky: "In 2023, I collaborated with METR to develop and pitch the basic idea of RSPs" (Q8, Q20).
- SB 813 (Ch. 179): registered SUPPORT Anthropic, Encode, Fathom; OPPOSITION BSA. Anthropic backed the state IVO law three weeks before commissioning METR. AB 1405 (Ch. 178) is the "registry" law with auditor-independence text. Cal-Access: only Encode registered; none of METR/Redwood/Coefficient/Fathom (Q14).
- Microsoft MAI Code of Conduct published Sep 14 13:00 UTC: no METR, AISI, CAISI or "third-party" strings (Q15, closes WATCHLIST item).
- Fathom: EIN 93-4840479, ruled 2024 as "Obsidian AI Inc"; FY2024 revenue $12.1M, zero employees; "hopes of becoming an MRO"; Halcyon and Fathom are IRS-independent, CauseIQ's "subordinate" rests on two shared directors (Q12).
- Muehlhauser resigned Anthropic's board May 28 2024 and "never held any Anthropic equity" (Q22). Plaintext Holdings (Schmidt) still 10–25% owner of D.E. Shaw & Co. on the Aug 2026 ADV; D.E. Shaw Ventures lists both labs (Q3).
- OpenAI, Inc. TY2024 990: 23 grants, $7.61M, CAIS $333K, nothing to METR's network (Q4).
- Q10 ingest package: 16 named posts with fresh counts (LeCun 1.31M; Wang 374K; Clark 117K; Sriram 21K/19K; Nanda 21.6K; Berger 19K), nine Roemmele and three HealthRanger posts, India Today captured (TR45), Painter Sep 14 12:19 on Christiano's OpenAI Foundation seat. Sayer Ji hop is Roemmele → Ji.
- Request-for-comment: contacts media@coefficientgiving.org, press@goodventures.org, press@anthropic.com; METR has no press inbox (route via Barnes/Painter). Twenty-plus numbered questions in GROKREVIEW-F §5.

### Q3. Do METR's funders hold OpenAI equity?  — SETTLED negative, scoped (10aa)
- Review B (G15): none of the six appears in the Mar 2026 $122B round (a16z, D.E. Shaw Ventures, MGX, TPG, T. Rowe co-leads; Amazon, Nvidia, SoftBank anchors), the Oct 2025 secondary, or the Nov 2024 tender; Tuna to Forbes Nov 7 2025: "neither the couple nor their foundation own a stake in OpenAI"; >$3B of the Mar 2026 round went to unnamed individuals via bank channels, so an individual could hold OpenAI unseen; the only indirect path found is Hillspire's 20% of D.E. Shaw & Co. while D.E. Shaw Ventures co-led OpenAI's round and is in Anthropic's Series H. Metaplanet's portfolio also lists xAI (2024). To do: rows for the Mar 2026 round, Tuna's sentence, the D.E. Shaw path, Metaplanet/xAI; extend the 10aa KPI from two rounds to three plus the tender.
- Rows: ST72 (Open Phil 2017: "This grant is not an investment. Open Philanthropy does not have equity in OpenAI."), ST73–ST74 (Oct 2024 and Mar 2025 round investor lists via CNBC; OpenAI's own posts name only SoftBank; live PDFs saved), ST75 (OpenAI Foundation ≈$130B equity, "the more OpenAI succeeds… the more the non-profit's equity stake will be worth"), ST76 (scoped negative), ST77 (no public OpenAI S-1).
- Not checked: private secondaries, fund-of-fund exposure. → G15 (pending review B).

### Q4. Does the OpenAI Foundation fund anything in METR's network?  — PARTIAL (10aa row 2)
- Review B: every published Foundation list checked (People-First waves 1–2, $50M 2026 program, Alzheimer's >$100M, Common Health $100M, farmers $60M) names no METR-network org; but the >$130M "AI Resilience" list, the one program citing "independent testing and evaluations", was unpublished as of Sep 10 2026; OpenAI Group PBC (not the Foundation) money reached ARC via the UK AISI Alignment Project ($7.5M / £5.6m); the Foundation is a founding partner of Intercept alongside "individuals from Jane Street Capital" and Anthropic. To do: soften the 10aa cell to "no published grant"; rows for the Foundation lists, the AISI path, Intercept; WATCHLIST the AI Resilience list and OpenAI, Inc.'s 2025 Form 990 Schedule I (EIN 81-0861541).

### Q5. How big are the early investors' Anthropic stakes?  — PARTIAL (10z, 10a-anthropic)
- Court-documented: Alameda/FTX 44,539,240 sh at $11.2261 (ST01–ST08, LD02); Jane Street 3,332,833 sh for $99,999,988 (ST20–ST21). Forbes estimate: Moskovitz $500M (Nov 2025). None: Tallinn (ST38–ST46), Schmidt (ST47–ST49), McClave (ST50–ST53), CERR (ST54–ST55). Per-share ladder LD01–LD22 (Series H $589.01, LD14).
- Paywalled pieces read 2026-09-14 (Kevin's PDFs): NYT Sep 3 2026 (Menlo/Lightspeed/Iconiq 1–2% each; ~300 investors; no METR-funder figure; ST96); WSJ Jun 20 2026 (no Jane Street number; ST97); Äripäev Jan 5 2026 (Tallinn: "we do not announce percentages"; ST98); Postimees Feb 22 2026 (matches ST40–ST42). Forbes Apr 2026: Moskovitz "less than 0.8%" (ST92).
- Closes it: Anthropic's S-1 going public (draft submitted Jun 1 2026) — but only >5% holders and insiders appear, so Moskovitz/Tallinn/Schmidt may never show.

### Q6. METR's rule on lab money, and the Farhi exception  — SETTLED (10s)
- Rows DR01–DR36: compensation footnote first 2025-04-18 (DR07); employee-donation ban appears between Jul 14 20:05 and Jul 19 17:12 UTC 2026 (DR19, DR35); Farhi named in all 76 recovered about-page captures since Dec 16 2025 (DR34); WIRED Jul 15 2026: Farhi left OpenAI summer 2025 (DR36).
- Review C: Farhi's only first-person statement is to WIRED ("As a leader of AI research at OpenAI for many years…"), no date or employer; WIRED also says he gave $3,000 to the Guardrails Alliance super PAC and "will appear in the group's July filing", so FEC Schedule A carries his self-reported employer on that date (lead); LinkedIn card still headlines "OpenAI" on Sep 14 2026 (stale-prone, like CHM). Donation amount: genuinely absent. To do: FEC pull; DR37 for LinkedIn.

### Q7. Terms and findings of the OpenAI/Hugging Face investigation  — SETTLED (10x, 10r)
- Rows HF01–HF119: no cash (HF14); ~$400K credits (HF15, K05); "impacted judgment calls" (HF05); four points contradicting OpenAI's report (HF38–HF43); zero recommendations to OpenAI (HF86); Sep 13 edit adding Cotra/Christiano and Greenblatt/Barnes footnotes (HF81–HF83, IF149, RW59).

### Q8. The Anthropic investigation  — OPEN until it reports (10aa, 10x)
- Rows: HF89, HF95, D08–D09 (Sep 9 agreement, eight weeks, "wide-ranging access"); expected ≈ Nov 4 2026 (WATCHLIST).
- Review C: Anthropic pre-announced the review on Jul 30 ("in dialogue with METR … including access to all transcripts and sampling access to the relevant models") and Aug 31; the Sep 9 terms name transcripts and employees but not model sampling; Anthropic's RSP v3.4 §3.6.1 requires that an external reviewing organization "may not have a financial interest in Anthropic" and that reviewers be selected with LTBT approval; Greenblatt: scope is METR's Jul 28 methodology post; METR job postings: embedded teams of "1-4 other METR staff"; Irregular is running its own investigation; no terms of engagement published as of Sep 14. To do: rows L21–L22 (Jul 30, Aug 31), RSP §3.6 text, Irregular; 10x note on the narrower Sep 9 scope; lead: was METR selected under §3.6 with LTBT approval, and does any team member hold Anthropic equity.

### Q9. Personal ties between METR and the labs  — SETTLED (10c, 10d, 10h, 10x)
- Cotra–Christiano (C11–C12, HF82); Greenblatt–Barnes (RW59, HF83); Karnofsky METR advisor → Anthropic Jan 2025 (S44); Ziegler → Anthropic (S45); Kwa → OpenAI (S46); Benton, Engels from Anthropic/GDM Sep 2026 (S13–S14, IF06, D02); "at least 6" close personal relationships (DR30).
- Review C: AR11 is Chase Hasbrouck, Army Cyber Command digital-forensics lead, retiring Oct 2026, joining as advisor; not on the team page; Benton's own posts say "will soon be joining" (S13 should read "announced"); Karnofsky in his own words (80,000 Hours, Jul 2025): "I'm married to the president and cofounder of Anthropic. I also work there. I'm not exactly a neutral party", RSP origins with "Paul Christiano and the folks at METR" in 2023; Muehlhauser was an Anthropic director until 2024-05-29 (Coefficient MD now); Tallinn calls himself an Anthropic board observer who declined a seat (Postimees). To do: B18 Hasbrouck; S13 wording; rows for Karnofsky quotes, Muehlhauser seat, Tallinn observer; 10k sequence.

### Q10. Who attacked and who defended METR on Sep 12–14  — SETTLED through 2026-09-14 07:07 UTC (10n, 10r, 10t, 10y)
- Rows IF01–IF149, SK01–SK86, X01–X113, SL01–SL31, OM01, AR01–AR11; all 627 X rows refetched 2026-09-14 ~07:00 UTC (agents S2: 623 OK, IF33 deleted since capture, IF06 quote is paragraph five). Views not refreshed in figures (Sacks-thread rows +18%).
- Review D: Painter replied to a security critic on Sep 14 05:07 UTC ("what conflicts of interest are you thinking of?", to Dardaman), so IF64's "only METR-officer post" is superseded; Sacks, Kratsios, White House, NIST: nothing after Sep 13 20:00 UTC; Neel Nanda (GDM) defended METR's funding (17K views); LeCun (1.2M and 396K views), Alexandr Wang (366K), Jensen Huang via Axios are lab-side voices absent from the ledger; Roemmele's ReadMultiplex article is published and reproduces the author's own graphs (so it cannot corroborate them); eleven Roemmele posts 8K–132K views, two on file. To do: IF rows for Painter–Dardaman, Nanda, LeCun ×2, Wang, Huang, Roemmele posts >10K; README disclosure note on the recirculation.

### Q11. How the Sacks sentence travelled through the press  — SETTLED through 2026-09-14 06:00 UTC (10v, 10v-lean, 10j)
- Rows PR01–PR61, TR01–TR44, LN01–LN18, CX01–CX17; NYT/WSJ PDFs read (IF140–IF148). Fifteen outlets carried the line, none national; NYT named METR once; no outlet reported asking METR.
- Review D: first post-cutoff article naming METR is a Chinese republication of Business Insider (no Sacks line, no funders); India Today carried a Sacks–METR piece at 03:07 UTC Sep 14, URL not captured (would make 16 outlets); Transformer's Sep 11 piece names METR and discloses "Coefficient Giving is Transformer's primary funder" (a disclosing counterexample for 10j); TIME carries the Tarbell line on the author page, not the article. To do: PR62, TR45 (find India Today), T10, T09 note.

### Q12. The incubator layer (Constellation, Halcyon, Tailwind)  — PARTIAL (10t, 10o)
- Rows M123–M133, RW57, RW60–RW62, IF69–IF76, IF92–IF97, IF132–IF139, EV21–EV24, D04, D11, D20–D22; Tailwind page text decoded (research/tailwind-*.txt); Halcyon 990s FY2023–24 (research/halcyon-990-*.xml).
- CORRECTION (GROKREVIEW-F, verified): the $10M SVCF → Constellation grant IS in SVCF's TY2024 Form 990 Schedule I (RecipientEIN 932465256, $10,000,000, "Sciences"; ST107); GROKREVIEW-D's "no Constellation string" was wrong. Constellation's 2024 contributions reconcile ($10M SVCF + Redwood lines). Advisor of that SVCF account unknown; Coefficient's indexed Constellation grants do not match $10M. Review D also: CauseIQ showed the line (possible Coefficient money via DAF; possible double count with M126–M128); Halcyon's funders beyond Good Ventures are Fidelity Charitable $210K, DAFgiving360 $100K, American Endowment Foundation $100K, Secure AI Future $50K; Halcyon grantees include Transluce (Clarity AI Research) $65K and Center for New Data $100K; Halcyon made AIUC's founding grant and seeded Goodfire; Coefficient's Lawsen: Tailwind's auditor stub tells founders to "strongly consider joining existing orgs"; no award since Sep 9; Fathom (SB 813 sponsor; Vanguard Charitable $400K FY2025; CauseIQ lists Halcyon as "subordinate under Fathom AI") is in no figure. To do: M rows for the SVCF line, Halcyon funders/grantees, Fathom; 10o Transluce/Halcyon; lead: Fathom.

### Q13. The security community's factual claims about the HF investigation  — PARTIAL (10t)
- Rows IF77, IF14, IF98–IF113 (claims); HF65 (METR's own limitation); AR11.
- Review D: OpenAI did retain CrowdStrike "since the early days of the incident response" (Jul 29 post; technical report p4), which rebuts IF105's "no recognized incident-response firm" for the HF incident (still unanswered for Anthropic's incidents); Hugging Face used unnamed "outside cybersecurity forensic specialists"; no investigator bio states incident-response experience; no outside showing or replication; third parties (Zvi, AlphaSignal, Decrypt) have written up all four OpenAI-vs-METR contradictions. To do: HF row for CrowdStrike (the local report text lacks the string; re-extract); HF120–HF123; 10t rebuttal card.

### Q14. Legislation, lobbying and who drafted the evaluator language  — PARTIAL (10g, 10i)
- Rows F01–F22, R01–R08; Thomas Lawfare paper; Bloomberg Jul 17 2026 FINRA-watchdog text.
- Review D: SB 813 is law (Chapter 179), sponsored by Fathom, creating state-designated "independent verification organizations" by 2028, voluntary, no METR; Politico says Newsom also signed an evaluator registry with ethics rules (verify); EO 14409 (Jun 2 2026) voluntary pre-release federal access, no METR; Sanders/Casar bill announced Sep 3, not introduced; LDA: METR, Redwood, Coefficient Giving, Policy Fund file nothing; Open Philanthropy Action Fund $110K/quarter (foreign-assistance issues); Encode, CAIS Action Fund and ARI lobby at $20K–$620K/quarter; Coefficient's AI policy team "moved over $140 million" in 2025; Rep. Trahan: "@Fathom_org is right". To do: F23–F25, OM02, lobbying rows; Cal-Access by hand.

### Q15. Other labs on METR and evaluators  — PARTIAL (10e, 10p)
- Rows L01–L24, LM01–LM10, K01–K21 (system cards naming METR; free tokens).
- Review D: Microsoft's code of conduct not published by 12:13 UTC Sep 14; METR's risk-assessment page names xAI as a token provider while the About page does not (K22); GPT-5.6 final system card adds a METR judgement sentence; LeCun, Wang, Huang, Nanda as above. To do: K22, E33 note, IF rows; WATCHLIST Microsoft.

### Q16. Coefficient-funded journalism and editorial lean  — SETTLED (10j, 10v-lean)
- Rows TB01–TB06, LN01–LN18, T01–T09. Review D: Transformer Sep 11 discloses Coefficient; Vox and staff newsletters silent on METR since Sep 9; Wikipedia: METR and Coefficient pages unedited since Sep 1, Christiano lede rewritten 3h35m after the OpenAI Foundation announcement, Moskovitz infobox renamed Open Philanthropy → Coefficient Sep 2.

### Q17. METR's self-assessment (AEF-1)  — SETTLED (10u). Rows AE01–AE40, aef1_preamble.txt.
### Q18. What METR pays  — SETTLED (10w). Rows PY01–PY79.
### Q19. Redwood as subcontractor  — SETTLED (10m). Rows RW01–RW62.
### Q20. Christiano's roles  — SETTLED (10c). Rows C01–C14.
### Q21. Board and advisors' ties  — SETTLED (10d). Rows B01–B17; S44–S49.
### Q22. Coefficient's own acknowledgement of the Anthropic conflict  — PARTIAL (underpins 10aa)
- Now on record: Politico Oct 13 2023 — Moskovitz: returns "will be entirely redirected back into our philanthropic work"; Muehlhauser "holds no financial interest" while on Anthropic's board (GROKREVIEW-A NF8); Muehlhauser Apr 2023: Anthropic board member, "no shares" (NF10; board seat until 2024-05-29 per Anthropic, GROKREVIEW-C NF15); Karnofsky Apr 2024: "I have a significant conflict of interest that isn't going away" (NF9); Semafor Sep 3 2026 — Berger: "We're definitely not the Anthropic Foundation" (NF11); Berger Dec 2025 (ST89); Tuna to Forbes: transfer made to "dispel any perception of conflict of interest" (ST33); Coefficient donor page Dec 2025: METR "is not a Coefficient Giving grantee" (GROKREVIEW-B NF17); Anthropic RSP §3.6.1: external reviewers "may not have a financial interest in Anthropic" (GROKREVIEW-C NF5); Karnofsky at Anthropic, RSP v3.1: reviewers need "not just 'no equity in Anthropic' but a broad lack of any connections" (NF14, Grok-only).
- Still missing: any Coefficient COI policy page or grant write-up naming the investment (none found by Wayback CDX or site search).
- To do: promote the verified items above into rows (stakes.csv for statements about the stake; a new coi_statements block in donor_rule.csv for the rest) before any figure cites them.

---

## Part 2 — Sources and routes already used (do not repeat blindly)

| Route | Works? | Notes |
|---|---|---|
| fxtwitter `api.fxtwitter.com/i/status/<id>` | yes | all X rows; recheck script research/agents-2026-09-14/S2-fx-recheck/recheck_fx.py |
| Grok /goal lanes G1–G34 | yes | briefs research/grok-briefs/, outputs research/grok-out/; ingestion = cite lane row ids or copy into CSVs with new ids (never both for the same fact) |
| gt990datalake XML by object id | lags | 2026 filings missing; use IRS bulk |
| IRS bulk zips `apps.irs.gov/pub/epostcard/990/xml/<year>/index_<year>.csv` | yes | deflate64 → `unzip -p`; batch 05 split into 05A/05B |
| IRS TEOS details API `apps.irs.gov/teos/details/<returnsSearch\|lettersSearch\|pub78Search\|ePostSearch\|revokeSearch>/<EIN>` | yes | scripts/irs_teos_pull.py; PDFs with UA only; app pages Akamai-blocked |
| ProPublica API v2 search/org | yes | no XML download (Security Check page); renders omit Schedule B |
| Candid/GuideStar | manual (Kevin) | balance-sheet export saved |
| CA Registry portal (evokeplatform) | manual (Kevin) | JS-only; RRF-1 PDFs saved research/ca-registry/ |
| Wayback CDX + `id_` raw (use `--compressed`) | yes | CNBC, Forbes, Open Phil 2017 page, OpenAI posts |
| r.jina.ai proxy | mostly | openai.com OK; cnbc article slugs must be exact; coefficientgiving.org grant slug 404 |
| WebFetch | limited | openai.com 403, reuters blocked; use jina or Wayback |
| WebSearch | exhausted this session (200/200) | Grok lanes are the substitute |
| SEC EDGAR full-text `efts.sec.gov/LATEST/search-index` | yes | no OpenAI/Anthropic S-1 public as of 2026-09-14 |
| Coefficient Algolia grants index (local JSON) | yes | anthropic-investors/research/04-openphil-grants-raw-2026-09-11.json |

Forbidden here: nmcli, resolvectl, protonvpn, sudo, systemctl, ip, iptables, nft. Codex quota only with Kevin's explicit yes.

---

## Part 3 — Deduplication rules (why we were treading water)

1. Before adding a row, grep every CSV for the URL and, for X posts, the status id: `grep -rl "<id-or-url>" research/*.csv research/grok-out/*.csv`.
2. A fact lives in exactly one place. Grok lane rows are citable by their own ids (e.g. RP12 in G9); do not also copy them into a slice CSV unless the row needs a note, and then cite the slice row only.
3. The five research families that overlapped this session and their single home from now on:
   - Anthropic stakes and vehicles → stakes.csv (ST); share_ladder.csv (LD) for prices only.
   - Money to METR's network → money_flows.csv (M); grantor-side 990 pulls → vanguard-*.csv, rand-990/, halcyon-990-*, coefficient-990/, irs-teos/ (files only, cited from M or ST rows).
   - People and roles → staff_origins.csv (S), board.csv (B), christiano.csv (C), redwood.csv (RW) for Redwood people; arrivals.csv (AR) for Sep 2026 arrivals only.
   - Sep 9–14 speech → independence_fight.csv (IF) for named actors; sacks_thread.csv (SK) for the thread census; x_amplifiers.csv (X) for amplifiers; sep9.csv (D) for the day itself. Do not add a post to two of these.
   - Press → press_sweep.csv (PR) one row per outlet, transmission.csv (TR) one row per carried sentence, press_context.csv (CX) for the NYT/WSJ context pieces.
4. Every X row records the fetch time in UTC (local time is CDT = UTC−5; earlier stamps were corrected).
5. Figures cite the row range, not the lane; audit.py must exit 0 after any change.

---

## Part 4 — Calendar (from WATCHLIST, the dated closers)

| Date | Event | Closes |
|---|---|---|
| 2026-09-14 | Microsoft MAI code of conduct | Q15 |
| 2026-10-20 | LDA Q3 2026 filings | Q14 |
| ≈2026-11-04 | METR's Anthropic report (eight weeks from Sep 9) | Q8, and the test of 10aa |
| 2026-11-16 | Calendar-2025 Forms 990 for the three Coefficient entities (extended deadline) | Q2 via Schedule M |
| now (30-day statutory response) | §6104(d) written request to NPT (Jenkintown PA) for FY2025 Form 990 incl. Schedule B Parts I–II, names redacted; same to Vanguard Charitable (Boston) and Fidelity Charitable (Cincinnati) | Q2 via Schedule B Part II noncash descriptions (ST121) |
| Nov 2026 | FY2025 990s: METR, Redwood, Halcyon, Constellation | Q1, Q12 |
| when public | Anthropic S-1, OpenAI S-1 | Q5, Q3 |
| when filed | Good Ventures FYE-2025 CA renewal and any audited statements | Q2 |

---

## Part 5 — Figure → question map

10a Q1 · 10a-anthropic Q1 Q5 · 10b Q15 · 10c Q20 · 10d Q21 · 10e Q15 · 10f Q10 · 10g Q14 · 10h Q9 · 10i Q14 · 10j Q16 · 10k Q1 · 10l Q1 · 10m Q19 · 10n Q10 · 10o Q12 · 10p Q15 · 10q Q1 · 10r Q10 · 10s Q6 · 10t Q10 Q12 Q13 · 10u Q17 · 10v/10v-lean Q11 Q16 · 10w Q18 · 10x Q7 Q8 · 10y Q10 · 10z Q5 Q2 · 10aa Q2 Q3 Q4 Q8 Q22

---

## Part 6 — Consolidated leads and manual pulls (from GROKREVIEW-A..D, 2026-09-14)

**Codex audits 3A–3D (2026-09-14) of figure 10a-anthropic** → `research/AUDIT-3A.md`…`AUDIT-3D.md`, evidence under `research/audit3-evidence/`. Verdicts: 3A 82/85 confirmed; 3B 66 rows, attribution the main defect; 3C 21/29; 3D 224/249. All figure-text corrections applied in 0.44. Standing rules reinforced: SVCF/NPT accounts are unattributed funding partners; bounded negatives stay bounded; SFF pipes say 'recs'; no 'no money' on relationship links. Open items from the audits: IV03 ($4.1B Series C post-money needs a source), IV04 (CNBC 'in talks' vs completed Series D), M59 ($220K Longview rests on GWWC), J02 (BEMC XMLs not recovered), AP49 (partner census not a primary register), LD Forge-only rows.

**Review J (2026-09-14, lanes G72/G73/G74/G75)** → `agents-2026-09-14/GROKREVIEW-J.md`. Rows ST133–ST139; URL fixes ST126/ST128/ST130; notes ST102/ST103/ST107/ST117/ST120/ST121. Leads: (1) send the NPT letter as revised; (2) NPT Part I for a ≈$1.59B cash contributor = the SVCF account arriving (ST135); (3) GVF FY2020 990-PF for Owl Rock/Dyal lines and FY2021 Schedule B — how the foundation acquired its Blue Owl units; (4) request for comment: which sponsor, shares or entity interests, and whether the Jan 2024 SVCF gift and the SVCF→NPT transfer were the Open Philanthropy Project fund; (5) Nov 2026 reads add BofA CGF and Greater Kansas City CF; (6) Moskovitz Investments LLC state record (browser only). Not pulled: NPT audit notes (PA BCO/Candid), Vanguard FY2026 (~May 2027), ADV checkbox answers (browser), CourtListener (account).

**Review I (2026-09-14, lanes G69/G70/G71/G76)** → `agents-2026-09-14/GROKREVIEW-I.md`. New: second filed Canary payment, High Tide Foundation → RAND $333,334 TY2024 (M143/AP46); the AP census missed twelve names on the 2024-10-09 partner list, now closed (AP49); Good Ventures was not an Audacious partner on announcement day (AP47, M117 amended); RAND's CAST funding page names the Canary funder circle plus Fathom as directed-grant funders (M146–M147); Good Ventures' own 990-PF pays RAND directly in both years (M144–M145), so Coefficient's RAND program runs through GVF, SVCF and NPT, and NPT's $61.6M matches no indexed award (ST132); RAND 2024 AR tiers (M148) and TASP seed funders (M149); Barnes Sep 2025: Audacious 'a bit under $16m' over 3 years, ~$13M/yr run-rate, 12–16 months runway (G14–G17); no public Anthropic S-1 as of 17:50 UTC. Leads: identify Sea Grape Foundation (no filer found; DAF account name?); reconcile GVF's eight RAND installments against the index (local); Fathom → RAND CAST amount (Fathom FY2025 990, Nov 2026); High Tide/Valhalla TY2025 990-PFs (Nov 2026); NPT→RAND question for the request for comment; date Good Ventures' Audacious listing via Wayback CDX; DALHAP Investments Ltd. Not pulled: Galaxy Gives and Tsai TY2025 e-files (IRS 2026 batch zips), Overdeck and TED TY2024 grant attachments (PDF), Longview donor-only report.

**Review G (2026-09-14, lanes G56/G57/G59/G61/G64)** → `agents-2026-09-14/GROKREVIEW-G.md`. New: VARA ADV Q20 — half of its four clients are LPs of VAR AI Fund, so a Good Ventures-linked charity is in the AI fund (ST125); charitable accounts 0% non-exchange-traded, so no Anthropic block in the VARA-managed account; Hoskin (VARA) sits on ARC's board (ST127); Form 4 2025 all Asana purchases, no gifts (ST128); Meta block ≈3.97M shares (~$2.9B) unaccounted after the trust's two gifts (ST129); GVF FY2025 payout lowest of four years and met from carryover, so the couple's headline giving runs through DAF accounts (ST130); ICONIQ FY2021 $561M (ST131). Leads: name the charitable LP (GVF FY2026 hedge-fund line; next ADV); VARA's second charitable client (a VARA-advised DAF at NPT/SVCF?); Meta residual via sponsor Schedule M; Monster Growth Ventures / Moskovitz Investments LLC as 2021 purchaser (G74). Contradictions: G61 dropped the 'In partnership with Good Ventures' clause; G56/G64 'none found' vs their own PDF's Q20.

**Review H (2026-09-14, lanes G60/G62/G65–G68)** → `agents-2026-09-14/GROKREVIEW-H.md`. Ranked leads: (1) §6104(d) request to NPT for Schedule B Part II; (2) NPT full audit notes via PA Bureau of Corporations and Charitable Organizations search or Candid; (3) re-test Vanguard and Fidelity on line 11; (4) Moskovitz Investments LLC as the 2021 purchaser → gift of LLC interests → line 11 (brief G74); (5) GVF FY2026 990-PF; (6) add 'which sponsor / shares or LLC interests' to the request for comment; (7) SVCF CY2025 demoted; (8) Founders Pledge / Longview CY2025. Contradictions logged: G65's 'new' 32b sentence is FY2024 boilerplate; NPT report prose (~3×) vs e-file (4.02×) — quote the e-file; NPT grants total: use e-file $6,415,072,479.

### Leads worth chasing, ranked by what they would change
1. **The stake's vehicle (Q2).** Test the DAF hypothesis: Good Ventures' FY2026 990-PF (Jul 2025–Jun 2026) for any late arrival; the sponsor's CY2025 Schedule M if the sponsor is small; Form 5227 for the Remainder Interest Trust (Form 4506-A); a full walk of Moskovitz's Bluesky feed (≈8,250 posts; ~1,500 read) via the public API; ask Coefficient what "not to us" covers.
2. **CERR's money into METR's network (10aa row 2).** Size and date the Redwood and Longview grants and the Apollo and Halcyon Venture Partners investments (Swiss Zefix for the entity; Longview's consortium page; Apollo's seed announcement).
3. **Fathom.** SB 813's sponsor, $400K from Vanguard Charitable, Halcyon filed as its subordinate, praised by Rep. Trahan: in no figure. ProPublica 93-4840479, fathom.org, the Coefficient index.
4. **The $10M SVCF → Constellation line.** Decides whether 10m double-counts Coefficient's $22.95M. SVCF's next 990 (EIN 20-5205488).
5. **RSP §3.6 applied to the Sep 9 engagement.** Was METR selected as an RSP external reviewer with LTBT approval; does any investigation-team member hold Anthropic equity; was §3.6.1 in v3.0 (Feb 2026, Karnofsky-led).
6. **Farhi on an FEC record.** Guardrails Alliance's July 2026 Schedule A gives his self-reported employer on the contribution date.
7. **OpenAI Foundation's >$130M AI Resilience list** and OpenAI, Inc.'s 2025 Form 990 Schedule I.
8. **Hillspire's 20% of D.E. Shaw & Co.** vs D.E. Shaw Ventures' OpenAI and Anthropic positions (Form ADV).
9. **India Today's Sacks–METR piece** (TR45; 10v count 15 → 16).
10. **Painter–Dardaman thread, Nanda, LeCun, Wang, Huang, Roemmele posts** → IF rows; README note that ReadMultiplex reproduces the author's own figures.
11. **Halcyon's DAF funders and grantees; Transluce's Halcyon seed** → M rows; 10o.
12. **SB 813 chaptering date, the Politico "registry" law, EO 14409, Sanders/Casar** → F23–F25; 10g.
13. **Tallinn's observer seat and Muehlhauser's board dates** → 10k sequence; 10z.
14. **Karnofsky's own words** (80,000 Hours; LessWrong RSP v3 post, verify verbatim) → 10h, 10c.
15. **Benton's start date and role on the Anthropic investigation** (he left Anthropic ~Aug 28).

### Manual pulls (browser or mail; the lanes could not)
- CA Registry portal (Good Ventures FYE-2025 filing, audited statements, Correspondence): https://ca-rcf.evokeplatform.com/app/publicPortal/verification
- Form 4506-A to the IRS: Form 5227 for the Dustin A Moskovitz Remainder Interest Trust; Form 1024-A for any c4.
- CA SOS bizfile: Statements of Information for Coefficient Giving LLC, Coefficient Giving Policy Fund, Outlier Projects Fund, The Train Family Foundation (API returned 429).
- Cal-Access lobbying employers for METR, Redwood, Coefficient entities, Encode, CAIS AF, ARI (Incapsula-blocked).
- lda.senate.gov registrant search "Coefficient" (API 429); Q3 2026 LD-2s after Oct 20.
- FEC: fec.gov individual contributions "Farhi, David", 2025–2026; Guardrails Alliance / Leading the Future committees.
- LinkedIn (login): Farhi (Experience end date), Benton, Engels, Hasbrouck, Constellation "People".
- NYT Sep 3 2026 (Anthropic cap table: Menlo/Lightspeed/Iconiq "1 to 2 percent"), Bloomberg Sep 12/14, FT, The Information, WSJ Jun 20 (Jane Street): subscriptions or archive.ph.
- Äripäev (Jan 5, Apr 15/21 2026), Delfi (Aug 24 2026): Estonian paywalls; DIGAR print archive.
- X advanced search (logged in): `from:moskov Anthropic` by year; `from:DavidSacks since:2026-09-13`; `from:chrislehane since:2026-09-09`; Founders Pledge and EA Forum member pages.
- Forbes Impact Summit Sep 2025 (Tuna talk) video; Stratechery Oct 20 2025, Tim Ferriss #686, Stanford PACS Apr 6 2026 (Moskovitz interviews found, unread).
- Microsoft MAI Code of Conduct: microsoft.ai/news, blogs.microsoft.com (daily).
- congress.gov advanced search "independent verification organization" OR "third-party evaluator", 119th, introduced ≥ 2026-09-09.

### Genuinely absent (stop looking)
Schedule B donor names for public charities and c4s; the OpenAI and Anthropic S-1 holder tables until the flips; Anthropic board observers on issuer pages; Farhi's donation amount; the Vanguard Charitable donor; the $71M commitments by donor; a CAISI X account; Cari Tuna posts since 2011; Moskovitz's deleted X history; SFF-2026 recommendations before they publish; Halcyon's and Constellation's 2025 Forms 990 before Nov 2026.
