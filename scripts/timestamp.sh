#!/usr/bin/env bash
# Prove when this repository's data existed, by anchoring it to the Bitcoin
# blockchain with OpenTimestamps.
#
# Scope: git-tracked files only. Untracked scratch files in the working tree are
# deliberately ignored, so the manifest describes exactly the bytes that a clone
# of this repo contains -- nothing local or incidental.
#
# One manifest, one proof: the .ots file commits to the manifest's bytes, and
# the manifest commits to every tracked file's bytes. That is enough to prove any
# single file in this repo existed in its current form at the stamped time.
#
#   ./scripts/timestamp.sh            build manifest + stamp it
#   ./scripts/timestamp.sh --upgrade  pull the Bitcoin attestation once confirmed
#   ./scripts/timestamp.sh --verify   check an existing proof
#   ./scripts/timestamp.sh --info     dump the raw proof structure
#
# Requires: opentimestamps-client  (pip install --user opentimestamps-client)

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$REPO/timestamps"
MANIFEST="$OUT_DIR/SHA256SUMS.txt"
PROOF="$MANIFEST.ots"

export PATH="$HOME/.local/bin:$PATH"
command -v ots >/dev/null || { echo "ots not found; pip install --user opentimestamps-client" >&2; exit 1; }

case "${1:-stamp}" in
  --verify)  exec ots verify "$PROOF" ;;
  --upgrade) exec ots upgrade "$PROOF" ;;
  --info)    exec ots info "$PROOF" ;;
  stamp)     ;;
  *)         echo "unknown option: $1" >&2; exit 1 ;;
esac

cd "$REPO"

# The manifest must describe exactly what the next commit will contain, so the
# working tree has to match the index. Unstaged edits or deletions would make the
# manifest describe bytes that were never committed.
if ! git diff --quiet; then
  echo "Refusing to stamp: tracked files have unstaged changes." >&2
  echo "Stage or revert them first, so the manifest matches the commit:" >&2
  git diff --name-only | sed 's|^|  |' >&2
  exit 1
fi

if [[ -e "$PROOF" ]]; then
  echo "Refusing to overwrite the existing proof: timestamps/SHA256SUMS.txt.ots" >&2
  echo "A manifest describes one moment. To stamp a new revision, move the old" >&2
  echo "manifest+proof pair aside (both, together) and re-run." >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

# Tracked files, from the index, in git's own sorted order. The manifest and its
# proof are excluded: a manifest cannot hash itself.
mapfile -d '' FILES < <(
  git ls-files -z | grep -zv '^timestamps/SHA256SUMS' || true
)

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No tracked files found." >&2
  exit 1
fi

echo "Hashing ${#FILES[@]} tracked files..." >&2

HEAD_SHA="$(git rev-parse HEAD)"
HEAD_DATE="$(git log -1 --format=%cI)"
STAGED_ADDS="$(git diff HEAD --name-only --diff-filter=A -- . || true)"
STAGED_MODS="$(git diff HEAD --name-only --diff-filter=MD -- . || true)"

{
  echo "# SHA-256 manifest of the git-tracked files in metr-money-figure."
  echo "#"
  echo "# Timestamped with OpenTimestamps; see timestamps/README.md to verify."
  echo "# Untracked files in the working tree are intentionally not covered."
  echo "#"
  echo "# Built:         $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "# Tracked files: ${#FILES[@]}"
  echo "# git HEAD:      $HEAD_SHA"
  echo "# HEAD date:     $HEAD_DATE"
  if [[ -n "$STAGED_MODS" ]]; then
    echo "#"
    echo "# Staged edits to files already in HEAD (this manifest reflects the staged"
    echo "# version, which the next commit will contain):"
    echo "$STAGED_MODS" | sed 's|^|#   |'
  fi
  if [[ -n "$STAGED_ADDS" ]]; then
    echo "#"
    echo "# Staged new files, not yet in HEAD (covered by this manifest, and"
    echo "# committed alongside it):"
    echo "$STAGED_ADDS" | sed 's|^|#   |'
  fi
  echo "#"
  echo "# Check file hashes:  sha256sum -c timestamps/SHA256SUMS.txt   (from repo root)"
  echo "# Check the date:     ots verify timestamps/SHA256SUMS.txt.ots"
  echo "#"
  printf '%s\0' "${FILES[@]}" | xargs -0 sha256sum --
} > "$MANIFEST"

echo "Wrote timestamps/SHA256SUMS.txt" >&2

# Submits only the manifest's 32-byte hash to the calendar servers. No file
# contents and no filenames leave this machine.
ots stamp "$MANIFEST"

echo >&2
echo "Stamped. The proof is 'pending' until it is confirmed in a Bitcoin block" >&2
echo "(usually a few hours). Then run: ./scripts/timestamp.sh --upgrade" >&2
