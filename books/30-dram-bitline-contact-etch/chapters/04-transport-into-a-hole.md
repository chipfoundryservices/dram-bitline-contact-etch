# Chapter 4 — Transport into a Contact Hole

## 4.1 The geometry

At the start of the recess, the floor of the DC lies under 70 nm of carbon mask and 20 nm of buffer. For a 26 nm hole the aspect ratio, measured from the top of the mask, is 90/26 = 3.5. By the end of a 25 nm recess it is about 4.4 for a flat floor. Gas pressures are a few to tens of millitorr, so the mean free path (millimetres) is far larger than the hole. Transport inside it is in the **Knudsen regime**, and particles collide only with walls.

## 4.2 Neutrals

A neutral enters the hole with a cosine angular distribution. At each wall hit it is lost (reacts or recombines) with probability *s*. Otherwise it is re-emitted diffusely. The floor fraction is the fraction that reaches the floor. For *s* = 1 it equals the view factor from the opening to the floor, which for a cylinder of depth *H* and radius *r* is

F = ½ (X − √(X² − 4)),  X = 2 + 4 AR²,  AR = *H* / 2*r*.

The Monte Carlo reproduces this limit within counting error at every aspect ratio (Appendix A).

## 4.3 Ions

Ions arrive nearly perpendicular to the wafer. Their angular spread σ is set by the sheath and the ion temperature, about 2° at the higher bias of recipes B and C and about 4° at the low bias of recipe A. In the model an ion travels in a straight line and is lost on any wall hit. Because the hole is convex, an ion reaches the floor exactly when its landing point lies inside the floor disk. Specular reflection and charging, which can deflect ions, are neglected.

{{FIG:transport}}

## 4.4 A hole is harder than a slot

A round hole restricts transport in two directions; the slot between two bit lines (Book 29) restricts it in one. The exact line-of-sight fractions compare as follows:

{{TABLE:holeslot}}

At AR = 4, a slot passes eight times as many line-of-sight neutrals to its floor as a hole of the same aspect ratio. Diffuse re-emission (*s* < 1) narrows the gap, but the hole still loses. With *s* = 0.1, 8 % of neutrals reach the floor at AR = 4, against about 14 % at AR = 3. Ions are affected less. At σ = 2° the floor fraction is 78 % at AR = 4. At σ = 4° it is 57 %.

## 4.5 Consequences for the DC

- **The mask dominates the aspect ratio.** 70 of the 90 nm above the floor is carbon. Thinning the mask at the start of the recess (or stripping it and using the buffer as the mask) moves the floor from AR ≈ 3.5 to AR ≈ 0.8. This changes the neutral-to-ion balance at the floor completely.
- **Neutral-driven etching slows most.** Recipe A depends more on neutrals than B or C. At AR 3.5 with *s* = 0.1 its neutral term is only 11 % of its open-field value, while the ion term is still about 62 %.
- **Sub-features see their own aspect ratio.** A silicon pit 16 nm wide and 25 nm deep has AR 1.6 of its own. A pit in the 3.5 nm gate-oxide liner reaches AR 5 after only 17 nm. Chapter 7 multiplies the hole and pit transport fractions to estimate each material's rate.

## 4.6 Limits of the model

The model treats a straight-walled cylinder. A tapered hole delivers slightly more flux to the floor. It also takes *s* as constant and independent of surface coverage, ignores flux re-emitted from the floor and etch products, and ignores charging. Charging matters more here than in the bit-line etch because the hole is lined by insulators down to the floor. Its effect, a deflection of low-energy ions toward the walls, would further reduce the ion fraction at small σ. Appendix B tabulates all transport values.
