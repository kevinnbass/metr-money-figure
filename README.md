# METR money figure — "Money that doesn't show up, with Anthropic", and ten companion figures

One figure, and everything under it: the funders that reach METR (Model Evaluation and Threat Research) through its parent, its joint-project partner, its pooled-fund donor, a board member's organization, its contractor, its office and a journalism fellowship; the same funders' Anthropic equity; and the donated Moskovitz stake whose location no public filing identifies.

- `figures/metr-01b-money-that-doesnt-show-up-with-anthropic.{html,png,jpg}` — the figure (10a-anthropic).
- `figures/metr-01-money-that-doesnt-show-up.{html,png,jpg}` — the companion without the Anthropic panel (10a).
- `NOTES.md` — the full coverage notes the figure used to carry as its footnote. Read this before quoting a number.
- `research/*.csv` — every row the figure cites, by row id (money_flows M…, stakes ST…, investments IV…, audacious-partners AP…, budget G…, tarbell_funding TB…, tarbell_outlets TO…, redwood RW…, shared_donors J…, board B…, compute_inkind K…, staff_origins S…). Each row carries its source URL, a verbatim quote and a note.
- `research/STATE.md` — the consolidated open-question list, including where the donated stake could sit and what would settle it.
- `research/AUDIT-3A.md` … `AUDIT-3D.md` — four independent audits of this figure run on 2026-09-14 (money pipes; Anthropic and the stake; Canary and Tarbell; framing and layout), with their seeds `AUDIT-SEED-3*.md`. Their verdicts were applied to the figure in v0.44.
- `evidence/` — primary documents: Good Ventures Foundation's FY2024 and FY2025 Forms 990-PF (IRS e-file XML, Schedule B included), Coefficient's 2024 returns, SEC filings, Moskovitz's public statements (Bluesky API payloads, Stratechery archive), the audit evidence registers, and the agent review reports.
- `MANIFEST.csv` — path, size and SHA-256 for every evidence file, including the ones too large for the repo (the DAF-sponsor e-files, 436 MB; the IRS TEOS PDFs, 74 MB; large audit captures). Those are IRS public files; the manifest gives the object ids so anyone can pull them from `apps.irs.gov/pub/epostcard/990/xml/` and check the hash.
- `timestamps/` — a SHA-256 manifest of every tracked file in this repo, timestamped against the Bitcoin blockchain with OpenTimestamps. It shows the data here is at least as old as the stamp and has not been altered since, without asking anyone to trust the author, GitHub or a commit date. `timestamps/README.md` has the commands that check it; `scripts/verify_timestamp.py` checks it without a Bitcoin node.
- `scripts/` — the render code. `generate.py` holds the whole pack's figures; this figure is `fig_money(anth=True)`. Rendering needs Python 3, Playwright with Chromium, and the research CSVs in place:

```
python3 scripts/generate.py metr-01b-money-that-doesnt-show-up-with-anthropic
python3 scripts/audit.py   # checks every cited row id exists
```

## Figures in this repo

| file | rows cited | title |
|---|---:|---|
| `figures/metr-01-money-that-doesnt-show-up.png` | 21 | Good Ventures Foundation, advised by Coefficient, has no METR grant on its books. Its grants reached METR's parent, partner, pooled donor and a board member's organization; ARC handed METR $4.55M at the spin-out, not attributable to any one ARC funder |
| `figures/metr-01b-money-that-doesnt-show-up-with-anthropic.png` | 75 | Funders that reach METR through ARC, RAND, Longview and pooled funds include Anthropic's Series A investors, two of them its board observers by their own account; Moskovitz donated a stake now worth up to $7.7B to what he calls "our foundation", and no filing checked shows where it sits; Good Ventures has no METR grant on its books |
| `figures/metr-07-who-gets-ordained.png` | 22 | Who gets ordained: 22 documents on a "FINRA for AI", and the only ones that say METR are a podcaster, Dario Amodei and David Sacks |
| `figures/metr-10-barnes-in-time-by-a-tarbell-fellow.png` | 15 | Both TIME100 AI profiles of METR's CEO were written by a fellow of a journalism program that Coefficient funds; neither told readers so |
| `figures/metr-11-same-donors-both-sides-of-the-table.png` | 19 | Same donors, both sides of the table: METR's funders who also hold a piece of the labs it evaluates |
| `figures/metr-12-ten-million-to-seventy-one.png` | 19 | METR raised $71M in the six months the evaluator's seat was being designed; the investigations came after the money, not before it |
| `figures/metr-13-the-subcontractor.png` | 41 | The investigator's subcontractor: Redwood's board held the funder's co-CEO, Anthropic's future trustee and METR's future staffer |
| `figures/metr-14-the-independence-fight.png` | 195 | "Stop pretending METR is independent": Amodei names it, Altman signs on, Sacks objects, no METR reply found |
| `figures/metr-15-the-candidates.png` | 24 | The candidates: of twenty possible evaluators, nine hold Coefficient awards, one refuses lab money, and the three put forward this week were METR, Stanford and Hugging Face |
| `figures/metr-17-the-vanguard-channel.png` | 4 | The Vanguard channel: donor-advised money to the AI-safety cluster grew from $8M to $66M in the year of Anthropic's first tender offer, and no filing says whose it is |
| `figures/metr-18-the-argument-vs-the-ledger.png` | 131 | No direct Coefficient grant to METR appears in the checked index and filings; both sides argued over one anyway. The filings do show an ARC program transfer and a Coefficient award to METR's RAND partner |
| `figures/metr-21-metr-grades-itself.png` | 45 | METR graded its own independence in May 2026: two requirements answered "No", no conflict-of-interest policy, "at least 6" staff and collaborators with close personal ties to lab employees |

Every row id a figure cites resolves to a row in `research/*.csv`; `python3 scripts/audit.py` checks this for every figure in the pack.

## Rules the figure follows

- Every number traces to a row id in `research/`. No number is on the figure without one.
- Money types are never summed with each other: Coefficient awards, SFF recommendations, the Audacious commitment, filed DAF grants and equity values stay separate, and the legend says which is which.
- Pipe width is 6 px + 1.4 px per $1M, no cap. The Anthropic equity band is a ceiling (Forbes' "less than 0.8%" × the $965B Series H post-money valuation), not a valuation, and is drawn at 1/30 of that scale because at full scale it would be five canvases wide.
- Negatives are bounded: "none found" means none in the sources named, with their dates.
- The accounts at SVCF and NPT that pay Coefficient-recommended grants are unattributed. No public document names their principals or the recipient of the donated Anthropic shares. The figure says so wherever it touches them.
- No motive is asserted about any person or organization. Only public people acting in public roles are named.

## Dating this repo

A commit date is self-reported and can be set to anything; a git history can be rewritten and force-pushed. That matters more now that AI makes documents cheap to fabricate and files easy to alter without a trace. It cuts both ways: challenged numbers can be quietly retrofitted so the record looks like it always said the new thing, and inconvenient evidence can be dismissed as "probably generated after the fact" — an accusation that costs nothing to make and, absent an anchor, nothing can answer. This repo is a fair target for both, having been assembled with AI agents (see Disclosure).

So the tracked files are hashed into `timestamps/SHA256SUMS.txt`, and that manifest is timestamped with OpenTimestamps, which anchors it in the Bitcoin blockchain. From the repo root:

```
sha256sum -c timestamps/SHA256SUMS.txt        # the files still match the manifest
ots verify timestamps/SHA256SUMS.txt.ots      # when the manifest was stamped
```

The second command needs a local Bitcoin node, which is the preferred way to check it and the only fully trustless one. Without a node, `python3 scripts/verify_timestamp.py` does the same check through a public block explorer; that trusts the explorer for one public block header, which is a small assumption and cross-checkable against any other explorer.

Both passing means these files are at least that old and unaltered since, provable without trusting the author or any single company. It fixes *when*, never *whether*: it does not prove the contents are true, or human-written — accuracy is what `NOTES.md`, the row ids and the audits are for. Full method, including why this matters against AI-era fabrication, how to check a single figure, and how to re-stamp after new data, is in `timestamps/README.md`.

## Disclosure

Built by Kevin Bass (@kevinnbass), who has publicly criticized Anthropic and Coefficient Giving. Data collection and rendering were done with Claude Code (Anthropic) and audited with OpenAI Codex and xAI Grok agents; the audit reports and every agent's evidence are in this repo so the reader can check the work rather than trust the author or the tools. Corrections: open an issue with the row id.

## Version

v0.45, 2026-09-14. Changes are logged in the parent pack's CHANGELOG; the audits that shaped this version are in `research/AUDIT-3*.md`.
