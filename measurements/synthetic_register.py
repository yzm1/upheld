"""Load and index a synthetic register an order of magnitude beyond any that
exists, and time it.

Results, one Linux container under unknown concurrent load: a 12.2 MB
register of 10,000 promises and 21,650 defenses loaded in 108 ms on 2026-09-05
and 481 ms on 2026-09-06; a reverse index from artifact to defenses built in
11 ms and 21 ms; a diff-first query over 12 changed files answered in under
0.1 ms both times. See RESULTS.md.

Consequence: the materialised reverse index in the lock is a convenience, not
a requirement, at any register size that exists.

Run:  python synthetic_register.py
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import tempfile
import time

PROMISES = 10_000
FILES = 540
GROUNDS = ("promise", "defense", "subject", "oracle", "environment")


def build() -> dict:
    rnd = random.Random(1)
    files = [f"tests/unit/test_mod{i}.py" for i in range(FILES)]
    promises = []
    for i in range(PROMISES):
        n = rnd.choice([1, 1, 1, 2, 3, 5])
        defenses = []
        for j in range(n):
            defenses.append(
                {
                    "id": f"P-{i:05d}:d{j}",
                    "guarded_by": rnd.choice(["test", "checker", "type"]),
                    "locator": rnd.choice(files) + f"::test_{rnd.randint(0, 80)}",
                    "grounds": {
                        k: hashlib.sha256(f"{i}{j}{k}".encode()).hexdigest()
                        for k in GROUNDS
                    },
                }
            )
        promises.append({"id": f"P-{i:05d}", "promise": "x" * 80, "defenses": defenses})
    return {"promises": promises}, files


def main() -> None:
    register, files = build()
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(register, fh)
        path = fh.name
    try:
        size_mb = os.path.getsize(path) / 1e6
        n_def = sum(len(p["defenses"]) for p in register["promises"])

        t = time.perf_counter()
        loaded = json.load(open(path))
        t_load = time.perf_counter() - t

        t = time.perf_counter()
        reverse: dict[str, list[str]] = {}
        for p in loaded["promises"]:
            for d in p["defenses"]:
                reverse.setdefault(d["locator"].split("::")[0], []).append(d["id"])
        t_index = time.perf_counter() - t

        changed = set(random.Random(2).sample(files, 12))
        t = time.perf_counter()
        hit = [d for f in changed for d in reverse.get(f, [])]
        t_query = time.perf_counter() - t

        print(f"register: {size_mb:.1f} MB, {PROMISES} promises, {n_def} defenses")
        print(f"load          {t_load * 1000:7.1f} ms")
        print(f"reverse index {t_index * 1000:7.1f} ms")
        print(f"query 12 files{t_query * 1000:7.2f} ms -> {len(hit)} defenses")
    finally:
        os.unlink(path)


if __name__ == "__main__":
    main()
