# Chapter 13 — Reactor, Recipe, Endpoint and Metrology

## 13.1 One chamber or two

The DC etch spans two kinds of chemistry. The mask open, buffer open and any fluorocarbon floor step (B or C) belong in a **dielectric etch chamber**, usually a capacitively coupled reactor with a high-frequency source and a low-frequency bias. The silicon-selective recess (A) belongs in a **conductor etch chamber**, an inductively coupled reactor with an independent bias, often pulsed. Three arrangements are common:

- **two chambers**: mask and buffer in a dielectric chamber, recess in a conductor chamber on the same platform, with a vacuum transfer between them;
- **one dielectric chamber**: all steps fluorocarbon-based, with the floor recess done by recipe B and a short HBr-free silicon step. This is simpler, but it pays in cap and liner margin;
- **one conductor chamber**: mask and buffer opened in an ICP with fluorocarbon gases, then HBr/Cl₂ for the recess. This is possible because the buffer is thin, but polymer memory effects between steps must be managed by in-situ cleans.

## 13.2 An illustrative recipe

| Step | Gases | Pressure | Source / bias | Time | Purpose |
|---|---|---|---|---|---|
| SiON open | CF₄/CHF₃ | 10 mT | 600 W / 150 W | EP + 20 % | transfer |
| carbon open + shrink | O₂/COS/Ar (+ CH₄) | 8 mT | 800 W / 200 W | EP + 30 % | transfer, shrink 42 → 32 nm |
| buffer main | CF₄/CHF₃/O₂/Ar | 15 mT | 500 W / 300 W | EP (CN drop) | open SiN |
| buffer over | CHF₃/Ar | 15 mT | 500 W / 250 W | 4 s | clear oxide, taper |
| recess | HBr/Cl₂/O₂ | 10 mT | 500 W / 60 W, pulsed | 46 s | Si recess 25 nm (A) |
| light etch | CF₄/O₂ downstream | 300 mT | 800 W / 0 W | 5 s | remove 1–2 nm damage |
| strip | N₂/H₂ | 500 mT | 2500 W / 0 W | 30 s | remove carbon, polymer |

All values are illustrative starting points for a designed experiment, not qualified conditions.

## 13.3 Endpoint

The SiON, carbon and buffer-nitride steps endpoint on optical emission. The DC open area is large (15–23 % of the array) and the transitions are clean: SiON to carbon (CO rises), carbon to SiN (CO falls, CN rises), SiN to oxide (CN falls). The oxide-to-floor transition is ambiguous because the floor is mixed (Chapter 6), so the last nanometres of buffer are timed.

The recess has no endpoint. Nothing in the plasma changes when the silicon passes 25 nm. It is run on time, with two corrections:

- **feed-forward from CD.** In recipe A the recess at a fixed time moves by 0.55 nm per nanometre of bottom CD (Chapter 7). At a rate of about 0.5 nm/s, this is about 1.1 s of time per nanometre of CD. A lot-average CD measured after the carbon open can be fed forward to the recess time;
- **feedback from recess metrology**, by scatterometry on array targets or by sampled cross-section. This corrects slow drifts of rate with chamber condition.

## 13.4 Chamber condition

HBr/Cl₂/O₂ deposits SiOₓBrᵧ on the chamber walls. Fluorocarbon steps deposit polymer. When both run in one chamber, each step's walls become the next step's initial condition. A waferless clean (SF₆/O₂ or NF₃) between wafers, followed by a short seasoning, keeps the first-wafer effect small. The recess rate is especially sensitive to wall state, because recipe A's neutral term depends on the recombination of Br and Cl on the walls.

## 13.5 Metrology

| What | How | When |
|---|---|---|
| top CD | CD-SEM | after carbon open, after etch |
| bottom CD | high-voltage SEM, OCD | after strip |
| Si recess, cap and STI recess | OCD on array targets; AFM after strip | per lot |
| profile, liner pit, pit shape | TEM / STEM-EDS cross-sections along BL and WL | sampled |
| residue, oxide | XPS on blanket monitors; STEM-EELS | qualification |
| opens | e-beam voltage-contrast inspection after poly CMP | per lot, sampled |
| resistance | Kelvin DC chains, DC-to-AA test structures | at electrical test |
| shorts | BL–WL and DC–SN comb structures | at electrical test |

Voltage-contrast inspection is the fastest in-line check of the DC. After the poly CMP, a well-connected plug charges differently from an open one under the electron beam and appears bright or dark. An open or high-resistance DC therefore shows up days before electrical test.

## 13.6 What to control

The variation budget (Chapter 14) shows that overlay dominates the DC's failure rate and that CD matters less. The etch controls the bottom CD through the buffer taper, and the recess depth through time. Its main levers on yield are to keep the hole near the node-limited regime, so that area is insensitive, and to keep the cap and liner margin intact, so that the word line is safe.
