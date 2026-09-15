# Timestamps

Proof of *when* the data in this repository existed, independent of anyone's word
for it — including ours. Anchored to the Bitcoin blockchain using
[OpenTimestamps](https://opentimestamps.org), an open, free, vendor-neutral
standard.

## Why this is here

Git commit dates are self-reported: whoever controls the repository can set them
to anything, and an entire history can be rewritten and force-pushed. That is fine
for development, but weak for an evidence corpus, where the natural challenge is
*"you assembled these numbers after the fact."*

A timestamp answers that challenge. It shows that these exact files existed at a
specific past moment, and it does so without asking anyone to trust the author,
GitHub, a commit date, or any single company or server.

### Why this matters more in the age of AI modification

Generative AI has made fabrication cheap and alteration invisible. A convincing
filing, screenshot, chart, quote or dataset can be produced in seconds, and
existing files can be edited without leaving any visible trace. The signals
readers used to rely on — it looks official, the formatting is right, it reads
like a real document — no longer carry weight, because every one of them can now
be synthesized on demand.

That erosion cuts in two directions, and a corpus like this one is exposed to
both:

- **Retrofitting.** Once a specific claim is challenged, numbers can be quietly
  adjusted and re-committed so the record appears to have always said the new
  thing. Git does not prevent this. Without an external anchor, "this file has
  always read this way" is unfalsifiable.
- **Blanket dismissal.** The mirror problem, and the more corrosive one. Because
  fabrication is now easy, *any* inconvenient evidence can be waved away as
  "probably AI-generated after the fact." That accusation costs nothing to make,
  and without a timestamp there is nothing that can answer it.

This repository is a fair target for both: it was assembled with AI agents, as the
disclosure in the root README states plainly.

A timestamp is what makes those two challenges answerable. It fixes a point in
time that no later party can move — not the author, not GitHub, not a hosting
company, not a model. Together with the manifest, it establishes that these exact
bytes existed by this date and have not changed since.

Be precise about what that does and does not settle:

- It **does** prove priority and integrity. The data predates whatever came later
  — a denial, a correction, a quietly edited source page, a deleted filing, a
  legal threat — and no one has retrofitted it in the meantime.
- It **does not** prove the contents are true, or human-written, or not
  AI-generated. Timestamping synthetic data only proves the synthesis happened
  early.

So the claim here is narrow and worth stating exactly: **it fixes *when*, never
*whether*.** Accuracy is what `NOTES.md`, the row ids in `research/*.csv`,
`MANIFEST.csv` and the audits are for. But "when, and unaltered since" is
precisely the property that lets a reader distinguish a record that was *kept*
from a story *assembled afterward* — and in an environment where nearly everything
else can be generated, verifiable time is one of the few things that still cannot
be.

## Files

| File | Role |
| --- | --- |
| `SHA256SUMS.txt` | SHA-256 hash of every git-tracked file, plus the git commit it was built from |
| `SHA256SUMS.txt.ots` | Timestamp proof committing to `SHA256SUMS.txt`'s exact bytes |

The chain has two links: the `.ots` proof commits to the manifest's bytes, and
the manifest commits to each file's bytes. So one small proof covers the entire
repository — enough to establish that **any** individual file already existed in
its current form at the stamped time. Changing any file, or backdating anything,
breaks one of the two hashes.

Scope is deliberately **git-tracked files only**, so the manifest describes
exactly what a clone of this repository contains — not local scratch files that
happened to be sitting in the working directory. The exact commit, file count and
build time are recorded in the manifest's own header:

```bash
head -20 timestamps/SHA256SUMS.txt
```

## How to verify

```bash
pip install --user opentimestamps-client
```

Then, from the repository root:

```bash
# 1. Do the files still match the manifest?
sha256sum -c timestamps/SHA256SUMS.txt

# 2. When was the manifest stamped?
ots verify timestamps/SHA256SUMS.txt.ots
```

Step 1 proves the files match the manifest. Step 2 proves the manifest is as old
as it claims. **Both passing means the files are as old as it claims** — neither
step alone is sufficient.

Keep the two files together and byte-exact. Re-generating or reformatting the
manifest — even changing a comment in its header — invalidates the proof.

To check a single file without hashing the whole repository, pull its line out of
the manifest:

```bash
grep 'figures/metr-01-money-that-doesnt-show-up.png' timestamps/SHA256SUMS.txt | sha256sum -c
```

### Which Bitcoin node checks the proof

`ots verify` confirms a proof by asking a **local Bitcoin Core node** over RPC. It
has no block-explorer fallback, so with no node running it stops with
`Could not connect to Bitcoin node` and exits non-zero. That reads like a bad
proof but only means it could not be checked. Point it at your node explicitly if
it is not on the default port:

```bash
ots --bitcoin-node http://user:pass@localhost:8332 verify timestamps/SHA256SUMS.txt.ots
```

**Your own node is the preferred way**, and it is the only one that is fully
trustless: it validates the chain itself and takes nobody's word for anything.

**Someone else's node will ordinarily suffice**, though, and is much better than
skipping the check. All an explorer is trusted for here is a *public block header*
— the merkle root and time of a block — which is identical across every honest
node on the network and cheap to look up in several places at once. An explorer
that lied would have to be corroborated by every independent one you try. That is
a real but small assumption, and a very different thing from trusting anyone about
the contents of this repo.

For anyone without a node, this does the same check via a public explorer:

```bash
python3 scripts/verify_timestamp.py
python3 scripts/verify_timestamp.py --explorer https://mempool.space/api   # cross-check
```

It confirms the proof commits to the manifest's exact bytes, then checks that the
merkle root the proof expects at each block height matches that block's real merkle
root, and prints the block times. Running it against two unrelated explorers and
getting the same answer reduces the residual trust to nearly nothing.

## Pending vs. confirmed

A fresh stamp is *pending*: the public calendar servers have committed to
including it, but it is not yet in a Bitcoin block, so `ots verify` prints
`Pending confirmation in Bitcoin blockchain` and exits non-zero. This is normal,
and the proof is not lost — the calendars are holding it.

Once it is mined into a block (usually a few hours, up to ~24h), fetch the
completed proof:

```bash
./scripts/timestamp.sh --upgrade          # rewrites the .ots in place, adding the Bitcoin attestation
python3 scripts/verify_timestamp.py       # should now print concrete block times
```

Upgrading matters: until it is done, verification depends on those calendar servers
still being online. Afterwards the proof stands on its own against the blockchain.
Commit the upgraded `.ots` — it grows by a few KB as the attestations are added.

`ots info timestamps/SHA256SUMS.txt.ots` lists the raw attestations. Pending ones
are kept alongside the confirmed ones, so seeing `PendingAttestation` after a
successful upgrade is normal and not a problem; what matters is that at least one
`BitcoinBlockHeaderAttestation` is present.

## Re-stamping after the data changes

A manifest describes one moment, so new data means a new pair rather than an edit.
The old proof remains valid for the contents it covered.

```bash
./scripts/timestamp.sh
```

The script refuses to overwrite an existing proof, and refuses to run with
unstaged changes to tracked files — that guarantees the manifest describes exactly
the bytes the next commit contains. To stamp a new revision, move the old
manifest and proof aside together (keeping superseded pairs gives a provable
revision history), then re-run.

Because `timestamps/` is committed alongside the data it covers, the manifest
records the commit it was built *from*; the manifest and proof land in the commit
immediately after. The manifest cannot hash itself or its own proof, so those two
paths are the only tracked files it excludes.

No separate archive of superseded proofs is kept, because git already is one. Each
manifest and its proof are consistent at the commit that introduced them, so an
earlier anchoring is checked by going back to that commit:

```bash
git checkout <commit> -- timestamps/
python3 scripts/verify_timestamp.py
```

### Earlier anchorings

| Commit | Anchored | Blocks |
| --- | --- | --- |
| `64a57d8` | 2026-09-15 01:30:16 UTC | 967051, 967053, 967098 |

That proof covers the same evidence — `research/`, `evidence/`, `figures/`,
`EVIDENCE.txt`, `MANIFEST.csv`, `NOTES.md` are untouched since — and was superseded
only because correcting this file's own text changed a file the manifest lists. It
remains the earliest date on record for the data itself.

## Privacy

`ots stamp` transmits only the manifest's 32-byte hash to the calendar servers. No
file contents, filenames, or per-file hashes leave the machine.
