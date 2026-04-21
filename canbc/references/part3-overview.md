# Workflow — Part 3 (Fire Protection, Occupant Safety and Accessibility)

**When to use this guide:** the user is working on a building that falls under Division B, Part 3 — anything that isn't Part 9 — and asks about construction type, fire separations, egress, sprinklers, mass timber, or high building provisions.

Part 3 is the largest and most-cited part of the NBC for architects working on commercial, institutional, and mid/high-rise residential projects.

## Part 3 vs Part 9 — which applies?

Read **Articles 1.3.3.2. and 1.3.3.3.** of Division A (PDF p.31–32).

Part 9 is limited to:
- Buildings ≤ 3 storeys in building height, **and**
- Building area ≤ 600 m², **and**
- Major occupancies of **Group C, D, E, or F-2/F-3 only** (residential, business, mercantile, medium/low-hazard industrial), **and**
- Not a post-disaster building, not a high building.

Anything outside those limits goes to Part 3. When in doubt, Part 3 applies.

> **Farm buildings exception (new in NBC 2020):** Farm buildings have their own Part — **Division B, Part 2** (PDF p.114+) — which supersedes Parts 3 and 9 for agricultural occupancies per Article 1.3.3.5.

## Core decision: construction type matrix (Articles 3.2.2.20 – 3.2.2.92)

The construction-type articles are the heart of Part 3. For each combination of **major occupancy + number of storeys + building area + sprinklered/unsprinklered**, the code specifies:
- **Combustible** / **noncombustible** / **encapsulated mass timber (EMTC)** construction permitted
- **Fire-resistance ratings** of floor assemblies, mezzanines, roof assemblies, loadbearing supports
- **Sprinklering** requirement (often makes the difference between a trade-up and a trade-down)

Key articles by occupancy (Division B; use `scripts/lookup.py`):

| Occupancy | Article range | Starts at PDF p. |
|---|---|---|
| Group A, Division 1 | 3.2.2.20 – 3.2.2.22 | 196 |
| Group A, Division 2 | 3.2.2.23 – 3.2.2.28 | 197 |
| Group A, Division 3 | 3.2.2.29 – 3.2.2.34 | 199 |
| Group A, Division 4 | 3.2.2.35 | ~201 |
| Group B, Division 1 | 3.2.2.36 – 3.2.2.38 | ~201 |
| Group B, Division 2 | 3.2.2.39 – 3.2.2.43 | ~202 |
| Group B, Division 3 | 3.2.2.44 – 3.2.2.46 | ~203 |
| Group C | 3.2.2.47 – 3.2.2.57 (incl. EMTC articles 3.2.2.48–.49) | 204 |
| Group D | 3.2.2.58 – 3.2.2.65 | ~210 |
| Group E | 3.2.2.66 – 3.2.2.71 | ~213 |
| Group F-1 | 3.2.2.72 – 3.2.2.75 | 216 |
| Group F-2 | 3.2.2.76 – 3.2.2.81 | 217 |
| Group F-3 | 3.2.2.82 – 3.2.2.92 | 219 |

Always read the specific article. Don't generalize from memory — sprinklering requirements and storey limits are specific to the combination.

## Encapsulated Mass Timber Construction (EMTC) — new in NBC 2020

NBC 2020 introduced **EMTC** as a third construction category alongside combustible and noncombustible, permitted up to **12 storeys** for certain occupancies:
- **Group C (residential)**: Article 3.2.2.48. — up to 12 storeys, sprinklered.
- **Group D (business)**: up to 12 storeys per the specific article — read it.

Key EMTC provisions:
- **Subsection 3.1.6. Encapsulated Mass Timber Construction** (PDF p.162) — what EMTC is.
- **Article 3.1.6.3. Structural Mass Timber Elements** — permitted structural types.
- **Article 3.1.6.4. Encapsulation of Mass Timber Elements** — encapsulation rating and material requirements.
- **Article 3.1.13.12.** — flame-spread / smoke-developed requirements for exposed mass timber.
- **Appendix notes A-3.1.6.** onward (PDF p.375+) — explanatory.

Nearly always sprinklered. Limited exposed mass timber permitted under specific conditions.

`scripts/lookup.py --search "mass timber"` and `--search "encapsulated"`.

## Other Part 3 sections you'll likely need

| Section | Topic | Starts at p. |
|---|---|---|
| 3.1.2. | Occupancy classification | 146 |
| 3.1.3. | Multiple occupancy requirements | 147 |
| 3.1.4. | Combustible construction | 149 |
| 3.1.5. | Noncombustible construction | ~153 |
| 3.1.6. | **Encapsulated Mass Timber Construction (EMTC)** | 162 |
| 3.1.7. | Fire-resistance ratings and Table 3.1.7.1. | ~174 |
| 3.1.8. | Fire separations and closures | ~175 |
| 3.1.9. | Penetrations in fire separations | ~183 |
| 3.1.10. | Firewalls | ~186 |
| 3.1.11. | Fire blocks in concealed spaces | ~188 |
| 3.1.12. | Flame-spread rating, smoke-developed classification | ~191 |
| 3.1.13. | Interior finish | ~192 |
| 3.1.17. | Occupant load | ~197 |
| 3.2.2. | Building size and construction relative to occupancy (core matrix) | 192 |
| 3.2.3. | Spatial separation and exposure protection | ~242 |
| 3.2.4. | Fire alarm and detection systems | — |
| 3.2.5. | Provisions for fire fighting | — |
| 3.2.6. | Additional requirements for high buildings | — |
| 3.3. | Safety within floor areas (corridors, egress within suites) | — |
| 3.4. | Exits | — |
| 3.6. | Service facilities | — |
| 3.7. | Health requirements (washrooms, etc.) | — |
| 3.8. | Accessibility (Barrier-Free Design) | 318 |

Use `scripts/lookup.py <section>` to resolve pages for anything above marked "—".

## High building (Subsection 3.2.6.)

Triggered by height from lowest fire-truck access level or storey count thresholds. Read **Article 3.2.6.1.** for the exact definition. Triggers: mechanical smoke control, emergency power, voice communication, firefighter elevators, two-way communication, enhanced firefighting access.

## Post-disaster building

Defined term in Division A, Article 1.4.1.2. (p.52). Drives seismic importance category, structural redundancy, sometimes construction type. Check Part 4 (Structural) Subsection 4.1.8. (earthquake) and the specific occupancy's 3.2.2.x article — many articles prohibit combustible construction for post-disaster buildings.

## Pull the authoritative text

```
python3 scripts/lookup.py 3.2.2.48              # Group C, 12 storeys EMTC
python3 scripts/lookup.py 3.1.6                 # EMTC subsection
python3 scripts/lookup.py 3.4.2.4               # travel distance
python3 scripts/lookup.py 3.2.6                 # high buildings
python3 scripts/lookup.py 3.2.3                 # spatial separation
python3 scripts/lookup.py --search "firewall"
python3 scripts/lookup.py --search "sprinklered"
```

Always end with: *"Construction type and life-safety decisions should be confirmed with a code consultant and the AHJ under the province/territory's adopted building code (NBC is a model code; the actual enforced code may differ). The 2020 cycle introduced EMTC and new Part 2 for farm buildings — verify against the current article and check the bundled 2025 Revisions & Errata package, not memory."*
