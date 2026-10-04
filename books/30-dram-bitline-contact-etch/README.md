# Book 30 — DRAM Bit-Line Contact Etch

16 chapters in four parts, Appendices A–G, glossary and index.

- Read: `build/out/book30-dram-bitline-contact-etch.html` or `.epub`
- Rebuild: `python3 build/build.py` (needs `markdown`)
- Re-run the simulation: `cd sim && python3 contact_mc.py` (needs `numpy`, about a minute)

`sim/contact_mc.py` computes the following. Everything else quantitative is illustrative.

- ion and neutral transport into a round contact hole, checked against the exact disk-to-disk view factor (Ch. 4, App. A–B);
- buffer clear times (Ch. 6);
- the recess of the mixed floor (node Si, STI oxide, word-line cap, gate-oxide liner) under three recipe families (Ch. 7–8);
- contact area, neighbour clearance and resistance against overlay (Ch. 10);
- the variation budget across three node scales (Ch. 14).
