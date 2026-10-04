# Chapter 1 — The Bit-Line Contact in the Cell

## 1.1 One contact for two cells

A DRAM cell stores a bit as charge on a capacitor and reads it through an access transistor onto a bit line. In the buried-channel array transistor (BCAT) used in modern 6F² DRAM, the transistor gate is a buried word line, and each active area (AA) is a short silicon bar crossed by two word lines. The bar therefore holds three diffusions. The two ends are **storage nodes**, each connected upward through a storage-node contact (SNC, also called a buried contact) to its own capacitor. The centre, between the two word lines, is the **bit-line node**, shared by the two cells. The bit-line contact connects that centre node to the bit line.

Because the node is shared, there is one bit-line contact for every two cells. In a 16 Gb die that is 8 × 10⁹ contacts, each of which must conduct, and each of which must stay isolated from the storage nodes and word lines packed around it.

## 1.2 What the contact must do

The bit-line contact has four jobs:

1. **Conduct.** The read signal is a small charge shared between the cell capacitor and the bit line. The write must drive the cell to full level within a few nanoseconds. Contact resistance is in series with both. In the reference process it is about 6 kΩ, a sizeable fraction of the access path resistance. At the specification edge, slow writes appear as tWR failures and weak reads appear as sense-margin loss.
2. **Insulate from the word lines.** The contact lands between two word lines whose metal tops lie 60 nm below the silicon surface under a nitride cap. Any recess of the cap or of the gate-oxide liner beneath the contact brings the n⁺ plug toward the word-line metal. That raises the field across the cap, adds coupling between bit line and word line, and in the limit causes a short.
3. **Insulate from the neighbouring storage nodes.** In the band between two word lines, the bit-line node of one active area sits beside storage-node ends of adjacent active areas, separated by STI. A hole that strays onto them connects a bit line to the wrong cell.
4. **Leave the junction healthy.** The etch exposes the node silicon to ions and halogens. Damage, residues and interfacial oxide raise contact resistance and add leakage to the bit-line junction.

## 1.3 Dimensions

With F = 17 nm, the 6F² cell occupies 34 nm × 51 nm = 1734 nm². The word-line pitch is 34 nm and each word-line trench is 18 nm wide, so the silicon between two word lines is 16 nm long along the bit line. The active area is 16 nm wide and tilted 21° from the bit line, so the node is a parallelogram 16 nm long and 16/cos 21° = 17.1 nm tall, with an area of 274 nm². This is the most silicon any contact can touch on the node's top surface.

The contact hole is larger than the node. In the reference process it is 32 nm across at the top of the buffer and 26 nm at the silicon surface. The hole therefore overhangs the node on all sides. In x (along the bit line) it overhangs onto the word-line caps. In y it overhangs onto STI oxide. The larger hole is deliberate. It makes the contact area insensitive to small CD and overlay errors, at the price of exposing other materials in the floor (Chapter 10).

## 1.4 Where the contact sits in the flow

The DC module follows the word-line module (trench, gate oxide, metal recess, cap fill and planarisation; Books 26–28) and precedes the bit-line stack (Book 29):

1. planarised surface with word-line caps flush with silicon and STI;
2. buffer deposition (oxide and nitride);
3. DC lithography on a carbon hard mask, with CD shrink;
4. **DC etch**: mask open, buffer open, mixed-floor recess;
5. strip, clean and in-situ doped polysilicon fill;
6. poly planarisation or etchback to the buffer top;
7. bit-line stack deposition and etch, which also trims the DC poly beside the line.

## 1.5 A specification sheet

An illustrative set of targets for the reference process:

| Parameter | Target | Set by |
|---|---|---|
| DC top CD (buffer top) | 32 ± 1.5 nm (3σ) | litho + shrink |
| DC bottom CD (Si surface) | 26 ± 2 nm (3σ) | buffer taper |
| Si recess | 25 ± 3 nm | recess step |
| WL cap remaining over metal | ≥ 30 nm | recess selectivity |
| DC-to-AA overlay | ≤ 6 nm per axis (3σ) | lithography |
| contact resistance | ≤ 10 kΩ | area, interface |
| clearance to neighbour storage node | > 0 at 4.5σ | CD, overlay |

## 1.6 Why this etch is hard

The DC etch is short (about a minute of plasma). It is not deep, with an aspect ratio below 5. It is hard for three other reasons. Its floor is four materials, so the floor's shape after etching depends on selectivities the engineer chooses and on transport into sub-features only a few nanometres wide. Its margins are set by overlay to a tilted active area, so the same error costs different amounts in different directions. Its failure modes (high resistance, word-line coupling, neighbour shorts, leakage) appear only at electrical test, weeks later. The rest of this book develops each of these points.
