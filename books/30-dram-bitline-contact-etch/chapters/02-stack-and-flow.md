# Chapter 2 — Stack, Layout and Process Flow

## 2.1 The incoming surface

The DC etch starts on a surface prepared by the word-line module. After the word-line metal is recessed (Book 28) and the cap nitride is deposited and planarised, the surface is a mosaic. It holds silicon active areas, STI oxide between them, and nitride-capped word-line trenches crossing both. The caps are flush with the silicon to within a few nanometres. Any step left by cap CMP is inherited by the DC floor.

Under the cap, each word-line trench is lined with gate oxide, 3.5 nm in the reference process. At the surface this liner appears as a thin oxide line between the silicon and the cap on both sides of every word line. Its top edge is exposed in the DC floor wherever the hole overhangs a word line, which is everywhere.

## 2.2 The buffer

A thin buffer is deposited before the DC mask. The reference buffer is 6 nm of SiO₂ under 14 nm of SiN, 20 nm in all. The buffer has three roles. It insulates the bit line from the silicon and word-line caps everywhere except at the DC. It acts as the etch stop for the bit-line stack etch (Book 29). It also protects the active-area surface from the DC mask processes.

Opening the buffer is the first part of the DC etch (Chapter 6). The buffer's oxide layer sits directly on the silicon and STI. The nitride layer is the stop that the bit-line etch later lands on, so the DC etch must not thin it outside the hole.

## 2.3 The mask

DC holes at this pitch are printed by immersion lithography, sometimes with double patterning or EUV. They are transferred into a carbon hard mask, either amorphous carbon (ACL) or spin-on carbon, under a SiON or SiARC cap. The lithographic hole is larger than the final contact, about 42 nm in the reference process. It is **shrunk** to 32 nm by depositing polymer on the hole walls during the SiON and carbon open (Chapter 5). The carbon left at the start of the recess step is about 70 nm, which dominates the aspect ratio seen by the floor.

## 2.4 The layout seen from above

The layout fixes the geometry the etch has to work with. Take *x* along the bit line and *y* along the word line. Word-line trenches occupy 8 < |*x*| < 26 nm on either side of the contact. The node silicon is the part of the tilted active-area strip with |*x*| < 8 nm. Neighbouring strips, which carry storage-node ends of adjacent cells, repeat every 32/cos 21° = 34.3 nm in *y*. A 26 nm hole centred on the node covers:

- the whole node, about 272 of its 274 nm² (the hole is node-limited);
- about 143 nm² of word-line cap nitride, as two lunes at |*x*| > 8 nm;
- about 116 nm² of STI oxide above and below the node;
- the two gate-oxide liner slivers where the hole crosses the trench walls.

Its edge is 11 nm from the nearest neighbouring strip.

## 2.5 The process flow in detail

| Step | Purpose | Typical chemistry |
|---|---|---|
| SiON open | transfer the resist hole | CF₄/CHF₃ |
| carbon open with shrink | transfer and shrink the hole | O₂/COS or N₂/H₂, with CH₄ or CHF₃ for polymer |
| buffer open | through SiN and SiO₂ to the floor | CF₄/CHF₃/O₂/Ar |
| floor recess | recess node Si (and other floor materials) | HBr/Cl₂/O₂, or CF₄/CHF₃/Ar, or C₄F₆/O₂/Ar |
| strip | remove carbon and polymer | O₂ or N₂/H₂ plasma |
| clean | remove residue, damaged layer and native oxide | dilute HF, SC1, or dry NF₃/NH₃ |
| poly fill | fill with in-situ doped poly | SiH₄/PH₃ CVD |
| poly CMP or etchback | plug flush with the buffer top | — |

The strip, clean and fill are covered in Chapters 11 and 12. The buffer open and floor recess may run in one chamber as a multi-step recipe. Some flows strip the carbon before the recess and use the buffer itself as the mask.

## 2.6 The quantities that matter downstream

The bit-line stack etch (Book 29) inherits two things from the DC module: the **height of the poly plug** relative to the buffer, and the **width of the DC** relative to the bit line. The width sets the gaps beside the line that the bit-line etch must clear of poly (Book 29, Chapter 8). The storage-node contact etch inherits the **cap and STI recess** left beside the DC. A deep recess there becomes a deeper pocket that the spacer and SNC must deal with.
