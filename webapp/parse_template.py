#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estrae il contenuto di un'edizione (template.html o un file rassegne/YYYY-MM-DD.html)
in un JSON, cosi' la grafica (React) resta fissa e cambiano solo i dati.
Uso: python3 parse_template.py <input.html> <output.json>
"""
import sys
import json
from bs4 import BeautifulSoup


def inner_html(tag):
    if tag is None:
        return ""
    return tag.decode_contents().strip()


def text(tag):
    if tag is None:
        return ""
    return tag.get_text(strip=True)


def parse_articles(container):
    articles = []
    for art in container.select(":scope > div.article"):
        h3 = art.find("h3")
        lead_p = art.find("p", recursive=False)
        body_extra = art.find("div", class_="body-extra")
        source = art.find("span", class_="source")
        articles.append({
            "lead": "lead" in art.get("class", []),
            "title": text(h3),
            "leadParagraph": inner_html(lead_p),
            "bodyExtra": [inner_html(p) for p in body_extra.find_all("p")] if body_extra else [],
            "sourceHtml": inner_html(source),
        })
    return articles


def parse_duel_side(side):
    headline = side.find("div", class_="duel-headline")
    tag = side.find("span", class_="duel-tag")
    body_p = side.find("p", class_="body", recursive=False)
    body_extra = side.find("div", class_="body-extra")
    source = side.find("span", class_="source")
    classes = side.get("class", [])
    variant = "third" if "third" in classes else ("right" if "right" in classes else "left")
    return {
        "variant": variant,
        "tag": text(tag),
        "headline": inner_html(headline),
        "body": inner_html(body_p),
        "bodyExtra": [inner_html(p) for p in body_extra.find_all("p")] if body_extra else [],
        "sourceHtml": inner_html(source),
    }


def parse_duel(duel_div):
    fact = duel_div.find("div", class_="duel-fact-text")
    sides = [parse_duel_side(s) for s in duel_div.select(".duel-side")]
    return {"fact": inner_html(fact), "sides": sides}


def parse_chart_card(card):
    bars = []
    for row in card.select(".bar-row"):
        fill = row.find("div", class_="bar-fill")
        bars.append({
            "label": text(row.find("div", class_="bar-label")),
            "value": inner_html(row.find("div", class_="bar-value")),
            "style": (fill.get("style", "") if fill else ""),
            "fillClass": " ".join(c for c in fill.get("class", []) if c != "bar-fill") if fill else "",
            "tooltip": fill.get("data-tooltip", "") if fill else "",
        })
    table = card.find("table", class_="data-table")
    side_notes = card.find_all("div", class_="side-note")
    return {
        "id": card.get("id", ""),
        "title": text(card.find("div", class_="chart-title")),
        "period": inner_html(card.find("div", class_="chart-period")),
        "bars": bars,
        "sideNotes": [inner_html(n) for n in side_notes],
        "tableHtml": inner_html(table.find_parent("details")) if table else None,
        "sources": inner_html(card.find("div", class_="dv-sources")),
    }


def parse_timeline(el):
    items = []
    for it in el.select(":scope > .pb-timeline-item"):
        items.append({
            "year": text(it.find("div", class_="pb-timeline-year")),
            "text": inner_html(it.find("div", class_="pb-timeline-text")),
        })
    return items


def parse_map(el):
    note = el.find("div", class_="pb-map-note")
    points = []
    for card in el.select(".pb-map-card"):
        classes = card.get("class", [])
        group = ""
        for c in classes:
            if c.startswith("pb-map-card-"):
                group = c[len("pb-map-card-"):]
        points.append({
            "label": text(card.find("div", class_="pb-map-card-label")),
            "group": group,
            "text": inner_html(card.find("div", class_="pb-map-card-text")),
        })
    return {"note": inner_html(note) if note else "", "points": points}


def parse_denunce(el):
    items = []
    for card in el.select(":scope > .pb-denuncia-card"):
        chi = card.find("span", class_="pb-denuncia-chi")
        tipo = card.find("span", class_="pb-denuncia-tipo")
        formale = bool(tipo) and "formale" in tipo.get("class", [])
        meta = card.find("div", class_="pb-denuncia-meta")
        testo = card.find("div", class_="pb-denuncia-testo")
        esito_div = card.find("div", class_="pb-denuncia-esito")
        esito_span = esito_div.find("span") if esito_div else None
        esito_classes = [c for c in (esito_div.get("class", []) if esito_div else []) if c != "pb-denuncia-esito"]
        esito_stato = esito_classes[0] if esito_classes else ""
        fonte = card.find("div", class_="pb-denuncia-fonte")
        items.append({
            "chi": text(chi),
            "formale": formale,
            "quando": text(meta),
            "cosa": inner_html(testo),
            "esito": inner_html(esito_span) if esito_span else "",
            "esitoStato": esito_stato,
            "fonteHtml": inner_html(fonte),
        })
    return items


def parse_processi(el):
    items = []
    for card in el.select(":scope > .pb-processo-card"):
        titolo = card.find("div", class_="pb-processo-title")
        sub = card.find("div", class_="pb-processo-sub")
        stato_div = card.find("div", class_="pb-processo-stato")
        stato_span = stato_div.find_all("span")[-1] if stato_div else None
        fasi = []
        for fase in card.select(".pb-processo-fase"):
            fasi.append({
                "label": text(fase.find("div", class_="pb-processo-fase-label")),
                "testo": inner_html(fase.find("div", class_="pb-processo-fase-testo")),
            })
        nota = card.find("div", class_="pb-processo-nota")
        items.append({
            "titolo": text(titolo),
            "sottotitolo": text(sub),
            "statoAttuale": inner_html(stato_span) if stato_span else "",
            "fasi": fasi,
            "notaHtml": inner_html(nota) if nota else None,
        })
    return items


def parse_kpi_blocks(sec):
    """Scorre i figli diretti della sezione in ordine e ricostruisce la
    sequenza esatta di sotto-titoli, righe di kpi e grafici a barre
    (una sezione 'dati' come sicurezza-pubblica ha piu' blocchi di questo
    tipo in successione, non un unico elenco piatto). Le dashboard piu'
    ricche (es. petrolio-basilicata) aggiungono sotto-titoli (pb-subhead),
    cronologia (pb-timeline), cartina (pb-map-wrap), articoli annidati
    (articles), denunce (pb-denunce-list) e processi (pb-processi-list)."""
    blocks = []
    for child in sec.find_all(recursive=False):
        classes = child.get("class", [])
        if "section-head" in classes or "context-box" in classes:
            continue
        if "section-note" in classes:
            blocks.append({"kind": "note", "html": inner_html(child), "style": child.get("style", "")})
        elif "kpi-row" in classes:
            kpis = [{
                "label": text(k.find("div", class_="kpi-label")),
                "value": text(k.find("div", class_="kpi-value")),
                "note": inner_html(k.find("div", class_="kpi-note")),
                "extraClass": " ".join(c for c in k.get("class", []) if c != "kpi"),
            } for k in child.select(":scope > .kpi")]
            blocks.append({"kind": "kpiRow", "kpis": kpis})
        elif "chart-card" in classes:
            blocks.append({"kind": "chartCard", "card": parse_chart_card(child)})
        elif "pb-subhead" in classes:
            tag = child.find("span", class_="pb-subhead-tag")
            blocks.append({"kind": "subhead", "label": text(tag), "style": child.get("style", "")})
        elif "pb-timeline" in classes:
            blocks.append({"kind": "timeline", "items": parse_timeline(child)})
        elif "pb-map-wrap" in classes:
            m = parse_map(child)
            blocks.append({"kind": "map", "note": m["note"], "points": m["points"]})
        elif "articles" in classes:
            blocks.append({"kind": "articles", "articles": parse_articles(child)})
        elif "pb-denunce-list" in classes:
            blocks.append({"kind": "denunce", "items": parse_denunce(child)})
        elif "pb-processi-list" in classes:
            blocks.append({"kind": "processi", "items": parse_processi(child)})
    return blocks


def parse_section(sec):
    sec_id = sec.get("id", "")
    tag_span = sec.find("span", class_="section-tag")
    title = sec.find("h2", class_="section-title")
    note = sec.find("div", class_="section-note", recursive=False)
    context_boxes = sec.find_all("div", class_="context-box", recursive=False)

    result = {
        "id": sec_id,
        "tag": text(tag_span),
        "tagClass": " ".join(c for c in tag_span.get("class", []) if c != "section-tag") if tag_span else "",
        "title": inner_html(title),
        "note": inner_html(note) if note else None,
        "context": [inner_html(p) for box in context_boxes for p in box.find_all("p")],
    }

    # scope a figli diretti: una sezione 'kpi' come petrolio-basilicata puo'
    # contenere un blocco 'articles' annidato tra i suoi blocchi (le "ultime
    # notizie" della dashboard), che non deve far scambiare l'intera sezione
    # per una sezione di tipo 'articles'
    duel = sec.find("div", class_="duel", recursive=False)
    articles_container = sec.find("div", class_="articles", recursive=False)
    kpi_row = sec.find("div", class_="kpi-row", recursive=False)
    if duel:
        result["type"] = "duel"
        result["duel"] = parse_duel(duel)
        divergence = sec.select_one(".context-box:nth-of-type(2) p, .context-box[style] p")
        result["divergence"] = inner_html(divergence)
    elif kpi_row:
        # priorita' a kpi_row rispetto ad articles_container: una dashboard
        # come petrolio-basilicata ha ENTRAMBI come figli diretti (un blocco
        # 'articles' annidato tra i suoi blocchi, per le "ultime notizie"),
        # e in quel caso il tipo della sezione resta 'kpi'
        result["type"] = "kpi"
        # per le sezioni 'dati' (es. sicurezza-pubblica) ci sono piu' note e
        # piu' blocchi kpi-row/chart-card in sequenza: teniamo tutto in
        # 'blocks', nell'ordine esatto in cui compaiono nell'HTML, e non
        # duplichiamo la prima nota anche nel campo 'note' generico
        result["note"] = None
        result["blocks"] = parse_kpi_blocks(sec)
    elif articles_container:
        result["type"] = "articles"
        result["articles"] = parse_articles(articles_container)
    else:
        result["type"] = "unknown"
    return result


def main(src_path, out_path):
    with open(src_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml")

    body = soup.body
    edition = body.get("data-edition", "")
    published = body.get("data-published", "")

    masthead_title = soup.find("h1", class_="masthead-title")
    masthead_sub = soup.find("div", class_="masthead-sub")
    masthead_top_spans = [text(s) for s in soup.select(".masthead-top span")]

    badges = [{"label": text(a), "href": a.get("href", "")} for a in soup.select(".masthead-badges a.badge")]

    ticker_all = [text(s) for s in soup.select(".ticker span")]
    # in alcune edizioni il ticker e' duplicato x2 per l'animazione css (scorrimento continuo):
    # se la seconda meta' e' identica alla prima, teniamo solo la prima meta'
    if len(ticker_all) % 2 == 0 and len(ticker_all) > 0:
        half = len(ticker_all) // 2
        if ticker_all[:half] == ticker_all[half:]:
            ticker_all = ticker_all[:half]
    ticker = ticker_all

    market = []
    for card in soup.select(".market-card"):
        delta = card.find("div", class_="market-delta")
        market.append({
            "label": text(card.find("div", class_="market-label")),
            "value": text(card.find("div", class_="market-value")),
            "delta": text(delta),
            "deltaDirection": "up" if delta and "up" in delta.get("class", []) else ("down" if delta and "down" in delta.get("class", []) else None),
            "source": text(card.find("div", class_="market-source")),
            "style": card.get("style", ""),
            "valueStyle": card.find("div", class_="market-value").get("style", "") if card.find("div", class_="market-value") else "",
        })

    sidebar_fixed = []
    for a in soup.select(".sidebar-block:nth-of-type(1) a.sidebar-item"):
        sidebar_fixed.append({
            "href": a.get("href", ""),
            "title": text(a.find("span", class_="sidebar-item-title")),
            "desc": text(a.find("span", class_="sidebar-item-desc")),
        })

    term_name = soup.find("div", class_="sidebar-term-name")
    term_def = soup.find("div", class_="sidebar-term-def")

    sidebar_stats = []
    for s in soup.select(".sidebar-stats > div"):
        sidebar_stats.append({
            "value": text(s.find("div", class_="sidebar-stat-value")),
            "label": text(s.find("div", class_="sidebar-stat-label")),
        })

    toc = [{"href": a.get("href", ""), "label": text(a)} for a in soup.select(".toc-link")]

    toc_dashboards = []
    for a in soup.select(".toc-dashboard-card"):
        toc_dashboards.append({
            "href": a.get("href", ""),
            "tag": text(a.find("span", class_="toc-dashboard-tag")),
            "label": text(a.find("span", class_="toc-dashboard-label")),
            "mobileOnly": "toc-dashboard-mobile-only" in a.get("class", []),
        })

    verify_badge = soup.find("div", class_="verify-badge-inner")

    quotes = []
    for q in soup.select(".quote-day"):
        quotes.append({
            "label": text(q.find("div", class_="quote-day-label")),
            "text": text(q.find("div", class_="quote-day-text")),
            "author": text(q.find("div", class_="quote-day-author")),
        })

    stats_div = soup.find("div", class_="stats")
    top_stats_note = None
    if stats_div:
        sib = stats_div.find_next_sibling("div", class_="section-note")
        if sib:
            top_stats_note = inner_html(sib)

    top_stats = []
    for st in soup.select(".stats > .stat"):
        classes = [c for c in st.get("class", []) if c != "stat"]
        top_stats.append({
            "label": text(st.find("div", class_="stat-label")),
            "value": text(st.find("div", class_="stat-value")),
            "delta": text(st.find("div", class_="stat-delta")),
            "style": st.get("style", ""),
            "extraClass": " ".join(classes),
            "href": st.get("href") if st.name == "a" else None,
        })

    agenda = []
    for item in soup.select(".agenda-item"):
        agenda.append({
            "time": text(item.find("span", class_="agenda-time")),
            "event": text(item.find("span", class_="agenda-event")),
        })

    sections = [parse_section(sec) for sec in soup.select("div.section")]

    data = {
        "edition": edition,
        "published": published,
        "masthead": {
            "topLine": masthead_top_spans,
            "titleHtml": inner_html(masthead_title),
            "subtitle": inner_html(masthead_sub),
        },
        "badges": badges,
        "ticker": ticker,
        "market": market,
        "sidebar": {
            "fixedLinks": sidebar_fixed,
            "term": {"name": text(term_name), "def": text(term_def)},
            "stats": sidebar_stats,
        },
        "toc": toc,
        "tocDashboards": toc_dashboards,
        "verifyBadgeHtml": inner_html(verify_badge),
        "quotes": quotes,
        "topStats": top_stats,
        "topStatsNote": top_stats_note,
        "agenda": agenda,
        "sections": sections,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"OK: {len(sections)} sezioni estratte -> {out_path}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
