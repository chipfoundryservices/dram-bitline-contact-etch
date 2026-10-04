# Chapter 14 — The Variation Budget

## 14.1 The model

Four sources of variation are sampled per contact in a Monte Carlo of 200 000 contacts:

- **top CD** at the buffer top, nominal 32 nm, standard deviation σ_CD;
- **buffer sidewall angle**, nominal 81.5°, standard deviation σ_θ, which turns into bottom-CD scatter through *D*_b = *D*_t − 2*H*_buf cot θ;
- **overlay** of the DC to the active area, independently in *x* and *y*, each with standard deviation σ_ov;
- **node scale**: all lateral dimensions of the cell and the hole multiplied by 1, 0.88 or 0.76 (F = 17, 15, 13 nm), with the variation kept as stated.

For each contact the model computes the area on the node, the resistance *R*_DC = ρ_c/*A* + plug, and the clearance from the hole edge to the nearest neighbouring active-area strip. A contact **fails high** if *R*_DC > 10 kΩ. It **touches** a neighbour if the clearance is below zero. In the scaled rows, ρ_c is multiplied by the stated factor to represent interface improvements.

## 14.2 Results

{{TABLE:var}}

## 14.3 Reading the table

- **CD and angle barely matter at the reference node.** A 1 nm (1σ) top-CD scatter gives an area scatter of only 2 nm². A 1° angle scatter gives 0.72 nm of bottom-CD scatter but only 1.6 nm² of area scatter. The 26 nm hole is node-limited (Chapter 10). Its area is set by the node, not by the hole.
- **Overlay dominates.** A 2 nm (1σ per axis) overlay alone gives an area scatter of 7.5 nm² and lowers the mean area by 7 nm². Combined with modest CD and angle scatter (1 nm, 0.5°), it yields about 10 ppm of high-resistance contacts and no touches in 200 000.
- **Poor control is catastrophic.** At 1.5 nm, 1° and 3 nm, the high-resistance rate is 0.5 % and touches appear at about 400 ppm.
- **Shrinking the node without shrinking overlay fails.** At F = 15 nm with the same variation and the same interface, the area falls to 204 nm². The median resistance rises to 8.2 kΩ, and 0.8 % of contacts exceed 10 kΩ. A 40 % lower ρ_c restores the median to 5.3 kΩ and the tail to about 5 ppm. At F = 13 nm, even a halved ρ_c leaves 275 ppm high and 25 ppm touching. Only when CD, angle and overlay variation scale down with the node (×0.7) do both failure rates vanish from the sample.

## 14.4 How many failures can be tolerated

A 16 Gb die has 8 × 10⁹ bit-line contacts, each serving two cells. Redundancy can repair failing bits at a rate of perhaps 10⁻⁶ to 10⁻⁵, depending on clustering. A DC failure rate of 10 ppm (10⁻⁵) consumes all of it. The rows that pass in this table are therefore only just acceptable. The model's resolution is one failing contact in 200 000, or 5 ppm, so rates of 5–25 ppm rest on one to five events. A production budget needs margin well below the table's resolution. It must be set by extrapolating the tail (for example from the Gaussian margin-to-failure in units of σ), not by counting.

## 14.5 Allocating the budget

The area is approximately a function of the radial overlay *o* = √(*o*ₓ² + *o*ᵧ²) once the hole is node-limited. It stays near the node area until *o* reaches the "free" overlay *o*_f, where the hole edge reaches the node corner, and falls beyond it. For the 26 nm hole *o*_f is about 3–4 nm. If *o* has Rayleigh distribution with scale σ_ov, the probability of exceeding a radial error *o*_c is exp(−*o*_c²/2σ_ov²). With *o*_c ≈ 10 nm (where *A* reaches 164 nm² along either axis) and σ_ov = 2 nm, this is exp(−12.5) ≈ 4 × 10⁻⁶, consistent with no failures in the overlay-only row. Adding CD and angle scatter moves the failure boundary inward and brings the rate up to the 10 ppm of the combined row. Because the exponent scales as 1/σ_ov², each 10 % reduction in σ_ov multiplies it by 1.23, which at this margin cuts the failure rate about twentyfold.

The etch owns the bottom CD (through the buffer taper) and the recess. Lithography owns the top CD and overlay. The budget is best allocated by keeping the hole node-limited, so that CD is cheap, and spending the margin on overlay.

## 14.6 What is not in the model

The model leaves out recess-depth variation, which matters through ρ_c via the doping profile (Chapter 10). It also leaves out the shape of the hole outline (striations, ellipticity) and within-node doping variation. Each adds scatter to the resistance. The model treats every contact independently. Real overlay errors are correlated over a field, so failures cluster, and clustering changes what redundancy can repair.
