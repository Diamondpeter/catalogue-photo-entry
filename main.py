#!/usr/bin/env python3
"""Compliment-O-Matic: catalogue photo of an impossible gadget.

Writes one studio product photograph to /output/entry.png.

The photograph itself is shipped as a binary asset (asset.png) made
during the build: a cream retro toaster whose toast comes up printed
with a compliment, with a single butter dish as its one accessory.
This program only copies that asset into place and verifies it meets
the competition's gate (whole PNG, <= 1 MiB, <= 1024 x 1024 px).
No network, no third-party packages: pure standard library.
"""

import os
import shutil
import struct
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset.png")
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_dimensions(path):
    """Read width and height from a PNG's IHDR chunk (stdlib only)."""
    with open(path, "rb") as fh:
        magic = fh.read(8)
        if magic != PNG_MAGIC:
            raise ValueError("not a PNG file")
        header = fh.read(25)
        if len(header) < 25 or header[4:8] != b"IHDR":
            raise ValueError("missing IHDR chunk")
        width, height = struct.unpack(">II", header[8:16])
        return width, height


def main():
    if not os.path.isfile(ASSET):
        print(f"missing asset: {ASSET}", file=sys.stderr)
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(ASSET, OUT_PATH)

    # The output must be the asset itself, byte for byte.
    with open(ASSET, "rb") as src, open(OUT_PATH, "rb") as dst:
        if src.read() != dst.read():
            print("entry does not match asset", file=sys.stderr)
            return 1

    size = os.path.getsize(OUT_PATH)
    if size > MAX_BYTES:
        print(f"entry too large: {size} bytes > {MAX_BYTES}", file=sys.stderr)
        return 1

    width, height = png_dimensions(OUT_PATH)
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"entry too big: {width}x{height} > {MAX_SIDE}x{MAX_SIDE}",
              file=sys.stderr)
        return 1

    print(f"wrote {OUT_PATH}: {width}x{height}px, {size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
