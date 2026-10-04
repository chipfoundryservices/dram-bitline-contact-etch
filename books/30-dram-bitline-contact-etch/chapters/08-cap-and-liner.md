# Chapter 8 — The Word-Line Cap and the Gate-Oxide Liner

## 8.1 What lies beneath

On either side of the node, the DC hole overhangs a buried word line. In the reference process the hole's edge, 13 nm from the node centre, lies 1.5 nm beyond the inner edge of the word-line metal at |*x*| = 11.5 nm. That metal edge is the 8 nm node half-length plus the 3.5 nm gate oxide. A 6 nm overlay error along the bit line puts the hole edge over half of the 11 nm metal slot on one side. Between the bottom of the DC and the top of the word-line metal there is only the cap nitride, 60 nm in the incoming stack. Along the trench wall there is also the gate-oxide liner.

Whatever the DC etch removes from the cap and liner is margin taken from the separation between the n⁺ poly plug (at bit-line potential) and the word line (switching between about −0.3 V and the boosted level V_PP ≈ 3 V).

## 8.2 Computed cap and liner attack

{{FIG:liner}}

With recipe A, the cap and liner lose less than 2 nm at the 25 nm silicon target, and the margin is essentially the incoming 60 nm. With recipe B, the cap loses 26 nm and the liner 28 nm by the time the silicon reaches 25 nm. That leaves 34 nm of cap over the metal. With recipe C run for 60 s, the cap loses 25 nm, but the liner pit runs 10 nm deeper, to 35 nm, leaving 25 nm between its tip and the metal.

## 8.3 Why the liner runs ahead

The liner is oxide, and recipe C etches oxide 1.7 times faster than nitride. It is also only 3.5 nm wide, so its pit enters the high-aspect-ratio regime almost at once. At a pit depth of 10 nm relative to the node, its own AR is already 2.9. These two effects oppose each other. Faster chemistry drives the liner down, and narrow-pit transport slows it. In the model the chemistry wins: the liner gains about 10 nm on the cap in 60 s. In a real process, the fluorocarbon film that deposits in a 3.5 nm slit is uncertain. Slit charging may also deflect ions into it or away from it. The real liner pit may run faster or slower than the model, and it should be measured by cross-section.

Recipe B shows the same effect more weakly. Its liner runs 1 nm ahead of the cap, because B's oxide and nitride rates are close.

## 8.4 What the margin protects

- **Dielectric integrity.** With 3.3 V across a 34 nm nitride cap, the mean field is 1 MV/cm. At the tip of a poly-filled liner slit it is several times higher. Time-dependent breakdown of the cap between bit line and word line is a reliability failure that grows with every nanometre lost.
- **Word-line-to-bit-line leakage.** Even below breakdown, trap-assisted conduction through a thin nitride adds leakage on the bit line. That leakage depends on which word line is active, and it is hard to tell apart from cell leakage.
- **Gate-induced drain leakage at the bit-line node.** n⁺ poly reaching down the liner toward the word-line top brings the bit-line potential closer to the gate edge. This raises the band-to-band tunnelling field in the overlap region of the bit-line-side junction.
- **Capacitance.** The added coupling is small. A few hundred nm² facing the word line through 30 nm of nitride is a fraction of an attofarad per contact. Even several hundred contacts per bit line add well under 1 % of the bit-line capacitance. Capacitance is not the reason to protect the cap.

## 8.5 The budget

An illustrative cap budget, from the 60 nm over the metal:

| Contributor | Loss (nm) |
|---|---|
| cap CMP below Si surface (incoming) | 0–3 |
| buffer overetch (Chapter 6) | 2–3 |
| recess step: A / B / C (to 25 nm Si or 60 s) | 2 / 26 / 25 |
| liner excess over cap: A / B / C | 0 / 1 / 10 |
| post-etch clean (dHF on oxide liner) | 1–2 |
| **remaining over metal, worst case: A / B / C** | **≈ 50 / ≈ 25 / ≈ 17** |

With a minimum of 30 nm, recipe A passes easily. Recipe B passes only with the shallowest incoming caps and the shortest clean. Recipe C fails unless it is cut to a short first step. This is why silicon-selective recesses dominate the DC, and why dielectric-first steps are kept short.

## 8.6 Overlay along the bit line

All of the above assumes the hole edge lies over the metal only near its inner edge. An overlay error along the bit line moves the hole over more of the metal on one side. The vertical margin is then the only protection over a larger area. Cap loss and DC-to-word-line overlay should therefore be budgeted together: a deep cap recess is tolerable only if overlay keeps the hole's edge near the trench wall.
