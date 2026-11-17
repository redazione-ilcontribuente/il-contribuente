#!/usr/bin/env python3
"""Archivia l'edizione del giorno di Il Contribuente.

Uso (dalla cartella del repo, dopo aver finito index.html):
    python3 strumenti/archivia.py

Fa tre cose:
1. copia index.html in rassegne/AAAA-MM-GG.html (link sistemati, titolo,
   descrizione e indirizzo propri per Google);
2. tiene online solo le ultime N edizioni create da questo script
   (i vecchi file senza il marcatore non vengono mai toccati);
3. riscrive l'elenco di archivio.html e la sitemap.xml.
Layout, CSS e struttura dell'edizione restano identici.
"""
import html, os, re, sys

N_EDIZIONI = 30          # quante edizioni tenere online (deciso da Mario, 17/11/2026)
BASE = "https://ilcontribuente.redazioneit.workers.dev/"
MARCATORE = "<!-- ic-archivio -->"
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]
PAGINE_FISSE = [
    ("", "daily", "1.0"),
    ("settimana/fatti.html", "weekly", "0.8"),
    ("SuperPotenze/superPower.html", "daily", "0.7"),
    ("sanzioni/sanzioni1.html", "daily", "0.7"),
    ("immigrazioneEuropa/immigrazione.html", "daily", "0.7"),
    ("guerre/index.html", "daily", "0.7"),
    ("guerre/israeleGuerre.html", "monthly", "0.6"),
    ("guerre/palestinaStoria.html", "monthly", "0.6"),
    ("guerre/pi.html", "monthly", "0.6"),
    ("guerre/ru.html", "monthly", "0.6"),
    ("dazi/dazi1.html", "daily", "0.7"),
    ("conflittiMondo/conflitto.html", "daily", "0.7"),
    ("glossario/glossario.html", "daily", "0.6"),
    ("archivio.html", "daily", "0.6"),
    ("redazione.html", "monthly", "0.5"),
    ("spazioPartner/comeFunziona.html", "monthly", "0.4"),
    ("spazioPartner/bitetti/", "monthly", "0.4"),
    ("spazioPartner/lucana/", "monthly", "0.4"),
    ("spazioPartner/testigrosso/", "monthly", "0.4"),
]


def data_lunga(d):
    a, m, g = d.split("-")
    return f"{int(g)} {MESI[int(m) - 1]} {a}"


def attr(t):
    return html.escape(t, quote=True)


def titoli_principali(s, quanti=3):
    out = []
    for m in re.findall(r"<h2[^>]*>(.*?)</h2>", s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m)).strip()
        t = re.sub(r"\s+", " ", t)
        if len(t) > 40 and t not in out:
            out.append(t.split(":")[0].split(".")[0])
        if len(out) == quanti:
            break
    return out


def prefissa_link(s):
    def fix(m):
        nome, v = m.group(1), m.group(2)
        if re.match(r"^(https?:|//|/|#|data:|mailto:|tel:|javascript:|\.\./)", v) or v == "":
            return m.group(0)
        return f'{nome}="../{v}"'
    return re.sub(r'\b(href|src)="([^"]*)"', fix, s)


def archivia(radice):
    s = open(os.path.join(radice, "index.html"), encoding="utf-8").read()
    d = re.search(r'data-edition="(\d{4}-\d{2}-\d{2})"', s).group(1)
    url = f"{BASE}rassegne/{d}.html"
    titolo = f"Il Contribuente — Rassegna stampa del {data_lunga(d)}"
    temi = titoli_principali(s)
    descr = f"Rassegna stampa del {data_lunga(d)}: " + "; ".join(temi) + "."
    a = prefissa_link(s)
    a = re.sub(r"<title>.*?</title>", f"<title>{html.escape(titolo)}</title>", a, count=1, flags=re.S)
    a = re.sub(r'<meta content="[^"]*" name="description"/>', f'<meta content="{attr(descr)}" name="description"/>', a, count=1)
    a = re.sub(r'<meta content="[^"]*" property="og:description"/>', f'<meta content="{attr(descr)}" property="og:description"/>', a, count=1)
    a = re.sub(r'<meta content="[^"]*" name="twitter:description"/>', f'<meta content="{attr(descr)}" name="twitter:description"/>', a, count=1)
    a = re.sub(r'<meta content="[^"]*" property="og:title"/>', f'<meta content="{attr(titolo)}" property="og:title"/>', a, count=1)
    a = re.sub(r'<meta content="[^"]*" property="og:url"/>', f'<meta content="{url}" property="og:url"/>', a, count=1)
    a = a.replace("<head>", f'<head>\n{MARCATORE}\n<link rel="canonical" href="{url}"/>', 1)
    barra = (f'<div id="ic-archivio-bar" style="background:#1b1e22;color:#efe9da;font-family:Inter,Arial,sans-serif;'
             f'font-size:14px;line-height:1.4;padding:10px 16px;text-align:center;">'
             f'Stai leggendo l\'edizione del {data_lunga(d)} · '
             f'<a href="../" style="color:#e8c66a;font-weight:600;text-decoration:underline;white-space:nowrap;">← Torna all\'edizione di oggi</a>'
             f' · <a href="../archivio.html" style="color:#efe9da;text-decoration:underline;white-space:nowrap;">Tutte le edizioni</a></div>')
    a = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + barra, a, count=1)
    os.makedirs(os.path.join(radice, "rassegne"), exist_ok=True)
    open(os.path.join(radice, "rassegne", f"{d}.html"), "w", encoding="utf-8").write(a)
    return d


def edizioni(radice):
    cart = os.path.join(radice, "rassegne")
    out = []
    for f in sorted(os.listdir(cart), reverse=True):
        p = os.path.join(cart, f)
        if re.match(r"\d{4}-\d{2}-\d{2}\.html$", f):
            with open(p, encoding="utf-8") as fh:
                if MARCATORE in fh.read(400):
                    out.append(f[:-5])
    return out


def pota(radice, eds):
    for d in eds[N_EDIZIONI:]:
        os.remove(os.path.join(radice, "rassegne", f"{d}.html"))
    return eds[:N_EDIZIONI]


def aggiorna_archivio(radice, eds):
    p = os.path.join(radice, "archivio.html")
    s = open(p, encoding="utf-8").read()
    voci = "".join(
        f'<a class="entry" href="rassegne/{d}.html">\n'
        f'<span class="entry-date">{int(d[8:])} {MESI[int(d[5:7]) - 1].capitalize()} {d[:4]}</span>\n'
        f'<span class="entry-arrow">Leggi →</span>\n</a>\n' for d in eds)
    i = s.index('<div class="list">') + len('<div class="list">')
    j = s.index("</div>", i)
    s = s[:i] + "\n" + voci + s[j:]
    open(p, "w", encoding="utf-8").write(s)


def aggiorna_sitemap(radice, eds, oggi):
    righe = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    voci = PAGINE_FISSE + [(f"rassegne/{d}.html", "never", "0.6") for d in eds]
    for p, f, pr in voci:
        lm = p[9:19] if p.startswith("rassegne/") else oggi
        righe += ["  <url>", f"    <loc>{BASE}{p}</loc>", f"    <lastmod>{lm}</lastmod>",
                  f"    <changefreq>{f}</changefreq>", f"    <priority>{pr}</priority>", "  </url>"]
    righe.append("</urlset>")
    open(os.path.join(radice, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(righe) + "\n")


if __name__ == "__main__":
    radice = sys.argv[1] if len(sys.argv) > 1 else "."
    oggi = archivia(radice)
    eds = pota(radice, edizioni(radice))
    aggiorna_archivio(radice, eds)
    aggiorna_sitemap(radice, eds, oggi)
    print(f"Archiviata {oggi}. Edizioni online: {', '.join(eds)}")
