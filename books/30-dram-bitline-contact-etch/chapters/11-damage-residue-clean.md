# Chapter 11 — Damage, Residues and the Pre-Fill Clean

## 11.1 What the plasma leaves behind

The floor of the DC is the most electrically sensitive surface the etch touches. Four things are left on it or in it:

1. **Lattice damage.** Ions of 50–300 eV penetrate 1–3 nm into silicon, displacing atoms and leaving an amorphised or defective layer. Br⁺ and Cl⁺ at the low bias of recipe A penetrate least. Ar⁺ and CFₓ⁺ at the higher bias of B and C penetrate most.
2. **Implanted and adsorbed species.** Bromine and chlorine (recipe A), fluorine and carbon (B, C, the buffer open), and hydrogen from HBr or CHF₃ diffuse a few nanometres into the silicon. Hydrogen can go deeper and passivate dopants.
3. **Surface films.** A SiOₓBrᵧ or SiOₓClᵧ layer forms from the oxygen in recipe A, and a fluorocarbon film from B and C. Both are 1–3 nm thick.
4. **Oxide.** The ash that removes the carbon mask oxidises the exposed silicon if it contains oxygen, and air exposure grows native oxide afterwards.

Each raises contact resistance. The damage also adds generation centres in the bit-line junction, which increase its leakage.

## 11.2 Why bit-line-node damage matters less, and more

Retention is set by leakage at the storage-node junction, not the bit-line node. Damage at the DC therefore does not directly shorten retention. It matters in other ways. Bit-line junction leakage loads every bit line with many cells. It shifts the precharge level during long refresh intervals and reduces sense margin. Damage at the gate edge near the bit-line side raises GIDL there. Contact resistance from residual damage drifts with later thermal steps, which makes it hard to screen.

## 11.3 The strip

The carbon mask is removed by an O₂ or N₂/H₂ plasma, downstream or with low bias. O₂ is faster and cleans fluorocarbon residues well, but it oxidises the silicon floor by 1–2 nm. N₂/H₂ oxidises less, but it removes fluorocarbon films more slowly and can leave hydrogen in the silicon. Many flows strip with N₂/H₂ and rely on the wet or dry clean to remove what is left.

## 11.4 Damage removal

A **light etch** removes the damaged layer after the main recess. It is a low-energy, nearly isotropic silicon removal of 1–3 nm, either by downstream CF₄/O₂ or NF₃/O₂, or by a final low-bias step in the same chamber. It is effective because the damaged layer is thin, and costly because it also widens the pit and recesses the dielectrics slightly. The recess target should include it.

## 11.5 The pre-fill clean

Before the poly fill, the floor must be free of oxide and residue. Two families are used:

- **Wet.** Dilute HF (100:1 to 500:1) removes the native and ash oxide and loosens halogen and fluorocarbon films. It also etches the STI and the gate-oxide liner. At 1–2 nm of oxide removal, the liner pit deepens by about as much (Chapter 8). An SC1 step before the HF helps remove particles and organic residue, but it re-oxidises the surface.
- **Dry.** A remote NF₃/NH₃ plasma forms ammonium fluorosilicate on oxide surfaces. A bake at about 100–180 °C sublimes it. The reaction self-limits on silicon and etches oxide more uniformly in narrow features than wet HF, since it does not depend on liquid transport into a 3.5 nm slit. It is often integrated on the same platform as the poly deposition, so the clean surface never sees air.

## 11.6 Queue time

Native oxide regrows on clean silicon at a few tenths of a nanometre per hour in clean-room air. A tunnelling contact is very sensitive to interfacial oxide: half a nanometre can raise ρ_c several-fold. A queue-time limit between clean and fill, typically a few hours, is enforced for the DC. An integrated pre-clean in the fill tool removes the limit and is the preferred practice at advanced nodes.

## 11.7 A checklist

| Residue or defect | Source | Signature | Remedy |
|---|---|---|---|
| amorphised layer | ion bombardment | high R_DC, junction leakage | lower bias, light etch |
| Br/Cl in Si | recipe A | R_DC drift with anneal | light etch, H₂ anneal |
| C/F film | buffer open, B, C | high R_DC, poor poly nucleation | O₂ ash, dHF, dry clean |
| interfacial oxide | ash, air | high, variable R_DC | dry clean, queue-time limit |
| liner pit | dHF, C | WL–BL leakage | limit oxide removal |
