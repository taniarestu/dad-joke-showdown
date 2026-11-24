"""Entry for make.fun: Dad Joke Showdown.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "The electrician wired my house for sound, and now every room is current."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
