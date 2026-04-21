# Install

Detailed install instructions for the NBC 2020 Claude Skill. For a
quick overview, see [README.md](README.md#install).

---

## Prerequisites

- **Claude Code** or **Claude.ai** with skills enabled.
- **Python 3.8+** on your `PATH` (only needed if you plan to run
  `scripts/lookup.py` directly — Claude runs it for you inside the
  skill).

---

## Option 1 — Personal install (Claude Code)

```bash
git clone https://github.com/dorianbanks/National-Building-Code-of-Canada-Skill.git
cd National-Building-Code-of-Canada-Skill
mkdir -p ~/.claude/skills
cp -R canbc ~/.claude/skills/canbc
```

Restart Claude Code. Ask an NBC question — the skill should auto-
trigger. Run `/plugin list` and look for `canbc`.

### Updating

```bash
cd National-Building-Code-of-Canada-Skill
git pull
cp -R canbc ~/.claude/skills/canbc
```

---

## Option 2 — Project-scoped install

From your project root:

```bash
mkdir -p .claude/skills
git clone https://github.com/dorianbanks/National-Building-Code-of-Canada-Skill.git /tmp/canbc-src
cp -R /tmp/canbc-src/canbc .claude/skills/canbc
rm -rf /tmp/canbc-src
```

Commit `.claude/skills/canbc` (or add to `.gitignore` if you prefer
everyone install it themselves).

---

## Option 3 — Organization-wide upload (Claude Team / Enterprise)

If your Claude plan has **Organization Settings → Add Skill** on
[claude.ai](https://claude.ai):

```bash
git clone https://github.com/dorianbanks/National-Building-Code-of-Canada-Skill.git
cd National-Building-Code-of-Canada-Skill/canbc
zip -r ../canbc.zip .
cd ..
```

Then upload `canbc.zip` via **Settings → Organization → Skills → Add
Skill**.

> **Size note:** the bundled PDFs total ~15 MB. If the upload UI
> enforces a smaller cap, see
> [Trimming the skill](#trimming-the-skill-for-upload-size-limits).

---

## Verifying the install

Open Claude Code (or claude.ai) and ask:

```
What does NBC 2020 Sentence 3.2.2.48.(1) say?
```

You should see Claude:

1. Acknowledge the `canbc` skill.
2. Resolve the article with `lookup.py`.
3. Read the PDF at the resolved page.
4. Quote the sentence with a *(PDF p. N)* citation.
5. Close with a provincial-AHJ disclaimer (NBC is a model code;
   provincial adoption determines enforceability).

If you get a generic answer with no PDF reference, the skill did not
load — confirm `~/.claude/skills/canbc/SKILL.md` exists and restart
Claude Code.

---

## Trimming the skill for upload size limits

The two PDFs dominate the bundle. If an org-upload UI rejects the
size:

1. **Host the PDFs externally.** Remove `canbc/assets/*.pdf` from the
   zip and host them somewhere the skill has access to. Update
   `SKILL.md` to reference the new path.
2. **Drop the first-printing PDF** (if present). The second printing
   supersedes it; the first printing is only retained for historical
   comparison.
3. **Ship only the index.** Omit the PDF entirely — the skill still
   resolves citations to pages via `references/index.json`. You lose
   the quote-from-authoritative-text step — not recommended.

---

## Uninstall

```bash
rm -rf ~/.claude/skills/canbc        # personal install
rm -rf .claude/skills/canbc          # project install
```

For org-uploaded skills, remove via the same claude.ai admin UI used
to install.
