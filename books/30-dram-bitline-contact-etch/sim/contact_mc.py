#!/usr/bin/env python3
"""Monte Carlo transport, mixed-floor recess and contact-variation models for
the DRAM bit-line contact (direct contact, DC) etch.

Geometry: a cylindrical contact hole of bottom diameter D (radius r = D/2),
depth measured from the top of the remaining carbon mask.  Lengths in the
transport model are in units of the hole radius; AR = depth / diameter.

Neutrals enter through the opening with a cosine distribution, re-emit
diffusely (cosine about the inward wall normal) and are lost at each wall
hit with probability s.  With s = 1 the floor fraction must equal the exact
view factor between two coaxial disks, 0.5 (X - sqrt(X^2 - 4)),
X = 2 + 4 AR^2.
Ions enter with independent Gaussian tilts (sigma) in two directions and are
lost on any wall hit.  The hole is convex, so an ion reaches the floor if
and only if its landing point lies inside the floor disk.

Mixed-floor recess model (after the buffer is cleared): the floor of the
hole holds silicon (the bit-line node of the active area), STI oxide and the
silicon-nitride caps of the two buried word lines, with the thin gate-oxide
liner of each word-line trench between silicon and cap.  Each material m recesses
  dd_m/dt = R_ion,m G_ion(AR_h) G_ion(AR_p,m) + R_n,m G_n(AR_h) G_n(AR_p,m)
  AR_h   = (H_mask + H_buf + d_min) / D        (the hole above the floor)
  AR_p,m = (d_m - d_min) / w_m                 (a pit of width w_m in the floor)
Contact model: top-view geometry of the bit-line node (an active-area strip
of width W_AA tilted by PHI, cut by two word-line trenches) and its two
neighbouring strips (storage-node sides of adjacent cells).  The contact area
is the part of the hole bottom that lands on the node; the resistance is
rho_c / A plus the poly plug.  Variation: Monte Carlo of top CD, taper and
overlay, at three node scales.
Outputs: transport_results.csv, buffer_clear.csv, recess_results.csv,
  contact_results.csv, variation_results.csv.
"""
import csv, math, sys
import numpy as np

rng = np.random.default_rng(30)
ARS = [0.25, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20]
SS = [0.01, 0.05, 0.1, 0.3, 1.0]
SIGS = [1.0, 2.0, 4.0, 8.0]           # ion angular width, degrees
N = 200_000


def write(name, rows):
    with open(name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)


# ---------------------------------------------------------------- transport
def cos_local(n):
    u = rng.random(n)
    phi = 2 * np.pi * rng.random(n)
    return np.sqrt(u), np.sqrt(1 - u), phi          # cos(theta), sin(theta), phi


def disk_points(n):
    r = np.sqrt(rng.random(n))
    a = 2 * np.pi * rng.random(n)
    return r * np.cos(a), r * np.sin(a)


def neutral(ar, s, n):
    """Floor fraction for a cylinder of radius 1 and depth H = 2 AR (z downward)."""
    H = 2.0 * ar
    x, y = disk_points(n)
    z = np.zeros(n)
    c, sn, ph = cos_local(n)
    dx, dy, dz = sn * np.cos(ph), sn * np.sin(ph), c
    floor = 0
    while x.size:
        a = dx * dx + dy * dy
        b = 2 * (x * dx + y * dy)
        cc = np.minimum(x * x + y * y - 1.0, 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            tw = np.where(a > 1e-14, (-b + np.sqrt(np.maximum(b * b - 4 * a * cc, 0))) / (2 * a), np.inf)
            tz = np.where(dz > 0, (H - z) / dz, np.where(dz < 0, -z / dz, np.inf))
        end = tz <= tw
        floor += int((end & (dz > 0)).sum())
        t = np.minimum(tw, tz)
        x, y, z = x + dx * t, y + dy * t, z + dz * t
        keep = ~end & (rng.random(x.size) >= s)
        x, y, z = x[keep], y[keep], z[keep]
        rr = np.hypot(x, y)
        x, y = x / rr, y / rr                         # snap to the wall
        c, sn, ph = cos_local(x.size)
        nx, ny = -x, -y                               # inward normal
        tx, ty = -y, x                                # tangent around the hole
        dx = c * nx + sn * np.cos(ph) * tx
        dy = c * ny + sn * np.cos(ph) * ty
        dz = sn * np.sin(ph)
        x, y = x * (1 - 1e-12), y * (1 - 1e-12)
    return floor / n


def ion(ar, sig_deg, n):
    H = 2.0 * ar
    x, y = disk_points(n)
    s = np.radians(sig_deg)
    xf = x + H * np.tan(s * rng.standard_normal(n))
    yf = y + H * np.tan(s * rng.standard_normal(n))
    return float((xf * xf + yf * yf <= 1.0).mean())


def disk_exact(ar):
    X = 2 + 4 * ar * ar
    return 0.5 * (X - math.sqrt(X * X - 4))


# ------------------------------------------------------- mixed-floor recess
H_MASK, H_BUF = 70.0, 20.0            # remaining carbon mask, oxide/nitride buffer (nm)
DIAMS = [22.0, 26.0, 30.0]            # hole diameter at the silicon surface (nm)
MATS = ["Si", "ox", "SiN", "liner"]
# width of each floor patch (nm); "liner" is the 3.5 nm gate-oxide sliver
# between the node silicon and the word-line cap, etched at the oxide rates
W_PIT = {"Si": 16.0, "ox": 8.0, "SiN": 5.0, "liner": 3.5}
# buffer open: fluorocarbon, rates nm/s (ion-driven, neutral-assisted)
BUF = dict(ri=1.2, rn=0.15, sig=2.0, s=0.3)
# floor recipes: per material (R_ion, R_n) in nm/s, ion width, neutral loss
RECIPES = {
    "A": dict(name="Si-selective HBr/Cl2/O2", sig=4.0, s=0.1,
              Si=(0.90, 0.60), ox=(0.03, 0.00), SiN=(0.06, 0.01)),
    "B": dict(name="co-recess CF4/CHF3/Ar", sig=2.0, s=0.3,
              Si=(0.70, 0.20), ox=(0.80, 0.05), SiN=(0.75, 0.10)),
    "C": dict(name="dielectric-first C4F6/O2/Ar", sig=2.0, s=0.3,
              Si=(0.08, 0.02), ox=(1.00, 0.05), SiN=(0.60, 0.05)),
}
T_FLOOR, DT = 60.0, 0.02


def main():
    trows = []
    for ar in ARS:
        r = dict(AR=ar)
        for s in SS:
            r[f"n_s{s}"] = neutral(ar, s, N)
        r["disk_exact"] = disk_exact(ar)
        for sg in SIGS:
            r[f"i_sig{sg:g}"] = ion(ar, sg, N)
        trows.append(r)
        print(r, file=sys.stderr, flush=True)
    write("transport_results.csv", trows)

    ar_g = np.array([0.0] + ARS)
    GN = {s: np.array([1.0] + [r[f"n_s{s}"] for r in trows]) for s in SS}
    GI = {sg: np.array([1.0] + [r[f"i_sig{sg:g}"] for r in trows]) for sg in SIGS}
    gn = lambda ar, s: float(np.interp(ar, ar_g, GN[s]))
    gi = lambda ar, sg: float(np.interp(ar, ar_g, GI[sg]))

    # buffer clear time per diameter (uniform layer)
    buf_clear = {}
    for D in DIAMS:
        d, t = 0.0, 0.0
        while d < H_BUF:
            ar = (H_MASK + d) / D
            d += (BUF["ri"] * gi(ar, BUF["sig"]) + BUF["rn"] * gn(ar, BUF["s"])) * DT
            t += DT
        buf_clear[D] = t
        print(f"buffer clear D={D}: {t:.2f} s", file=sys.stderr)

    rows = []
    nsteps = int(round(T_FLOOR / DT))
    state = {(k, D): {m: 0.0 for m in MATS} for k in RECIPES for D in DIAMS}
    for i in range(nsteps + 1):
        t = i * DT
        if i % 10 == 0:
            row = dict(t=round(t, 2))
            for k in RECIPES:
                for D in DIAMS:
                    for m in MATS:
                        row[f"{k}_D{D:g}_{m}"] = state[(k, D)][m]
            rows.append(row)
        for k, rc in RECIPES.items():
            for D in DIAMS:
                st = state[(k, D)]
                dmin = min(st.values())
                arh = (H_MASK + H_BUF + dmin) / D
                gih, gnh = gi(arh, rc["sig"]), gn(arh, rc["s"])
                new = {}
                for m in MATS:
                    arp = (st[m] - dmin) / W_PIT[m]
                    ri, rn = rc["ox" if m == "liner" else m]
                    new[m] = st[m] + (ri * gih * gi(arp, rc["sig"]) + rn * gnh * gn(arp, rc["s"])) * DT
                st.update(new)
    write("recess_results.csv", rows)

    # ------------------------------------------------ contact geometry
    contact_rows = contact_sweep()
    write("contact_results.csv", contact_rows)
    vrows = variation()
    write("variation_results.csv", vrows)
    with open("buffer_clear.csv", "w") as f:
        f.write("D,t_clear\n" + "".join(f"{D:g},{buf_clear[D]:.2f}\n" for D in DIAMS))


# Top view: x along the bit line, y along the word line.  Word-line trenches
# occupy XB < |x| < XB + W_WL; the bit-line node is the active-area strip of
# width W_AA (normal to its axis), tilted by PHI from x, inside |x| < XB.
# Neighbouring strips (storage-node ends of adjacent cells) repeat at a
# perpendicular pitch P_AA.
PHI = math.radians(21.0)
GEOM = dict(XB=8.0, W_WL=18.0, W_AA=16.0, P_AA=32.0)
RHO_C = 1.5e6            # specific contact resistivity, ohm nm^2 (1.5e-8 ohm cm^2)
RHO_POLY = 1.0e4         # in-situ doped poly, ohm nm (1 mohm cm)
L_PLUG = 45.0            # plug height, buffer + recess (nm)
R_SPEC = 10_000.0        # contact resistance limit (ohm)
THETA0 = 81.5            # sidewall angle in the buffer (deg); top CD 32 -> 26 nm
D_TOP0 = 32.0

# Vogel spiral: quasi-uniform points in the unit disk for area integrals
K = 900
_k = np.arange(K) + 0.5
SPX = np.sqrt(_k / K) * np.cos(_k * math.pi * (3 - math.sqrt(5)))
SPY = np.sqrt(_k / K) * np.sin(_k * math.pi * (3 - math.sqrt(5)))


def in_strip(x, y, k, g):
    h = g["W_AA"] / (2 * math.cos(PHI))
    off = k * g["P_AA"] / math.cos(PHI)
    return (np.abs(x) < g["XB"]) & (np.abs(y - x * math.tan(PHI) - off) < h)


def para_vertices(k, g):
    h = g["W_AA"] / (2 * math.cos(PHI))
    off = k * g["P_AA"] / math.cos(PHI)
    t = math.tan(PHI)
    xb = g["XB"]
    return [(-xb, -xb * t + off - h), (xb, xb * t + off - h), (xb, xb * t + off + h), (-xb, -xb * t + off + h)]


def dist_to_para(cx, cy, k, g):
    """Distance from points (cx, cy) to the k-th strip parallelogram (0 if inside)."""
    V = para_vertices(k, g)
    inside = in_strip(cx, cy, k, g)
    d = np.full(np.shape(cx), np.inf)
    for i in range(4):
        (ax, ay), (bx, by) = V[i], V[(i + 1) % 4]
        ex, ey = bx - ax, by - ay
        tt = np.clip(((cx - ax) * ex + (cy - ay) * ey) / (ex * ex + ey * ey), 0, 1)
        d = np.minimum(d, np.hypot(cx - ax - tt * ex, cy - ay - tt * ey))
    return np.where(inside, 0.0, d)


def areas(D, ox, oy, g):
    """Fractions of the hole bottom on node Si, neighbour Si, WL cap and STI oxide."""
    r = D / 2
    x = ox + r * SPX
    y = oy + r * SPY
    node = in_strip(x, y, 0, g)
    nb = in_strip(x, y, 1, g) | in_strip(x, y, -1, g)
    cap = (np.abs(x) >= g["XB"]) & (np.abs(x) < g["XB"] + g["W_WL"])
    A = math.pi * r * r
    return A * node.mean(), A * nb.mean(), A * cap.mean(), A * (~node & ~nb & ~cap).mean()


def node_perimeter_in_hole(D, ox, oy, g, n=4000):
    """Length of node-Si edge inside the hole (sidewall exposed if Si stands as a mesa)."""
    r = D / 2
    L = 0.0
    V = para_vertices(0, g)
    for i in range(4):
        (ax, ay), (bx, by) = V[i], V[(i + 1) % 4]
        t = (np.arange(n) + 0.5) / n
        px, py = ax + t * (bx - ax), ay + t * (by - ay)
        inside = (px - ox) ** 2 + (py - oy) ** 2 <= r * r
        L += math.hypot(bx - ax, by - ay) * inside.mean()
    return L


def resistance(A, D):
    return RHO_C / np.maximum(A, 1e-9) + RHO_POLY * L_PLUG / (math.pi * D * D / 4)


def contact_sweep():
    g = GEOM
    rows = []
    for D in DIAMS:
        for direction in ("x", "y"):
            for o in np.arange(0.0, 10.01, 0.5):
                ox, oy = (o, 0.0) if direction == "x" else (0.0, o)
                a_node, a_nb, a_cap, a_ox = areas_fine(D, ox, oy, g)
                per = node_perimeter_in_hole(D, ox, oy, g)
                clr = float(min(dist_to_para(np.array(ox), np.array(oy), k, g) for k in (1, -1))) - D / 2
                rows.append(dict(D=D, dir=0 if direction == "x" else 1, ov=float(o),
                                 A_node=a_node, A_nb=a_nb, A_cap=a_cap, A_ox=a_ox,
                                 perim=per, clear_nb=clr,
                                 R=float(resistance(a_node, D))))
    return rows


def areas_fine(D, ox, oy, g, h=0.05):
    r = D / 2
    xs = np.arange(-r + h / 2, r, h)
    X, Y = np.meshgrid(xs, xs)
    m = X * X + Y * Y <= r * r
    x, y = X[m] + ox, Y[m] + oy
    node = in_strip(x, y, 0, g)
    nb = in_strip(x, y, 1, g) | in_strip(x, y, -1, g)
    cap = (np.abs(x) >= g["XB"]) & (np.abs(x) < g["XB"] + g["W_WL"])
    dA = h * h
    return (float(node.sum() * dA), float(nb.sum() * dA), float(cap.sum() * dA),
            float((~node & ~nb & ~cap).sum() * dA))


def variation():
    M, CH = 200_000, 5_000
    # (node scale, sigma top CD nm, sigma angle deg, sigma overlay per axis nm, rho_c factor)
    cases = [(1.0, 0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 0.0, 0.0, 1.0), (1.0, 0.0, 1.0, 0.0, 1.0),
             (1.0, 0.0, 0.0, 2.0, 1.0), (1.0, 1.0, 0.5, 2.0, 1.0), (1.0, 1.5, 1.0, 3.0, 1.0),
             (0.88, 1.0, 0.5, 2.0, 1.0), (0.88, 1.0, 0.5, 2.0, 0.6),
             (0.76, 1.0, 0.5, 2.0, 0.5), (0.76, 0.7, 0.35, 1.4, 0.5)]
    out = []
    for f, s_cd, s_ang, s_ov, rcf in cases:
        g = {k: v * f for k, v in GEOM.items()}
        hb = H_BUF * f
        Ds, As, Rs, CL = [], [], [], []
        for _ in range(M // CH):
            dt = D_TOP0 * f + s_cd * rng.standard_normal(CH)
            th = np.radians(THETA0 + s_ang * rng.standard_normal(CH))
            D = np.maximum(dt - 2 * hb / np.tan(th), 1.0)
            ox = s_ov * rng.standard_normal(CH)
            oy = s_ov * rng.standard_normal(CH)
            r = D[:, None] / 2
            x = ox[:, None] + r * SPX[None, :]
            y = oy[:, None] + r * SPY[None, :]
            A = math.pi * D * D / 4 * in_strip(x, y, 0, g).mean(axis=1)
            clr = np.minimum(dist_to_para(ox, oy, 1, g), dist_to_para(ox, oy, -1, g)) - D / 2
            Ds.append(D); As.append(A); CL.append(clr)
            Rs.append(rcf * RHO_C / np.maximum(A, 1e-9) + RHO_POLY * L_PLUG * f / (math.pi * D * D / 4))
        D, A, R, CLR = (np.concatenate(v) for v in (Ds, As, Rs, CL))
        row = dict(scale=f, sig_cd=s_cd, sig_ang=s_ang, sig_ov=s_ov, rho_f=rcf,
                   mean_D=float(D.mean()), std_D=float(D.std()),
                   mean_A=float(A.mean()), std_A=float(A.std()),
                   median_R=float(np.median(R)),
                   p_rhigh_ppm=float(1e6 * (R > R_SPEC).mean()),
                   mean_clr=float(CLR.mean()),
                   p_touch_ppm=float(1e6 * (CLR < 0).mean()))
        out.append(row)
        print(row, file=sys.stderr, flush=True)
    return out


if __name__ == "__main__":
    main()
