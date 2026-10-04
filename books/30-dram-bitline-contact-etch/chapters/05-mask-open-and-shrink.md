# Chapter 5 — Mask Open and CD Shrink

## 5.1 Why shrink

Lithography prints contact holes most reliably at a diameter well above the one the cell wants. A 42 nm printed hole has better dose latitude, depth of focus and local CD uniformity (LCDU) than a 32 nm one. The extra 10 nm is removed by the etch, which narrows the hole as it transfers it into the carbon hard mask. This **CD shrink** is the first thing the DC etch has to do, and it is the main control on the final contact size.

## 5.2 How the shrink is made

Two mechanisms are used, often together:

- **Polymer deposition on the walls.** During the SiON open, a polymerising fluorocarbon (CHF₃, CH₂F₂) coats the walls of the resist and SiON hole. During the carbon open, gases such as CH₄, COS or a small CHF₃ addition to an O₂ or N₂/H₂ plasma deposit carbon or sulphur-containing passivation on the carbon walls faster than ions can remove it. The hole narrows by the passivation thickness on each side.
- **Taper.** If the walls are passivated faster than the floor is etched sideways, the carbon wall slopes inward. A carbon layer 110 nm thick with a wall angle of 87.4° narrows a hole by 2 × 110 × cot 87.4° ≈ 10 nm.

In the reference process the hole leaves the carbon at 32 nm. The buffer etch then tapers it further to 26 nm at the silicon surface (Chapter 9).

## 5.3 Shrink and local CD uniformity

A shrink of fixed thickness, applied to every hole, reduces the mean CD but not its spread. If the deposition fills small holes relatively faster than large ones, as it does when the passivation flux depends on the hole's view of the plasma, the shrink also compresses the spread. A hole that prints small sees less passivant per unit wall area and narrows less. In practice, the hole-to-hole 3σ falls from about 2.5 nm after lithography to about 1.5–2 nm after the carbon open. The CD scatter used in Chapter 14 (σ = 1 nm at the buffer top) assumes this.

The shrink cannot compress errors that come from the mask itself or from placement. Overlay is untouched by shrink. A smaller hole tolerates less of it (Chapter 10).

## 5.4 The carbon budget

The carbon mask must survive the buffer open and the recess. Fluorocarbon chemistries (recipes B and C, and the buffer open) erode carbon at perhaps a fifth to a tenth of the oxide rate. HBr/Cl₂/O₂ (recipe A) erodes it slowly, because the oxygen content is small. A 110 nm carbon layer typically arrives at the recess step with 60–80 nm left; the reference value is 70 nm. Facets at the top corners of the carbon widen the top of the hole as it erodes, but at these thicknesses faceting rarely reaches the buffer.

The mask height matters to the floor more than to the mask. As Chapter 4 showed, 70 of the 90 nm the floor sits below the mask top is carbon. Every 10 nm of carbon removed lowers the aspect ratio by about 0.4 and raises the neutral flux to the floor by roughly 20 % at *s* = 0.1. Mask erosion during a long recess therefore speeds it up slowly. This drift is ignored in the model, which holds the mask at 70 nm.

## 5.5 Striations and hole shape

Resist line-edge roughness becomes hole-edge roughness. Polymerising shrinks smooth it somewhat. Elliptical holes are common at the DC because the active area is tilted and some lithography schemes print the DC as the crossing of two line patterns. An ellipse 34 × 28 nm aligned with the active area places more of the floor on the node and less on the word-line caps than a circle of the same area. The model in this book uses circles. The same geometry routines handle ellipses with a change of coordinates.

## 5.6 Monitoring

The shrink is monitored by CD-SEM after the carbon open (on a sample of holes per die) and after the full etch on dedicated metrology. Because the bottom CD at the silicon surface cannot be seen by top-down SEM once the hole is deep, it is inferred. The inference uses the top CD and the buffer taper, calibrated by cross-section (Chapter 13).
