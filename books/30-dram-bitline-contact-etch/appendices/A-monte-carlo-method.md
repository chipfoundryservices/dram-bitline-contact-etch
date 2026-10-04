# Appendix A — The Monte Carlo Method

## A.1 Geometry

The contact hole is a cylinder of radius 1 (all lengths in units of the hole radius) and depth *H* = 2 AR, where AR is the depth divided by the diameter, measured from the top of the remaining mask. *z* increases downward from the opening at *z* = 0 to the floor at *z* = *H*.

## A.2 Neutrals

Each neutral starts at a uniformly random point on the opening disk with a direction drawn from the cosine (Lambertian) distribution about +*z*. It travels in a straight line to the first of: the wall (solving |(*x*, *y*) + *t*(*d*ₓ, *d*ᵧ)| = 1 for the positive root), the floor, or the opening. At the wall it is lost with probability *s*. Otherwise it is re-emitted from the wall point with a new cosine direction about the inward normal. The floor fraction is the number that reach *z* = *H* divided by the number launched. 200 000 particles are used per point.

## A.3 Ions

Each ion starts at a uniformly random point on the opening with independent Gaussian tilts of width σ in *x* and *y*. Because the cylinder is convex, a straight trajectory that starts and ends inside it stays inside it. An ion therefore reaches the floor if and only if its landing point (*x* + *H* tan θₓ, *y* + *H* tan θᵧ) lies inside the unit disk.

## A.4 Validation

For *s* = 1 the neutral floor fraction must equal the view factor between two coaxial disks of radius *r* separated by *H*, F = ½(X − √(X² − 4)), X = 2 + 4 AR² (Appendix E):

{{TABLE:valid}}

The differences are within counting error. The relative error is about 1/√(counts), which is 4–7 % at AR 15–20, where only 120–200 particles reach the floor. At the aspect ratios that matter for the DC (≤ 6), the agreement is better than 1 %.

## A.5 Mixed-floor recess

The four floor materials (node Si, STI oxide, cap SiN, gate-oxide liner) are integrated explicitly with a step of 0.02 s:

d*d*ₘ/d*t* = R_ion,m G_ion(AR_h) G_ion(AR_p,m) + R_n,m G_n(AR_h) G_n(AR_p,m),

with AR_h = (70 + 20 + *d*_min)/*D* and AR_p,m = (*d*ₘ − *d*_min)/*w*ₘ. Transport fractions are interpolated linearly in AR from the tables of Appendix B, with G = 1 at AR = 0. The liner uses the oxide rates. The buffer clear time uses the same law for a uniform 20 nm layer starting at AR = 70/*D*. Results are written every 0.2 s.

## A.6 Contact geometry

The node is the parallelogram |*x*| < 8 nm, |*y* − *x* tan 21°| < 8/cos 21° nm. Neighbouring strips are offset by ±32/cos 21° nm in *y*. Word-line caps occupy 8 < |*x*| < 26 nm. In the overlay sweep (Chapter 10), areas are integrated on a 0.05 nm grid. Clearance is the exact distance from the hole centre to each neighbour parallelogram, minus the radius. In the variation model (Chapter 14), each contact's area is integrated over 900 points of a Vogel spiral in the hole. The spiral's systematic error is about 0.4 % (273.6 against 272.5 nm² at the nominal point).

## A.7 Reproducibility

The random generator is seeded (`default_rng(30)`), so all tables are reproducible. A full run takes about a minute on four cores.
