# Chapter 7 — The Mixed-Floor Recess

## 7.1 The model

When the buffer clears, the floor of the hole holds four materials: node silicon, STI oxide, word-line cap nitride and gate-oxide liner. Each recesses at its own rate. The model in `sim/contact_mc.py` writes, for each material *m*,

d*d*ₘ/d*t* = R_ion,m · G_ion(AR_h) · G_ion(AR_p,m) + R_n,m · G_n(AR_h) · G_n(AR_p,m)

where AR_h = (70 + 20 + *d*_min)/*D* is the aspect ratio of the hole down to the shallowest part of the floor, and AR_p,m = (*d*ₘ − *d*_min)/*w*ₘ is the aspect ratio of the pit that material *m* has dug below it. The pit widths are 16 nm (Si node), 8 nm (STI patch), 5 nm (cap lune) and 3.5 nm (liner). Multiplying the two transport fractions is an approximation. It treats the pit as a small hole at the floor of a larger one. It captures the main effect: a material that runs ahead slows down.

## 7.2 Three floor shapes

{{FIG:recess}}

The three recipe families of Chapter 3 make three different floors from the same starting point:

- **Recipe A (Si-selective)** digs a **pit** in the node. The STI and caps barely move (about 1–2 nm), while the silicon goes down 25 nm in 46 s. The pit walls are STI oxide and cap nitride.
- **Recipe B (co-recess)** moves the whole floor down together. After 45 s the silicon is at 25 nm, the STI at 28 nm and the caps at 26 nm. The floor stays flat to within 3 nm.
- **Recipe C (dielectric-first)** leaves the node standing as a **mesa**. The STI drops 42 nm and the caps 25 nm in 60 s while the silicon loses only 4 nm.

{{TABLE:recess_t}}

The last column is the height of the node silicon above the STI floor. A negative value means the silicon lies below the oxide (a pit). A positive value means it stands above it (a mesa).

## 7.3 Time to target and CD sensitivity

{{TABLE:recess25}}

Recipe A takes 51 s in a 22 nm hole and 42 s in a 30 nm hole to reach 25 nm. At a fixed time of 45.6 s (the 26 nm target), the 22 nm hole reaches 22.5 nm and the 30 nm hole 26.9 nm, a spread of 0.55 nm of recess per nanometre of CD. Recipe B spreads half as much (23.8 to 26.0 nm, 0.28 nm per nm). It depends less on neutrals and runs with tighter ion angles. A recess run on time therefore inherits CD variation through ARDE. With recipe A and a 1 nm (1σ) bottom-CD scatter, this alone is about 0.6 nm (1σ) of recess scatter.

## 7.4 The pit slows itself

In recipe A, the silicon rate falls from 0.63 nm/s at the start of the recess to 0.49 nm/s at 25 nm. The hole hardly changes: because the STI barely moves, its aspect ratio rises only from 3.46 to 3.50. The slowdown comes from the pit. At 25 nm deep and 16 nm wide its own aspect ratio is 1.6, and at *s* = 0.1 just under a third of the neutrals arriving at the pit mouth reach its bottom. The pit is in effect a second contact etched at the floor of the first.

## 7.5 Choosing a floor

Each floor shape has consequences downstream:

| Floor | Contact area | Cap/liner margin | Poly fill | Neighbour isolation |
|---|---|---|---|---|
| Si pit (A) | node top only, ≤ 274 nm² | best (cap −2 nm) | pit is narrow, AR 1.6: voids possible | pit walls are dielectric: good |
| flat (B) | node top only | cap −26 nm, liner −28 nm | easy | STI recessed beside node |
| Si mesa (C) | node top + sidewalls | cap −25 nm, liner −35 nm | wraps the mesa | STI recessed 40 nm: deep pocket near the neighbour |

Production recipes often combine families. A short C or B step first lowers the dielectrics a few nanometres and removes the fluorocarbon-rich surface left by the buffer. An A step then sets the silicon recess. The resulting shallow mesa or flat floor gains a little sidewall area without exposing the liner deeply. The model handles such sequences by running the steps in turn.

## 7.6 What the model omits

The model has no lateral etching, so the pit walls do not move. It has no faceting at the pit corners, no loading by the floor materials on the plasma, and no change of the fluorocarbon film with depth. Each of these shifts the numbers. None of them changes the qualitative result that the floor shape follows the selectivity, and that the narrowest features slow first.
