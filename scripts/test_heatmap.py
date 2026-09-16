"""Check that one enormous day cannot repaint the rest of the year.

Scaling colour steps to the maximum makes every other day lighter as soon as a
single outlier appears. Ranking does not. This asserts the difference against
the real contribution data committed in heatmap-light.svg.

    python scripts/test_heatmap.py
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("hm", HERE / "contribution_heatmap.py")
hm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hm)


def real_counts() -> dict[dt.date, int]:
    svg = (HERE.parent / "heatmap-light.svg").read_text(encoding="utf-8")
    pairs = re.findall(r"<title>(\d+) contributions? on (\d{4}-\d{2}-\d{2})</title>", svg)
    if not pairs:
        sys.exit("no data found in heatmap-light.svg")
    return {dt.date.fromisoformat(d): int(n) for n, d in pairs}


def colours(counts: dict[dt.date, int]) -> dict[dt.date, int]:
    cuts = hm.thresholds(counts)
    return {d: hm.level(n, cuts) for d, n in counts.items()}


def old_colours(counts: dict[dt.date, int]) -> dict[dt.date, int]:
    """The previous behaviour: steps as fractions of the busiest day."""
    ceiling = max(counts.values()) or 1

    def level(c: int) -> int:
        if c <= 0:
            return -1
        for i, frac in enumerate((0.25, 0.5, 0.75)):
            if c <= max(1, round(ceiling * frac)):
                return i
        return 3

    return {d: level(n) for d, n in counts.items()}


def repainted(before: dict, after: dict, spiked: dt.date) -> int:
    return sum(1 for d in before if d != spiked and before[d] != after[d])


def main() -> None:
    counts = real_counts()
    busiest = max(counts, key=counts.get)
    quiet = next(d for d in sorted(counts) if counts[d] == 0)
    total = len(counts) - 1
    failures = []

    for label, day in (("a busy day spikes", busiest), ("an empty day spikes", quiet)):
        spiked = dict(counts)
        spiked[day] = 2000

        n_new = repainted(colours(counts), colours(spiked), day)
        n_old = repainted(old_colours(counts), old_colours(spiked), day)

        print(f"{label} to 2000 ({day}, was {counts[day]})")
        print(f"   ranked  : {n_new:>3} / {total} other days change colour")
        print(f"   scaled  : {n_old:>3} / {total} other days change colour  (old behaviour)")

        # ranking may shift a quartile by one position; it must never cascade
        if n_new > total * 0.05:
            failures.append(f"{label}: {n_new} days repainted, expected under 5%")
        if n_old <= n_new:
            failures.append(f"{label}: old behaviour was no worse, test is not meaningful")

    print()
    if failures:
        for f in failures:
            print("FAIL:", f)
        sys.exit(1)
    print("PASS: an outlier does not repaint the year")


if __name__ == "__main__":
    main()
