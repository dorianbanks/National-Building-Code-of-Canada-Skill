# Workflow — Part 9 (Housing and Small Buildings)

**When to use this guide:** single-family houses, duplexes, small multi-family, small commercial (≤ 600 m² building area, ≤ 3 storeys). Also secondary suites.

## Scope test (Division A, Article 1.3.3.3.)

Part 9 applies if **all** of the following are true:
- Building ≤ 3 storeys in *building height*, **and**
- Building area ≤ 600 m², **and**
- Major occupancies limited to Group C (residential), D (business), E (mercantile), or F-2 / F-3 (medium-/low-hazard industrial), **and**
- Not a post-disaster building, not a high building.

If any one fails, Part 3 applies. Watch for:
- **Any Group A, B, or F-1 occupancy** → Part 3 (Part 9's occupancy list is closed to C/D/E/F-2/F-3).
- **Mass timber mid-rise residential** — Part 3, not Part 9 (EMTC lives in Subsection 3.1.6., referenced from 3.2.2.48 for Group C up to 12 storeys).
- **Farm buildings** — **Division B, Part 2** (new in NBC 2020), not Part 9, per Article 1.3.3.5.

## Part 9 — complete section list

| Section | Topic | Starts at p. |
|---|---|---|
| 9.1. | General (incl. floor-area limits for secondary suites at 9.1.2.1.) | 823 |
| 9.2. | Definitions | 823 |
| 9.3. | Materials, Systems and Equipment (concrete, lumber, wood, masonry, glass) | 823 |
| 9.4. | Structural Requirements (loads, deflection, site investigation, seismic) | 828 |
| 9.5. | Design of Areas and Spaces (room sizes, ceiling heights, barrier-free) | 832 |
| 9.6. | Glass (safety glazing, areas) | 834 |
| 9.7. | Windows, Doors and Skylights | 838 |
| 9.8. | Stairs, Ramps, Handrails and Guards | 843 |
| 9.9. | Means of Egress | 855 |
| 9.10. | Fire Protection (separations, flame-spread, smoke alarms, sprinklers) | 867 |
| 9.11. | Sound Transmission | 905 |
| 9.12. | Excavation | 907 |
| 9.13. | Dampproofing, Waterproofing and Soil Gas Control | 909 |
| 9.14. | Drainage | 914 |
| 9.15. | Footings and Foundations | 916 |
| 9.16. | Floors-on-Ground | 925 |
| 9.17. | Columns | 927 |
| 9.18. | Crawl Spaces | 929 |
| 9.19. | Roof Spaces | 931 |
| 9.20. | Masonry and Insulating Concrete Form Walls Not In Contact with the Ground | 932 |
| 9.21. | Masonry and Concrete Chimneys and Flues | 947 |
| 9.22. | Fireplaces | 952 |
| 9.23. | Wood-Frame Construction (the bread-and-butter section) | 954 |
| 9.24. | Sheet Steel Stud Wall Framing | 983 |
| 9.25. | Heat Transfer, Air Leakage and Condensation Control | 986 |
| 9.26. | Roofing | 992 |
| 9.27. | Cladding | 1003 |
| 9.28. | Stucco | 1016 |
| 9.29. | Interior Wall and Ceiling Finishes | 1020 |
| 9.30. | Flooring | 1026 |
| 9.31. | Plumbing Facilities | 1029 |
| 9.32. | Ventilation | 1031 |
| 9.33. | Heating and Air-conditioning | 1045 |
| 9.34. | Electrical Facilities | 1054 |
| 9.35. | Garages and Carports | 1056 |
| 9.36. | Energy Efficiency | 1058 |
| 9.37. | Objectives and Functional Statements (attribution tables) | 1103 |

> **Note:** NBC 2020 does **not** have a dedicated "secondary suite" section (contrast with some provincial adoptions). Secondary-suite requirements are distributed: floor-area limit (9.1.2.1.), sound transmission (9.11., see also A-9.11.1.1.(2)), separation (9.10.), smoke alarms (9.10.19.). NBC 2020 also does **not** include ADU provisions — those are a provincial amendment (e.g., BCBC 2024 added them).

## Common Part 9 question shapes

- **Stair and guard dimensions** — 9.8. (risers/treads/winders/landings), 9.8.8. (guards). Use `lookup.py 9.8.4` for riser/tread dimensions.
- **Egress windows / bedroom windows** — 9.9.10. (means of escape from dwelling units); sizing in 9.9.10.1.
- **Smoke alarms and CO alarms** — 9.10.19. (smoke), 9.32.3. (CO via ventilation, often reinforced in provincial amendments).
- **Spatial separation between houses** — 9.10.14. / 9.10.15.
- **Firewalls between dwelling units** (row housing) — 9.10.11.
- **Headroom, room sizes, natural light** — 9.5.
- **Energy efficiency** — 9.36. (interacts with provincial tiered-energy programs like BC Step Code, Ontario SB-10/12).
- **Secondary suite floor area and separation** — 9.1.2.1. (area), 9.10. (fire separations), 9.11. (sound).

## Pull the authoritative text

```
python3 scripts/lookup.py 9.8.4                 # stair riser/tread dimensions
python3 scripts/lookup.py 9.9.10.1              # egress window sizing
python3 scripts/lookup.py 9.10.19               # smoke and CO alarms
python3 scripts/lookup.py 9.1.2.1               # secondary suite floor-area limits
python3 scripts/lookup.py 9.23                  # wood-frame construction
python3 scripts/lookup.py --search "secondary suite"
```

Always end with: *"Part 9 includes many prescriptive values (stair risers, window sizes, joist spans) that should be confirmed against the current article. The NBC is a model code — the project's province/territory (e.g., BCBC, ABC, OBC) may amend these provisions. Check the bundled 2025 Revisions & Errata package, and confirm with the AHJ before construction."*
