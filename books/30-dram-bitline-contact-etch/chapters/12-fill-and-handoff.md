# Chapter 12 — Polysilicon Fill and the Hand-off to the Bit-Line Stack

## 12.1 The fill

The DC is filled with in-situ phosphorus-doped silicon by LPCVD. It is usually deposited amorphous at 500–550 °C and crystallised by later anneals. The deposition is conformal. It closes the 26–32 nm hole from the walls inward and leaves a seam on the hole axis. In a recipe-A pit (16 nm wide, 25 nm deep, AR 1.6) the pit fills first and the seam starts above it. If the pit is wider at the top than at the bottom, which is the normal case, the seam closes cleanly. If its walls overhang, because of corner fences or a re-entrant STI profile, a void can close inside the pit, where it removes contact area directly.

The gate-oxide liner slit, if a dielectric-first or wet step has opened it, is 3.5 nm wide. Poly enters it and pinches off, leaving a thin n⁺ fin that points down toward the word-line metal (Chapter 8).

## 12.2 Doping and the bit-line junction

The plug is doped at about 10²⁰–10²¹ cm⁻³. During later anneals, phosphorus diffuses from the plug into the node and joins the implanted bit-line junction. A few nanometres of out-diffusion make the contact ohmic even if the recess has landed below the implant peak. Excess diffusion moves the junction toward the word-line gate edge and raises GIDL. The recess depth and the thermal budget are therefore set together.

## 12.3 Planarisation

The fill overburden is removed by poly CMP or etchback, stopping on the buffer nitride. The plug top is left flush or slightly recessed. The plug height (about 45 nm from the recess floor to the buffer top) enters the plug resistance. Its variation is set by CMP dishing in the dense DC array.

## 12.4 What the bit-line etch inherits

The bit-line stack (barrier, tungsten, nitride cap) is deposited on the buffer and plug, and etched into lines 20 nm wide at the bottom (Book 29). Where a line crosses a DC, the poly beside it must be removed down to below the level where the storage-node contact will land. Otherwise the storage-node contact touches the poly and shorts bit line to storage node.

The gap beside the line is set by the DC, not by the line. At the buffer top it is (32 − 20)/2 = 6 nm per side at perfect overlay. At the silicon surface the DC has tapered to 26 nm, and the gap is (26 − 20)/2 = 3 nm. In a recipe-B or recipe-C floor, the poly fills a recess below that as well. The bit-line etch must therefore clear poly from a gap that narrows with depth. The taper that helped the contact (Chapter 9) works against the bit-line etch. Book 29 (Chapter 8) shows that a 4 nm gap does not clear in any practical overetch.

Three resolutions are used:

- **Keep the gap wider at depth.** Use a less tapered DC, accepting a larger top CD.
- **Make the plug narrower than the hole.** A nitride liner in the DC before the fill turns the hole into a plug with insulating sides. The liner protects the cap and STI and moves the bit-line etch's gap outward.
- **Seal what remains.** A nitride gap-fill after the bit-line etch insulates any poly left deep in the gap. This works if the residue lies below the storage-node contact's landing level.

## 12.5 The pockets beside the plug

A recipe-B or recipe-C floor recesses the STI and caps beside the node by 25–40 nm. After the bit-line etch removes the poly there, these pockets are open cavities next to the bit line. The bit-line spacer and gap-fill must fill them. The storage-node contact etch must then cut through that fill to reach the storage node. Deep pockets therefore make the storage-node contact etch longer and the spacer harder to fill. This cost of a non-selective DC recess appears two modules later.

## 12.6 Integration checklist

| DC choice | Helps | Hurts |
|---|---|---|
| larger bottom CD | contact area, BL-etch gap | neighbour clearance |
| steeper buffer taper | BL-etch gap | contact area tolerance |
| deeper Si recess | removes damage, plug–node area on a mesa | doping at interface, cap margin (B, C) |
| dielectric-first step | sidewall contact | liner pit, pockets for SNC |
| nitride liner in DC | BL-etch gap, cap protection | plug area, R_DC |
