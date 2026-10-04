# Chapter 16 — The Contact in Future DRAM

## 16.1 Planar 6F² scaling

Chapter 14 showed what happens when the reference cell shrinks from F = 17 to 13 nm with overlay unchanged. The contact area falls with F², and the resistance tail and neighbour touches appear together. Three changes keep the planar DC alive:

- **Lower ρ_c.** Higher active doping at the interface, oxide-free interfaces from integrated dry cleans, and epitaxial rather than polycrystalline plugs. A selectively grown epitaxial silicon or SiP plug removes the grain boundaries and the interfacial oxide of the poly–Si interface. It can halve ρ_c or better.
- **Self-aligned DCs.** The DC is printed as a line crossing many active areas, and the word-line caps and STI act as the mask in one direction. Overlay in that direction drops out of the area budget. The floor etch must then be strongly silicon-selective (recipe A by construction), and the cap must be thick enough to serve as a mask.
- **Atomic-layer recess.** Cyclic Cl₂ adsorption and low-energy Ar⁺ removal recesses silicon at a fixed amount per cycle, with little damage and almost no aspect-ratio dependence. Recess control of ±1 nm becomes possible. The cost is throughput.

## 16.2 Metal contacts

Replacing the poly plug with a metal (TiSiₓ/TiN/W or a ruthenium or molybdenum plug on a silicide) lowers the plug term and allows a silicide interface. The DC etch then has to leave a surface fit for silicidation. That requires low damage and no oxide, and the poly out-diffusion that previously compensated for a deep recess is gone.

## 16.3 4F² vertical-channel DRAM

In a 4F² cell with a vertical-channel transistor (VCT), the transistor stands as a silicon pillar. The bit line is buried below the pillars, or bonded onto their bottom after wafer flipping, and the storage node sits on top. The bit-line contact becomes the bottom junction of the pillar. It is formed by doping or silicidation at the pillar base, not by an etched hole. Its etch challenges move to the pillar etch and the buried bit-line trench. Isolating a metal bit line from the pillar's gate a few nanometres away is a related problem. The trade-off between contact area and isolation moves with it.

## 16.4 3D DRAM

In stacked 3D DRAM, horizontal transistors are stacked in tens of layers and the bit line runs vertically through the stack. Each layer's transistor must contact the vertical bit line, so the bit-line contact becomes a high-aspect-ratio vertical hole or slot, much like a 3D NAND channel hole. Its sidewall must make contact to a silicon layer in every tier. The transport problems of Chapter 4 return at aspect ratios of 30–60. The mixed-floor problem of Chapter 7 becomes a mixed-sidewall problem: silicon tiers between dielectric tiers, each to be recessed, cleaned and contacted uniformly from top to bottom.

## 16.5 What carries over

Whatever the cell architecture, the bit-line contact has the same four jobs: conduct, stay clear of the word line, stay clear of the neighbour, and leave the junction healthy. The quantitative tools in this book carry over directly: transport fractions in a hole, rate laws for a mixed floor, area-against-overlay geometry, and a variation budget counted in ppm. So does the lesson of the reference process: **the floor's shape follows the selectivity, the area follows the overlay, and the margin is whatever the etch did not remove.**
