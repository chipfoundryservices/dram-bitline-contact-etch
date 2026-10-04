# Chapter 9 — Profile, Taper and Bottom CD

## 9.1 The diameter that matters

The contact touches the silicon at the bottom of the hole, not at the top. In the reference process, the 32 nm hole at the buffer top narrows to 26 nm at the silicon surface. It narrows because the buffer open is run with enough polymer to give a sidewall angle of about 81.5°. For a straight taper,

*D*_b = *D*_t − 2 *H*_buf cot θ,

so 20 nm of buffer at 81.5° removes 6.0 nm from the diameter. The taper is deliberate. It is a second shrink, done in the buffer, and it lets the carbon hole stay a little larger and easier to open.

## 9.2 Sensitivity to angle

The bottom diameter's sensitivity to sidewall angle is

∂*D*_b/∂θ = 2 *H*_buf / sin² θ,

which is 0.71 nm per degree for a 20 nm buffer at 81.5°. A 1° (1σ) scatter of the angle therefore adds about 0.7 nm (1σ) to the bottom CD. That is comparable to the 1 nm top-CD scatter. The variation model reproduces this: σ_θ = 1° alone gives σ*D*_b = 0.72 nm (Chapter 14). The angle is set by the polymer balance in the buffer step, so it drifts with chamber condition and wafer temperature. A centre-to-edge temperature difference of a few degrees can change it by a fraction of a degree.

## 9.3 Profile defects

- **Bowing.** Ions scattered off the carbon facets strike the buffer wall below the mask and widen it. In a 20 nm buffer the bow is small, but it widens the hole where the bit-line poly will later sit. That leaves more poly for the bit-line etch to clear (Chapter 12).
- **Necking.** Excess polymer at the carbon–buffer interface narrows the hole there and shadows the floor. The bottom CD then drops more than the angle formula predicts.
- **Striations.** Roughness carried down from the mask makes the bottom outline ragged. The node area changes little, because the hole overhangs the node, but the clearance to the neighbour (Chapter 10) is set by the worst point of the outline, not the mean.
- **Twisting and tilt.** At an aspect ratio of 3–4, a hole is not deep enough to twist. A tilt of the whole hole from an off-normal ion flux (at the wafer edge, from a worn edge ring) shifts the bottom relative to the top. It acts as an additional overlay error at the floor.

## 9.4 Profile below the silicon surface

Below the silicon surface, the shape depends on the recess recipe (Chapter 7):

- with **recipe A**, the pit walls are the existing interfaces between node silicon and STI oxide or gate oxide. They are as steep as the STI and word-line trench walls, typically 87–89°, and the node widens slightly with depth. A 25 nm pit in a node whose walls slope at 88° gains about 1.7 nm in width at its floor. Polymer or oxide fences at the pit corners can remove more than this from the effective area;
- with **recipe B**, the hole keeps tapering through the floor. At 86° over 25 nm it loses another 3.5 nm of diameter, so a 26 nm hole reaches the bottom of the recess at about 22.5 nm. The contact is then the intersection of that smaller disk with the node (260 nm² at zero overlay, Chapter 10);
- with **recipe C**, the node stands as a mesa. Its sidewalls are exposed down to the depth of the surrounding recess, and the poly wraps them.

## 9.5 Measuring it

Top CD is measured by CD-SEM. The bottom CD of a 26 nm hole 90 nm deep (under the mask) or 20 nm deep (after strip) can be seen with high-voltage SEM after strip, or by scatterometry on arrays of contacts. Profile and recess shape need cross-sections (TEM, STEM-EDS) on a sample basis. Cross-sections taken along the bit line show the cap lunes. Those taken along the word line show the STI recess and the neighbour.
