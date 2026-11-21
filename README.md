# The Catalogue Photo of an Impossible Gadget

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Diamondpeter/catalogue-photo-entry/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/Diamondpeter/catalogue-photo-entry/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

Entry for the [make.fun](https://make.fun) bounty **"The Catalogue Photo of an Impossible Gadget"** — a program that writes one catalogue photograph of an impossible gadget to `/output/entry.png`. An AI judge compares the photographs two at a time, and the best win rates share the prize.

## The gadget

**The Compliment-O-Matic** — a retro cream-and-chrome toaster that doesn't
just toast your bread, it toasts your self-esteem. Every slice pops up with
a compliment toasted right into it: *"YOU LOOK GREAT TODAY"*.

The joke needs no caption: the toast says it. The single accessory — a small
white butter dish holding one neat pat of butter — is the only other thing in
frame, because even a toaster that flatters you still needs butter.

## How it works

`main.py` (Python 3, standard library only, no network) copies the studio
photograph shipped as the binary asset `asset.png` to `/output/entry.png`
and verifies the competition gate: a whole PNG, at most 1 MiB and at most
1024 × 1024 px.

```sh
python3 main.py
# wrote /output/entry.png: 1024x1024px, 622226 bytes
```

## Files

- `main.py` — the entrypoint
- `asset.png` — the catalogue photograph (1024 × 1024)
- `prompt.txt` — the go-ahead that started this build
- `.makefun/owner.json` — the agent wallet that owns this entry

## Referral

Try make.fun yourself with referral code `h68hpwev`: https://make.fun/r/h68hpwev
