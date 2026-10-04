# Chapter 15 — Yield, Reliability and Electrical Signatures

## 15.1 Failure modes

| Mode | Cause in the DC etch | Electrical signature |
|---|---|---|
| DC open / high R | small area (overlay, small bottom CD), residue, interfacial oxide, void in pit | both cells sharing the DC fail write or read; paired-bit failure |
| BL–WL short or leakage | cap loss, liner pit, overlay along BL | bit line fails when one word line is selected; word-line-dependent leakage |
| DC–SN short | hole touches neighbour storage node; DC poly not cleared in BL etch | cell reads its neighbour's data; pattern-dependent failures |
| BL junction leakage | damage at the node, Br/F/C contamination | bit-line leakage, precharge drift, sense-margin loss |
| GIDL at the BL node | n⁺ poly close to the gate edge (liner pit, deep recess, out-diffusion) | temperature-activated leakage on the bit line |

## 15.2 The paired-bit signature

Two cells share every DC. They lie on the same bit line and on the two adjacent word lines that cross their active area. A DC that is open or highly resistive therefore fails both cells together. The bitmap shows a pair of vertically adjacent failing bits in one column. This **paired-bit failure** is the strongest diagnostic link from test back to the DC module. A random single-bit failure points elsewhere (capacitor, storage-node contact, storage junction). A paired-bit failure points to the DC or the bit-line node.

Pair failures that cluster at the wafer edge suggest tilt or bottom-CD loss from the edge ring. Clustering along one direction of a lithography field suggests overlay. Pair failures that depend on test temperature and timing suggest high resistance rather than an open.

## 15.3 Word-line-dependent failures

A bit line that fails only when a particular word line is selected is leaking to or shorted to that word line. Where the DC is the cause, the failing word line is one of the two adjacent to a DC on that bit line. If cap loss or a liner pit is responsible, the failure is often voltage-dependent and may grow with stress. That makes it a reliability failure as well as a yield failure.

## 15.4 Reliability

- **Cap dielectric breakdown.** Between the DC plug and the word line, the cap nitride sees the word-line swing for the life of the part. Time-dependent dielectric breakdown accelerates with field. A cap thinned from 60 to 25 nm more than doubles the mean field. At a poly-filled liner fin, the field is concentrated further. Burn-in screens the weakest contacts. The margin of Chapter 8 must cover the rest.
- **Contact resistance drift.** Halogen residues and interfacial oxide can change during later anneals and under current. A contact near the resistance limit at test may drift beyond it. Excursions in clean quality are therefore reliability issues as well as yield issues.
- **Row-hammer and disturbance.** A plug close to the word line (deep cap loss, liner fin) increases coupling between word-line activity and the bit-line node. Its effect is small next to the main row-hammer mechanisms, but it adds to the leakage of the bit-line-side junction under repeated activation.

## 15.5 Test structures

The DC module is qualified with:

- **Kelvin DC chains** of thousands of contacts, alternating poly plugs and active-area segments, to measure *R*_DC and its tail;
- **combs** of DCs against word lines, to measure BL–WL leakage and breakdown;
- **DC-to-neighbour structures** in which the neighbouring storage nodes are wired separately, to measure DC–SN isolation;
- **array test** with bitmap analysis classified by failure pattern (single bit, paired bit, column, row).

## 15.6 Connecting back to the etch

Each signature has a measurable counterpart in the etch module. Paired-bit failures correlate with bottom CD, overlay and voltage-contrast opens. BL–WL failures correlate with cap remaining and liner pit depth in cross-section. DC–SN failures correlate with *y* overlay and with poly residue in the bit-line etch. Junction leakage correlates with recess recipe and clean. Keeping these correlations up to date is the main job of yield engineering for the DC.
