# Workflow — Occupancy Classification

**When to use this guide:** the user describes a building or space ("a 1,200 m² daycare", "a warehouse with a small office") and needs the major occupancy group, or they're trying to figure out mixed-use implications.

Authoritative text lives in **Division B, Section 3.1.2.** (p.146 of the PDF). Read the PDF. This file is a navigation + mental-model aid, not a substitute.

## The six major occupancy groups (Table 3.1.2.1.)

| Group | Division | Description |
|---|---|---|
| **A** | 1 | Assembly — production and viewing of performing arts |
| **A** | 2 | Assembly — not elsewhere classified in Group A |
| **A** | 3 | Assembly — arena type |
| **A** | 4 | Assembly — open air |
| **B** | 1 | Detention |
| **B** | 2 | Treatment |
| **B** | 3 | Care |
| **C** | — | Residential |
| **D** | — | Business and personal services |
| **E** | — | Mercantile |
| **F** | 1 | High-hazard industrial |
| **F** | 2 | Medium-hazard industrial |
| **F** | 3 | Low-hazard industrial |

Each group's divisions matter — they drive construction-type requirements, sprinklering, fire load. See **Table 3.1.2.1.** in the PDF (`python3 scripts/lookup.py 3.1.2.1`).

## Workflow

1. **Start with Article 3.1.2.1. and Table 3.1.2.1.** — `python3 scripts/lookup.py 3.1.2.1` then read that page (PDF p.146).
2. **Identify the major occupancy** — the principal use of the building or fire compartment. Don't over-index on ancillary spaces.
3. **Check for multiple major occupancies** — if two or more groups qualify as "major" (not just incidental), read **Subsection 3.1.3.** (p.147). This drives whether the building must be separated by fire separations with specific ratings (Table 3.1.3.1.), or designed to the most restrictive occupancy.
4. **Check the special reclassification articles** — Articles 3.1.2.3. through 3.1.2.6. permit reclassification in specific cases:
   - 3.1.2.3. Arena-type buildings for occasional trade-show use → Group A-3.
   - 3.1.2.4. Police stations with detention quarters → Group B-2 if ≤ 1 storey and ≤ 600 m².
   - 3.1.2.5. Convalescent and children's custodial homes (ambulatory, ≤ 10 persons, single housekeeping unit) → Group C.
   - 3.1.2.6. Baled combustible fibres storage → medium-hazard industrial.
5. **B-1, B-2, B-3 distinctions.** "Care occupancy" and "treatment occupancy" are defined terms in Division A 1.4.1.2. — look them up (`python3 scripts/lookup.py 1.4.1.2`). The distinction between B-2 (treatment) and B-3 (care) affects egress, alarms, and sprinkler trade-offs significantly.
6. **Industrial hazard levels** — F-1 (high-hazard), F-2 (medium-hazard), F-3 (low-hazard). Driven by the flammability / combustibility of contents, not the building type alone. "High-hazard industrial occupancy", "medium-hazard industrial occupancy", and "low-hazard industrial occupancy" are each defined terms.
7. **Farm buildings** — the new **Division B, Part 2** (NBC 2020) applies. See Article 2.1.4. for farm-building classification.

## Common traps

- **A daycare is Group A, Division 2**, not Group B. A daycare "feels" like a care occupancy, but a daycare facility for children is classified as A-2 (Assembly, not elsewhere classified). Group B-3 (care) is for residents who live on site (group homes, certain children's custodial homes) — a daycare is not B-3.
- **Group A in a small building kicks it to Part 3.** Part 9 is only available when every major occupancy is Group C, D, E, F-2, or F-3 (Article 1.3.3.3., Division A). Adding any Group A, B, or F-1 use — even a small one — pulls the whole building into Part 3.
- **Offices inside industrial buildings** — usually ancillary / subsidiary if small. Large enough offices become a separate major occupancy requiring multi-occupancy treatment under 3.1.3.
- **Live/work** — check the major-occupancy test carefully; dwelling-unit vs business-use separation requirements can be non-trivial.
- **Restaurants** — A-2 typically; a small café inside a retail store (E) may be subsidiary.
- **Clinics** — outpatient medical is typically D (business, personal services); treatment with overnight stay is B-2.
- **Police station with cells** — special article (3.1.2.4.) permits B-2 under size limits, not B-1, which is important for trade-offs.

## Pull the authoritative text

```
python3 scripts/lookup.py 3.1.2.1              # Classification of Buildings (Table 3.1.2.1.)
python3 scripts/lookup.py 3.1.2                # All classification articles
python3 scripts/lookup.py 3.1.3                # Multiple Occupancy Requirements
python3 scripts/lookup.py 1.4.1.2              # Defined Terms (Division A)
python3 scripts/lookup.py --search "occupancy"
```

Always end with: *"Classification should be confirmed with the Authority Having Jurisdiction and your code consultant under the province/territory's adopted building code (NBC is a model code). The 2025 Revisions & Errata package may also affect classification articles — check before relying on this for a permit submission."*
