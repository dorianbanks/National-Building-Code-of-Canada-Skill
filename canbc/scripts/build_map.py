#!/usr/bin/env python3
"""Derive compact navigation files from references/index.json.

Outputs:
  references/map.md        — Parts, Sections, Subsections only (context-friendly)
  references/tables.md     — every numbered Table with page number
  references/figures.md    — every numbered Figure with page number
  references/definitions.md — Part 1.4 defined terms list with page numbers
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX = SKILL_DIR / "references" / "index.json"
MAP_MD = SKILL_DIR / "references" / "map.md"
TABLES_MD = SKILL_DIR / "references" / "tables.md"
FIGURES_MD = SKILL_DIR / "references" / "figures.md"
DEFINITIONS_MD = SKILL_DIR / "references" / "definitions.md"

TABLE_RE = re.compile(r"\bTable\s+(?P<cite>[A-Z]?-?\d+\.\d+\.\d+\.\d+\.?(?:\(\d+\))?)[.\s]", re.I)
FIGURE_RE = re.compile(r"\bFigure\s+(?P<cite>[A-Z]?-?\d+\.\d+\.\d+\.\d+\.?(?:\(\d+\))?)", re.I)
SECTION_RE = re.compile(r"^(Section\s+)?(\d+\.\d+\.)\s+")
SUBSECTION_RE = re.compile(r"^(\d+\.\d+\.\d+\.)\s+")
PART_RE = re.compile(r"^Part\s+(\d+)\b")
DIVISION_RE = re.compile(r"^Division\s+([ABC])\b", re.I)
DEFINED_TERM_RE = re.compile(r"^1\.4\.1\.2\.\((\d+)\)")  # defined terms sit under 1.4.1.2.


def load_rows() -> list[dict]:
    return json.loads(INDEX.read_text())


def build_map(rows: list[dict]) -> str:
    lines = [
        "# NBC 2020 — Structural Map",
        "",
        "High-level navigation: Divisions, Parts, Sections, and Subsections only.",
        "For articles and sentences, see `index.md` or run `scripts/lookup.py <citation>`.",
        "The PDF is `assets/nbc_2020.pdf` — pages are 1-indexed.",
        "",
    ]
    for r in rows:
        t = r["title"].strip()
        p = r["page"]
        if DIVISION_RE.match(t):
            lines.append(f"\n## {t}  _(p.{p})_\n")
        elif PART_RE.match(t):
            lines.append(f"\n### {t}  _(p.{p})_\n")
        elif SECTION_RE.match(t):
            lines.append(f"- **{t}**  _(p.{p})_")
        elif SUBSECTION_RE.match(t):
            lines.append(f"  - {t}  _(p.{p})_")
    return "\n".join(lines) + "\n"


def build_tables(rows: list[dict]) -> str:
    lines = [
        "# NBC 2020 — Table Index",
        "",
        "Every titled Table in the code with its page number in `assets/nbc_2020.pdf`.",
        "Tables carry a lot of the code's decision-making weight (occupancy, construction",
        "type, spatial separation, fire-resistance ratings). Read the PDF page for the",
        "authoritative text.",
        "",
    ]
    seen = set()
    for r in rows:
        t = r["title"].strip()
        m = TABLE_RE.search(t)
        if not m:
            continue
        cite = m.group("cite").rstrip(".")
        key = (cite, t)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- **Table {cite}** — {t}  _(p.{r['page']})_")
    return "\n".join(lines) + "\n"


def build_figures(rows: list[dict]) -> str:
    lines = [
        "# NBC 2020 — Figure Index",
        "",
        "Every titled Figure in the code with its page number in `assets/nbc_2020.pdf`.",
        "",
    ]
    seen = set()
    for r in rows:
        t = r["title"].strip()
        m = FIGURE_RE.search(t)
        if not m:
            continue
        cite = m.group("cite").rstrip(".")
        key = (cite, t)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- **Figure {cite}** — {t}  _(p.{r['page']})_")
    return "\n".join(lines) + "\n"


def build_definitions(rows: list[dict]) -> str:
    """Extract likely defined-term bookmarks.

    Division A Article 1.4.1.2. is "Defined Terms". Notes under A-1.4.1.2.(1) also
    name individual terms. We list both so Claude can jump to the right page.
    """
    lines = [
        "# NBC 2020 — Defined Terms",
        "",
        "Defined terms live in **Division A, Article 1.4.1.2.** of the code.",
        "Application notes (labelled `A-1.4.1.2.(1)`) expand on individual terms.",
        "Read the PDF page for the authoritative definition.",
        "",
        "## Article & general notes",
        "",
    ]
    term_rows = []
    in_a_142 = False
    for r in rows:
        t = r["title"].strip()
        if "1.4.1.2." in t and "Defined Terms" in t:
            lines.append(f"- **1.4.1.2.** — {t}  _(p.{r['page']})_")
        if t.startswith("A-1.4.1.2."):
            in_a_142 = True
            lines.append(f"- **{t}**  _(p.{r['page']})_")
            continue
        if in_a_142 and r["depth"] >= 6:
            # Individual term names listed as child bookmarks under A-1.4.1.2.(1).
            term_rows.append(r)
        elif in_a_142 and r["depth"] < 6 and not t.startswith("A-1.4.1.2."):
            in_a_142 = False
    if term_rows:
        lines.append("")
        lines.append("## Individual term notes (under A-1.4.1.2.(1))")
        lines.append("")
        for r in term_rows:
            lines.append(f"- {r['title']}  _(p.{r['page']})_")
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = load_rows()
    MAP_MD.write_text(build_map(rows))
    TABLES_MD.write_text(build_tables(rows))
    FIGURES_MD.write_text(build_figures(rows))
    DEFINITIONS_MD.write_text(build_definitions(rows))
    print("Wrote:")
    for p in (MAP_MD, TABLES_MD, FIGURES_MD, DEFINITIONS_MD):
        print(f"  {p.relative_to(SKILL_DIR)} ({p.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
