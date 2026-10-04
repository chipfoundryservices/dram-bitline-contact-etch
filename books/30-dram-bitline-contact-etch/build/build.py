#!/usr/bin/env python3
"""Assemble Book 30 into HTML and EPUB; tables/figures come from sim results."""
import csv, glob, html, math, os, re, zipfile, uuid
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(ROOT, "figures"), exist_ok=True)
TITLE = "DRAM Bit-Line Contact Etch"
SLUG = "book30-dram-bitline-contact-etch"

PARTS = {1: "Part I — Foundations", 5: "Part II — Contact Etch Physics",
         9: "Part III — Contact Formation and Integration",
         13: "Part IV — Control, Variation and Outlook"}


def load(name):
    return [{k: float(v) for k, v in r.items()}
            for r in csv.DictReader(open(os.path.join(ROOT, "sim", name)))]


TR = load("transport_results.csv")
RR = load("recess_results.csv")
CR = load("contact_results.csv")
VR = load("variation_results.csv")
BC = load("buffer_clear.csv")
SS = [0.01, 0.05, 0.1, 0.3, 1.0]
SIGS = [1, 2, 4, 8]
DIAMS = [22, 26, 30]
MATS = [("Si", "Si node"), ("ox", "STI oxide"), ("SiN", "WL cap SiN"), ("liner", "gate-oxide liner")]
RECIPES = {"A": "A — Si-selective HBr/Cl₂/O₂", "B": "B — co-recess CF₄/CHF₃/Ar",
           "C": "C — dielectric-first C₄F₆/O₂/Ar"}


def fmt(x):
    return f"{x:.4f}" if x >= 1e-3 else f"{x:.1e}"


def g(x):
    return f"{x:g}"


def table(head, body):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def t_neutral():
    return table(["AR"] + [f"s={g(s)}" for s in SS],
                 [[g(r["AR"])] + [fmt(r[f"n_s{s}"]) for s in SS] for r in TR])


def t_ion():
    return table(["AR"] + [f"σ={s}°" for s in SIGS],
                 [[g(r["AR"])] + [fmt(r[f"i_sig{s}"]) for s in SIGS] for r in TR])


def t_valid():
    return table(["AR", "MC, s=1", "exact disk-to-disk", "difference", "counts at floor (N = 200 000)"],
                 [[g(r["AR"]), fmt(r["n_s1.0"]), fmt(r["disk_exact"]),
                   f"{r['n_s1.0']-r['disk_exact']:+.4f}", f"{r['n_s1.0']*200000:.0f}"] for r in TR])


def t_holeslot():
    body = []
    for ar in (0.5, 1, 2, 3, 4, 5, 8, 10):
        slot = math.sqrt(1 + ar * ar) - ar
        X = 2 + 4 * ar * ar
        hole = 0.5 * (X - math.sqrt(X * X - 4))
        body.append([g(ar), fmt(slot), fmt(hole), f"{slot/hole:.1f}"])
    return table(["AR", "slot √(1+AR²)−AR", "round hole", "slot / hole"], body)


def t_buffer():
    return table(["hole diameter at Si (nm)", "AR at buffer top", "AR at Si surface", "buffer clear time (s)"],
                 [[g(r["D"]), f"{70/r['D']:.2f}", f"{90/r['D']:.2f}", f"{r['t_clear']:.1f}"] for r in BC])


def depth(r, k, D, m):
    return r[f"{k}_D{D}_{m}"]


def t_recess_t():
    body = []
    for k in RECIPES:
        for r in RR:
            if r["t"] in (10, 20, 30, 40, 50, 60):
                body.append([k, g(r["t"])] + [f"{depth(r, k, 26, m):.1f}" for m, _ in MATS]
                            + [f"{depth(r, k, 26, 'ox') - depth(r, k, 26, 'Si'):+.1f}"])
    return table(["recipe", "t (s)"] + [f"{n} (nm)" for _, n in MATS] + ["step oxide − Si (nm)"], body)


def t_recess25():
    body = []
    for k in RECIPES:
        for D in DIAMS:
            hit = next((r for r in RR if depth(r, k, D, "Si") >= 25 - 1e-9), None)
            if hit is None:
                last = RR[-1]
                body.append([k, g(D), "> 60"] + [f"{depth(last, k, D, m):.1f}" for m, _ in MATS[1:]] + ["(at 60 s)"])
            else:
                body.append([k, g(D), g(hit["t"])] + [f"{depth(hit, k, D, m):.1f}" for m, _ in MATS[1:]]
                            + [f"{60 - depth(hit, k, D, 'SiN'):.1f}"])
    return table(["recipe", "D (nm)", "t for 25 nm Si (s)", "STI oxide (nm)", "WL cap SiN (nm)",
                  "liner (nm)", "cap left over WL (nm)"], body)


def t_contact():
    body = []
    for D in DIAMS:
        for dr, dn in ((0, "x"), (1, "y")):
            for r in CR:
                if r["D"] == D and r["dir"] == dr and r["ov"] in (0, 2, 4, 6, 8, 10):
                    body.append([g(D), dn, g(r["ov"]), f"{r['A_node']:.0f}", f"{r['A_cap']:.0f}",
                                 f"{r['A_ox']:.0f}", f"{r['A_nb']:.1f}", f"{r['perim']:.1f}",
                                 f"{r['clear_nb']:.1f}", f"{r['R']/1000:.2f}"])
    return table(["D (nm)", "overlay axis", "overlay (nm)", "node Si (nm²)", "WL cap (nm²)", "STI (nm²)",
                  "neighbour Si (nm²)", "node edge in hole (nm)", "clearance to neighbour (nm)", "R (kΩ)"], body)


def t_contact_short():
    body = []
    for D in DIAMS:
        for r in CR:
            if r["D"] == D and r["dir"] == 1 and r["ov"] in (0, 4, 8):
                rx = next(q for q in CR if q["D"] == D and q["dir"] == 0 and q["ov"] == r["ov"])
                body.append([g(D), g(r["ov"]), f"{rx['A_node']:.0f}", f"{r['A_node']:.0f}",
                             f"{rx['R']/1000:.2f}", f"{r['R']/1000:.2f}", f"{r['clear_nb']:.1f}"])
    return table(["D (nm)", "overlay (nm)", "node Si, x-shift (nm²)", "node Si, y-shift (nm²)",
                  "R, x-shift (kΩ)", "R, y-shift (kΩ)", "clearance, y-shift (nm)"], body)


def t_var():
    return table(["node scale", "σ CD (nm)", "σ angle (°)", "σ overlay /axis (nm)", "ρc factor", "σ bottom D (nm)",
                  "mean area (nm²)", "σ area (nm²)", "median R (kΩ)", "R > 10 kΩ (ppm)",
                  "mean clearance (nm)", "touches neighbour (ppm)"],
                 [[g(r["scale"]), g(r["sig_cd"]), g(r["sig_ang"]), g(r["sig_ov"]), g(r["rho_f"]),
                   f"{r['std_D']:.2f}", f"{r['mean_A']:.0f}", f"{r['std_A']:.1f}", f"{r['median_R']/1000:.2f}",
                   f"{r['p_rhigh_ppm']:.0f}", f"{r['mean_clr']:.1f}", f"{r['p_touch_ppm']:.0f}"] for r in VR])


def t_recess_full(k):
    body = []
    for r in RR:
        if abs(r["t"] / 5 - round(r["t"] / 5)) < 1e-6:
            body.append([g(r["t"])] + [f"{depth(r, k, D, m):.1f}" for D in DIAMS for m in ("Si", "ox", "SiN", "liner")])
    head = ["t (s)"] + [f"D{D} {m}" for D in DIAMS for m in ("Si", "ox", "SiN", "lin")]
    return table(head, body)


COLS = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#555"]
DASH = {"solid": "", "dash": ' stroke-dasharray="7 4"', "dot": ' stroke-dasharray="2 3"'}


def svg_plot(series, title, xlabel, ylabel, logx=False, logy=False, legend=(None, None), ymax=None):
    """series: list of (name, points, colour index, dash style)."""
    W, H, L, R, T, B = 620, 400, 70, 20, 30, 55
    xs = [p[0] for s in series for p in s[1]]
    ys = [p[1] for s in series for p in s[1] if not logy or p[1] > 0]
    fx = math.log10 if logx else (lambda v: v)
    fy = math.log10 if logy else (lambda v: v)
    x0, x1 = fx(min(xs)), fx(max(xs))
    if logy:
        y0, y1 = math.floor(math.log10(min(ys))), math.ceil(math.log10(max(ys)))
        yt = [(10**e, f"1e{e}") for e in range(y0, y1 + 1)]
    else:
        top = ymax or max(ys); step = 10 ** math.floor(math.log10(top))
        if top / step < 3: step /= 2
        y0, y1 = 0.0, math.ceil(top / step) * step
        yt = [(k * step, g(round(k * step, 6))) for k in range(int(round(y1 / step)) + 1)]
    px = lambda x: L + (fx(x) - x0) / (x1 - x0) * (W - L - R)
    py = lambda y: T + (y1 - fy(max(y, 10**y0) if logy else y)) / (y1 - y0) * (H - T - B)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<text x="{W/2}" y="18" text-anchor="middle" font-weight="bold">{title}</text>']
    for v, lab in yt:
        y = py(v)
        o.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" stroke="#ddd"/>'
                 f'<text x="{L-6}" y="{y+4:.1f}" text-anchor="end">{lab}</text>')
    if logx:
        ticks = [v for v in (0.25, 0.5, 1, 2, 5, 10, 20, 50) if min(xs) <= v <= max(xs)]
    else:
        span = max(xs) - min(xs)
        st = 1 if span <= 12 else 2 if span <= 24 else 10 if span <= 100 else 20
        ticks = [v for v in range(int(min(xs)), int(max(xs)) + 1) if v % st == 0]
    for x in ticks:
        o.append(f'<line x1="{px(x):.1f}" x2="{px(x):.1f}" y1="{T}" y2="{H-B}" stroke="#eee"/>'
                 f'<text x="{px(x):.1f}" y="{H-B+16}" text-anchor="middle">{g(x)}</text>')
    o.append(f'<rect x="{L}" y="{T}" width="{W-L-R}" height="{H-T-B}" fill="none" stroke="#444"/>')
    o.append(f'<text x="{(L+W-R)/2}" y="{H-12}" text-anchor="middle">{xlabel}</text>')
    o.append(f'<text transform="translate(16 {(T+H-B)/2}) rotate(-90)" text-anchor="middle">{ylabel}</text>')
    lx = W - R - 190 if legend[0] == "right" else L + 10
    ly = H - B - 16 * len(series) - 10 if legend[1] == "bottom" else T
    o.append(f'<rect x="{lx-4}" y="{ly+2}" width="186" height="{16*len(series)+8}" fill="white" fill-opacity="0.85"/>')
    for i, (name, pts, ci, ds) in enumerate(series):
        c = COLS[ci % len(COLS)]
        d = " ".join(f"{px(x):.1f},{py(min(y, y1) if not logy else y):.1f}" for x, y in pts)
        o.append(f'<polyline points="{d}" fill="none" stroke="{c}" stroke-width="2"{DASH[ds]}/>')
        o.append(f'<line x1="{lx}" x2="{lx+16}" y1="{ly+10+i*16}" y2="{ly+10+i*16}" stroke="{c}" stroke-width="2"{DASH[ds]}/>'
                 f'<text x="{lx+22}" y="{ly+14+i*16}">{name}</text>')
    o.append("</svg>")
    return "\n".join(o)


def fig_transport():
    s = [(f"neutral s={g(v)}", [(r["AR"], r[f"n_s{v}"]) for r in TR], i, "dash") for i, v in enumerate((0.1, 1.0))]
    s += [(f"ion σ={v}°", [(r["AR"], r[f"i_sig{v}"]) for r in TR], i + 2, "solid") for i, v in enumerate(SIGS)]
    s.append(("exact disk view factor", [(r["AR"], r["disk_exact"]) for r in TR], 5, "dot"))
    return ("Figure 4.1", "Fraction of neutrals (wall loss s, dashed) and of ions (angular width σ, solid) entering a round contact hole that reach its floor. The s = 1 Monte Carlo curve lies on the exact disk-to-disk view factor (dotted) within counting error.",
            svg_plot(s, "Ion and neutral delivery to the floor of a contact hole", "aspect ratio (depth / diameter)", "floor fraction", logx=True, logy=True, legend=(None, "bottom")))


def fig_recess():
    s = []
    for ci, k in enumerate(RECIPES):
        for m, ds, lab in (("Si", "solid", "Si"), ("ox", "dash", "STI ox"), ("SiN", "dot", "cap SiN")):
            s.append((f"{k}: {lab}", [(r["t"], depth(r, k, 26, m)) for r in RR], ci, ds))
    return ("Figure 7.1", "Recess of each floor material below the silicon surface against time after the buffer clears, 26 nm hole, for the three recipe families. Solid: node silicon; dashed: STI oxide; dotted: word-line cap nitride. A digs a silicon pit, B keeps the floor nearly flat, C leaves a silicon mesa.",
            svg_plot(s, "Mixed-floor recess, 26 nm contact", "time after buffer clear (s)", "recess below Si surface (nm)"))


def fig_liner():
    s = []
    for ci, k in enumerate(RECIPES):
        if k == "A":
            continue
        s.append((f"{k}: cap SiN", [(r["t"], depth(r, k, 26, "SiN")) for r in RR], ci, "solid"))
        s.append((f"{k}: gate-oxide liner", [(r["t"], depth(r, k, 26, "liner")) for r in RR], ci, "dash"))
        s.append((f"{k}: node Si", [(r["t"], depth(r, k, 26, "Si")) for r in RR], ci, "dot"))
    return ("Figure 8.1", "Depth reached in the word-line cap nitride and down the 3.5 nm gate-oxide liner, against time, for recipes B and C (26 nm hole); node-silicon depth dotted for reference. The word-line metal top is 60 nm below the silicon surface.",
            svg_plot(s, "Cap and liner attack beside the node", "time after buffer clear (s)", "depth below Si surface (nm)"))


def fig_contact():
    s = []
    for ci, D in enumerate(DIAMS):
        for dr, ds, lab in ((0, "solid", "x (along BL)"), (1, "dash", "y (along WL)")):
            s.append((f"D={D} nm, {lab}", [(r["ov"], r["A_node"]) for r in CR if r["D"] == D and r["dir"] == dr], ci, ds))
    return ("Figure 10.1", "Contact area on the bit-line node against overlay error along the bit line (solid) and along the word line (dashed) for three hole diameters at the silicon surface. The node itself is 274 nm²; above about 26 nm the hole covers it and area becomes insensitive to CD.",
            svg_plot(s, "Node contact area versus overlay", "overlay error (nm)", "contact area on node Si (nm²)", legend=(None, "bottom")))


def figure_html(f, name):
    label, cap, svg = f()
    open(os.path.join(ROOT, "figures", name + ".svg"), "w").write(svg)
    return f'<figure>{svg}<figcaption><b>{label}.</b> {cap}</figcaption></figure>'


def subst(md):
    rep = {"{{TABLE:neutral}}": t_neutral, "{{TABLE:ion}}": t_ion, "{{TABLE:valid}}": t_valid,
           "{{TABLE:holeslot}}": t_holeslot, "{{TABLE:buffer}}": t_buffer,
           "{{TABLE:recess_t}}": t_recess_t, "{{TABLE:recess25}}": t_recess25,
           "{{TABLE:contact}}": t_contact, "{{TABLE:contact_short}}": t_contact_short, "{{TABLE:var}}": t_var,
           "{{TABLE:recessA}}": lambda: t_recess_full("A"), "{{TABLE:recessB}}": lambda: t_recess_full("B"),
           "{{TABLE:recessC}}": lambda: t_recess_full("C"),
           "{{FIG:transport}}": lambda: figure_html(fig_transport, "transport_vs_ar"),
           "{{FIG:recess}}": lambda: figure_html(fig_recess, "mixed_floor_recess"),
           "{{FIG:liner}}": lambda: figure_html(fig_liner, "cap_and_liner"),
           "{{FIG:contact}}": lambda: figure_html(fig_contact, "contact_area_vs_overlay")}
    for k, v in rep.items():
        if k in md:
            md = md.replace(k, "\n\n" + v() + "\n\n")
    return md


def read(p):
    return open(p, encoding="utf-8").read()


# ---- collect sections: (id, label, title, markdown)
secs = [("front", "", "Preface", read(os.path.join(ROOT, "frontmatter.md")))]
for p in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md"))):
    n = int(os.path.basename(p).split("-")[0])
    md = read(p)
    secs.append((f"ch{n:02d}", str(n), md.splitlines()[0].lstrip("# ").strip(), md))
for p in sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md"))):
    L = os.path.basename(p)[0]
    md = read(p)
    secs.append((f"app{L}", L, md.splitlines()[0].lstrip("# ").strip(), md))
secs.append(("glossary", "", "Glossary", read(os.path.join(ROOT, "backmatter", "glossary.md"))))

# ---- index
plain = {s[0]: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s[3])) for s in secs}
def ref(sid):
    return sid[2:].lstrip("0") if sid.startswith("ch") else ("App. " + sid[3:] if sid.startswith("app") else None)
idx = {}
for line in read(os.path.join(ROOT, "backmatter", "index_terms.txt")).splitlines():
    if not line.strip():
        continue
    term, *pats = line.split("|")
    hits = []
    for sid, text in plain.items():
        r = ref(sid)
        if r and any(re.search(re.escape(p), text, re.I) for p in pats):
            hits.append((sid, r))
    idx[term] = hits
missing = [t for t, h in idx.items() if not h]
if missing:
    print("index terms with no hits:", ", ".join(missing))
idx_md = "# Index\n\n" + "\n\n".join(
    f"**{t}** — " + ", ".join(f'<a href="#{sid}">{r}</a>' for sid, r in h)
    for t, h in sorted(idx.items(), key=lambda kv: kv[0].lower()) if h) + "\n"
secs.append(("index", "", "Index", idx_md))

md_ext = ["tables", "fenced_code", "sane_lists"]
bodies = {}
for sid, lab, title, md in secs:
    bodies[sid] = markdown.markdown(subst(md), extensions=md_ext)
left = [m for sid in bodies for m in re.findall(r"\{\{[A-Z]+:\w+\}\}", bodies[sid])]
if left:
    raise SystemExit(f"unresolved placeholders: {left}")

CSS = """body{font:17px/1.6 Georgia,serif;max-width:46em;margin:2em auto;padding:0 1em;color:#222}
h1{border-bottom:2px solid #333;padding-bottom:.2em;margin-top:2.5em}h2{margin-top:1.8em}
table{border-collapse:collapse;margin:1em 0;font:14px sans-serif;display:block;overflow-x:auto}td,th{border:1px solid #bbb;padding:3px 8px;text-align:right}
th{background:#eee}td:first-child,th:first-child{text-align:left}blockquote{border-left:4px solid #999;margin:1em 0;padding:.2em 1em;color:#444}
code,pre{background:#f3f3f3;font-size:14px}pre{padding:.7em;overflow-x:auto}figure{margin:1.5em 0}figure svg{width:100%;height:auto}
figcaption{font:14px sans-serif;color:#444}.part{font:700 1.1em sans-serif;text-transform:uppercase;letter-spacing:.1em;margin-top:4em;color:#555}"""

# ---- HTML
toc = ["<h1>Contents</h1><ul>"]
for sid, lab, title, _ in secs:
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        toc.append(f'<li><b>{PARTS[int(sid[2:])]}</b></li>')
    toc.append(f'<li><a href="#{sid}">{title}</a></li>')
toc.append("</ul>")
parts_html = []
for sid, lab, title, _ in secs:
    pre = ""
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        pre = f'<div class="part">{PARTS[int(sid[2:])]}</div>'
    parts_html.append(f'{pre}<section id="{sid}">{bodies[sid]}</section>')
doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title>'
       f'<meta name="viewport" content="width=device-width,initial-scale=1"><style>{CSS}</style></head><body>'
       + parts_html[0] + "".join(toc) + "".join(parts_html[1:]) + "</body></html>")
open(os.path.join(OUT, SLUG + ".html"), "w", encoding="utf-8").write(doc)

# ---- EPUB
def xhtml(title, body):
    body = re.sub(r"<(br|hr|img)([^>]*?)(?<!/)>", r"<\1\2/>", body)
    return ('<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
            f'<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"/></head>'
            f'<body>{body}</body></html>')

epub = os.path.join(OUT, SLUG + ".epub")
uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "dram-bitline-contact-etch/book30"))
with zipfile.ZipFile(epub, "w") as z:
    z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip")
    z.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
    items, spine, nav = [], [], []
    for sid, lab, title, _ in secs:
        fn = f"{sid}.xhtml"
        z.writestr("OEBPS/" + fn, xhtml(title, re.sub(r'href="#(\w+)"', r'href="\1.xhtml"', bodies[sid])), zipfile.ZIP_DEFLATED)
        items.append(f'<item id="{sid}" href="{fn}" media-type="application/xhtml+xml" properties="svg"/>'
                     if "<svg" in bodies[sid] else f'<item id="{sid}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{sid}"/>')
        nav.append(f'<li><a href="{fn}">{html.escape(title)}</a></li>')
    z.writestr("OEBPS/nav.xhtml", '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>Contents</title></head><body><nav epub:type="toc"><h1>Contents</h1><ol>' + "".join(nav) + "</ol></nav></body></html>", zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", f'<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="id">{uid}</dc:identifier><dc:title>{TITLE}</dc:title><dc:language>en</dc:language><meta property="dcterms:modified">2026-10-04T00:00:00Z</meta></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="css" href="style.css" media-type="text/css"/>' + "".join(items) + "</manifest><spine>" + "".join(spine) + "</spine></package>", zipfile.ZIP_DEFLATED)
words = sum(len(t.split()) for t in plain.values())
print(f"built {len(secs)} sections, ~{words} words -> {OUT}")
