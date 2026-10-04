# DRAM Bit-Line Contact Etch

### Opening the Direct Contact: Transport, Mixed-Floor Recess and Contact-Area Control at the Bit-Line Node

*Book 30 · dram-bitline-contact-etch series*

---

## Preface

Every cell pair in a buried-channel DRAM shares one connection to its bit line. That connection is the **bit-line contact**, also called the **direct contact** (DC): a hole about 30 nm across, etched through a thin insulating buffer, landing on the centre of the active area between two buried word lines, and recessed a few tens of nanometres into the silicon before it is filled with doped polysilicon. When the bit-line stack is etched later (Book 29), the line passes over this plug and the plug becomes the bit line's foot in the cell.

The contact is small and shallow by the standards of other contact etches, but its floor is unusual. It does not land on one material. At the bottom of a single hole there is the silicon of the bit-line node, the oxide of the shallow trench isolation on either side of it, the silicon-nitride caps of the two word lines that bracket it, and between silicon and cap the edge of each word line's gate oxide, a sliver only 3.5 nm wide. The DC etch recesses all of these at once, and every recipe makes a different shape out of them. A silicon-selective recipe digs a pit in the node. A non-selective recipe moves the whole floor down together. An oxide-selective recipe leaves the node standing as a mesa and can drill down the gate-oxide liner toward the word line.

Four outcomes are decided at this step. The **contact area** on the node, together with the interface left by the etch and clean, sets the contact resistance in series with every read and write. The **cap and liner loss** sets the margin between the bit-line plug and the word line beneath it. The **clearance** from the hole to the neighbouring storage-node silicon decides whether the plug touches a cell it should not. The **damage and residue** left in the silicon set leakage and resistance drift. A few nanometres of overlay or a few seconds of recipe decide all four.

This book treats the bit-line contact etch as a problem of transport, selectivity and geometry. It has four parts and sixteen chapters, with seven appendices, a glossary and an index.

**Part I — Foundations** (Chapters 1–4): the contact's role in the cell, the stack and process flow, the chemistry of a mixed floor, and a computed treatment of ion and neutral transport into a round hole.

**Part II — Contact Etch Physics** (Chapters 5–8): the mask open and CD shrink, the buffer open, the computed recess of the mixed floor, and the attack on the word-line cap and gate-oxide liner.

**Part III — Contact Formation and Integration** (Chapters 9–12): profile and bottom CD, the computed contact area and resistance, damage and the pre-fill clean, and the polysilicon fill and hand-off to the bit-line stack.

**Part IV — Control, Variation and Outlook** (Chapters 13–16): reactor, recipe, endpoint and metrology; the computed variation budget; yield and reliability; and the contact in 4F² and 3D DRAM.

### How the numbers were made

Ion and neutral transport into a round hole (Chapter 4, Appendix B), the buffer clear times (Chapter 6), the recess histories of the four floor materials under three recipe families (Chapters 7 and 8), the contact area, clearance and resistance against overlay (Chapter 10) and the variation budget (Chapter 14) are computed by `sim/contact_mc.py`. The Monte Carlo neutral transport is checked against the exact view factor between the opening and the floor of a cylinder. Everything else quantitative (dimensions, rates, recipes, windows) is *illustrative*. These values are chosen to show orders of magnitude and relationships, and none of them describes a specific manufacturer's process. The recipe rates in the model are assumptions, not measurements. Their purpose is to show how a choice of selectivity becomes a shape. References are listed in Appendix G; readers should verify citation details against the originals.

### The reference process

One illustrative process ties the chapters together:

```
Cell:          6F² buried-channel DRAM, F = 17 nm; word-line pitch 34 nm,
               bit-line pitch 51 nm
Active area:   16 nm wide, tilted 21° from the bit line; perpendicular pitch
               32 nm (16 nm STI between strips)
Bit-line node: silicon between two 18 nm word-line trenches → a 16 nm ×
               17.1 nm parallelogram, 274 nm²
Word line:     metal top 60 nm below the Si surface; SiN cap above it;
               3.5 nm gate-oxide liner on the trench wall
Buffer:        6 nm SiO₂ + 14 nm SiN = 20 nm on the planarised surface
DC mask:       amorphous carbon (70 nm left at the recess step) + SiON
DC hole:       lithography 42 nm → 32 nm after shrink at the buffer top →
               26 nm at the Si surface (81.5° in the buffer)
Recess:        target 25 nm into the node silicon
Fill:          in-situ phosphorus-doped polysilicon, 1 mΩ·cm; plug 45 nm
Interface:     specific contact resistivity 1.5 × 10⁻⁸ Ω·cm²
               → R_DC ≈ 6.3 kΩ nominal; limit 10 kΩ
```
