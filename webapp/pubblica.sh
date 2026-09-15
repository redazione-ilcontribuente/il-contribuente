#!/bin/bash
# Pubblica l'edizione del giorno sul sito React di Il Contribuente.
#
# Uso:
#   ./pubblica.sh /percorso/al/nuovo_file_del_giorno.html
#
# Fa tutto tranne il push finale (git add / commit / push li vedi
# scritti alla fine, li lanci tu dopo aver controllato che sia tutto ok).

set -e

if [ -z "$1" ]; then
  echo "Uso: ./pubblica.sh <percorso al nuovo file HTML del giorno>"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"       # .../Il_Contribuente/webapp
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"          # .../Il_Contribuente
NEW_HTML="$1"

if [ ! -f "$NEW_HTML" ]; then
  echo "File non trovato: $NEW_HTML"
  exit 1
fi

echo "== 1/5: Controllo i pacchetti Python =="
if ! python3 -c "import bs4, lxml" 2>/dev/null; then
  echo "Mancano dei pacchetti Python. Esegui prima:"
  echo "  pip3 install beautifulsoup4 lxml"
  exit 1
fi

echo "== 2/5: Archivio l'edizione uscente e aggiorno la pagina archivio =="
python3 "$SCRIPT_DIR/publish_helper.py" archive "$NEW_HTML" "$ROOT_DIR"

echo "== 3/5: Estraggo i dati della nuova edizione =="
python3 "$SCRIPT_DIR/parse_template.py" "$NEW_HTML" "$SCRIPT_DIR/src/data/edition.json"

echo "== 4/5: Ricostruisco il sito (npm run build) =="
cd "$SCRIPT_DIR"
npm run build

echo "== 5/5: Metto il sito nuovo al posto giusto =="
cp "$SCRIPT_DIR/dist/index.html" "$ROOT_DIR/index.html"
mkdir -p "$ROOT_DIR/assets"
rm -f "$ROOT_DIR"/assets/*.js "$ROOT_DIR"/assets/*.css
cp "$SCRIPT_DIR"/dist/assets/*.js "$SCRIPT_DIR"/dist/assets/*.css "$ROOT_DIR/assets/"

echo ""
echo "Fatto. Il sito nuovo e' pronto in locale."
echo ""
read -p "Vuoi pubblicarlo ora online? (s/n) " RISPOSTA
if [ "$RISPOSTA" = "s" ] || [ "$RISPOSTA" = "S" ]; then
  cd "$ROOT_DIR"
  git add .
  git commit -m "edizione $(date +%d.%m.%Y)"
  git push
  echo ""
  echo "Pubblicato. Controlla ilcontribuente.redazioneit.workers.dev"
else
  echo ""
  echo "Non pubblicato. Quando vuoi farlo, lancia:"
  echo "  cd ~/Desktop/Il_Contribuente"
  echo "  git add ."
  echo "  git commit -m \"edizione $(date +%d.%m.%Y)\""
  echo "  git push"
fi
echo ""
