#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aiuto per la pubblicazione quotidiana di Il Contribuente in React.
Si occupa di:
  1) salvare una copia del nuovo file del giorno dentro rassegne/
     (sia nella radice del sito che dentro webapp/public/), cosi' domani
     l'edizione di oggi diventa automaticamente un'edizione d'archivio;
  2) se cambia il giorno rispetto a quello attualmente pubblicato,
     aggiungere quel giorno (quello uscente) alla pagina archivio.html
     (sia in radice che dentro webapp/public/).

Uso: python3 publish_helper.py archive <nuovo_file.html> <cartella_radice_Il_Contribuente>
"""
import sys
import json
import re
import shutil
from pathlib import Path

MESI = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
        "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]


def archive(new_html_path, root_dir):
    new_html_path = Path(new_html_path)
    root_dir = Path(root_dir)
    webapp_dir = root_dir / "webapp"

    with open(new_html_path, encoding="utf-8") as f:
        content = f.read()
    m = re.search(r'data-edition="([0-9-]+)"', content)
    if not m:
        print("ERRORE: non trovo data-edition=\"YYYY-MM-DD\" nel nuovo file. Controlla a mano.")
        sys.exit(1)
    new_date = m.group(1)
    print(f"Data della nuova edizione: {new_date}")

    edition_json_path = webapp_dir / "src" / "data" / "edition.json"
    old_date = None
    if edition_json_path.exists():
        with open(edition_json_path, encoding="utf-8") as f:
            old_data = json.load(f)
        old_date = old_data.get("edition")

    # 1) salva la nuova edizione anche in rassegne/, sia in radice che in webapp/public/
    for rassegne_dir in [root_dir / "rassegne", webapp_dir / "public" / "rassegne"]:
        rassegne_dir.mkdir(parents=True, exist_ok=True)
        dest = rassegne_dir / f"{new_date}.html"
        if dest.resolve() == new_html_path.resolve():
            print(f"{dest} e' gia' il file di partenza, non lo ricopio.")
            continue
        shutil.copy(new_html_path, dest)
        print(f"Copiato in {dest}")

    # 2) se cambia il giorno, aggiungi l'edizione USCENTE (quella vecchia) all'archivio
    if old_date and old_date != new_date:
        y, mo, d = (int(x) for x in old_date.split("-"))
        label = f"{d} {MESI[mo - 1]} {y}"
        entry = (
            f'    <a href="rassegne/{old_date}.html" class="entry">\n'
            f'      <span class="entry-date">{label}</span>\n'
            f'      <span class="entry-arrow">Leggi &rarr;</span>\n'
            f'    </a>\n'
        )
        for arch_path in [root_dir / "archivio.html", webapp_dir / "public" / "archivio.html"]:
            if not arch_path.exists():
                continue
            with open(arch_path, encoding="utf-8") as f:
                arch = f.read()
            if f"rassegne/{old_date}.html" in arch:
                print(f"{arch_path}: {old_date} c'e' gia', non lo riaggiungo.")
                continue
            marker = '<div class="list">\n'
            if marker not in arch:
                print(f"ATTENZIONE: non trovo il punto di inserimento in {arch_path}, aggiungi a mano.")
                continue
            arch = arch.replace(marker, marker + entry, 1)
            with open(arch_path, "w", encoding="utf-8") as f:
                f.write(arch)
            print(f"{arch_path}: aggiunta voce '{label}'")
    else:
        print("Stessa data di prima (o prima pubblicazione): non tocco l'archivio.")


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != "archive":
        print(__doc__)
        sys.exit(1)
    archive(sys.argv[2], sys.argv[3])
