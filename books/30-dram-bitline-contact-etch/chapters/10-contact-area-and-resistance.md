# Chapter 10 — Contact Area and Resistance

## 10.1 What the contact touches

The contact area is the part of the hole bottom that lands on the node silicon. With the node a 16 nm × 17.1 nm parallelogram (274 nm²), the area depends on the hole diameter *D* at the silicon surface and on the overlay (*o*ₓ, *o*ᵧ) between the hole and the active area. The model computes it by integrating over the disk. It also reports the node edge length inside the hole (relevant when the node stands as a mesa) and the clearance from the hole edge to the nearest neighbouring active-area strip.

## 10.2 Computed area against overlay

{{FIG:contact}}

{{TABLE:contact_short}}

Three regimes appear:

- **Node-limited.** For *D* ≥ 26 nm at zero overlay, the hole covers 99–100 % of the node. Area is then insensitive to CD. A 1 nm (1σ) CD scatter changes the area by only about 2 nm² (1σ) (Chapter 14).
- **Overlay-limited.** Overlay moves part of the node out from under the hole. A 26 nm hole tolerates about 4 nm of overlay in either axis with less than 6 % area loss. Beyond that the loss accelerates, to about 25 % at 8 nm. A 30 nm hole loses under 2 % at 4 nm and 3–6 % at 6 nm.
- **Hole-limited.** A 22 nm hole covers 95 % of the node at zero overlay (260 nm²), and its area falls from the first nanometre of overlay.

## 10.3 The price of a large hole

A larger hole buys area tolerance by spending clearance. At zero overlay the hole edge is 13.0 nm from the nearest neighbouring strip for *D* = 22, 11.0 nm for 26, and 9.0 nm for 30. Overlay along the word line (*y*) subtracts almost one-for-one: 0.93 nm of clearance per nanometre of overlay, because the strips are tilted. A 30 nm hole touches the neighbour at 10 nm of *y* overlay. A 26 nm hole would touch at about 12 nm. Overlay along the bit line (*x*) moves the hole toward the word-line caps instead, and costs clearance only slowly.

The DC diameter is therefore a trade between resistance (favours large) and neighbour isolation (favours small). The trade is resolved by the overlay distribution (Chapter 14).

## 10.4 From area to resistance

The resistance of the DC is modelled as

*R*_DC = ρ_c / *A* + ρ_poly *L* / (π*D*²/4),

with ρ_c = 1.5 × 10⁻⁸ Ω·cm² (1.5 × 10⁶ Ω·nm²), ρ_poly = 1 mΩ·cm and a plug length *L* = 45 nm. At *A* = 272 nm² the interface term is 5.5 kΩ and the plug about 0.85 kΩ, for 6.35 kΩ in all. The interface dominates. A 10 kΩ limit is reached when the area falls below 164 nm².

ρ_c is not a constant of nature. For a tunnelling contact it depends exponentially on the doping at the interface, roughly as exp(*C* φ_B / √*N*), with *C* ∝ √(ε_s *m*\*)/ħ. It also rises steeply with any interfacial oxide. Two etch choices feed it directly:

- **Recess depth against the doping profile.** The bit-line node is doped by implant and by phosphorus out-diffused from the poly plug. A deeper recess lands the interface where the implanted doping is lower, unless the out-diffusion anneal makes up the difference. A recess that is 5 nm too deep can raise ρ_c more than it gains in any other way.
- **Surface condition.** Damage, halogen and carbon residues, and re-grown native oxide all raise ρ_c (Chapter 11).

## 10.5 Sidewall contact on a mesa

When the node stands as a mesa (recipe C, or a short C step before A), its sidewalls add contact area. At *D* = 26 nm and zero overlay, 63 nm of node edge lies inside the hole. A mesa 5 nm tall then adds up to 315 nm² of sidewall, more than the top. The sidewall is a poorer contact. It is plasma-exposed, it lies deeper in the doping profile, and on two sides it faces the word-line gate oxide. If only half of it counts, the effective area becomes about 430 nm² and *R*_DC falls to about 4.3 kΩ. The cost is in Chapter 8: the dielectric-first step that makes the mesa also recesses the cap and drives the liner pit down. A shallow mesa, a few nanometres tall, captures much of the gain at a small cost in margin.

## 10.6 Elliptical and self-aligned contacts

A hole elongated along the active-area direction (Chapter 5) keeps more of its area on the node under overlay along the active area. It also keeps the edge farther from the neighbours across it. Self-aligned schemes go further. The DC is patterned as a line crossing the active areas, and the cap and STI act as the mask in one direction. Overlay in that direction then drops out of the area budget, at the price of requiring high selectivity of the floor etch to those materials. In effect this is recipe A by construction (Chapter 16).
