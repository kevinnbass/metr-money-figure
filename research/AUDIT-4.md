# AUDIT-4 — figure 10a-anthropic, v0.46b

Audit date: 2026-09-14. Governing instruction: the revised [AUDIT-SEED-4.md](AUDIT-SEED-4.md), reread after the user's steering. Scope is the single `metr-01b` HTML/PNG and its 75-block evidence set. This report does not audit the companion figure or repository. **This audit session** changed no source CSV, bibliography, `generate.py`, or `fig_common.py`. The user reported that the separate Fable session was recovering IDs; its concurrent changes were checked without editing its files. The initial snapshot and the later recovery check are distinguished below.

## Verdict: FIX

1. **The original path corruption is now repaired, but citation coverage is not yet complete.** The initial snapshot had nineteen zero-length paths out of 31. In the later recovery check, **all 31 paths render**, and a fresh render exactly matches the updated PNG. Do not treat the historical path damage as an outstanding defect. The retained ID inventory is still the same 75 IDs at this check.
2. **The bibliography does not cover the figure.** Its 75 IDs exactly match the `rows:` comment, but the comment omits most grant-total inputs, all six TO outlet rows, the Audacious payment/history rows, and the row supporting the index search. Several visible figures have no block. The footnote's “Every number cites a row id” claim therefore fails.
3. **Substantive bibliography errors survive.** Among them: 22 rather than 18 sponsor returns; the temporally invalid SVCF/RAND match; approximately $170M rather than $146,860,783; double-counting that total in its significance sentence; overstatements about account migration, legal vehicles, and negative searches; incomplete or unsuitable source links; and missing corrections to quotations. Exact replacements are in the bibliography failures table.
4. **Cards need corrections.** Forbes's sentence is accurate after conventional nested-quotation typography normalization. Card 2 omits the author's April 12 correction to the $20B statement. Card 3 inserts a sentence-ending period where the transcript continues.
5. **Text and layout still need fixes.** The recovery removed all six `(, )` remnants and the six empty panel text elements. The free-token caption still ends in an unnecessary semicolon and is clipped at the right edge. **Two standard nodes**, Audacious and Redwood, still fail the required height formula, down from five. Five unrelated label/box intersections remain. The cleaned Anthropic panel still exceeds the stipulated formula by 31px, although its actual glyphs fit.
6. **Framing and arithmetic labels need bounds.** The title's current-value and direct-grant negatives, the family/funding-partner grouping, “BEMC is not a METR donor,” and several significance sentences exceed their evidence. The exact conditional ceiling is **less than $7.72B**, not a literal upper bound of $7.7B; “×15” is approximate; the valuation date is May 28, 2026, not a September priced round. Constellation's $22.9M is the generator's floating-point rounding of $22.95M.

The audit is complete with a FIX verdict; completion of the requested audit does not mean the figure passes.

## Evidence and method

I read all 257 nonempty rendered text nodes, including every title, subtitle, legend, node, label, chart element, card, and footnote. [Visible strings](audit4-evidence/visible-strings.txt) numbers them from 000 to 256; those numbers are used below. The table groups repeated wording and wrapped parts of the same factual claim. CONFIRMED means the stated fact matches the identified evidence; DIFFERS includes a missing bibliography citation even where the underlying source supports the value; UNVERIFIABLE identifies a factual inference or source claim the inspected evidence cannot establish. For computed totals and negative searches, the evidence column gives the observed source fields or search result, since those results are not literal sentences in a primary document.

The initial generator, intercepted at `render()` without writing a figure, produced byte-identical HTML. A fresh Chromium render reproduced the initial PNG, **4400 × 5120**, SHA-256 `b90d25030dcee4556dc957e2f4e5cd95b9acdc245975673940c60feae83b41db`, **zero changed pixels**. Initial HTML SHA-256: `236cdab3e01f82b9f9dbdf231ff6c6ee63055e8b5bd39549f72523812ce366f5`. Initial receipts: [integrity](audit4-evidence/integrity.json), [layout measurements](audit4-evidence/layout.json), [render comparison](audit4-evidence/layout-summary.json), [replayed PNG](audit4-evidence/rendered-check.png).

The later recovery check reproduced updated HTML SHA-256 **`a055204f4b2e17ee0fecae272a8000827017e51b6aaea4a55356c07e7ac4d527`** and PNG SHA-256 **`676b311b50fdb7b3a40b83029b763db76ef299cb3b15b24d56bddf23bbb854b9`**, again **4400 × 5120 with zero changed pixels**. All 75 blocks and their complete CSV row records are unchanged. I compared all **250** updated nonempty text nodes with the original 257: differences are citation-punctuation cleanup and rewrapping, not changes to the substantive claims. Task 1 retains the original visible-string indices as stable fact locators; Task 6 gives the updated geometry. Updated receipts: [integrity](audit4-evidence/recovery-check-1/integrity.json), [visible strings](audit4-evidence/recovery-check-1/visible-strings.txt), [layout](audit4-evidence/recovery-check-1/layout.json), [PNG comparison](audit4-evidence/recovery-check-1/layout-summary.json). The old helper's `pre_ids` interception no longer catches IDs stripped earlier in `wrap()`; its `comment_extra` field is an instrumentation limitation, not 75 spurious IDs. The independently compared comment and bibliography sets still match exactly.

Every one of the 75 bibliography blocks was joined to its actual CSV row; all 75 Source fields reproduce the builder's chosen source field. That is a mechanical match, not proof that the URL supports every claim. I made GET-only checks of all **68 distinct HTTP(S) URLs** in those fields, plus relevant primary-source alternatives. Responses were capped at 1 MiB; the IRS ZIP was deliberately not downloaded in full because the extracted filing is already saved. A 200 status alone is not evidence of substantive content, especially for social-media shells and the adviser-information app. [URL register](audit4-evidence/url-checks.csv), [supplemental URLs](audit4-evidence/supplemental-url-checks.json), and [all blocks with their source rows](audit4-evidence/blocks.json) preserve the checks. No posts by `@kevinnbass` were used as sources, no messages were sent, and no network or system settings were changed.

## Task 1 — per-fact table

“Missing” in the bibliography column means absent from the 75 blocks, even if a supporting row exists elsewhere in the research CSVs. Rows cited for calculations were also opened and checked against the saved 2,911-record issuer index, current SFF pages, and the relevant filing evidence. The [index comparison](audit4-evidence/index-checks.json) matches amounts for all 38 checked awards: M01–M32, M126–M128, and TB02–TB04.

| Visible strings / fact | Bibliography row(s) | Verdict | Source text or observed evidence; discrepancy |
|---|---|---|---|
| 000: figure identifier and directional kicker | Editorial label | CONFIRMED | `10a (with Anthropic)` identifies this figure. “Lab → funders” requires the equity/valuation qualifications below; it is not a cash-payment claim. |
| 001–002: connected funders include Anthropic Series A investors | IV01; grant-chain inputs mostly missing | DIFFERS | Anthropic's May 28, 2021 announcement names Tallinn, Moskovitz, Schmidt, McClave, and CERR. ARC/RAND/Longview connections need the omitted M rows, and intermediary awards do not prove onward passage of the same money. |
| 001–002, 030–033, 122–125, 234–248: Moskovitz and Tallinn describe themselves as board observers | ST118, ST41 | CONFIRMED | Stratechery: “I'm a board observer at Anthropic.” Postimees says Tallinn is a `nõukogu vaatleja` and quotes his earlier radio explanation for declining a board seat. ST41 should attribute that reporting chain correctly. |
| 001–002, 128–138: donated stake, “our foundation,” no identified recipient | ST33, ST78–ST79, ST89, ST110–ST113 | CONFIRMED, bounded | Forbes reports a nonprofit transfer; Moskovitz uses “our foundation”; Berger says “not to us.” The checked records do not identify the receiving account. They do not prove it can never be identified or exclude all indirect exposure. |
| 001: “now worth up to $7.7B” | ST92, IV10 | DIFFERS | Forbes gives an estimated percentage bound; Anthropic gives a May 28 valuation. Multiplying them is a conditional ceiling, not evidence of current realizable value or an independently measured holding. |
| 001–002: “Good Ventures has no METR grant on its books”; “No METR grant is on its books” | No bounded direct-grant block | DIFFERS | The saved index has no METR-named organization; checked GVF filings have no METR grantee. The title omits the dates and narrows neither “Good Ventures” nor “books”; subtitle's `its` is ambiguous. |
| 002, 008–020: Moskovitz/Tuna philanthropy, Coefficient, Good Ventures, SVCF/NPT funding-partner grouping | ST105, ST109, ST124 | DIFFERS | Coefficient names “external funding partners” and separate approvals. It does not say the SVCF/NPT account principals are the couple. The family bracket and “their philanthropy is the money” still suggest that attribution. |
| 002, 021–024: Good Ventures Foundation, $10.1B endowment, June 2025 | ST100 filing; ST113 CSV notes identify its total assets | CONFIRMED amount/date | FY2025 XML `TotalAssetsEOYAmt = 10107955038`. The rounded number and date are supported. Use “total assets” for the precise filing measure; making that field explicit in ST100 would improve provenance. |
| 025–028: $10M to Open Philanthropy Advisors, now Coefficient Giving Advisors, FY2024 | ST140 | CONFIRMED | FY2024 paid-grant group names `OPEN PHILANTHROPY ADVISORS INC`, `GENERAL SUPPORT`, `Amt = 10000000`. Historical payee is correctly distinguished. |
| 003–007, 256: colors and money types; SFF recommendations vs awards vs commitment vs filed grants | Partial; most M inputs missing | DIFFERS | These are distinct measures in the rows and code; no cross-type grand total is calculated. However, the blue legend's “Good Ventures Foundation or its funding partners at SVCF/NPT” assigns the partner relationship to the wrong entity. They are Coefficient's named partners. Widths and exceptions are audited below. |
| 029: “the money” on Good Ventures→Coefficient arrow | ST140 | DIFFERS | ST140 supports one historical grant, not a comprehensive characterization of Coefficient's funding. Both arrow paths were damaged in the initial snapshot and render in the recovery check. |
| 030–033, 139–141, 181: Tallinn, Series A lead, Series B investor, undisclosed percentage | IV01–IV02, ST41, ST98 | CONFIRMED | Issuer releases identify the early investments; Tallinn's reported words include “protsente ei kuuluta” (“we do not announce percentages”). The quotation is translated, not an original English utterance. |
| 034–045: Audacious, TED, Canary with RAND/METR, 2024 cohort, direct partner payments | No AP or M57–M58/M118 block | DIFFERS | Current Audacious material describes partners funding projects; RAND and METR's October 9, 2024 releases identify Canary and the commitment. These sources need bibliography blocks. |
| 040–042: Valhalla→RAND $10.0M; High Tide→RAND $333K | Missing M119, M143/AP46 | DIFFERS | Filed amounts are $10,000,000 and $333,334, rounded correctly. The retained grant purposes identify Project Canary. These are payments to RAND, not evidence that METR received either amount. |
| 042–045: no METR payment in filings read; Good Ventures joined after announcement; none traced | Missing M117/AP47/AP49 | DIFFERS | The statement needs the actual filing/date and partner-list comparison in the bibliography. “None traced” should explicitly end “in the records checked through June 2025.” A current partner list alone cannot establish when a partner joined. |
| 046–053: Founders Pledge grants match Tallinn; SVCF within $450; other named sponsors unattributed | Missing M77–M96 | DIFFERS | The CSV/filing and Tallinn-ledger comparisons support matches, not proof of donor identity solely from an amount. Vanguard, Effective Ventures, Every.org, AEF, Fidelity are sponsor/regrantor names; their account principals are not established here. |
| 054–057: Alignment Research Center, Christiano, parent until December 2023, $4.55M spin-out | Missing M61–M63 | DIFFERS | ARC's FY2024 Schedule I records $4,477,169 cash + $76,766 noncash = $4,553,935, “Program Spin-Off,” distribution April 30, 2024. December 2023 organization separation and April 2024 asset distribution are different events; add their dated sources. |
| 058–063: RAND/Canary ~$38M; ~$21M RAND and ~$17M METR | Missing M57–M58; G14 covers later amount | DIFFERS | RAND: “Approximately $38 Million”; METR: “Approximately $17 million of this will support work at METR.” The ~$21M remainder is subtraction, not RAND's quoted allocation. |
| 062–063: “a bit under $16m” over 3 years | G14 | CONFIRMED | Barnes's September 28, 2025 comment: “This ended up being a bit under $16m, and is a commitment across 3 years.” It is a later commitment statement, not a paid amount. |
| 064–066: Longview Philanthropy, pooled-fund relationship | M140 Why; underlying M60 missing | CONFIRMED relationship; citation incomplete | METR's About page names “pooled funds such as those of Longview Philanthropy”; Longview names METR among supported work. The Macroscopic grant to Longview is for specified programs and does not establish onward routing to METR. |
| 067–069, 102: FAR AI founder Adam Gleave, METR board seat | B05 | CONFIRMED | Gleave/METR pages identify the FAR.AI co-founder/CEO and board role. “No grant on record” needs a named search scope; it does not establish unpaid work or absence of a contract. |
| 070–075, 094: Redwood/OpenAI work; Anthropic subcontract per Redwood; terms undisclosed | RW31–RW34, RW36, RW58 | CONFIRMED, bounded | METR names a Redwood staff member contracting with it; Redwood's own September 12 post says “Several staff from Redwood have been subcontracted by METR to work on this investigation.” Anthropic's announcement alone does not name Redwood. |
| 076–078, 095: Constellation Berkeley office; no grant on record | Missing M126 for office; no bounded negative block | DIFFERS | The research record identifies Constellation as office context. Neither “office” nor an unbounded zero establishes payment terms. Supply M126 and a scoped record-search citation. |
| 079–082: METR's name and stated funding restriction | K01 | CONFIRMED | About page: “METR has not accepted funding from AI companies”; also says it cannot accept donations “made by or at the direction of frontier AI company employees.” This is METR's stated policy/report, not an independent certification of all receipts. |
| 083: $1.5M, 2022, ARC | Missing M01–M02 | DIFFERS | Issuer-index awards $265,000 + $1,250,000 = $1,515,000; dates March 1 and November 18, 2022. Rounded display correct, bibliography missing. |
| 084: $10.0M, 2025, “AI Evaluation and Testing,” RAND | Missing M03 | DIFFERS | Saved issuer index: title `AI Evaluation and Testing`, amount $10,000,000, September 20, 2025. |
| 085: $26.3M, 2022–25, Longview | Missing M04–M14 | DIFFERS | Eleven matched issuer-index awards total $26,251,590. Dates and rounded total match; source programs are not all METR grants. |
| 086: $59.3M, 2021–25, FAR AI | B05 Why and full CSV row; M15–M32 index inputs | CONFIRMED | B05's `other_org_funders` field supplies $59,347,676 across 18 awards, October 2021–September 2025. All eighteen amounts/dates match the saved issuer index. Exposing the input IDs in the public block would improve reproducibility, but this is not an unsupported total. |
| 087: $5.6M SFF recommendations, 2022–24, ARC/ARC Evals | Missing M35–M37 | DIFFERS | SFF source tables show $2,179,000, $3,247,000, and $197,000; total $5,623,000. |
| 088: $752K SFF recommendations, 2024–25, METR, conditional match included | Missing M38–M39 | DIFFERS | $204,000 + $548,000 = $752,000. SFF 2025 separately identifies the $428,000 matching component within its $548,000 recommendation; do not add it again. |
| 089, 098: $38.0M Canary commitment (2024); ~$17M committed to METR | Missing M57–M58 | DIFFERS | Matches the two dated October 9, 2024 releases, subject to the later G14 update. The two amounts are total and component, not additive flows. |
| 090: $70M+ 2026 recommendation to Redwood | M120 | CONFIRMED | Coefficient's September 9, 2026 post: “recently recommended more than $70 million over the next two years.” It is an internal recommendation, not a $70M paid grant. |
| 091: $2.4M SFF recommendations, 2022–23, Redwood | Missing M47–M48 | DIFFERS | SFF tables: $1,274,000 + $1,098,000 = $2,372,000. Rounding is correct. |
| 092: $22.9M, 2023–24, Constellation | Missing M126–M128 | DIFFERS | Matched awards $3,000,000 + $3,200,000 + $16,750,000 = $22,950,000. Prefer $22.95M or explicitly rounded $23.0M. |
| 093: $10.0M, 2024, SVCF→Constellation | ST107 | CONFIRMED | SVCF 2024 Schedule I: `CONSTELLATION RESEARCH CENTER` and $10,000,000. Sponsor disclosed, originating donor not disclosed. |
| 096: $10.8M filed grants to ARC, 2022–25; $4.2M matching Tallinn | Missing M77–M96 | DIFFERS | Selected filed grants sum to $10,835,635. The ledger-match amount is an identified subset, not additional money; add the actual compared rows. |
| 097: $4.2M to METR, 2024–25; Vanguard $4M, FP $184K, SVCF $20K | Missing M79/M83/M87; ST107 gives only SVCF component | DIFFERS | Filed components $4,000,000 + $184,000 + $20,000 = $4,204,000. No block gives the total, Vanguard/FP components, or the ledger match. |
| 099: $4.6M spin-out transfer, April 2024 | Missing M63 | DIFFERS | Same $4,553,935 source as node's $4.55M, rounded to a different precision. Label the transfer date April 30, 2024 if precision is desired. |
| 100–101: $220K, 2023, per GWWC; additional pooled funding undisclosed | Missing M59–M60 | DIFFERS | GWWC says Longview “recommended a grant of $220,000 from its public fund in 2023.” The label omits “recommended”; this secondary report is not proof of disbursement. |
| 103: $5.3M Coefficient awards, 2024–25, Tarbell Center | TB02–TB04 | CONFIRMED | Index amounts $816,000, $1,587,930, $2,888,000 total $5,291,930. All components are in the bibliography; TB02's Why also gives the approximate $5.29M aggregate. Source URLs need the replacements in Task 5. |
| 104: SFF $1.3M recommendations, 2024–25, $200K conditional match | TB05–TB06 | CONFIRMED | $520,000 + $783,000 = $1,303,000; $200,000 match is included in the latter. TB05 names Tarbell Fellowship via Players Philanthropy Fund, not the identical receiving charity as TB06. These are recommendations, not demonstrated payments. |
| 105–109: Tarbell fellowship; reporters work at outlets; Coefficient-funded AI articles found in captured windows | TB02–TB04 for funding; missing TO01–TO06 for articles | DIFFERS | Fellowship/award evidence supports affiliations and funding. It does not prove editorial control. “AI articles” needs the classifier, window, and partial-coverage qualifications now absent from the figure. |
| 110: TIME · 45 | Missing TO01 | DIFFERS | TO01: 45, September 12, 2025–September 11, 2026, partial; 42 keyword-fallback + 3 tag-page articles. No block supports the displayed count. |
| 111: The Verge · 37 | Missing TO02 | DIFFERS | TO02: 37, June 25–September 11, 2026, partial publisher-tag window. No block. |
| 112: MIT Tech Review · 26 | Missing TO03 | DIFFERS | TO03: 26, September 12, 2025–September 11, 2026, complete captured window; 22 tag + 4 keyword-fallback. No block. |
| 113: Lawfare · 22 | Missing TO04 | DIFFERS | TO04: 22, September 15, 2025–August 20, 2026, partial keyword-fallback sample. No block. |
| 114: The Guardian · 20 | Missing TO05 | DIFFERS | TO05: 20, September 18, 2025–September 11, 2026, partial publisher-tag window. No block. |
| 115: LA Times · 14 | Missing TO06 | DIFFERS | TO06: 14, June 5–August 31, 2026, partial publisher-tag window. No block. These six counts reproduce the CSV inputs; an absent bibliography block is not repaired by that agreement. |
| 116–118: Anthropic is evaluated and investigated by METR | RW36/RW58 investigation; evaluation source not explicit in these blocks | DIFFERS | Anthropic's incident announcement establishes its agreement with METR; the broader evaluation assertion needs a corresponding evaluation citation, not merely the subcontract post. |
| 119–121: Series H, May 2026, $965B; WSJ IPO target ~$2T | IV10, IV11 | CONFIRMED | Anthropic: May 28, 2026, $965B post-money. Retained September 12 WSJ text says an IPO “could” value it around $2T. The latter is reporting, not a priced financing. |
| 126–127: “Investors among METR's funders” | IV01–IV02, M75, J08 and the relationship rows below | DIFFERS in grouping | METR names “individuals from Jane Street” and Schmidt Sciences; these are not interchangeable with the Jane Street firm or Schmidt's investing vehicle. Prefer “Investor connections to METR's funders” and retain the individual/entity and direct/indirect distinctions. |
| 128–138: Moskovitz named Series A investor in 2021; under 0.8%; donated 2025; no such gift in GVF return through June 2025 | IV01, ST32–ST33, ST78–ST79, ST89, ST92 | CONFIRMED, bounded | The issuer names the investor, not the purchasing vehicle. Forbes's percentage is an estimate. GVF Schedule B shows one noncash gift described as publicly traded securities, not Anthropic shares. |
| 142–147: Schmidt Series A; Hillspire owns 20% of D.E. Shaw; venture arm Series H; Schmidt Sciences METR supporter | IV01, ST49, ST26, J08 | DIFFERS | The issuer and METR support the named investments/supporter. Forbes says his family's vehicle **bought** 20% in May 2015; its profile does not name Hillspire or establish unchanged current ownership. Replace “owns” with dated acquisition wording or add a suitable source. |
| 148–154: Jane Street firm, $100M/3.3M shares/~$30, March 2024 estate sale; Series E–H; individuals named as METR donors | IV05, IV07–IV10, M75 | CONFIRMED, rounded | Court exhibit cited in ST20–ST21: `Jane Street Global Trading, LLC 3,332,833 $99,999,988`; quotient $30.00447. Four issuer releases name Jane Street. METR says “individuals from Jane Street,” not the firm. Add the court exhibit to IV05's sources. |
| 155–156: McClave Series A/B; “BEMC is not a METR donor” | IV01–IV02, J02 | DIFFERS | Issuer names confirmed. A searched filing set cannot establish universal absence. Five `.xml` files in `audit3-evidence/shared/` are actually challenge-page text; the two substantive recent filing renders do not establish all five claimed years. |
| 157–161: CERR/Macroscopic Series A/B; Redwood and Longview grants; Apollo and Halcyon venture-arm investments | ST54, M139–M142 | CONFIRMED | Issuer releases name CERR; Macroscopic's current Grants page names Redwood and Longview programs and lists Apollo Research and Halcyon Venture Partners under “Impact Investments.” Not a grant to METR or Halcyon Futures. |
| 162–166: June 2025 GVF book, TSMC $509M, SK Hynix $400M, Broadcom $290M, Vistra/Micron/Vertiv | ST100 | CONFIRMED | FY2025 stock schedule: $508,854,795; $399,749,206; $290,449,924; $202,021,342; $184,134,391; $178,712,948 respectively. Rounded displayed amounts match. |
| 166–170: manager launched VAR AI Fund March 2025; $4.35B sold to 116 by June 2026 | ST101 | CONFIRMED figure; DIFFERS bibliography | March 21 Form D says first sale yet to occur/$0 sold; June 15, 2026 amendment gives `4346290561`, `116`. Figure separates the dates; the bibliography still calls the launch multi-billion-dollar. |
| 170–173: at least one of two charitable clients is LP; identity unstated | ST125 | CONFIRMED as explicit inference | ADV lists four clients, two charitable organizations, and Q20 `50%` invested in the fund. The master cannot invest in itself, so at least one charitable client is implicated; the source does not identify it as GVF. |
| 174–177: manager's co-owner is ARC board member; “METR's parent” | ST127 | DIFFERS | ADV names Benjamin Hoskin; ARC's FY2024 officer list says `BOARD MEMBER`. ARC is METR's **former** parent. The ADV URL alone does not establish the board role. |
| 178–180, 196–202, 256: ≤$7.7B donated stake, 1/30 scale, 0.8% × $965B = $7.72B, no-floor ceiling, ×15 | ST92, IV10; chart calculations not explicit in blocks | DIFFERS | Conditional exact ceiling < $7.72B; plotted rounded ceiling $7.7B; ratio 15.4 plotted / 15.44 exact. “≤$7.7B” and unqualified “×15” are not exact identities. Scaling is a drawing convention. |
| 182–185: possible SVCF/NPT DAF route; NPT $1.18B in 19 FY2025 gifts; donor/issuer unattributed | ST104, ST121 | CONFIRMED conditional wording | NPT Schedule M: count `19`, amount `1183079981`. The words “possible route no source confirms” correctly withhold attribution. Schedule B disclosure cannot be assumed to reveal an issuer or donor. |
| 186: unnamed frontier companies→METR free tokens, “unbooked and unquantified” | K01 | DIFFERS | “Significant free tokens” and no named company/amount are supported. This source does not establish bookkeeping treatment. Remove “unbooked” or add accounting evidence. The text is also clipped. |
| 187: Joe Benton, Anthropic alignment staff→METR, September 2026 | S13 | DIFFERS date precision | NBC September 10 reports the role/move. Benton's September 2 self-post says “Last week I left Anthropic to join @METR_Evals”; use **announced September 2, 2026**, rather than treating September as a proved effective start date. |
| 188–201: two published bounds at different dates; early-2025 transfer, Forbes estimate November 2025; “Sep 2026 ceiling”; “already skyrocketed in value” | ST32–ST33, ST92, IV10 | DIFFERS in ceiling date/interpretation | Forbes November estimate/transfer timing and April reranking wording are supported. The $965B round is May 28, 2026. “Two estimates/bounds at different dates” must not imply the two amounts measure investment growth on equivalent bases. |
| 203–217: Forbes card, byline/date, sentence, unnamed vehicle, April reranking | ST32–ST33, ST92 | CONFIRMED wording with typography qualification | Saved US and AU copies contain the same full sentence, including the two inner quotations and “she says.” US: Phoebe Liu, November 7, 2025; AU: November 10. See Task 4 for exact comparison. |
| 218–228: March 30/April 11 Bluesky excerpts including $20B and Anthropic | ST110, ST112–ST113 | DIFFERS by omitted correction | Quoted excerpts match the saved posts, but the same April 11 thread contains the April 12 correction that not all of the $20B was in the foundation. The card and bibliography omit it. |
| 229–233: June 2025 return, two contributors, no private stock; “not to us”; account unattributed | ST78–ST79, ST89 | DIFFERS scope of “no private stock” | Two listed contributors and no **direct noncash private-stock gift** match Schedule B. The return also lists aggregate private-equity/venture investments; “no private stock” should not exclude indirect exposure. |
| 234–245: October 20, 2025 Stratechery observer/boardroom quotation | ST118 | DIFFERS punctuation/truncation | Both passages are present, including the transcript's awkward “a chair of at” and “in at.” The second passage continues after “not quite that naive”; the figure adds a full stop without an ellipsis. |
| 246–253: observers not directors by their account; Tuna chairs Coefficient; Moskovitz manager; grants for own programs; “No motive is asserted” | ST41, ST118, ST124; program/recipient M rows mostly missing | CONFIRMED governance; DIFFERS grant coverage | Governance page identifies `Cari Tuna (Chair of the Board)` and lists Moskovitz as a manager. The disclaimer is present. Add the grant rows and describe Coefficient as recommending awards where that is the source's measure. |
| 254: direct-negative annotation, 2,911-row index September 11, 2026, GVF filings through June 2025 | Missing M33/M104 | DIFFERS bibliography coverage | Saved issuer snapshot has exactly 2,911 records and no METR-named organization. The displayed annotation is bounded, unlike the title, but its bibliography support disappeared with the long footnote. |
| 255–256: coverage statement, research/CSV provenance, September 11 snapshot, build September 14, “every source file,” four audits | No factual-completeness block | DIFFERS | These are provenance labels, not financial amounts. “Every number cites a row id” is false for the missing blocks above. “Every source file” is not established by the figure's evidence links. Replace with a precise pointer to the source register. |

Computed totals are accepted when the listed blocks and their source rows supply the inputs; an additional aggregate block is not mandatory. B05 supplies FAR AI's amount and date span through its full CSV row. In contrast, ST107's SVCF components do not supply the omitted Vanguard/Founders Pledge inputs or all the ledger comparisons.

## Task 2 — arithmetic table

The following are independent measures. Rows sharing a destination do not authorize adding awards, recommendations, commitments, filed payments, asset transfers, or equity values together. [Arithmetic receipt](audit4-evidence/arithmetic.json) records the selected CSV IDs and exact sums.

Widths are SVG user units. The element is 2,156 CSS pixels wide, but the flex layout shrinks its height and `preserveAspectRatio` scales the drawing uniformly by **0.9951140873**, not the width-only ratio. PNG widths are multiplied by **1.9902281746** at device scale 2. The measured screen transform is `x_css = 65.0813492 + 0.9951140873 × x_svg`, `y_css = 578.671875 + 0.9951140873 × y_svg`. A printed “px” rule should explicitly mean SVG units or account for the actual transform. See [transform receipt](audit4-evidence/svg-transform.json). **Path-damage remarks in this arithmetic table describe the initial snapshot only: every listed path renders in the recovery check, with unchanged width attributes.**

| Flow / code inputs | Exact amount in USD | Printed amount | Required width `6 + 1.4 × millions` → SVG width | Result |
|---|---:|---|---|---|
| Coefficient→ARC, M01–M02 | 1,515,000 | $1.5M | 8.121 → 8.1 | Arithmetic correct; path destroyed. |
| Coefficient→RAND, M03 | 10,000,000 | $10.0M | 20 → 20.0 | Correct; path destroyed. |
| Coefficient→Longview, M04–M14 | 26,251,590 | $26.3M | 42.752226 → 42.8 | Correct; path destroyed. |
| Coefficient→FAR AI, M15–M32 | 59,347,676 | $59.3M | 89.0867464 → 89.1 | Correct; path destroyed. |
| SFF→ARC/ARC Evals, M35–M37 | 5,623,000 | $5.6M | 13.8722 → 13.9 | Correct recommendation sum; path destroyed. |
| SFF→METR, M38–M39 | 752,000 | $752K | 7.0528 → 7.1 | Includes $428,000 conditional match; path destroyed. |
| Audacious→Canary, M57 | approximately 38,000,000 | $38.0M | 59.2 → 59.2 | Approximate commitment; path destroyed. |
| Coefficient→Redwood, M120; code uses 70,000,000 | more than 70,000,000 | $70M+ | 104 → 104.0 at lower bound | Width represents the $70M lower bound, not the unknown exact recommendation; path destroyed. |
| SFF→Redwood, M47–M48 | 2,372,000 | $2.4M | 9.3208 → 9.3 | Correct; path destroyed. |
| Coefficient→Constellation, M126–M128 | 22,950,000 | $22.9M | 38.13 → 38.1 | Width correct. Binary floating-point `.1f` yields $22.9M; use $22.95M to remove ambiguity. Path destroyed. |
| SVCF→Constellation, ST107 | 10,000,000 | $10.0M | 20 → 20.0 | Correct filed amount; path destroyed. |
| DAF/regrantor→ARC, M77–M78/M80–M82/M84–M86/M88–M90/M93–M96 | 10,835,635 | $10.8M | 21.169889 → 21.2 | Correct selected filed-grant sum; path destroyed. |
| DAF/regrantor→METR, M79/M83/M87 | 4,204,000 | $4.2M | 11.8856 → 11.9 | Correct; $184,000 + $20,000 + $4M. Path destroyed. |
| RAND/Canary→METR, M58 | approximately 17,000,000 | ~$17M | 29.8 → 29.8 | Drawn correctly; older commitment estimate, not a new payment. G14 supplies later < $16M. |
| ARC→METR, M63 | 4,553,935 | $4.6M pipe; $4.55M node | 12.375509 → 12.4 | Drawn correctly; both labels round the same asset transfer at different precision. |
| Longview→METR, M59 | 220,000 recommended per GWWC | $220K | 6.308 → 6.3 | Width correct; payment interpretation not established. |
| Coefficient→Tarbell, TB02–TB04 | 5,291,930 | $5.3M | 13.408702 → 13.4 | Correct award sum; path destroyed. |
| SFF Tarbell recommendations, TB05–TB06, label only | 1,303,000 | $1.3M | No SFF Tarbell path exists | Correct recommendation sum; includes the $200,000 conditional match. |
| Implied RAND share | approximately 38M − 17M = 21M | ~$21M | No separate allocation path | Valid subtraction if explicitly labelled implied; not a sourced RAND quote. |
| Valhalla / High Tide labels | 10,000,000 / 333,334 | $10.0M / $333K | No individual payment paths | Correct rounding, separate filed payments. |
| DAF ledger-match labels | approximately $4.2M ARC; $184K + $20K METR | $4.2M, $184K, $20K; within $450 | No separate additional paths | Subsets/comparisons of filed grants, not additional inflows. Missing bibliography inputs. |
| Forbes percentage × Series H | 0.008 × 965,000,000,000 = 7,720,000,000 | ≤$7.7B; small text $7.72B | `int((6 + 7,700 × 1.4)/30) = 359` band height | 359-unit band matches code's rounded $7.7B base. Because source says **less than** 0.8%, use **< $7.72B** for the exact conditional ceiling. |
| Chart lower bar / upper bar | 500M / 7,700M plotted | $500M / ≤$7.7B | Computed heights `300 × 500/7700 = 19.48051948`, `300`; emitted with `.0f` as `19`, `300` | Integer-rounded heights match the generator. They compare a press estimate with a later conditional upper bound. |
| Chart multiplier | 7,700/500 = 15.4; exact bound 7,720/500 = 15.44 | ×15 | N/A | DIFFERS if exact. Print `≈15× at the ceiling` or `≈15.4×`; do not call it measured appreciation. |

Three orange relationship paths are 6 units at a code amount of zero, matching the formula's intercept; that zero is a drawing input, not evidence of zero compensation. The two dashed red equity paths are explicitly 8 units and are not monetary pipes. The 3-unit red annotation, 12-unit Good Ventures connector, arrowhead, and 3-unit outlet connectors are also annotations, not values on the money scale. The footnote should explicitly exempt these. The 22 flow-group paths have no individual opacity attribute and sit in one `opacity="0.55"` group; this part of the requested style is implemented. Sixteen paths in that group were malformed initially; all 22 are valid in the recovery check.

## Task 3 — text integrity and citations

The initial capture preserved all **75 expanded pre-strip IDs** in the HTML comment, and that set equals the 75 keyed block IDs: no missing or extra IDs in either direction. The updated comment still contains exactly that set. This says nothing about facts whose generating text never contained an ID. In particular, `idl` and `anth_note` are still assembled in `fig_money()` but are no longer included in the short footnote; the generated numeric pipe labels and outlet chips often lack their own IDs.

In the initial snapshot, the stripping function operated on HTML/SVG markup, not only human-readable text. For example:

```text
Before: M700,200 C915.0,200 915.0,110 1130,110
After:  ,200.0,200 915.0,110 1130,110
```

The original row-ID regular expression consumed `M700` and `C915`; the resulting path had no initial moveto. All nineteen initially affected paths are enumerated, with their `d` strings and measured zero lengths, in [layout-summary.json](audit4-evidence/layout-summary.json). The updated `strip_ids()` preserves tag attributes and cleans text before wrapping; all 31 paths now have nonzero lengths. The following residue inventory records the original defects: **the six `(, )` remnants have all been removed in the recovery check**, while the free-token caption's final semicolon remains.

| Location / visible indices | Residue | Required fix |
|---|---|---|
| Coefficient subtitle, 019–020 | `principals are not public (,` followed by `)` | Strip the whole citation before wrapping, eliminating both punctuation and the residual line. |
| Tallinn/SFF subtitle, 032–033 | `by his own account (,` then `)` | Same. |
| Anthropic observer paragraph, 124–125 | `and Tallinn (,` then `).` | Same; retain the sentence's period. |
| Anthropic manager/ARC paragraph, 176–177 | `parent ARC (,` then `)` | Same; also change “parent” to “former parent.” |
| Possible DAF route caption, 184–185 | `unattributed (,` then `)` | Same. |
| Chart ceiling explanation, 199–200 | `no floor (,` then `);` | Remove the citation parentheses and keep only punctuation joining the actual sentences. |
| Free-token caption, 186 | final `;` with no following clause | Use a period; distinguish this minor punctuation issue from the unsupported “unbooked” claim and clipping. |

No doubled spaces, additional empty `()` or `( )` text, or sentence that lost a substantive human-language object was found after joining wrapped lines. The six initially empty SVG text elements in the Anthropic panel are also gone in the recovery check. Quotation-card phrases “a chair of at” and “in at” are in the saved transcript, not stripping errors.

The clean bibliography is exactly the current builder's transformation of the keyed text: the same 75 blocks in the same order, with block/inline IDs and section-heading CSV names removed. However, the stronger requirement “minus IDs and CSV names” is not fully met: ST94 retains `index_2025.csv`/`index_2026.csv`, ST115 retains `sit-2022.csv`, ST127 retains `people.csv`, and J02/J08 retain `01-funding-rounds.csv` in their Source paths. The generic header also says `research/*.csv`. There is no other unexplained text divergence. Preserve useful source provenance in a separate register rather than corrupting a URL to remove a filename.

## Task 4 — cards

[Card comparison receipt](audit4-evidence/card-checks.json) records the source hashes, dates, exact comparison results, and relevant post bodies.

1. **Forbes:** both saved US and AU copies have the same complete stake sentence. The figure preserves the estimate, early-2025 timing, both inner quotations, the comma inside the second inner quotation, and **“she says.”** Its inner single quotation marks are conventional nesting inside the figure's outer double quotation marks; the sources use curly double quotation marks. Thus words/punctuation placement are confirmed after that stated typographic normalization, but this is not a byte-for-byte character match. The US copy identifies **Phoebe Liu, November 7, 2025, 06:30am EST**; the AU copy identifies **Phoebe Liu, November 10, 2025**. The bibliography's AU URL should also identify that reprint date and link the archived US original when giving the US date.
2. **Bluesky:** the matching source timestamps are March 30, 2026, `05:24:03.877Z` and `05:28:20.270Z`, and April 11, 2026, `20:59:50.704Z`. The first two card excerpts are verbatim selections. The ellipsis in the third omits the author's additional-personal-assets parenthetical; its omission is visibly marked. But the same saved thread includes his April 12, `02:46:25.482Z`, correction: not all, though still most, of the $20B was in the foundation. Add that correction or remove the $20B excerpt. Do not compare the April 2026 statement with June 2025 assets to “prove” that “foundation” includes DAFs.
3. **Stratechery:** the October 20, 2025 Wayback transcript supports the observer statement and all words in the displayed boardroom passage. The last displayed word `naive` is followed in the original by `and I think Open Philanthropy has been more measured...`, not a period. Replace the inserted period with a visible ellipsis or include the continuation. The card's governance explanation correctly says Tuna chairs Coefficient and Moskovitz sits on its Board of Managers. Preserve the transcript's awkward words only if visibly presented as a verbatim transcript quotation.

## Task 5 — bibliography, all 75 blocks

The following failures table distinguishes source/wording problems from access limitations. An inaccessible live source with a substantive saved copy can support the claim, but the bibliography must direct the reader to that copy. Exact source-field fidelity is **75/75**; it does not excuse a wrong, incomplete, or nonportable source field. A full per-block disposition follows the failures table.

### Bibliography failures table — exact fixes

| Block(s) | Failure observed | Exact correction recommended |
|---|---|---|
| ST32 | Why says “the only published dollar estimate” and puts `$500M` in the title, which now says $7.7B. Source is AU reprint but Claim gives US date. | Replace Why with: **“Forbes's November 2025 estimate supplies the chart's $500M bar and card 1; it is not a transfer-date valuation.”** Identify US original November 7 and AU reprint November 10, 2025; add the archived US source below. |
| ST41 | “Tallinn told Postimees (Feb 2026)” misidentifies the interview outlet/time. | Claim: **“Postimees reported in February 2026 that Tallinn is an Anthropic board observer and quoted his explanation to Äripäev radio in early January 2026 for declining a board seat.”** The source distinguishes the reporter's characterization from Tallinn's quotation. |
| ST49 | Profile supports a family vehicle's 20% acquisition, not the Hillspire name or present ownership. | Claim: **“Forbes's Schmidt profile says his family's investment vehicle bought 20% of D.E. Shaw & Co. in May 2015; the profile does not name Anthropic.”** If retaining Hillspire, add the saved acquisition report naming it; do not infer unchanged 2026 ownership. |
| ST54 | Claim and Why join Series B and Macroscopic grants to a Source containing only the Series A release. | Keep supported claims, but add the Series B issuer URL and `https://macroscopic.org/grants` as the specific primary sources for those clauses. Do not present the Series A release as the source for later grantees. |
| ST78 | Why concludes the shares “had not reached” the filer, exceeding the directly reported contribution evidence. | Why: **“GVF's FY2025 Schedule B reports one noncash gift, described as publicly traded securities, and no direct gift described as Anthropic/private stock. This does not identify the recipient of the donated stake or exclude indirect exposure.”** Retain exact amounts and dates. |
| ST89 | “Coefficient's own entities are out” treats an attributed `not to us` as an exhaustive legal-entity exclusion. | Why: **“Berger says the donated stake went ‘not to us.’ This is Coefficient's CEO's statement, not an independently established exclusion of every affiliated legal entity or account.”** |
| ST90 | Why's “giving complex” interpretation can be mistaken for an identified holding entity. | Why: **“Moskovitz says ‘GV’ benefits through Anthropic and other investments; the post does not identify the legal entity, account, or direct versus indirect exposure.”** Keep the attributed quotation. |
| ST91 | “The foundation's largest holdings do not include Anthropic” enlarges a journalist's examples into a complete investment inventory. | Claim ending: **“The article's examples of large foundation holdings do not name Anthropic.”** Retain its independently quoted DAF statement without naming SVCF/NPT accounts. Add the saved US archive route for the 403 live URL. |
| ST92 | Why rounds an exact conditional ceiling without explaining rounding or the two source dates. | Why: **“Applying Forbes's April 20, 2026 estimated bound of less than 0.8% to the May 28, 2026 $965B round gives a conditional ceiling below $7.72B (about $7.7B), not a measured stake value.”** Add the saved April archive for the 403 URL. |
| ST94 | Claims “every” released/received return and approximately 900,000 returns; the current retained log instead records 24 batch completions and 1,134,796 file visits, without a deduplicated unique-return count. Directory URL 404; clean file retains CSV filenames. | Claim/Why: **“The retained 2025–2026 bulk-scan records, completed September 14, 2026, contain 11 matching return records; none identifies a Moskovitz/Tuna vehicle holding Anthropic. This is a negative within the scanned files, not all filed or future returns.”** Cite `irs-anthropic-scan/hits.csv`, context files and completion log in the keyed register; do not present file visits as unique returns. Remove unsupported approximately-900,000/all-returns wording. |
| ST95 | Why says the trust's holdings are “on no public document,” while Claim itself identifies publicly disclosed Meta shares. | Why: **“The 2020 Meta proxy identifies the trust and its disclosed Meta holding; no Anthropic holding for it was identified in the reviewed records.”** Replace any categorical Asana/Kodiak or current-holdings absence with a dated, searched-record statement. |
| ST96 | “Nothing in the press resolves the stake” extends one article's silence to all press. | Why: **“This September 2026 NYT article gives no percentage for the METR-linked early funders named in the figure and does not resolve their stakes.”** Identify the saved subscriber PDF instead of treating the 403 as an evidentiary negative. |
| ST99 | “The Remainder Interest Trust holds neither Asana nor Kodiak” turns absence from selected ownership filings into actual non-ownership. | Claim opening: **“The reviewed Asana and Kodiak ownership filings do not list the 2018 Remainder Interest Trust as a holder.”** Keep dated, positively reported holdings and identify the saved filings behind the blocked SEC search URL. |
| ST100 | Source is an IRS directory that now returns 404; “AI-infrastructure portfolio” is editorial classification. | Source: the two identified FY2024/FY2025 XML extracts, with their object IDs/download provenance. Preface the characterization **“The listed public holdings include substantial AI-infrastructure exposure (analysis).”** For clearer provenance, add **FY2025 total assets $10,107,955,038 as of June 30, 2025**, already supported by the filing and identified in ST113's CSV notes. |
| ST101 | Claim still says a multi-billion-dollar fund was launched “in the transfer window,” despite the $0 launch filing. | Replace that clause with **“VAR AI Fund filed its initial Form D on March 21, 2025, reporting first sale yet to occur and $0 sold; the June 15, 2026 amendment reports $4,346,290,561 sold to 116 investors.”** Do not assert overlap with an unknown exact donation date. Preserve manager/fund distinction. |
| ST102 | Values match the 13Fs, but blocked browse URL supplies no accessible filings and “positions” can be mistaken for unique issuers. | Source: identify all three saved 13F filings. Use **“72, 86, and 123 table entries”** for the counts and **“reported 13F portfolio values”** for the totals; do not describe them as the foundation's holdings alone or as an inventory of private stock. |
| ST103 | Claim's source-type label still says 22 returns; Why says 18 and claims the line-11 correction is reflected when Claim still lists line 10 only. | Replace **“22 returns” → “18 saved e-file returns.”** Add **“These Schedule M line-10 figures do not cover every form of private-stock exposure; partnership/trust interests are reported separately on line 11.”** State the snapshot date for unavailable years. Replace dead directory link with the saved return register. |
| ST104 | The NPT complex-assets policy page resolves but does not contain the FY2025 $1.183B/19/$162.7M/52 figures. | Add the FY2025 NPT filing, object **202601289349302480**, as Source for the numeric claims; retain the policy page only for liquidation policy. Why: **“The reported aggregate intake is unattributed and does not identify an Anthropic gift or a Moskovitz/Tuna account.”** |
| ST107 | Claim says “a fund of that size moved”; Why states “the account family ... moved from SVCF to NPT.” Neither account identity nor migration is established by a sponsor-level grant. | Claim: **“SVCF's 2024 Schedule I reports $1,591,322,838 in grants to NPT and $10,000,000 to Constellation; originating account(s), donor(s), and any connection to the Anthropic stake are not identified.”** Why: **“These are sponsor-level payment records; they do not establish account migration or ownership.”** Retain other supported grantee totals with the same limitation. |
| ST108 | Why's unqualified “NPT has no METR or ARC line” loses the filing window. | Replace with **“No METR- or ARC-named grantee appears in the reviewed NPT FY2023–FY2025 Schedule I lists.”** Describe the listed grants as NPT grants, without assigning donor accounts. |
| ST109 | Claim still includes SVCF calendar-2024 RAND $2M matched to a Coefficient award dated May 2, 2025; nineteen examples conflict with Why's eighteen. “Prove” overstates amount matches. Source `/grants/` 404. | Remove the **RAND $2M comparison from this block's match list** (do not delete the underlying CSV grant row). State **“18 temporally compatible same-recipient, same-amount comparisons are consistent with the documented external-partner payment arrangement; they do not identify account principals or prove each transaction's attribution.”** Cite the saved index and sponsor filings. |
| ST111 | Source URL points to the August 26 reply, not the July 23 root quoted in Claim. The saved thread contains both. | Source: **`https://bsky.app/profile/moskov.goodventures.org/post/3mrdb7fhfqs2w`** for the July 23 statement; retain the thread capture as supporting context. |
| ST113 | Omits the April 12 correction. Why claims “foundation” must cover more than GVF by comparing statements nine months apart. | Add: **“On April 12 he corrected this: not all, though still most, of the $20B was in the foundation.”** Why: **“The statements do not specify a legal entity or establish the location of the Anthropic stake; comparing different dates does not establish a DAF allocation.”** Add the correction post `3mjbdjoiydc2a`. |
| ST114 | Requested October 1 Wayback URL resolves to an actual September 27 capture. | Cite **`https://web.archive.org/web/20240927040853/https://www.openphilanthropy.org/how-to-apply-for-funding/`** and label the capture **September 27, 2024**. The account-name quotation is supported, but it does not locate the donated stake. |
| ST115 | Why falsely says the file has “no Moskovitz” and concludes that the trust route is private/unreadable. The 98,802-row file has two unrelated Moskovitz name matches; no identified Dustin/Cari family trust was established. | Why: **“No identified Dustin Moskovitz/Cari Tuna family trust was found in the checked 2022 SOI extract. That does not determine the trust's legal form, other-year filing status, or current holdings.”** Cite the saved dataset/hash and distinguish unrelated matches. Remove `sit-2022.csv` from clean narrative if enforcing the no-filenames requirement. |
| ST116 | Claim says approximately $170M twice. Why says $50M **and** $146.9M, although $50M is included in that sum. | Claim and Why: **“The seven listed NPT FY2025 grants total $146,860,783, including $50,000,000 to Coefficient Giving Advisors. This identifies recipient payments, not their underlying donors or an Anthropic-share route.”** Remove both approximately-$170M occurrences and do not add the $50M again. |
| ST117 | Why turns a selling-stockholder table into proof of an earlier private-unit holding. | Why: **“The 2021 Blue Owl selling-stockholder table names these family vehicles and Good Ventures Foundation; it does not identify the purchaser or recipient of the Anthropic stake.”** Use the saved S-1 for the blocked SEC URL; omit the unsupported private-unit inference. |
| ST121 | Threshold truncated to $303,073,355; Why says Schedule B must be publicly inspectable without the identifying-information exception or limits on issuer disclosure. | Use **$303,073,355.54**, with **$303,073,356** the first whole-dollar amount strictly above it. State that the special reporting threshold applies when its conditions are met; donor names/addresses and other information clearly identifying the donor may be withheld from public inspection. **Asset class/value/date do not guarantee an issuer name or identify the stake's sponsor.** |
| ST124 | Claim's “no public statement on the Anthropic stake” contradicts the Tuna interview used in ST33. “No Bluesky” is an unbounded identity-search negative. | Remove those categorical negatives. Keep **“GVF lists Tuna as president/board chair/director; Coefficient's current governance page names her Board of Managers chair and lists Moskovitz as a manager.”** If relevant, say **“No additional statement was found in the specifically reviewed sources as of September 14, 2026.”** |
| ST127 | “METR's parent” is outdated; ADV alone does not prove ARC directorship; clean text retains `people.csv`. | Claim/Why: **“VARA co-owner Benjamin Hoskin appears as a board member in ARC's FY2024 filing; ARC is METR's former parent.”** Cite that ARC return alongside the saved ADV. Remove the CSV parenthetical from the clean prose. |
| ST140 | Source is a local XML path rather than a Source URL. | Explicitly label it **“Saved source: research/990pf-goodventures-202501349349105365.xml, IRS object 202501349349105365, FY2024.”** Add the recorded download URL when rebuilding the source field; the existing saved XML itself resolves and supports the amount. |
| IV01 | Claim includes an unverified ~$623M post-money estimate absent from Anthropic's release. | Replace valuation clause with **“Anthropic did not disclose a post-money valuation in this announcement.”** Keep the $124M raise, date, and issuer-named investors. |
| IV02 | Source releases do not support all individual dollar allocations ($10M Ellison/$40M Singh) or an exact implied post-money value. “Same early investors” can imply every Series A participant returned. | Keep the **$580M announced round** and named participants; separately attribute the approximately $500M FTX/Alameda purchase and approximate dilution data to the cited bankruptcy reporting/filing. Omit unsupported individual allocations or add their actual source. Say **“Tallinn, McClave and CERR also participated.”** Do not turn an approximate equity fraction into an issuer-stated valuation. |
| IV05 | Secondary sale described as “Anthropic ... $884,000,000 raised”; approximate aggregate printed as exact dollars; linked article is blocked. | Claim: **“FTX estate secondary sale reported March 2024: approximately $884M of estate proceeds, not capital raised by Anthropic. The retained exhibit totals $884,109,327 for 29,465,891 shares; Jane Street's line is 3,332,833 shares for $99,999,988.”** Add the court exhibit cited in ST20–ST21. Treat the implied ~$18B valuation as analysis or omit it. |
| IV06 | Same secondary-sale/raise confusion. Retained linked article says over $450M, not exactly $452,000,000; ~$18B post-money is not a new priced round. | Claim: **“The FTX estate's remaining-share sale, reported June 1, 2024, generated over $450M, with approximately 15M shares at about $30; the article reports G Squared bought 4.5M shares for $135M.”** Use a specific filing if retaining a more precise aggregate. Delete the automatic “raised; post-money” template for this row. |
| IV07 | Claim's roughly-$1B Lightspeed allocation is absent from the cited issuer release. Why assumes the March round valuation was in force on an unknown exact early-2025 transfer date. | Omit the individual allocation absent a supporting source. Why: **“The March 3, 2025 Series E set a $61.5B post-money valuation; the exact stake-transfer date is not established.”** |
| IV11 | Template appends “raised” to a prospective, reported IPO target. | Claim: **“WSJ reported September 12, 2026 that a prospective IPO could raise up to $100B at around a $2T valuation; this was not a completed financing.”** Cite the saved article for the live 401 response. |
| M120 | Source is a prose description of a saved PDF, not its issuer URL. | Add **`https://coefficientgiving.org/research/were-urgently-scaling-our-work-on-ai-and-biosecurity/`** (GET 200) and retain the saved September 9 PDF/text. Claim/Why's recommendation measure and >$70M amount are supported. |
| TB02–TB04 | Three live grant URLs 404; no archived grant-page URL is supplied in these rows' notes. | Cite the saved **September 11, 2026 issuer-index records** and the row-note lineage `01-tarbell-bylines/research/funding.csv` **F002/F003/F004**. Do not invent archived grant-page URLs. The existing component blocks suffice to recompute $5,291,930; stating that exact aggregate alongside the existing approximate total would be helpful, not a separate citation requirement. |
| TB05 | Why says “paid via Players Philanthropy Fund,” contrary to the row's “Recommendation, not a disbursement.” | Why: **“SFF recommended $520,000 in 2024 for Tarbell Fellowship, with Players Philanthropy Fund listed as the receiving charity; disbursement is not established.”** |
| RW58 | “No ... web page” / “no page” turns a searched-source absence into a universal negative and suppresses the row's self-identification context. | Claim/Why: **“The reviewed METR/Redwood web pages did not name the full subcontracted staff or terms as of September 14, 2026; Greenblatt publicly identified his participation, and Anthropic's announcement names METR.”** Retain RW36's separate Redwood statement. |
| J02 | Source is an absolute path to another pack; five-year filing conclusion is not reproduced by the purported XML captures inspected here. | Source: link the Anthropic Series A/B releases plus the exact substantive BEMC filing copies checked. Claim/Why: **“BEMC was not found as a METR donor in the specified checked records.”** Do not claim all FY2020–FY2024 filings unless five valid returns and the grant search are supplied; the five existing `.xml` captures are not XML. |
| J08 | Absolute local funding-round CSV is the only Source; it does not provide accessible primary support for both parts. | Source: **`https://metr.org/about`** and the **May 28, 2021 Anthropic Series A announcement**. These directly support Schmidt Sciences as named supporter and Schmidt as named investor. |
| B05 | Source includes an absolute external raw-index path. | Keep the resolving METR/Gleave/FAR sources; identify the saved issuer-index snapshot reproducibly. Optionally expose the full CSV row's supported **“$59,347,676 across 18 awards dated October 2021–September 2025”** and its M15–M32 mapping in the public block. |
| K01 | Why adds “unbooked,” which neither the source statement nor row quantification establishes. | Why: **“METR reports significant free tokens from unnamed frontier AI companies; the quoted statement gives no quantity or dollar value.”** Do not infer accounting treatment from unquantified source prose. |
| S13 | September is treated as an established joining month; source is a September 10 press report, while the September 2 primary announcement says “last week.” | Claim: **“On September 2, 2026, Joe Benton announced he had left Anthropic to join METR for embedded AI-risk assessment.”** Add **`https://x.com/JoeJBenton/status/2095179369966960905`** and the saved substantive API payload. Keep NBC as corroboration. |

These are recommendations for Claim/Why/source cells and the builder's row-specific overrides. If implemented later, preserve each old value in a note exactly of the seed's form `audit-4 2026-09-14: was <old>`; do not delete rows. The current bibliography has not been silently regenerated or corrected during this audit.

### URL failures and retained alternatives

The 68 distinct Source URLs returned **50 × 200, 11 × 403, 5 × 404, 2 × 401**. Multiple URLs per block were checked separately. Source alternatives below are saved documents or archive routes actually identified in the rows/source records; absence of an archive link is reported, not filled with a guessed Wayback timestamp.

| Affected block(s) | Current response / source issue | Retained alternative and exact action |
|---|---|---|
| ST94, ST100, ST103 | IRS `/pub/epostcard/990/xml/2026/` redirects to IRS 404 | ST94 notes identify `irs-anthropic-scan/hits.csv` and context files. ST100 notes identify the two `990pf-goodventures-*.xml` extracts. ST103 notes identify `daf-sponsors/` and IRS batches. Link these specific saved records and their register; a dead directory is not a source document. |
| ST109 | Coefficient `/grants/` 404 | Notes identify the September 11 index and `daf-sponsors/` returns. Use those exact records for the eighteen revised comparisons. No archived landing-page URL in the row notes. |
| TB02, TB03, TB04 | `/grants/general-support-3/`, `/general-support-49/`, `/operating-costs/` all 404 | Row notes point to F002/F003/F004 in the funding CSV. The saved issuer-index amounts/dates were rechecked directly. The notes supply no individual Wayback grant-page alternative. |
| ST91 | Forbes US original 403 | Notes identify Wayback **20251107132055** and `agents-2026-09-14/S11-stakes/docs/forbes-us-2025-11-07-tuna.txt`. Use that archive of the exact US URL; ST32–ST33's AU reprint also returns 200 but has a different publication date. |
| ST92 | Forbes April reranking 403 | Notes identify Wayback **20260421043155** and `moskovitz-words/forbes-2026-04-20-true-net-worth-wayback-20260421043155.html` / `.txt`. |
| ST95 | SEC Meta proxy 403 | Notes identify `sec-proxies/meta-2020-def14a.htm` and the 2015 comparison. |
| ST96 | NYT September investor article 403 | Notes identify `press-pdfs/nyt-2026-09-03-anthropic-ipo-investors.pdf`. Preserve it as the read source; no public archived alternative is given in the row notes. |
| ST97 | WSJ Jane Street article 401 | Notes identify `press-pdfs/wsj-2026-06-20-jane-street-ai.pdf`. Do not treat authentication failure as evidence that the claimed holding is absent. |
| ST99 | SEC company search 403 | Notes identify the saved `sec-filings/` Asana/Meta/Kodiak/Apercen documents. A browse query is not a substitute for citing the individual dated filings. |
| ST101 | SEC fund company search 403 | Saved initial/amended Form Ds are in `audit3-evidence/sec/vara-form-d-initial.xml`, `vara-form-d-amendment.xml`, and `vara-form-d-2026-06-15.xml`; row notes describe the submissions/primary-document retrieval. |
| ST102 | SEC 13F browse query 403 | Notes identify `sec-filings/vara-13f-hr-2025-08-14.xml`, `...2026-02-17.xml`, `...2026-08-17.xml`. Parsed totals are $4,734,560,970; $9,944,995,059; $40,111,386,090. |
| ST117 | SEC S-1 403 | Retained substantive copy: `audit3-evidence/sec/st117-blue-owl-s1.html`. The row notes supply the S-1/table context but no separate archive URL. |
| IV05 | The Block March article 403 | Substantive court exhibit `audit3-evidence/investors/ftx-DI-10241-1.{pdf,txt}`; primary URL in ST20–ST21: `https://storage.courtlistener.com/recap/gov.uscourts.deb.188450/gov.uscourts.deb.188450.10241.1.pdf`. IV05's own short note supplies no archive URL. |
| IV06 | The Block June article 403 | `agents-2026-09-14/S11-stakes/docs/wb-theblock-ftx-sale2.{html,txt}` contains the substantive June 1 story. IV06's own note supplies no archive URL. Its text supports **over $450M**, not the block's exact $452M. |
| IV11 | WSJ IPO story 401 | Row note identifies `press-pdfs/wsj-2026-09-12-anthropic-boss-warns-slow-the-pace.txt`. Preserve “could” and “reported,” not “raised.” |
| RW33 | OpenAI blog 403; its separate PDF URL 200 | The same Source field's PDF resolves and supports the METR/Redwood clause. Saved `openai-hf-incident-technical-report-2026-08.{pdf,txt}` is a substantive alternative. |
| ST118 | Live Stratechery 200 but paywalled | Row notes identify Wayback **20251020103508** and `moskovitz-words/stratechery-2025-10-20-moskovitz-wayback-20251020103508.html`. The saved full transcript, not the paywall response, supports the quotation. |
| ST104, ST125, ST127 | HTTP 200 does not by itself supply the numeric/board evidence | ST104 requires its NPT return; ST125 requires the saved ADV PDF/text; ST127 additionally requires the ARC return. Preserve these document-level sources. |
| ST140, M120, J02, J08; local component of B05 | Non-HTTP source fields/components | Resolve and label the saved XML/PDF where available; replace absolute external-pack paths with the primary URLs and stable source records specified in the failures table. |

### Per-block disposition (75 of 75)

`C/W` are Claim / Why verdicts. `P` means supported, `F` requires the exact fix above. Source column records live status or a content/location defect; it is not a claim that 200 proves the fact. All blocks match the clean-file transformation; `D` identifies remaining explicit CSV filenames under the seed's stricter “minus CSV names” requirement. The generic clean-file header is separately noted in Task 3.

| ID | C/W | Source check | Clean-copy issue / result |
|---|---|---|---|
| ST26 | P/P | 200, issuer Series H | P |
| ST32 | P/F | 200 AU; add US date/archive | P |
| ST33 | P/P | 200 AU; full quotation and US provenance in CSV | P |
| ST41 | F/P | 200; source attribution chain differs | P |
| ST49 | F/P | 200; dated family-vehicle acquisition only | P |
| ST54 | P/P | 200 Series A; add sources for joined clauses | P |
| ST78 | P/F | 200 ZIP; substantive extracted filing checked | P |
| ST79 | P/P | 200 ZIP; 406 issuers/categories checked | P |
| ST89 | P/F | 200; saved author payload used | P |
| ST90 | P/F | 200; saved author payload used | P |
| ST91 | F/P | 403; saved US Forbes | P |
| ST92 | P/F | 403; saved April Forbes | P |
| ST93 | P/P | 200; author self-statement retained as such | P |
| ST94 | F/F | 404 directory; local scan records | D: index CSV names |
| ST95 | P/F | 403; saved proxies | P |
| ST96 | P/F | 403; saved NYT | P |
| ST97 | P/P | 401; saved WSJ | P |
| ST98 | P/P | 200; source-language statement/translation checked | P |
| ST99 | F/P | 403; saved individual filings | P |
| ST100 | P/P | 404 directory; saved FY2024/FY2025 XML | P; explicit total-assets field would clarify provenance |
| ST101 | F/P | 403; saved initial/amended Form Ds | P |
| ST102 | P/P | 403; three 13F tables checked | P; clarify entry counts |
| ST103 | F/F | 404 directory; 18 saved returns | P |
| ST104 | P/P | 200 policy page; numeric source missing from URL field | P |
| ST105 | P/P | 200, redirects to issuer's current process page | P |
| ST106 | P/P | 200, Schedule D redirect resolves | P |
| ST107 | F/F | 200; aggregate grant supports no migration claim | P |
| ST108 | P/F | 200; three local Schedule I lists | P |
| ST109 | F/F | 404; invalid dated match remains | P |
| ST110 | P/P | 200; saved author post exact | P |
| ST111 | P/P | 200 but wrong post; root URL also verified 200 | P |
| ST112 | P/P | 200; saved author post exact | P |
| ST113 | F/F | 200; correction in saved thread / separate post | P |
| ST114 | P/P | 200, actual capture September 27, 2024 | P; correct capture date |
| ST115 | P/F | 200 landing page; 98,802-row saved dataset checked | D: dataset CSV name |
| ST116 | F/F | 200; exact seven-grant sum recomputed | P |
| ST117 | P/F | 403; saved S-1 checked | P |
| ST118 | P/P | 200 paywall; saved Wayback transcript checked | P; figure quote truncation differs |
| ST121 | F/F | 200 IRS instructions; public-inspection exception matters | P |
| ST124 | F/P | 200 governance page | P |
| ST125 | P/P | 200 app; saved ADV is substantive evidence | P |
| ST127 | F/F | 200 ADV app; add ARC filing | D: people.csv |
| ST140 | P/P | Local XML exists; not HTTP URL | P |
| IV01 | F/P | 200 issuer; no source for ~$623M estimate | P |
| IV02 | F/F | Both URLs 200; remove unsupported allocations | P |
| IV05 | F/P | 403 article; substantive court exhibit checked | P |
| IV06 | F/P | 403 article; saved article gives over $450M | P |
| IV07 | F/F | 200 issuer; no transfer date / $1B allocation | P |
| IV08 | P/P | 200 issuer; $13B/$183B/date/investor list | P |
| IV09 | P/P | 200 issuer; $30B/$380B/date/D.E. Shaw | P |
| IV10 | P/P | 200 issuer; $65B/$965B/date/Amazon component | P |
| IV11 | F/P | 401; saved prospective IPO reporting | P |
| M75 | P/P | 200 METR About; individuals, not firm | P |
| M120 | P/P | Source prose; actual issuer URL independently 200 | P |
| M139 | P/P | 200 Macroscopic grants page | P |
| M140 | P/P | 200 Macroscopic grants page | P |
| M141 | P/P | 200, explicitly listed impact investment | P |
| M142 | P/P | 200, explicitly listed venture-arm investment | P |
| G14 | P/P | 200, dated Barnes comment | P |
| TB02 | P/P | 404; issuer-index amount/date matched | P |
| TB03 | P/P | 404; issuer-index amount/date matched | P |
| TB04 | P/P | 404; issuer-index amount/date matched | P |
| TB05 | P/F | 200 SFF recommendation, not payment | P |
| TB06 | P/P | 200; $200K conditional match included | P |
| RW31 | P/P | Both URLs 200; substantive API quote | P |
| RW32 | P/P | 200 METR report | P |
| RW33 | P/P | PDF 200 / blog 403; PDF supports claim | P |
| RW34 | P/P | Both URLs 200; Redwood cross-post/byline | P |
| RW36 | P/P | Both URLs 200; substantive API quote | P |
| RW58 | F/F | Three URLs 200; bounded search only | P |
| J02 | F/F | Absolute CSV path; five-return proof inadequate | D: source CSV name |
| J08 | P/P | Absolute CSV path; both primary alternatives verified | D: source CSV name |
| B05 | P/P | Four URLs 200; local raw-index component nonportable | P; full CSV row supplies amount/date span |
| K01 | P/F | 200 METR; accounting inference unsupported | P |
| S13 | F/F | 200 NBC; primary post indicates prior-week departure | P |

Claims marked P here are assessed at their stated attribution: a person's statement, a journalist's report, or a filing entry is not converted into proof of a hidden account's ownership. Cross-row connections such as “METR supporter” require the accompanying METR/issuer evidence in Task 1. No block establishes motive, coordination, or wrongdoing.

## Task 6 — layout table on the current PNG

All coordinates below are SVG coordinates; the measured transform above converts them to CSS coordinates and multiplication by 2 gives PNG coordinates. **This table uses the later, recovered PNG**, identified by its hash above. Node ownership was assigned from the actual sequence of a node's title/subtitle elements, not merely by whether a text box happens to lie inside a rectangle. The custom Anthropic panel and the three card boxes were checked separately; none has a foreign-label intersection. [Updated node measurements](audit4-evidence/recovery-check-1/node-heights.csv), [updated collisions](audit4-evidence/recovery-check-1/label-collisions.csv), [complete updated text geometry](audit4-evidence/recovery-check-1/layout.json).

| Node | Box `(x,y,w,h)` | Subtitle lines | Required `lines×21+62` | Margin | Verdict |
|---|---|---:|---:|---:|---|
| Coefficient Giving | `(400,148,300,215)` | 7 | 209 | +6 | PASS after cleanup |
| Good Ventures Foundation | `(400,410,300,190)` | 6 | 188 | +2 | PASS after cleanup |
| Jaan Tallinn / SFF | `(400,635,300,110)` | 2 | 104 | +6 | PASS after cleanup |
| Audacious Project | `(400,775,300,290)` | 11 | 293 | −3 | FAIL |
| DAFs and regrantors | `(400,1090,300,215)` | 7 | 209 | +6 | PASS |
| Alignment Research Center | `(1130,50,340,125)` | 3 | 125 | 0 | PASS |
| RAND | `(1130,240,340,185)` | 5 | 167 | +18 | PASS |
| Longview | `(1130,460,340,110)` | 2 | 104 | +6 | PASS |
| FAR AI | `(1130,660,340,110)` | 2 | 104 | +6 | PASS |
| Redwood | `(1130,860,340,150)` | 5 | 167 | −17 | FAIL |
| Constellation | `(1130,1060,340,110)` | 2 | 104 | +6 | PASS |
| METR | `(1760,380,290,180)` | 3 | 125 | +55 | PASS |
| Tarbell Center | `(1430,1190,300,150)` | 4 | 146 | +4 | PASS |
| Anthropic custom panel | `(30,60,200,1270)` | 59, all nonempty | 1301 | −31 | Still fails the stipulated formula by 31px, although actual 13px text/16px spacing fits: last text bottom 1125.01, box bottom 1330. |

The formula is a conservative requirement; failure does not by itself mean every final glyph visibly crosses the box edge. The two remaining standard-node failures should be corrected by deriving their required height from cleaned wrapped text. The custom panel still exceeds the seed's stipulated formula, though by less than before; its different line spacing is not itself authorization to waive that rule.

| Foreign label | Text bounding box `[left,top]–[right,bottom]` | Box overlapped | Overlap rectangle |
|---|---|---|---|
| Group-header `recommends` | `[400.00,133.94]–[475.05,149.01]` | Coefficient | `[400.00,148.00]–[475.05,149.01]` |
| `$5.6M 2022–24 SFF recs → ARC / ARC Evals` | `[686.88,526.53]–[1043.51,545.62]` | Good Ventures | `[686.88,526.53]–[700.00,545.62]` |
| Red `Direct: none found...` annotation | `[720.00,31.92]–[1813.49,52.02]` | ARC | `[1130.00,50.00]–[1470.00,52.02]` |
| `board seat (Gleave); no grant on record` | `[1306.81,566.93]–[1625.90,586.02]` | Longview | `[1306.81,566.93]–[1470.00,570.00]` |
| `office; no grant on record` | `[1465.84,960.53]–[1672.55,979.62]` | Redwood | `[1465.84,960.53]–[1470.00,979.62]` |

Additional clipping: the free-token caption spans approximately **`[1634.33,587.94]–[2175.68,603.01]`**. With the actual screen transform its right edge is about CSS x=2230.13, beyond the SVG viewport's x=2178 right edge; `overflow` is `hidden`. About 52 CSS pixels of its right end are clipped. Wrap it or move it left, then remeasure.

The three card boxes are `(1040,1402,320,480)`, `(1375,1402,320,480)`, `(1710,1402,320,480)`. Their final text bottoms are 1715.01, 1731.01, and 1788.01 respectively, all within bottom 1882. The footnote ends at CSS y=2544 on a 2560px canvas. There is no whole-page overflow.

The initial Tallinn→METR path had length zero, so its initial clearance was not measurable. In the recovery check it has length **1097.62 SVG units**. Sampling 20,001 points along it gives approximately **19.01 units of stroke-edge clearance** from Longview's rectangle, after subtracting half the 7.1-unit stroke width. This is a sampled measurement, not an analytic minimum. All 31 path lengths are now positive.

## Task 7 — framing

No current figure sentence explicitly accuses a named person of wrongdoing or coordinated action. Card 1 attributes the stated conflict-perception purpose to Tuna through Forbes; it does not establish an independently discovered motive. Card 3's disclaimer is present. The diagram still needs the following framing corrections:

- **Title:** replace the current-value assertion with a conditional, dated ceiling. Bound the direct-grant negative to Coefficient's September 11, 2026 index and GVF filings through June 2025. Distinguish “Good Ventures Foundation” from the speaker's undefined “GV” or “our foundation.”
- **Subtitle/group header/blue legend:** do not place unidentified SVCF/NPT accounts under the couple's ownership or call them Good Ventures' funding partners. Coefficient names the sponsors as its external funding partners. The account principals remain unidentified in the checked sources.
- **Anthropic panel:** replace BEMC's categorical non-donor assertion with a specified-record negative. Change “parent ARC” to “former parent ARC.” Replace a dated acquisition reported by Forbes with appropriately dated wording, not present-tense ownership.
- **Chart/cards:** do not imply measured 15-fold appreciation from an estimate and a conditional ceiling. Include the $20B correction, and mark the truncated Stratechery passage. “No private stock” must specify direct reported contributions rather than excluding indirect investment exposure.
- **Bibliography:** ST107's account-migration statement, ST113's inferred legal-entity definition, ST115's private/unreadable conclusion, and the other overclaims above must not be allowed to supply certainty that the figure's own caveats withhold.

## Figure text recommendations

1. Preserve the concurrently implemented ID-removal repair: **only human-readable strings, before wrapping them into SVG text elements; never tag attributes**. The recovery check confirms all SVG paths restored and the six punctuation residues and six empty panel text elements removed. This audit session did not implement or overwrite that repair. Recheck generated artifacts after the separate ID-inventory recovery finishes.
2. Suggested title: **“Some funders connected to METR are also Anthropic investors. Moskovitz says his stake was donated; applying Forbes's percentage bound to Anthropic's May 2026 valuation gives a ceiling below $7.72B. The records checked do not identify the receiving account.”** Put the separately bounded direct-grant finding beside its annotation.
3. Suggested funding header/legend clause: **“Moskovitz/Tuna philanthropy and Coefficient's funding partners. Coefficient recommends grants; its own grantmaking entity or external partners, including GVF, SVCF and NPT, separately approve grants. The reviewed sources do not identify the SVCF/NPT account principals.”** Visually keep unidentified accounts outside a family-ownership bracket.
4. Suggested direct annotation: **“No METR-named grant found in Coefficient's 2,911-row index (September 11, 2026) or GVF filings through June 2025; unlisted or later gifts are not excluded.”** Add the actual supporting rows to the bibliography/comment.
5. Make the bibliography complete by registering the omitted monetary inputs, M33/M104, M57–M63, M117–M119/M143/AP47/AP49, M126–M128, and TO01–TO06. Existing TB component blocks, B05's full row and ST33's complete CSV quotation already support their respective totals/quote; do not mislabel these as missing facts. Explicit aggregate blocks and source fields can improve readability but are not substitutes for the actual inputs. Add an evaluation or office source for unreferenced relationship claims. Rebuild both copies only after their Claim/Why/source corrections are reviewed.
6. Use **“$22.95M Coefficient awards”**, **“~$21M implied RAND remainder”**, **“GWWC reports a $220K recommendation in 2023; additional pooled funding undisclosed”**, and **“> $70M recommendation over two years”**. Keep SFF recommendation/match labels separate from Coefficient awards and all commitments separate from paid grants.
7. Chart: **“Forbes estimate published November 2025; transfer reported in early 2025”** and **“Conditional ceiling using the May 28, 2026 Series H valuation: < $7.72B”**. Use **“≈15× at the ceiling; not measured investment growth.”** State drawing scale in SVG units and exempt relationship/decorative paths.
8. Retain the verified Forbes attribution and typography; add the next-day correction to card 2 or drop its $20B excerpt; replace card 3's inserted final period with an ellipsis. Keep the corrected governance roles and the no-motive disclaimer.
9. Tarbell: **“Fellows' articles classified as AI using publisher tags or keyword fallback in outlet-specific captured windows; most windows are partial.”** Include the six exact ranges/completeness statuses in the bibliography, and cite those blocks from the figure's retained ID inventory. Do not imply editorial control or comparable full-year shares.
10. Resize the two remaining failing standard nodes, Audacious and Redwood; resolve the Anthropic panel's remaining 31px formula shortfall; reposition the five colliding labels; wrap the clipped token caption. Replace **“unbooked and unquantified”** with **“unquantified in METR's statement”**, **“BEMC is not a METR donor”** with a dated searched-record negative, and **“Sep 2026”** for Benton's move with **“announced September 2, 2026.”** Verify the corrected render, not just the generator's strings.

## Completion check

Final snapshot verification at **2026-09-14 21:44:57 UTC** confirmed the recovery-check HTML/PNG hashes above still match the files on disk. The per-fact table covers all 257 original visible-string indices; all 250 updated strings were compared against them. The per-block table contains exactly the 75 distinct IDs in the unchanged bibliography, with no missing or extra block. Every local report link resolves. All 17 monetary-path width attributes match the formula rounded to one decimal, and all 31 recovered paths have positive lengths. Recovery of any additional IDs after this snapshot is not certified by this report.

From `/mnt/f/projects/memes/ai-machine/10-metr`, the prescribed `python3 scripts/audit.py` completed with **exit 0**. Its exact last line:

```text
figures=29 pngs=29 row_ids_in_research=2214 cited=1069 missing=0
```

This script tests row-ID existence and PNG presence across the parent pack; it does **not** verify source truth, expanded-range coverage, bibliography completeness, SVG validity, quotation fidelity, or layout. Its required pack-wide sanity check is not an audit of other figures. A zero exit cannot override this report's **FIX** verdict.
