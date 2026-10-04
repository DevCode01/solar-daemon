# Solar Daemon

**Python** · **v0.1.0**

_Text analyzer: line, word and character counts plus most frequent words_

---

## Features

- Reads a file or piped stdin
- Counts lines, words, characters and unique words
- Top-N most frequent words ranking

## Installation

```bash
git clone https://github.com/DevCode01/solar-daemon.git
cd solar-daemon
```

## Usage

```bash
cat file.txt | ./solar-daemon.py --top 10
```

## How it works

Reads a text file (or stdin) and computes line, word and character counts. Words are normalized to lowercase and stripped of punctuation, then ranked by frequency so the most common terms stand out.

## Options

- `file` - path to the text file (reads stdin if omitted)
- `-t, --top N` - number of most frequent words to show (default 10)
- `-h, --help` - show usage

## Example

```bash
$ printf 'hello world hello again
foo bar
' | ./solar-daemon.py
Lines:        2
Words:        6
Characters:   32
Unique words: 5

Top 10 most frequent words:
  hello           2
  world           1
  again           1
  foo             1
  bar             1
```

## Testing

```bash
bash tests/run.sh
```

Includes a functional check against real captured output, plus the build/syntax check.

## License

MIT
