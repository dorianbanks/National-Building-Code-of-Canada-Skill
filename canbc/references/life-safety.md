# Workflow — Fire & Life Safety / Egress

**When to use this guide:** questions about occupant load, travel distance, exits, fire separations, fire-resistance ratings, sprinkler trade-offs, corridor widths, dead-end limits, stair pressurization.

Most life-safety provisions live in **Division B, Part 3**: Subsections 3.1.7 (ratings), 3.1.8 (fire separations), 3.3 (safety within floor areas), 3.4 (exits). Part 9 mirrors a simpler version in 9.9 and 9.10.

## Occupant load (Subsection 3.1.17.)

Drives exit sizing, number of exits, plumbing fixture count. Occupant load per m² varies by use — see **Table 3.1.17.1.** in Article 3.1.17.1. (PDF p.188).

Typical design occupant loads (always verify against the table):
- Assembly with fixed seats — 1 person / seat
- Assembly without fixed seats (standing / dining) — ~0.6–1.2 m² / person
- Classrooms — ~1.85 m² / person
- Office / business use — ~9.3 m² / person
- Mercantile ground floor — ~3.7 m² / person
- Residential — 2 persons / sleeping room (or based on occupants)
- Industrial / storage — varies up to ~46 m² / person for warehouse storage

## Exits — number, width, travel distance (Section 3.4)

- **Minimum number of exits.** Normally 2 from a floor area; Article 3.4.2.1. governs. Single-exit permitted only under specific small-building conditions.
- **Exit remoteness.** Article 3.4.2.3. — exits must be remote, typically a fraction of the diagonal of the floor area served.
- **Travel distance.** **Article 3.4.2.4.** (PDF p.288) — maximum distance from any point in a floor area to the nearest exit. The limit depends on occupancy and whether the building is sprinklered. Sprinklering generally extends the allowed distance.
- **Exit width.** Article 3.4.3.2. (PDF p.289) — based on occupant load served, with reductions for sprinklered buildings.
- **Exit stairs.** Minimum clear width between handrails; enclosed in a fire separation per Subsection 3.4.4.

## Dead-end corridors (Article 3.3.1.9., p.266)

Dead-end limits apply in public corridors serving more than one suite. Sprinklered buildings receive more permissive limits. Read 3.3.1.9. for the current values.

## Fire separations and firewalls

| Concept | Where | What it does |
|---|---|---|
| **Fire separation** | 3.1.8., 9.10.9. | Assembly that resists the passage of flame; may or may not have a fire-resistance rating |
| **Fire-resistance rating** | Table 3.1.7.1., 9.10.3.1. | Time rating (45 min, 1 h, 2 h, etc.) from standard test |
| **Firewall** | 3.1.10., 9.10.11. | Separates buildings from a code standpoint; continuous, structurally independent, usually 2–4 h |
| **Closure** | 3.1.8.10. | Doors, dampers, shutters in fire separations — rated closures |

## Spatial separation and exposing building face (Subsection 3.2.3., p.223)

Drives **limiting distance**, **percent glazing permitted**, **fire-resistance rating of exterior wall**, **combustibility of cladding**. Key tables:
- **Table 3.2.3.1.B** — unsprinklered
- **Table 3.2.3.1.C** — sprinklered

Part 9 mirrors this at Articles 9.10.14. and 9.10.15.

## Fire alarms and detection (Section 3.2.4., 9.10.18.)

- Required in most Part 3 buildings above thresholds.
- Single-stage vs two-stage signalling — detailed in 3.2.4.
- Voice communication required in high buildings (3.2.6.).

## Sprinklers — trade-offs

Sprinklering unlocks many trade-offs throughout the code:
- Increased building area and height allowances in 3.2.2.x. (most articles have a "sprinklered" version).
- Reduced fire-resistance ratings in some assemblies.
- Longer travel distance in 3.4.2.4.
- Larger dead-end corridors in 3.3.1.9.
- Reduced spatial-separation glazing restrictions (Tables 3.2.3.1.B vs .C).
- Required in EMTC buildings (Subsection 3.1.6.) and most Group C buildings over 3 storeys.

See Section **3.2.5.** for fire-fighting provisions and NFPA 13 / 13R / 13D references.

## Accessibility — interacts with life safety (Section 3.8, p.318)

NBC 2020 places accessibility in Division B, Section 3.8 (Barrier-Free Design). Key for egress:
- **3.8.1.** Scope & definitions
- **3.8.2.** Occupancy requirements
- **3.8.3.** Design standards (PDF p.322) — includes areas of refuge and accessible means of egress

## Pull the authoritative text

```
python3 scripts/lookup.py 3.1.17.1              # occupant load table
python3 scripts/lookup.py 3.4.2.4               # travel distance
python3 scripts/lookup.py 3.4.3.2               # exit width
python3 scripts/lookup.py 3.3.1.9               # dead-end corridors
python3 scripts/lookup.py 3.2.3                 # spatial separation subsection
python3 scripts/lookup.py 3.8                   # accessibility
python3 scripts/lookup.py --search "fire alarm"
python3 scripts/lookup.py --search "sprinklered"
```

Always end with: *"Life-safety calculations (occupant load, exit width, travel distance) should be confirmed by a code consultant and reviewed by the AHJ. The NBC is a model code — the enforced provincial/territorial code (BCBC, ABC, OBC, etc.) may amend these provisions. Check the bundled 2025 Revisions & Errata package before relying on any article."*
