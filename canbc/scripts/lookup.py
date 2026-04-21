#!/usr/bin/env python3
"""NBC 2020 citation → PDF page resolver.

Usage:
    python3 scripts/lookup.py 3.2.2.48
    python3 scripts/lookup.py "Part 9"
    python3 scripts/lookup.py 9.8.4       # partial match OK
    python3 scripts/lookup.py --search "spatial separation"
    python3 scripts/lookup.py --extract 3.2.2.48   # also print extracted text

Prints page number(s) in `assets/nbc_2020.pdf`. Use with the Read tool:
    Read(file_path=".../assets/nbc_2020.pdf", pages="<page>-<page+2>")

For the authoritative text, always read the PDF page — this script's --extract is
best-effort PDF text extraction and can lose layout/tables.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CITATIONS = SKILL_DIR / "references" / "citations.json"
INDEX = SKILL_DIR / "references" / "index.json"
PDF_PATH = SKILL_DIR / "assets" / "nbc_2020.pdf"


def normalize(cite: str) -> str:
    """Normalize a user-provided citation.

    Architects write citations many ways: "3.2.2.48", "3.2.2.48.", "3.2.2.48(3)",
    "3.2.2.48.(3)", "Sentence 3.2.2.48.(3)". Normalize to the internal form
    used by the index: "3.2.2.48" or "3.2.2.48.(3)". Appendix-note prefixes
    ("A-1.1.1.1.(1)") are preserved.
    """
    s = cite.strip()
    # Preserve "Part N" form — the index uses it as a citation key.
    m = re.match(r"^Part\s+(\d+)\b", s, flags=re.I)
    if m:
        return f"Part {m.group(1)}"
    # Strip level words like "Sentence", "Article", "Subsection", "Section".
    s = re.sub(r"^(Section|Sentence|Article|Subsection|Clause)\s+", "", s, flags=re.I)
    s = re.sub(r"\s+", "", s)
    # Separate optional Appendix prefix.
    app = ""
    m = re.match(r"^[Aa]-(.*)$", s)
    if m:
        app = "A-"
        s = m.group(1)
    # Collapse trailing period at end of article: 3.2.2.48. -> 3.2.2.48
    m = re.match(r"^(\d+(?:\.\d+){1,3})\.?(\(\d+\))?$", s)
    if m:
        base = m.group(1)
        sent = m.group(2) or ""
        if sent:
            # Index stores sentences as "9.8.4.2.(1)" — with trailing period before paren.
            return f"{app}{base}.{sent}"
        return f"{app}{base}"
    return f"{app}{s}"  # "Part 3" etc.


def find_exact(cite: str, cites: dict, alternates: dict) -> list[dict]:
    hits = []
    if cite in cites:
        hits.append({"citation": cite, "page": cites[cite], "source": "primary"})
    for alt in alternates.get(cite, []):
        hits.append({"citation": cite, "page": alt["page"], "title": alt["title"], "source": "alternate"})
    return hits


def find_partial(cite: str, rows: list[dict]) -> list[dict]:
    """Partial-prefix match: "9.8.4" matches all sub-entries under 9.8.4."""
    return [r for r in rows if r["citation"] and r["citation"].startswith(cite)]


def search_titles(query: str, rows: list[dict], limit: int = 25) -> list[dict]:
    q = query.lower()
    return [r for r in rows if q in r["title"].lower()][:limit]


def extract_text(page_num: int, context_pages: int = 1) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return "(pypdf not installed; cannot extract text)"
    reader = PdfReader(str(PDF_PATH))
    start = max(0, page_num - 1)
    end = min(len(reader.pages), page_num + context_pages)
    chunks = []
    for i in range(start, end):
        chunks.append(f"--- Page {i+1} ---\n{reader.pages[i].extract_text() or ''}")
    return "\n\n".join(chunks)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("citation", nargs="?", help="Citation like 3.2.2.48 or 'Part 9'")
    ap.add_argument("--search", metavar="QUERY", help="Substring search over outline titles")
    ap.add_argument("--extract", action="store_true", help="Also print extracted text from the PDF page")
    ap.add_argument("--json", action="store_true", help="Emit JSON result")
    args = ap.parse_args()

    if not (args.citation or args.search):
        ap.print_help()
        return 2

    data = json.loads(CITATIONS.read_text())
    rows = json.loads(INDEX.read_text())
    cites = data["citations"]
    alternates = data["alternates"]

    if args.search:
        hits = search_titles(args.search, rows)
        if args.json:
            print(json.dumps(hits, indent=2))
        else:
            if not hits:
                print(f"No outline entries match: {args.search!r}", file=sys.stderr)
                return 1
            for r in hits:
                c = f"[{r['citation']}] " if r["citation"] else ""
                print(f"p.{r['page']:>4}  {c}{r['title']}")
        return 0

    cite = normalize(args.citation)
    hits = find_exact(cite, cites, alternates)
    # Sentence-level citations (e.g. 9.8.4.2.(1)) aren't always bookmarked.
    # Fall back to the containing Article — the sentence lives on that page.
    if not hits:
        m = re.match(r"^(A-)?(\d+\.\d+\.\d+\.\d+)\.\(\d+\)$", cite)
        if m:
            article = f"{m.group(1) or ''}{m.group(2)}"
            hits = find_exact(article, cites, alternates)
            for h in hits:
                h["note"] = f"sentence {cite} lives in Article {article}"
    if not hits:
        partial = find_partial(cite, rows)
        if partial:
            if args.json:
                print(json.dumps(partial, indent=2))
            else:
                print(f"No exact match for {cite!r}. Partial matches (prefix):")
                for r in partial[:25]:
                    print(f"  p.{r['page']:>4}  [{r['citation']}] {r['title']}")
            return 0
        print(f"No match for citation {cite!r}. Try --search instead.", file=sys.stderr)
        return 1

    if args.json and not args.extract:
        print(json.dumps(hits, indent=2))
        return 0

    for h in hits:
        label = h.get("title", cite)
        extra = f" — {h['note']}" if h.get("note") else ""
        print(f"{h['citation']}  →  p.{h['page']}  ({h['source']}: {label}){extra}")
        if args.extract:
            print()
            print(extract_text(h["page"], context_pages=1))
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
