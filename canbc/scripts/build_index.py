#!/usr/bin/env python3
"""Build a citation -> page index from the NBC 2020 PDF outline.

Produces three files alongside the skill:
  references/index.json   — machine-readable: {citation, title, page, depth}
  references/index.md     — human-readable: hierarchical TOC with page refs
  references/citations.json — fast path for scripts/lookup.py (citation key -> page)

Run once after dropping a new NBC PDF into assets/nbc_2020.pdf.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from pypdf import PdfReader

SKILL_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = SKILL_DIR / "assets" / "nbc_2020.pdf"
INDEX_JSON = SKILL_DIR / "references" / "index.json"
INDEX_MD = SKILL_DIR / "references" / "index.md"
CITATIONS_JSON = SKILL_DIR / "references" / "citations.json"

# Matches NBC citation patterns at the start of a bookmark title:
#   "1.1.1."           (Subsection)
#   "1.1.1.1."         (Article)
#   "1.1.1.1.(3)"      (Sentence)
#   "Section 3.2."     (Section)
#   "Part 3"           (Part)
# Also matches Appendix-note bookmarks like "A-1.1.1.1.(1)".
CITATION_RE = re.compile(
    r"""^\s*(?:
        (?P<app>A-)?(?:Section\s+)?(?P<section>\d+\.\d+\.)\s+               |
        (?P<app2>A-)?(?P<subsection>\d+\.\d+\.\d+\.)\s+                     |
        (?P<app3>A-)?(?P<article>\d+\.\d+\.\d+\.\d+\.)(?:\((?P<sent>\d+)\))? |
        Part\s+(?P<part>\d+)(?:\b|\s)
    )""",
    re.VERBOSE,
)


def walk(reader: PdfReader, items, depth: int, rows: list) -> None:
    for it in items:
        if isinstance(it, list):
            walk(reader, it, depth + 1, rows)
            continue
        try:
            title = (it.title or "").strip()
            page = reader.get_destination_page_number(it) + 1  # 1-indexed
        except Exception:
            continue
        if not title:
            continue
        citation = extract_citation(title)
        rows.append(
            {
                "depth": depth,
                "title": title,
                "page": page,
                "citation": citation,
            }
        )


def extract_citation(title: str) -> str | None:
    m = CITATION_RE.match(title)
    if not m:
        return None
    gd = m.groupdict()
    prefix = ""
    if gd.get("app") or gd.get("app2") or gd.get("app3"):
        prefix = "A-"
    if gd.get("article"):
        base = gd["article"].rstrip(".")
        cite = f"{base}.({gd['sent']})" if gd.get("sent") else base
        return f"{prefix}{cite}"
    for key in ("subsection", "section"):
        if gd.get(key):
            return f"{prefix}{gd[key].rstrip('.')}"
    if gd.get("part"):
        return f"Part {gd['part']}"
    return None


def to_markdown(rows: list[dict]) -> str:
    lines = [
        "# NBC 2020 — Citation Index",
        "",
        "Auto-generated from the PDF bookmark tree. Pages are 1-indexed and refer to",
        "`assets/nbc_2020.pdf`. Use `scripts/lookup.py <citation>` to resolve a citation",
        "to a page, or read the PDF directly with the Read tool and the `pages` parameter.",
        "",
    ]
    for r in rows:
        indent = "  " * min(r["depth"], 6)
        cite = f"**{r['citation']}** — " if r["citation"] else ""
        lines.append(f"{indent}- {cite}{r['title']}  _(p.{r['page']})_")
    return "\n".join(lines) + "\n"


def main() -> int:
    if not PDF_PATH.exists():
        print(f"PDF not found at {PDF_PATH}", file=sys.stderr)
        return 1
    reader = PdfReader(str(PDF_PATH))
    rows: list[dict] = []
    walk(reader, reader.outline, 0, rows)

    INDEX_JSON.write_text(json.dumps(rows, indent=2))
    INDEX_MD.write_text(to_markdown(rows))

    # Fast lookup map. For duplicate citations (Division A vs B), keep the
    # first occurrence but also store alternates under `_alternates`.
    cites: dict[str, int] = {}
    alternates: dict[str, list[dict]] = {}
    for r in rows:
        c = r["citation"]
        if not c:
            continue
        if c not in cites:
            cites[c] = r["page"]
        else:
            alternates.setdefault(c, []).append({"page": r["page"], "title": r["title"]})
    CITATIONS_JSON.write_text(
        json.dumps({"citations": cites, "alternates": alternates}, indent=2)
    )

    print(f"Indexed {len(rows)} entries across {len(reader.pages)} pages.")
    print(f"Unique citations: {len(cites)} (with {sum(len(v) for v in alternates.values())} alternates)")
    print("Wrote:")
    print(f"  {INDEX_JSON.relative_to(SKILL_DIR)}")
    print(f"  {INDEX_MD.relative_to(SKILL_DIR)}")
    print(f"  {CITATIONS_JSON.relative_to(SKILL_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
