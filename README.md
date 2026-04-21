# National Building Code of Canada (NBC 2020) — Claude Skill

A [Claude Skill](https://code.claude.com/docs/en/skills) that turns Claude
into a practitioner-grade reference for the **National Building Code of
Canada, 2020 edition (second printing)**, as amended by the **2025
Revisions & Errata** package. It bundles the full code PDF, the errata
package, a page-numbered citation index (3,800+ entries), and workflow
guides for the questions architects actually ask.

**The NBC is a model code.** Provinces and territories adopt it with
amendments — BCBC (British Columbia), OBC (Ontario), Quebec's Code de
construction, Alberta Building Code, and so on. Use this skill for the
baseline national text; always confirm the provincial/territorial
overlay before relying on any output for a permit.

---

## What it does

Ask Claude an NBC question in plain English or by citation, and the
skill will:

1. **Route** the question to the right workflow guide (occupancy,
   Part 3, Part 9, life safety).
2. **Resolve** any article you name (e.g. `3.2.2.48`, `9.8.4.1`) to a
   PDF page via the bundled `lookup.py` script.
3. **Read the authoritative text** from the bundled NBC 2020 PDF and
   cross-check the 2025 Revisions & Errata package.
4. **Quote and cite** in the standard form: *NBC 2020, Division B,
   Sentence 3.2.2.48.(1) (PDF p. 218)*.
5. **Flag provincial overlays** — when a question has province-specific
   deltas (e.g. EMTC mass-timber heights, secondary-suite rules,
   accessibility), point you at the applicable provincial code and any
   relevant companion skill.
6. **Close with the AHJ disclaimer.** Always. Binding determinations
   belong to the provincial/territorial AHJ, not to Claude.

### Triggers on things like

- *"What's the occupancy classification for a mixed retail +
  residential building under the NBC?"*
- *"NBC 2020 — maximum storeys for Encapsulated Mass Timber
  Construction (EMTC)."*
- *"Minimum stair width in a Part 9 house."*
- *"Quote Article 3.2.2.48."*
- *"What did the 2025 Revisions & Errata change for spatial
  separation?"*

---

## Install

### Personal use (single machine)

1. Clone this repository.
2. Copy the `canbc/` folder into your Claude skills directory:

   ```bash
   cp -R canbc ~/.claude/skills/canbc
   ```

3. Restart Claude Code. Run `/plugin list` and look for `canbc`.

### Team / studio use

Every team member clones the repo and copies the `canbc/` folder into
`~/.claude/skills/canbc`. Pull to update. For Claude Team/Enterprise
plans with **Organization Settings → Add Skill**, zip the `canbc/`
folder and upload:

```bash
cd canbc && zip -r ../canbc.zip . && cd ..
```

See [INSTALL.md](INSTALL.md) for project-scoped installs and size-limit
workarounds. The NBC PDF is ~14 MB.

---

## How to use it

Once installed, just ask — the skill auto-triggers on NBC / national
building-code questions.

```
> What does NBC 2020 require for spatial separation on an exposing
  building face?

> Summarize Part 9 stair and guard dimensional requirements.

> Did the 2025 Errata change any fire-rating values in Table 3.1.7.1?

> Quote Sentence 9.8.4.1.(1).
```

---

## What's in the skill

```
canbc/
├── SKILL.md                                  # skill definition + operating instructions
├── assets/
│   ├── nbc_2020.pdf                          # 1,536-page NBC 2020 (second printing)
│   └── nbc_2020_revisions_errata_2025-03.pdf # 102-page 2025 Revisions & Errata
├── references/
│   ├── index.md / index.json                 # 3,800+ entry page-numbered outline
│   ├── map.md                                # top-level structural map
│   ├── citations.json                        # citation → page lookup
│   ├── tables.md / figures.md                # tables and figures with pages
│   ├── definitions.md                        # defined-term index (Article 1.4.1.2.)
│   ├── occupancy-classification.md           # workflow: Groups A–F, mixed use
│   ├── part3-overview.md                     # workflow: construction type, EMTC
│   ├── part9-overview.md                     # workflow: houses & small buildings
│   └── life-safety.md                        # workflow: exits, egress, occupant load
└── scripts/
    ├── lookup.py                             # citation → page resolver + keyword search
    ├── build_index.py                        # regenerate index from a new PDF edition
    └── build_map.py                          # regenerate derived navigation files
```

---

## Provincial adoption

The NBC is adopted with amendments across the country. Where a question
depends on a provincial delta, use the applicable provincial code:

- **British Columbia** — BCBC 2024. Companion skill:
  [British-Columbia-Building-Code-Skill](https://github.com/dorianbanks/British-Columbia-Building-Code-Skill).
- **City of Vancouver** — VBBL 2025 (its own by-law). Companion skill:
  [Vancouver-Building-By-law-Skill](https://github.com/dorianbanks/Vancouver-Building-By-law-Skill).
- **Northwest Territories** — NBC applies as adopted; use the
  [Northwest-Territories-Building-Code-Skill](https://github.com/dorianbanks/Northwest-Territories-Building-Code-Skill)
  for the northern design-guide overlay.
- **Other provinces/territories** — consult the applicable provincial
  building code directly.

For energy, the companion skill is
[National-Energy-Code-of-Canada-Skill](https://github.com/dorianbanks/National-Energy-Code-of-Canada-Skill)
(NECB 2020).

---

## Scope & limits

- **Division B focus.** The skill emphasises Division B (Acceptable
  Solutions) — the technical bulk. Division A (Compliance, Objectives,
  Functional Statements) and Division C (Administrative Provisions)
  are indexed but lightly profiled.
- **Model code, not binding on its own.** The NBC becomes enforceable
  only through provincial/territorial adoption, usually with
  amendments. Always confirm the applicable provincial code.
- **Not a code consultant.** Binding determinations belong to the
  provincial/territorial AHJ and your code consultant.
- **Authoritative text wins.** Always verify by reading the cited PDF
  page before relying on an answer for a permit submission.

---

## Credits

Built by **Dorian Banks**. Released under the MIT License — see
[LICENSE](LICENSE).

The National Building Code of Canada is published by the National
Research Council of Canada on behalf of the Canadian Commission on
Building and Fire Codes. This repository redistributes the 2020 second
printing and 2025 Revisions & Errata PDFs for reference use inside the
skill; consult the official source at
[nrc-cnrc.gc.ca](https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada)
for authoritative and current versions.

---

## Disclaimer

This skill is a reference aid for licensed practitioners. It is not
legal advice, not a substitute for a code consultant, and not a
substitute for review by the Authority Having Jurisdiction. Always
verify against the applicable provincial/territorial adoption of the
NBC and confirm with the AHJ before relying on any output for a permit
submission or construction.
