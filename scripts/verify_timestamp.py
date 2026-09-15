#!/usr/bin/env python3
"""Verify this repo's OpenTimestamps proof without running a Bitcoin node.

The `ots verify` command needs a local Bitcoin Core node over RPC; it has no
block-explorer fallback, so without a node it stops at "Could not connect to
Bitcoin node" and exits non-zero. That reads like a bad proof but only means it
could not be checked.

This does the same check using a public block explorer instead of a node, so
anyone can confirm the date:

  1. the proof commits to the manifest's exact bytes, and
  2. for each Bitcoin block the proof names, the merkle root it expects matches
     that block's real merkle root.

Together those pin the manifest to the earliest block's time.

Your own node is the preferred way to check this -- `ots verify --bitcoin-node ...`
validates the chain yourself and asks nobody for anything. Someone else's node,
which is what this script uses, is a weaker but ordinarily sufficient substitute:
all it is trusted for is a public block header, and a lying explorer would have to
be corroborated by every other one. Cross-check with --explorer against an
independent API and the residual trust is small. Use a node if you have one; use
this if you do not, rather than not checking at all.

  python3 scripts/verify_timestamp.py
  python3 scripts/verify_timestamp.py --offline    # skip the network, just print
  python3 scripts/verify_timestamp.py --explorer https://mempool.space/api

Requires: opentimestamps-client  (pip install --user opentimestamps-client)
"""

import argparse
import datetime
import hashlib
import json
import pathlib
import sys
import urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = REPO / "timestamps" / "SHA256SUMS.txt"
PROOF = REPO / "timestamps" / "SHA256SUMS.txt.ots"
DEFAULT_EXPLORER = "https://blockstream.info/api"


def fetch_block(explorer, height, timeout):
    """Return (merkle_root, unix_time) for a block height, via an explorer."""
    with urllib.request.urlopen(f"{explorer}/block-height/{height}", timeout=timeout) as r:
        block_hash = r.read().decode().strip()
    with urllib.request.urlopen(f"{explorer}/block/{block_hash}", timeout=timeout) as r:
        block = json.load(r)
    return block["merkle_root"], block["timestamp"]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true",
                    help="do not contact an explorer; print what the proof claims")
    ap.add_argument("--explorer", default=DEFAULT_EXPLORER,
                    help=f"Esplora-compatible API base (default: {DEFAULT_EXPLORER})")
    ap.add_argument("--timeout", type=float, default=30.0, help="network timeout, seconds")
    args = ap.parse_args()

    try:
        from opentimestamps.core.notary import (BitcoinBlockHeaderAttestation,
                                                PendingAttestation)
        from opentimestamps.core.serialize import StreamDeserializationContext
        from opentimestamps.core.timestamp import DetachedTimestampFile
    except ImportError:
        sys.exit("opentimestamps not installed: pip install --user opentimestamps-client")

    for path in (MANIFEST, PROOF):
        if not path.exists():
            sys.exit(f"missing {path.relative_to(REPO)}")

    # 1. The proof must commit to the manifest we actually have on disk.
    actual = hashlib.sha256(MANIFEST.read_bytes()).digest()
    with open(PROOF, "rb") as f:
        detached = DetachedTimestampFile.deserialize(StreamDeserializationContext(f))
    claimed = detached.file_digest

    print("manifest  timestamps/SHA256SUMS.txt")
    print(f"  sha256 on disk   {actual.hex()}")
    print(f"  sha256 in proof  {claimed.hex()}")
    if actual != claimed:
        print("\nFAIL: the proof does not commit to this manifest.")
        print("The manifest was modified, or proof and manifest are from different runs.")
        return 1
    print("  -> match: the proof covers this exact manifest\n")

    bitcoin, pending = [], 0
    for msg, att in detached.timestamp.all_attestations():
        if isinstance(att, BitcoinBlockHeaderAttestation):
            # msg is the merkle root in Bitcoin's internal little-endian order;
            # explorers display it reversed.
            bitcoin.append((att.height, msg[::-1].hex()))
        elif isinstance(att, PendingAttestation):
            pending += 1

    if not bitcoin:
        print(f"No Bitcoin attestations yet ({pending} pending).")
        print("The stamp is not in a block yet. Run: ./scripts/timestamp.sh --upgrade")
        return 1

    bitcoin.sort()
    confirmed = []
    for height, expected_root in bitcoin:
        print(f"block {height}")
        print(f"  merkle root in proof  {expected_root}")
        if args.offline:
            print("  (offline: not checked against the chain)")
            continue
        try:
            actual_root, block_time = fetch_block(args.explorer, height, args.timeout)
        except Exception as exc:
            print(f"  could not reach explorer: {exc}")
            continue
        print(f"  merkle root on chain  {actual_root}")
        when = datetime.datetime.fromtimestamp(block_time, datetime.timezone.utc)
        if actual_root == expected_root:
            print(f"  -> match, mined {when:%Y-%m-%d %H:%M:%S} UTC")
            confirmed.append((when, height))
        else:
            print("  -> MISMATCH: this attestation does not match the chain")
            return 1

    if args.offline:
        print("\nOffline: the proof names the blocks above. Re-run without --offline "
              "to check them against the chain.")
        return 0
    if not confirmed:
        print("\nCould not reach the explorer. Try --explorer https://mempool.space/api")
        return 1

    when, height = min(confirmed)
    print(f"\nVerified. The manifest existed by {when:%Y-%m-%d %H:%M:%S} UTC "
          f"(block {height}).")
    print("Every file listed in the manifest is at least that old, and unchanged since.")
    print("\nThat the files still match the manifest is a separate check:")
    print("  sha256sum -c timestamps/SHA256SUMS.txt")
    print(f"\nBlock headers above came from {args.explorer}, which you are trusting")
    print("for them. Your own node is better -- ots verify --bitcoin-node ... -- and")
    print("cross-checking one other explorer (--explorer https://mempool.space/api)")
    print("is usually enough if you have no node.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
