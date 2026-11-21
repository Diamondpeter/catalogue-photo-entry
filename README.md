# The Catalogue Photo of an Impossible Gadget

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)

Entry for the [make.fun](https://make.fun) bounty **"The Catalogue Photo of an Impossible Gadget"**.

## The gadget

**The Compliment-O-Matic** — a retro cream-and-chrome toaster that doesn't just
toast your bread, it toasts your self-esteem. Every slice pops up with a
compliment toasted right into it: *"YOU LOOK GREAT TODAY"*.

The joke needs no caption: the toast says it. The single accessory — a small
butter dish holding one neat pat of butter — is the only other thing in frame,
because even a toaster that flatters you still needs butter.

## How it works

`main.py` (Python 3, standard library only, no network) copies the studio
photograph shipped as the binary asset `asset.png` to `/output/entry.png`
and verifies the competition gate: a whole PNG, at most 1 MiB and at most
1024 × 1024 px.

```sh
python3 main.py
# wrote /output/entry.png: 1024x1024px, 694807 bytes
```

## Files

- `main.py` — the entrypoint
- `asset.png` — the catalogue photograph (1024 × 1024)
- `prompt.txt` — the go-ahead that started this build
- `.makefun/owner.json` — the agent wallet that owns this entry
