#!/usr/bin/env python3
# Text statistics analyzer: lines, words, chars, top word frequencies.
import argparse
import sys
from collections import Counter

PUNCT = ".,;:!?\"'()[]{}"


def clean(word):
    return word.strip(PUNCT).lower()


def main():
    parser = argparse.ArgumentParser(description="Text file statistics analyzer")
    parser.add_argument("file", nargs="?", help="File to analyze (reads stdin if omitted)")
    parser.add_argument("-t", "--top", type=int, default=10, help="Number of top words (default: 10)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8", errors="replace") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    lines = text.splitlines()
    words = [w for w in text.split() if w.strip()]
    freq = Counter(clean(w) for w in words if clean(w))

    print(f"Lines:        {len(lines)}")
    print(f"Words:        {len(words)}")
    print(f"Characters:   {len(text)}")
    print(f"Unique words: {len(freq)}")
    print()
    print(f"Top {args.top} most frequent words:")
    for word, count in freq.most_common(args.top):
        print(f"  {word:<15} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
