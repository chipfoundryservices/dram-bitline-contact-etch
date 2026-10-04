# Chapter 6 — The Buffer Open

## 6.1 The task

The buffer is 14 nm of SiN on 6 nm of SiO₂. The buffer open must clear both from every DC in the array without thinning the buffer elsewhere, where it is protected by the carbon mask. It must also put as little extra recess as possible into the floor materials before the recess step chooses its own selectivity. A hydrofluorocarbon (CF₄/CHF₃/O₂/Ar) step etches SiN and SiO₂ at similar rates. In the model both rates are 1.2 nm/s ion-driven plus 0.15 nm/s neutral-driven in the open field.

## 6.2 Computed clear times

The buffer front starts at AR = 70/*D* (the carbon above it) and ends at AR = 90/*D*. Integrating the rate law with the transport fractions of Chapter 4 (σ = 2°, *s* = 0.3) gives:

{{TABLE:buffer}}

In the open field the buffer would clear in 20/1.35 = 14.8 s. The hole slows it by a third, mostly because the neutral term has collapsed. Across the CD range the ARDE is mild: a 22 nm hole needs 7 % longer than a 30 nm hole. The buffer open is ion-driven and its aspect ratio is modest, so it is not the step where CD sensitivity matters most. That step is the recess (Chapter 7).

## 6.3 Overetch

The buffer overetch must cover:

- the clear-time spread from CD (about 1.5 s over the CD range);
- buffer thickness non-uniformity (±1 nm, about ±1 s);
- topography of the incoming surface. Cap CMP can leave the nitride caps 2–3 nm proud of or below the silicon, and the buffer is correspondingly thinner or thicker over them.

A 15–20 % overetch (3–4 s) is typical. Because the buffer chemistry etches oxide and nitride at similar rates, and silicon several times slower, this overetch already recesses the STI and cap by about 2–3 nm before the recess step begins. It also removes the native oxide on the node and starts a fluorocarbon film on it. The recess budget in Chapter 8 includes this pre-recess.

## 6.4 Endpoint

The DC open area is large for a contact layer. One 32 nm hole per 3468 nm² cell pair is 23 % of the array at the buffer top and 15 % at the silicon surface. The array occupies about half of the die. Optical emission therefore shows usable transitions:

- the **CN** band at 387 nm falls when the SiN layer clears into the oxide layer;
- **CO** (and SiF) changes when the oxide clears onto the mixed floor.

The second transition is weak, because the floor is itself partly oxide (STI, liner) and partly nitride (caps). It is ambiguous for the same reason. The usual practice is to endpoint the SiN-to-oxide transition and time the rest of the buffer. Interferometric or reflectance endpoint on the array is also used.

## 6.5 Stopping on the floor

The buffer's own oxide layer is a convenient pause. A short, oxide-selective step can clear the last few nanometres of oxide while barely touching nitride or silicon, so the floor arrives at the recess step flat and clean. If the recess step uses recipe A (silicon-selective), this is the natural sequence. If it uses recipe B (co-recess), the transition matters less, because B etches all floor materials together.

## 6.6 Charging

The hole is lined with dielectric (carbon, SiN, SiO₂) down to a floor that is partly silicon. Electron shading charges the walls negatively and the floor positively. On a silicon floor connected to the substrate, the charge leaks away and the effect is small. On floor patches of oxide and nitride it does not, and slow ions can be deflected toward the walls or into the narrow liner slit. This is one mechanism by which the liner pit of Chapter 8 can run ahead of the model.
