# Chapter 3 — Etch Chemistry of a Mixed Floor

## 3.1 Three materials, three chemistries

A fluorocarbon plasma etches oxide and nitride well. A bromine–chlorine plasma etches silicon well. No single chemistry etches silicon, oxide and nitride at the same rate across the range of ion energy and polymer coverage met in production. The DC recess step chooses which material leads.

## 3.2 Fluorocarbon etching of oxide and nitride

In CF₄, CHF₃, C₄F₆ or C₄F₈ plasmas, a fluorocarbon film forms on all surfaces. Ions mix it into the substrate and drive the reactions. On SiO₂, the oxygen released from the film consumes carbon, so the film stays thin and etching proceeds. On silicon, no oxygen is released, the film thickens and etching slows. This is the basis of oxide-to-silicon selectivity. On SiN, nitrogen leaves as CN and the film is intermediate, so nitride etch rates lie between oxide and silicon. Hydrogen (CHF₃, CH₂F₂) increases nitride etching relative to oxide. Lean gases (CF₄, O₂ added) reduce selectivity overall.

Three regimes are useful at the DC floor:

- **Lean (CF₄/CHF₃/Ar, high ion energy):** oxide, nitride and silicon at comparable rates. This is the co-recess family, labelled B in this book.
- **Polymerising (C₄F₆/O₂/Ar):** oxide fast, nitride moderate, silicon very slow. This is the dielectric-first family, C.
- **Hydrofluorocarbon (CH₂F₂/O₂, CH₃F/O₂):** nitride faster than oxide. It is used for the SiN part of the buffer.

## 3.3 Halogen etching of silicon

In HBr/Cl₂/O₂, silicon etches as SiBrₓ and SiClₓ. The products are volatile at room temperature under ion bombardment. Oxide and nitride etch slowly because the Si–O and Si–N bonds are stronger and oxygen passivates the surface. Selectivities of 30:1 to silicon over oxide are routine at low bias. This is the silicon-selective family, A. Oxygen added to the plasma forms a thin SiOₓBrᵧ layer on the sidewalls that keeps the pit anisotropic. Too much oxygen grows an oxide on the floor that stops etching.

## 3.4 The illustrative recipe set

The simulation (Chapter 7) uses these open-field rates, each split into an ion-driven and a neutral-driven part (nm/s):

| Recipe | Si (ion / neutral) | SiO₂ | SiN | σ ion (°) | s neutral |
|---|---|---|---|---|---|
| A — Si-selective HBr/Cl₂/O₂ | 0.90 / 0.60 | 0.03 / 0 | 0.06 / 0.01 | 4 | 0.1 |
| B — co-recess CF₄/CHF₃/Ar | 0.70 / 0.20 | 0.80 / 0.05 | 0.75 / 0.10 | 2 | 0.3 |
| C — dielectric-first C₄F₆/O₂/Ar | 0.08 / 0.02 | 1.00 / 0.05 | 0.60 / 0.05 | 2 | 0.3 |
| buffer open, CF₄/CHF₃ (SiN/SiO₂) | — | 1.20 / 0.15 | 1.20 / 0.15 | 2 | 0.3 |

Recipe A runs at low bias (wider ion angular distribution σ) and with a less sticky etchant (wall loss *s* = 0.1). B and C run at higher bias with stickier fluorocarbon radicals. These numbers are illustrative. They have plausible ratios, and they are chosen to show how a selectivity becomes a floor shape.

## 3.5 Selectivity in a pit is not selectivity in the open

Selectivity measured on blanket films is a ratio of open-field rates. At the DC floor, each material sits at a different depth and in a patch of different width. The silicon node is 16 nm wide, STI patches about 8 nm, cap lunes about 5 nm, and the gate-oxide liner 3.5 nm. A material that etches faster forms a pit. Transport into that pit falls as it deepens (Chapter 4), so its rate drops. The effective selectivity at the end of the step is therefore lower than the blanket value, and lowest for the narrowest patches. Chapter 7 computes this.

## 3.6 Residues

Each family leaves its own residue. HBr/Cl₂/O₂ leaves bromine and chlorine in a thin oxidised layer on the silicon. Fluorocarbon chemistries leave a carbon–fluorine film on the floor and fluorine in the top nanometres of silicon. Both raise contact resistance if not removed. Chapter 11 discusses the strip and clean that remove them.

## 3.7 Temperature

Silicon etch in HBr/Cl₂ is weakly temperature dependent. Fluorocarbon polymer deposition is strongly temperature dependent: colder surfaces collect more polymer, raising selectivity and slowing oxide. A radial temperature profile across the chuck therefore becomes a radial profile of floor shape. Recipe C is the most sensitive, recipe A the least.
