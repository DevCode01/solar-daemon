#!/usr/bin/env bash
# Auto-generated test harness — run after cloning to verify the build.
set -uo pipefail
FAIL=0

echo "-- syntax/build check --"
if python3 solar-daemon.py --help; then echo "  ok"; else echo "  FAIL"; FAIL=1; fi

echo "-- functional check --"
OUT="$(printf 'hello world hello again
foo bar
' | ./solar-daemon.py 2>&1)"
if echo "$OUT" | grep -qF -- 'Lines:        2'; then
  echo "  ok   - contains: Lines:        2"
else
  echo "  FAIL - expected to contain: Lines:        2"
  echo "  got: $OUT"
  FAIL=1
fi

if [ "$FAIL" = "1" ]; then echo; echo "FAILED"; exit 1; fi
echo; echo "All tests passed."
