#!/usr/bin/env python3
"""Compliment-O-Matic — catalogue photo of an impossible gadget.

Entrypoint for the make.fun bounty "The Catalogue Photo of an
Impossible Gadget". Running this program writes one studio product
photograph to /output/entry.png.

The photograph is a binary asset shipped with the entry (asset.png),
made during this build: a cream retro toaster whose toast pops up
printed with a compliment, a single butter dish as its one accessory.
The program's only job is to place that asset in the output slot and
prove it passes the competition gate: a whole PNG no larger than
1 MiB and no side longer than 1024 px. Standard library only, and
the program makes no network calls.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(HERE, "asset.png")
OUT_PATH = "/output/entry.png"

LIMIT_BYTES = 1_048_576
LIMIT_SIDE = 1024
MAGIC = b"\x89PNG\r\n\x1a\n"


def read_png_size(path):
    """Return (width, height) read from a PNG's IHDR chunk."""
    with open(path, "rb") as handle:
        if handle.read(8) != MAGIC:
            raise ValueError("not a PNG file")
        chunk = handle.read(25)
        if len(chunk) < 25 or chunk[4:8] != b"IHDR":
            raise ValueError("missing IHDR chunk")
        return struct.unpack(">II", chunk[8:16])


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    if not os.path.isfile(ASSET):
        return fail(f"asset not found: {ASSET}")

    # Validate the asset itself before it becomes the entry, so a
    # corrupt asset fails here instead of shipping a bad output.
    asset_w, asset_h = read_png_size(ASSET)
    if asset_w > LIMIT_SIDE or asset_h > LIMIT_SIDE:
        return fail(f"asset too big: {asset_w}x{asset_h}px")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    shutil.copyfile(ASSET, OUT_PATH)

    with open(ASSET, "rb") as original, open(OUT_PATH, "rb") as copy:
        if original.read() != copy.read():
            return fail("output does not match the asset")

    size = os.path.getsize(OUT_PATH)
    if size > LIMIT_BYTES:
        return fail(f"output too large: {size} bytes > {LIMIT_BYTES}")

    width, height = read_png_size(OUT_PATH)
    if width > LIMIT_SIDE or height > LIMIT_SIDE:
        return fail(f"output too big: {width}x{height}px")

    print(f"wrote {OUT_PATH}: {width}x{height}px, {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
