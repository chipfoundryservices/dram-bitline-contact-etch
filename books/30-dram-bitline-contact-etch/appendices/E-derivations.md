# Appendix E — Derivations

## E.1 View factor of a cylinder's floor from its opening

For two coaxial parallel disks of radii *r*₁, *r*₂ separated by *H*, with *R*ᵢ = *r*ᵢ/*H* and X = 1 + (1 + *R*₂²)/*R*₁², the view factor is F₁₂ = ½[X − √(X² − 4(*R*₂/*R*₁)²)]. For equal radii *R* = *r*/*H* = 1/(2 AR), so X = 2 + 4 AR² and F = ½(X − √(X² − 4)). For large AR, F → 1/X ≈ 1/(4 AR²). The corresponding slot result is √(1 + AR²) − AR → 1/(2 AR). At large AR the hole therefore passes a factor of about 2 AR fewer line-of-sight neutrals than the slot.

## E.2 Ion floor fraction for small σ

An ion tilted by a small angle vector **θ** lands displaced by δ = *H*|**θ**|. The fraction of a disk of radius *r* that stays inside after a shift δ is the lens overlap of two circles, ≈ 1 − 2δ/(π*r*) for δ ≪ *r*. |**θ**| has a Rayleigh distribution with mean σ√(π/2). Averaging, with *H* = 2 AR *r*,

G_ion ≈ 1 − (4/√(2π)) AR σ ≈ 1 − 1.60 AR σ (σ in radians).

At AR = 1 and σ = 2° (0.0349 rad), G_ion ≈ 0.944, as computed (0.9445). The slot coefficient is 0.80 (Book 29). The hole loses ions twice as fast, because both directions of tilt count.

## E.3 Bottom CD from taper

A hole of top diameter *D*_t through a layer of thickness *H* with wall angle θ has bottom diameter *D*_b = *D*_t − 2*H* cot θ. Its sensitivity is ∂*D*_b/∂θ = 2*H*/sin²θ per radian, which is 0.71 nm per degree for *H* = 20 nm and θ = 81.5°.

## E.4 Area at the resistance limit

With *R*_DC = ρ_c/*A* + *R*_plug, the limit *R*_max is reached at *A*_min = ρ_c/(*R*_max − *R*_plug) = 1.5 × 10⁶/(10 000 − 847) ≈ 164 nm².

## E.5 Recess sensitivity to CD and the feed-forward gain

If the recess at fixed time changes by ∂*d*/∂*D* per nanometre of CD and the rate at the end of the step is *r*, the time correction that restores the target is Δ*t* = −(∂*d*/∂*D*) Δ*D*/*r*. For recipe A, (0.55 nm/nm)/(0.49 nm/s) ≈ 1.1 s per nm.

## E.6 Rayleigh tail of radial overlay

If *o*ₓ and *o*ᵧ are independent normal with standard deviation σ, the radial error *o* is Rayleigh distributed and P(*o* > *o*_c) = exp(−*o*_c²/2σ²). Since the exponent scales as 1/σ², a fractional reduction ε in σ multiplies it by 1/(1 − ε)².

## E.7 Pit transport

A pit of width *w* and depth *p* at the floor of a hole receives the flux that reaches the hole floor, F_h. Of that, a fraction G(*p*/*w*) reaches the pit bottom. The model uses the round-hole transport fractions for both factors. This is an approximation: the flux entering the pit is not cosine-distributed, and the pits are not round. It is used for its qualitative behaviour (narrow, deep pits slow down), not for precise rates.
