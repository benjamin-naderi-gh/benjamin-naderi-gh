"""Render a contribution heatmap whose weeks start on Monday.

GitHub's own calendar starts weeks on Sunday and offers no setting to change it
(community discussion #42104, open since 2022). This regenerates the grid from
the raw daily counts with Monday-first columns and correct date alignment.

    python scripts/contribution_heatmap.py --demo        # synthetic data
    GH_TOKEN=... python scripts/contribution_heatmap.py  # real data

Writes heatmap-light.svg and heatmap-dark.svg.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import urllib.request

GRAPHQL = "https://api.github.com/graphql"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# Sequential encoding: one hue, light to dark. Level 0 recedes into the surface.
LIGHT = {
    "surface": "#fcfcfb",
    "empty": "#ebebe8",
    "levels": ["#cde2fb", "#86b6ef", "#3987e5", "#184f95"],
    "text": "#52514e",
}
DARK = {
    "surface": "#1a1a19",
    "empty": "#2e2e2c",
    "levels": ["#184f95", "#256abf", "#3987e5", "#86b6ef"],
    "text": "#c3c2b7",
}

CELL, GAP = 11, 3
LEFT, TOP = 30, 20


def fetch(login: str, token: str) -> dict[dt.date, int]:
    to = dt.datetime.now(dt.timezone.utc)
    frm = to - dt.timedelta(days=364)
    body = json.dumps(
        {"query": QUERY, "variables": {
            "login": login,
            "from": frm.isoformat(),
            "to": to.isoformat(),
        }}
    ).encode()
    req = urllib.request.Request(
        GRAPHQL, data=body,
        headers={"Authorization": f"bearer {token}",
                 "Content-Type": "application/json",
                 "User-Agent": "contribution-heatmap"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    weeks = (payload["data"]["user"]["contributionsCollection"]
             ["contributionCalendar"]["weeks"])
    return {
        dt.date.fromisoformat(d["date"]): d["contributionCount"]
        for w in weeks for d in w["contributionDays"]
    }


def demo() -> dict[dt.date, int]:
    rng = random.Random(7)
    today = dt.date.today()
    out = {}
    for i in range(365):
        day = today - dt.timedelta(days=364 - i)
        # quieter at weekends, which is the whole point of a Monday-first grid
        base = 1 if day.weekday() >= 5 else 6
        out[day] = max(0, int(rng.gauss(base, base * 0.8)))
    return out


def level(count: int, ceiling: int) -> int:
    if count <= 0:
        return -1
    for i, frac in enumerate((0.25, 0.5, 0.75)):
        if count <= max(1, round(ceiling * frac)):
            return i
    return 3


def render(counts: dict[dt.date, int], theme: dict, path: str) -> None:
    days = sorted(counts)
    # start the grid on the Monday on or before the first day
    start = days[0] - dt.timedelta(days=days[0].weekday())
    end = days[-1] + dt.timedelta(days=6 - days[-1].weekday())
    ceiling = max(counts.values()) or 1

    weeks = (end - start).days // 7 + 1
    width = LEFT + weeks * (CELL + GAP) + 10
    height = TOP + 7 * (CELL + GAP) + 34

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}" '
        f'font-family="system-ui,-apple-system,Segoe UI,sans-serif">',
        f'<rect width="{width}" height="{height}" fill="{theme["surface"]}"/>',
    ]

    # month labels, placed at the column where each month first appears
    seen = set()
    for w in range(weeks):
        d = start + dt.timedelta(weeks=w)
        if d.month not in seen and d.day <= 7:
            seen.add(d.month)
            x = LEFT + w * (CELL + GAP)
            out.append(
                f'<text x="{x}" y="{TOP - 6}" font-size="9" '
                f'fill="{theme["text"]}">{d.strftime("%b")}</text>'
            )

    # Monday first. Label alternate rows only, so the axis stays recessive.
    for row, name in enumerate(["Mon", "", "Wed", "", "Fri", "", "Sun"]):
        if not name:
            continue
        y = TOP + row * (CELL + GAP) + CELL - 2
        out.append(
            f'<text x="0" y="{y}" font-size="9" fill="{theme["text"]}">{name}</text>'
        )

    for w in range(weeks):
        for row in range(7):
            day = start + dt.timedelta(weeks=w, days=row)
            if day not in counts:
                continue
            n = counts[day]
            lv = level(n, ceiling)
            fill = theme["empty"] if lv < 0 else theme["levels"][lv]
            x = LEFT + w * (CELL + GAP)
            y = TOP + row * (CELL + GAP)
            plural = "" if n == 1 else "s"
            out.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                f'fill="{fill}"><title>{n} contribution{plural} on '
                f'{day.isoformat()}</title></rect>'
            )

    # legend
    ly = TOP + 7 * (CELL + GAP) + 14
    lx = LEFT + weeks * (CELL + GAP) - 5 * (CELL + GAP) - 58
    out.append(f'<text x="{lx}" y="{ly + CELL - 2}" font-size="9" '
               f'fill="{theme["text"]}">Less</text>')
    for i, fill in enumerate([theme["empty"], *theme["levels"]]):
        x = lx + 26 + i * (CELL + GAP)
        out.append(f'<rect x="{x}" y="{ly}" width="{CELL}" height="{CELL}" '
                   f'rx="2" fill="{fill}"/>')
    out.append(f'<text x="{lx + 26 + 5 * (CELL + GAP) + 4}" y="{ly + CELL - 2}" '
               f'font-size="9" fill="{theme["text"]}">More</text>')

    out.append("</svg>")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"wrote {path} ({weeks} weeks, {len(counts)} days)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--login", default="benjamin-naderi-gh")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()

    if args.demo:
        counts = demo()
    else:
        token = os.environ.get("GH_TOKEN")
        if not token:
            raise SystemExit("set GH_TOKEN, or pass --demo")
        counts = fetch(args.login, token)

    render(counts, LIGHT, "heatmap-light.svg")
    render(counts, DARK, "heatmap-dark.svg")


if __name__ == "__main__":
    main()
