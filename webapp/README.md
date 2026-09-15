# Il Contribuente — versione React (in costruzione)

Questa cartella non tocca index.html, rassegne/ né gli altri file della versione attuale del sito. È il progetto React separato, per ora solo con il layout di template.html.

## Cosa c'è già

- Struttura Vite + React (package.json, vite.config.js, index.html, src/)
- Tutto il CSS del sito copiato in src/index.css (nessuna modifica alla grafica)
- Componenti per ogni pezzo del layout: masthead, ticker, market-bar, sidebar, indice, verify-badge, citazioni, statistiche, agenda, sezioni con articoli, sezioni Confronto (duel), sezioni con grafici a barre (kpi)
- parse_template.py: script Python che legge un file HTML del sito (template.html o un file di rassegne/) ed estrae tutto il contenuto in src/data/edition.json — così il giorno dopo non si tocca il codice, si cambia solo il JSON

## Come si usa

```
npm install       # solo la prima volta
npm run dev       # apre il sito in locale per vedere le modifiche
npm run build     # genera la versione finale in dist/
```

Per estrarre il contenuto di un'altra edizione (es. una di rassegne/):

```
python3 parse_template.py ../rassegne/2026-09-14.html src/data/edition.json
```

## Cosa manca ancora (prossimi passi)

- Collegare le pagine di approfondimento fisse (guerre, dazi, sanzioni, ecc.) come pagine separate del sito React
- Automatizzare la pubblicazione su GitHub Pages
- Decidere se ogni giorno resta un file JSON nuovo o si passa a un archivio di edizioni dentro l'app
