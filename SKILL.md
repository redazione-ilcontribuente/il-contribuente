---
name: rassegna-stampa-quotidiana
title: "Rassegna stampa quotidiana — 5:00"
description: "Rassegna stampa giornaliera che confronta fonti giornalistiche italiane e internazionali, traduce e sintetizza le notizie in italiano e mette in evidenza differenze, convergenze e prospettive delle diverse testate. La linea editoriale di Il Contribuente è il confronto tra fonti, non l'espressione di una posizione politica propria."
---

# Rassegna stampa quotidiana — Il Contribuente

## 1. IDENTITÀ EDITORIALE — REGOLA PRINCIPALE

Il Contribuente è una rassegna stampa comparativa.

La sua caratteristica distintiva non è semplicemente raccogliere molte notizie, ma mostrare al lettore COME testate diverse raccontano gli stessi fatti.

La linea editoriale permanente è quindi il CONFRONTO TRA FONTI.

Il giornale deve:

- selezionare le notizie più rilevanti della giornata;
- confrontare, quando disponibili, più fonti sullo stesso fatto;
- utilizzare testate italiane e internazionali;
- utilizzare fonti primarie e istituzionali quando servono a verificare i fatti;
- evidenziare convergenze e divergenze tra le fonti;
- distinguere sempre i fatti verificabili dalle interpretazioni;
- riportare le posizioni delle diverse parti senza trasformarle automaticamente nella posizione del giornale;
- tradurre in italiano le fonti straniere;
- offrire abbastanza contesto da permettere al lettore di capire la notizia;
- evitare qualsiasi filler creato soltanto per aumentare il numero di articoli.

Il Contribuente NON deve diventare un giornale che sceglie una narrativa e cerca fonti che la confermino.

Il confronto è il prodotto.

### Principio fondamentale

NON bisogna creare artificialmente un conflitto tra fonti quando non esiste.

Se più fonti concordano sui fatti principali, riportare il fatto e indicare le fonti.

Se invece differiscono per:

- fatti riportati;
- numeri;
- attribuzione di responsabilità;
- ricostruzione degli eventi;
- interpretazione;
- enfasi;
- conseguenze politiche;

la differenza deve essere resa visibile.

Il lettore deve poter capire:

1. cosa sappiamo;
2. cosa sostiene ciascuna fonte;
3. dove le fonti concordano;
4. dove divergono;
5. quali elementi restano non verificati.

Il giornale non deve dire al lettore cosa pensare.

Deve metterlo nella condizione di farsi un'idea.

---

# 2. CONTROLLO DI INTEGRITÀ — PRIMA DI PRODURRE LA RASSEGNA

Prima di costruire l'edizione quotidiana:

1. Verificare che `SKILL.md` sia integro.
2. Verificare che `template.html` esista nella stessa cartella.
3. Leggere integralmente `template.html`.
4. Verificare che il template contenga almeno:
   - `.article-image`;
   - la logica di layout dinamico già prevista dal template;
   - l'overlay "Un modo diverso di leggere le notizie";
   - il blocco `.footer-legal`;
   - gli script permanenti del template.
5. Se il template manca o è chiaramente incompleto, NON inventare una nuova struttura HTML.
6. Informare Mario di ciò che manca e chiedere il ripristino del template/backup.

Il template è la fonte di verità per struttura, CSS e comportamento della pagina.

---

# 3. TEMPLATE HTML — REGOLA ASSOLUTA

`template.html` è il template permanente del quotidiano "Il Contribuente".

Deve essere utilizzato come base di ogni nuova edizione.

NON ridisegnare il giornale ogni giorno.

NON creare un CSS alternativo.

NON cambiare arbitrariamente:

- struttura HTML;
- CSS;
- classi;
- font;
- dimensioni;
- bordi;
- colori;
- script;
- overlay;
- footer legale;
- licenza;
- comportamento responsive.

Quando Mario richiede una modifica strutturale o grafica permanente, la modifica deve essere fatta nel `template.html`, non soltanto nell'edizione del giorno.

Ogni nuova edizione deve aggiornare i contenuti, non reinventare il contenitore.

---

# 4. ORDINE DI COSTRUZIONE

L'ordine operativo corretto è:

1. controllo integrità;
2. lettura del template;
3. verifica dell'indice e delle sezioni;
4. ricerca delle notizie;
5. confronto e verifica delle fonti;
6. selezione dei titoli;
7. presentazione a Mario dell'elenco dei titoli;
8. dopo il passaggio titoli, scrittura degli articoli;
9. inserimento delle immagini fornite da Mario;
10. aggiornamento ticker, mercati, citazioni, agenda, statistiche e dashboard;
11. controllo finale di freschezza, fonti, lunghezza, layout e coerenza;
12. generazione dell'HTML definitivo.

Quando l'esecuzione è completamente automatica e non è disponibile un passaggio umano, la regola di approvazione dei titoli deve essere considerata un passaggio informativo non bloccante: non si deve fingere di aver ricevuto un'approvazione che non c'è.

---

# 5. INDICE — STRUTTURA DA RISPETTARE

L'indice attuale di Il Contribuente è:

1. Confronto
2. Dall'estero
3. Italia
4. Disagio città
5. Europa
6. Mondo
7. Finanza
8. Benessere
9. Tecnologia
10. IA
11. Immigrazione Italia
12. Dati Immigrazione

Queste sono le voci da rispettare.

NON aggiungere automaticamente nuove sezioni all'indice.

In particolare, "Immigrazione Europa" NON è una voce autonoma dell'indice attuale e quindi non deve essere trasformata in una sezione separata senza una richiesta esplicita di Mario.

Le notizie sull'immigrazione europea possono essere trattate:

- nella sezione Europa, quando sono principalmente una notizia europea;
- nella sezione Immigrazione Italia, quando riguardano l'Italia;
- nel Confronto, quando esiste un vero contrasto di prospettive;
- nei Dati Immigrazione, quando si tratta di dati e serie statistiche.

L'ordine delle sezioni deve rimanere invariato.

---

# 6. LAYOUT — PRIMA LA STRUTTURA, POI I CONTENUTI

Il layout è una regola strutturale, non editoriale.

Il CSS del template decide automaticamente la disposizione delle card.

La prima notizia di una sezione a formato articoli è il lead e occupa tutta la larghezza.

Regola generale:

- 1 articolo → piena larghezza;
- 2 articoli → entrambi a piena larghezza, uno sotto l'altro;
- 3 articoli → lead pieno + due card affiancate;
- 4 articoli → lead pieno + tre card affiancate.

NON scegliere manualmente larghezze diverse per le singole card.

REGOLA VINCOLANTE E PERMANENTE (Mario, 20/9/2026, "da oggi in poi"): gli articoli non vanno MAI impilati uno sotto l'altro a piena larghezza quando sono più di uno nella stessa sezione — devono sempre stare affiancati in orizzontale nella stessa riga, sullo stesso principio già fissato per "Le ultime notizie" di Petrolio Basilicata. Aggiornata di conseguenza la regola per 2 articoli totali: ora stanno affiancati in 2 colonne uguali (non più impilati uno sopra l'altro). La regola vale per tutte le sezioni a formato articoli, incluso qualunque caso limite (5 o più notizie) analogo a quello già risolto per Petrolio Basilicata: applicare la stessa tecnica CSS (`:has()` + colonne `minmax(0, 1fr)`) se il numero di articoli di una sezione standard dovesse mai superare 4.

NON lasciare spazi vuoti intenzionali.

NON modificare il CSS dell'edizione per correggere manualmente la griglia.

Il primo articolo deve essere marcato come:

`class="article lead"`

e il template deve occuparsi del resto.

Dati Immigrazione utilizza il proprio formato dashboard e non segue la griglia `.articles`.

---

# 7. COMPONENTI E BOX

Devono essere mantenuti i componenti già presenti nel template, tra cui:

- masthead;
- ticker;
- market bar;
- statistiche;
- agenda;
- verify badge;
- section;
- section-head;
- section-title;
- section-note;
- context-box;
- articles;
- article;
- article.lead;
- article-image;
- body-extra;
- source;
- duel;
- duel-side;
- chart-card;
- kpi-row;
- footer-legal.

Non creare componenti alternativi quando il template possiede già quello necessario.

## Da sapere per capire

`context-box` deve spiegare il contesto del fatto.

Può contenere:

- precedenti;
- quadro normativo;
- dati storici;
- definizioni;
- spiegazioni necessarie.

Non deve diventare un resoconto del lavoro della redazione.

REGOLA VINCOLANTE (Mario, 20/9/2026): il box "Da sapere per capire" di OGNI sezione deve essere corposo, non una singola riga stringata. Target: 3-5 frasi (un vero paragrafo), che diano al lettore un quadro reale del contesto e non un sottotitolo travestito da box. Vale per tutte le sezioni, ogni giorno.

---

# 8. IMMAGINI — SOLO QUELLE FORNITE DA MARIO

Le immagini generate autonomamente da Claude per le card degli articoli sono vietate.

Se Mario fornisce una fotografia per un articolo:

- usarla;
- inserirla nel contenitore `.article-image`;
- mantenerla pulita;
- non applicare testo sopra;
- non applicare titoli sopra;
- non applicare scrim o gradiente;
- non modificarne arbitrariamente l'aspetto.

Regola vincolante (Mario, 4/9/2026): OGNI articolo di OGNI sezione a formato articoli (incluse le voci del Confronto) deve avere, una propria immagine.

Regola vincolante e PRIORITARIA (Mario, 4/9/2026, ribadita la sera stessa): NON RIPETERE MAI LA STESSA IMMAGINE NELLA STESSA EDIZIONE. Questo divieto è assoluto e viene prima della regola "ogni articolo deve avere un'immagine": se garantire un'immagine a un articolo significherebbe riusare una foto già assegnata a un altro articolo della stessa edizione, quell'articolo resta SENZA immagine. Meglio una card senza foto che due card con la stessa foto nello stesso giorno.

Come procedere quando la cartella tematica ha meno foto non ancora usate oggi delle notizie della sezione (es. 2 foto disponibili per 4 articoli):

- usare prima tutte le foto non ancora usate nell'edizione del giorno in quella cartella;
- se non bastano, guardare in cartelle affini per argomento già presenti nel repository (es. `salute/` in aggiunta a `benessere/`, `guerra/` e `confronto/` per la sezione Confronto) per trovare scatti non ancora usati oggi;
- se anche le cartelle affini sono esaurite, gli articoli restanti della sezione restano semplicemente SENZA immagine. NON riutilizzare in nessun caso, per nessun motivo, una foto già assegnata a un altro articolo della stessa edizione, nemmeno all'interno della stessa sezione.

Variazione nel tempo (Mario, 4/9/2026): la selezione delle foto all'interno di una cartella non deve ripetere sempre le stesse preferite edizione dopo edizione. A parità di idoneità, scegliere in modo variato/casuale tra le foto disponibili della cartella, così che nell'arco di più giorni vengano effettivamente usati scatti diversi e non un sottoinsieme fisso.

Controllo obbligatorio prima di pubblicare: contare i file immagine effettivamente usati nell'edizione (i valori dentro `src="immagini/..."`) e verificare che non ci siano duplicati. Se un doppione emerge, rimuovere l'immagine dal secondo articolo (non sostituirla con un'altra presa da una sezione slegata solo per riempire).

Resta fermo quanto segue:

- NON usare SVG generate da Claude;
- NON usare immagini segnaposto;
- NON inventare o generare una fotografia;
- meglio nessuna immagine che un'immagine ripetuta o presa da una cartella tematicamente slegata.

## Hero di sezione

Se Mario fornisce un hero fotografico per una sezione:

- inserirlo come previsto dal template;
- mantenerlo pulito;
- nessun titolo sovrapposto;
- nessuna didascalia sovrapposta;
- nessun gradiente;
- nessuno scurimento.

Se non viene fornito, non inventarlo.

## Persone reali

Non generare immagini fotorealistiche di persone reali riconoscibili e presentarle come fotografie di cronaca.

---

# 9. COLORI E STILE

Il colore non è una regola editoriale separata.

I colori, i bordi, gli sfondi, i font e le dimensioni sono quelli definiti nel template.

NON modificarli durante la produzione quotidiana.

Se Mario vuole cambiare la grafica, la modifica va applicata al template permanente.

REGOLA VINCOLANTE E PERMANENTE (Mario, 20/9/2026): il font (tipo di scrittura) di titolo, testo e approfondimento deve essere lo STESSO per tutti gli articoli di tutte le sezioni, Confronto incluso — mai mescolare famiglie diverse tra un articolo e l'altro o tra una sezione e l'altra. Applicato nel template: `Georgia, 'Times New Roman', serif` per `.article h3`, `.article p`, `.duel-outlet`, `.duel-headline`, `.duel-fact-text`, `.duel-side p.body`. Le etichette tecniche (fonte, badge, ticker, market bar) restano nel loro font monospazio/sans dedicato: la regola riguarda il testo editoriale degli articoli, non la chrome dell'interfaccia.

REGOLA ASSOLUTA E PRIORITARIA (Mario, 20/9/2026): l’uniformità del font deve valere per TUTTO il contenuto editoriale di TUTTI gli articoli presenti nelle sezioni dell’indice, sia nello stato iniziale sia dopo il clic su `Continua a leggere`. Titolo, testo sempre visibile, paragrafi dentro `.body-extra`, approfondimenti espansi, callout editoriali interni all’articolo e testo delle tre prospettive del Confronto devono usare la stessa famiglia tipografica editoriale: `Georgia, 'Times New Roman', serif`. L’apertura di un articolo NON deve mai cambiare font, dimensione tipografica di base, stile o famiglia rispetto alla parte visibile prima dell’espansione. È vietato assegnare a `.body-extra`, ai suoi `p`, o ad altri elementi dell’approfondimento font `Inter`, `Fraunces`, `JetBrains Mono` o altre famiglie. Le sole eccezioni sono elementi tecnici dell’interfaccia come `.source`, badge, pulsanti `Continua a leggere / Mostra meno`, ticker, market bar e altre etichette di navigazione. Questa regola prevale su qualunque CSS precedente incompatibile e deve essere applicata nel `template.html` permanente, non soltanto nell’edizione del giorno.


REGOLA VINCOLANTE E PERMANENTE (Mario, 20/9/2026): le sezioni NON mostrano più l'etichetta colorata (TAG) prima del titolo di sezione (es. "Confronto", "Europa"). Il tag è nascosto via CSS (`.section-tag{display:none;}`) nel template: non va riattivato senza richiesta esplicita di Mario, e non va rimosso dal markup (serve comunque per l'accessibilità/struttura interna).

---

# 10. NUMERO DI ARTICOLI

Il giornale deve essere PIENO E CORPOSO.

Per le sezioni principali a formato articoli, lo standard è:

- 4 articoli;
- 1 lead;
- 3 articoli successivi.

Lo standard di 4 vale per:

- Italia;
- Disagio città;
- Europa;
- Mondo;
- Finanza;
- Benessere;
- Tecnologia.

Per Dall'estero e IA:

- minimo 2;
- massimo 4.

Per Immigrazione Italia:

- minimo 2;
- massimo 4.

Confronto non rientra nella regola numerica standard perché utilizza un formato editoriale differente.

Dati Immigrazione non rientra nella regola perché è una dashboard.

### Regola anti-filler

Il numero non deve mai essere raggiunto inventando o riciclando una notizia debole.

Se ci sono soltanto 2 notizie solide:

1. effettuare ulteriori ricerche;
2. cercare altre fonti;
3. cercare altri fatti realmente rilevanti nella finestra temporale;
4. solo dopo valutare se la sezione può essere mantenuta con meno contenuti.

MAI:

- inventare;
- ripetere la stessa notizia con titoli diversi;
- usare una notizia vecchia solo per riempire;
- inserire notizie insignificanti.

---

# 11. FRESCHEZZA

Ogni notizia deve essere realmente attuale.

Regola vincolante (Mario, 4/9/2026, sostituisce la precedente finestra 24-36 ore): pubblicazione della fonte originale entro le ultime 12 ore, MASSIMO 24 ore, rispetto al momento della costruzione della rassegna. Non 24-36: 24 ore è il tetto assoluto, non l'obiettivo. Verificare data E ora di pubblicazione di ogni fonte, non solo il giorno.

La regola vale per tutte le sezioni di attualità:

- Dall'estero;
- Italia;
- Disagio città;
- Europa;
- Mondo;
- Finanza;
- Benessere;
- Tecnologia;
- IA;
- Immigrazione Italia.

La data della fonte deve essere verificata.

Non utilizzare una notizia vecchia soltanto perché è più completa.

## Eccezioni

Sono ammessi contenuti più vecchi esclusivamente quando sono chiaramente:

- contesto storico;
- quadro normativo;
- spiegazione;
- serie statistica periodica.

Questi contenuti non devono essere presentati come "notizie del giorno".

---

# 12. LUNGHEZZA — GIORNALE CORPOSO

Gli articoli devono essere più pieni della precedente versione.

Obiettivo indicativo:

**250-350 parole per articolo**, salvo casi in cui la natura della notizia richieda una lunghezza diversa.

La priorità non è raggiungere un numero artificiale di parole, ma fornire informazioni sufficienti.

Ogni articolo deve normalmente contenere:

### Lead

Circa 70-100 parole.

Deve rispondere rapidamente a:

- chi;
- cosa;
- quando;
- dove;
- numeri;
- dichiarazioni rilevanti.

### Approfondimento

Almeno 2 paragrafi aggiuntivi quando la notizia lo consente.

Devono sviluppare:

- contesto;
- precedenti;
- reazioni;
- conseguenze;
- dati;
- posizioni delle parti;
- elementi emersi da fonti diverse.

### Regola di qualità

Non allungare l'articolo con:

- ripetizioni;
- aggettivi inutili;
- frasi generiche;
- commenti della redazione non supportati.

Il giornale deve essere corposo di INFORMAZIONI, non di parole.

---

# 13. STRUTTURA DI OGNI ARTICOLO

Ogni articolo dovrebbe seguire questo schema:

1. Titolo informativo.
2. Lead.
3. Primo approfondimento.
4. Secondo approfondimento.
5. Eventuale ulteriore paragrafo se la notizia lo richiede.
6. Fonte/i.

La domanda editoriale da applicare a ogni paragrafo è:

**Cosa è successo e perché conta?**

---

# 14. CONFRONTO TRA FONTI — IL CUORE DEL GIORNALE

Ogni notizia importante deve essere cercata attraverso più fonti.

Non è obbligatorio avere sempre 3 fonti che dicono esattamente la stessa cosa.

È invece obbligatorio cercare di capire come il fatto viene raccontato da fonti differenti.

Per una notizia importante, preferire:

- una fonte primaria o istituzionale;
- una o più agenzie/testate;
- una fonte internazionale quando pertinente.

Esempio:

- fonte ufficiale → cosa è stato deciso;
- ANSA/Reuters → cronaca e dettagli;
- altra testata → interpretazione o reazioni;
- testata straniera → prospettiva esterna.

## Quando le fonti divergono

Indicare chiaramente la divergenza.

Non scegliere arbitrariamente una versione.

Separare:

**Fatto verificabile**

da

**Versione/interpretazione della fonte A**

e

**Versione/interpretazione della fonte B**.

Quando il contrasto è particolarmente importante, utilizzare la sezione Confronto.

---

# 15. SEZIONE CONFRONTO

La sezione Confronto è il simbolo editoriale di Il Contribuente.

Deve essere dedicata soprattutto a:

- geopolitica;
- guerre;
- crisi internazionali;
- temi politici controversi;
- grandi controversie nelle quali fonti diverse raccontano lo stesso fatto in maniera significativamente differente.

Regola vincolante (Mario, 4/9/2026, RIBADITA il 20/9/2026 — "la sezione confronto ha sempre 3 notizie"): la sezione Confronto deve avere SEMPRE E OBBLIGATORIAMENTE tre voci, non due, in ogni edizione senza eccezioni. Il formato è sempre:

- "Prospettiva A" (duel-side left);
- "Prospettiva B" (duel-side right);
- "Terza voce" (duel-side third) — indipendente, non allineata né a A né a B: una fonte neutrale, un'analisi critica, un dato verificabile di terze parti (agenzia neutrale, autorità/organizzazione internazionale, esperto di settore). Non è opzionale.

Markup di riferimento (già presente e testato in template.html/index.html): due `.duel-side` (left/right) dentro il primo `.duel-grid`, poi un secondo `.duel-grid` con `style="grid-template-columns:1fr; border-top:1px solid var(--rule);"` contenente il solo `.duel-side.third` a piena larghezza. Non modificare il CSS: questo secondo `.duel-grid` con lo style inline è il modo corretto, già previsto dal template, per ottenere la terza voce senza toccare la regola `.duel-grid{grid-template-columns:1fr 1fr;}`.

La sezione non deve essere costruita per creare artificialmente un equilibrio 50/50 — la terza voce serve ad aggiungere un elemento verificabile o un'angolazione diversa, non a fare da ago della bilancia forzato.

Se una versione è supportata da prove molto più solide, va detto.

L'obiettivo è il confronto, non la falsa equivalenza.

---

# 16. GEOPOLITICA

Per:

- Ucraina;
- Russia;
- Medio Oriente;
- Gaza;
- Israele;
- Iran;
- USA;
- Cina;
- Taiwan;
- altri conflitti;

cercare fonti provenienti da prospettive differenti quando disponibili.

Utilizzare, secondo il caso:

- fonti occidentali;
- fonti del Paese coinvolto;
- fonti russe/cinesi;
- fonti regionali;
- fonti indipendenti;
- fonti istituzionali.

Non imporre una narrativa unica.

Non presentare una dichiarazione di una parte come fatto verificato se non è stata verificata.

Quando i dati sono contestati, attribuire sempre il dato alla fonte che lo sostiene.

---

# 17. LINGUE E FONTI INTERNAZIONALI

La ricerca non deve essere limitata all'italiano.

Per temi internazionali usare, quando pertinente:

- inglese;
- francese;
- tedesco;
- spagnolo;
- russo;
- cinese;
- lingua locale del Paese coinvolto.

L'inglese è la lingua internazionale di riferimento.

Per Dall'estero, privilegiare la lingua originale della testata straniera.

Tutto l'output finale deve essere in italiano.

---

# 18. SEZIONE DALL'ESTERO

Dall'estero NON significa "notizie estere".

È la sezione dedicata a:

**come i media e le fonti internazionali raccontano l'Italia.**

Può riguardare:

- governo italiano;
- politica;
- economia;
- immigrazione;
- diplomazia;
- rating;
- rapporti Italia-UE;
- rapporti con altri Paesi;
- giudizi internazionali sull'Italia;
- grandi fatti italiani osservati dall'estero.

Fonti preferibili:

- Reuters;
- BBC;
- The Guardian;
- Financial Times;
- Le Monde;
- Der Spiegel;
- El País;
- testate belghe;
- altre fonti internazionali pertinenti.

Numero:

**2-4 articoli.**

---

# 19. ITALIA

Copre:

- politica;
- governo;
- Parlamento;
- cronaca;
- economia interna;
- istituzioni;
- provvedimenti;
- giustizia;
- lavoro;
- temi sociali.

Privilegiare notizie che abbiano un impatto concreto o un peso politico/sociale significativo.

---

# 20. DISAGIO CITTÀ

Copre:

- criminalità;
- sicurezza urbana;
- rapine;
- aggressioni;
- violenza;
- degrado;
- sicurezza sui trasporti;
- episodi urbani rilevanti.

Evitare di trasformare una serie di micro-cronache insignificanti in una falsa emergenza.

Se la sezione viene costruita con più episodi, spiegare chiaramente che sono episodi distinti.

---

# 21. EUROPA

Copre:

- Unione Europea;
- Commissione;
- Parlamento europeo;
- BCE quando il tema è principalmente europeo;
- Germania;
- Francia;
- Spagna;
- Polonia;
- Ungheria;
- Balcani;
- altri Paesi europei;
- politica e economia europea;
- immigrazione europea quando è principalmente una questione UE/europea.

Fonti:

- istituzioni UE;
- testate europee;
- fonti nazionali dei Paesi coinvolti;
- stampa italiana e internazionale.

---

# 22. MONDO

Copre:

- USA;
- Cina;
- Russia;
- Medio Oriente;
- guerre;
- crisi internazionali;
- diplomazia;
- sicurezza internazionale;
- grandi eventi mondiali.

Quando una notizia geopolitica presenta versioni molto diverse, può essere approfondita nella sezione Confronto e richiamata brevemente in Mondo.

---

# 23. FINANZA

Copre:

- Borse;
- tassi;
- inflazione;
- banche;
- obbligazioni;
- materie prime;
- energia;
- aziende;
- trimestrali;
- mercati internazionali.

Per i numeri di mercato indicare sempre:

- valore;
- variazione;
- data/ora di riferimento quando importante;
- fonte.

Non confondere dati di mercato con previsioni.

---

# 24. BENESSERE

Copre:

- medicina;
- salute;
- ricerca scientifica;
- nutrizione;
- prevenzione;
- innovazione sanitaria.

Fonti preferibili:

- riviste scientifiche;
- università;
- ospedali;
- enti sanitari;
- studi peer-reviewed;
- istituzioni pubbliche.

Evitare titoli sensazionalistici quando lo studio non dimostra una relazione causale.

Distinguere:

- studio osservazionale;
- studio clinico;
- associazione;
- causalità;
- risultati preliminari;
- risultati consolidati.

---

# 25. TECNOLOGIA

Copre la tecnologia generale:

- hardware;
- cybersecurity;
- internet;
- social network;
- dispositivi;
- telecomunicazioni;
- aziende tech;
- software.

Le notizie specificamente dedicate all'intelligenza artificiale devono andare nella sezione IA.

---

# 26. IA — INTELLIGENZA ARTIFICIALE

Sezione separata da Tecnologia.

Copre:

- modelli di IA;
- OpenAI;
- Anthropic;
- Google;
- Nvidia;
- Meta quando la notizia riguarda direttamente IA;
- nuovi chip IA;
- data center;
- robotica/IA incarnata;
- regolamentazione;
- AI Act;
- impatto sul lavoro;
- ricerca;
- sicurezza dell'IA.

Numero:

**2-4 articoli.**

La sezione deve essere realmente aggiornata e non riempita con notizie tecnologiche generiche.

---

# 27. IMMIGRAZIONE ITALIA

Copre:

- sbarchi;
- rimpatri;
- hotspot;
- CPR;
- centri di accoglienza;
- decreti;
- sentenze;
- protezione internazionale;
- flussi regolari;
- click day;
- accordi con Paesi terzi;
- ONG e soccorsi in mare;
- rapporti Italia-UE.

Quando disponibili, riportare:

- sbarchi giornalieri;
- sbarchi da inizio anno;
- confronto con anno precedente;
- rimpatri forzati;
- rimpatri volontari assistiti;
- nazionalità;
- minori non accompagnati;
- dati sugli hotspot.

Confrontare, quando utile:

- fonte istituzionale;
- agenzie;
- testate con orientamenti differenti;
- fonti europee.

Numero:

**2-4 articoli.**

---

# 28. DATI IMMIGRAZIONE

È la dashboard finale.

Non trattarla come una normale sezione di articoli.

Può contenere:

- sbarchi;
- confronto annuale;
- nazionalità;
- minori non accompagnati;
- rimpatri;
- trasferimenti;
- rotte europee;
- dati Frontex;
- altri KPI pertinenti.

Ogni dato deve riportare:

- periodo;
- fonte;
- data di aggiornamento.

Non usare un dato vecchio facendolo sembrare corrente.

I dati periodici possono essere più vecchi della finestra 12-24 ore se sono gli ultimi dati ufficiali disponibili, purché siano chiaramente datati.

---

# 29. FONTI

Le fonti devono essere citate alla fine dell'articolo nel blocco `.source`.

Quando possibile:

- linkare direttamente la fonte;
- indicare più fonti se sono state realmente utilizzate;
- distinguere fonte primaria da fonte giornalistica quando utile.

Il badge:

"Oggi abbiamo confrontato N fonti su M testate"

deve essere calcolato sui dati reali dell'edizione.

NON inventare il numero.

---

# 30. COPYRIGHT

Le fonti vengono utilizzate per informazione e confronto.

Non copiare integralmente articoli o titoli protetti.

Il testo finale deve essere una sintesi e rielaborazione originale.

Le citazioni dirette devono essere brevi e realmente necessarie.

Il resto deve essere parafrasato.

---

# 31. TONO

Il testo deve essere:

- giornalistico;
- chiaro;
- diretto;
- concreto;
- neutrale nel linguaggio;
- ricco di fatti.

Evitare:

- propaganda;
- slogan;
- commenti personali della redazione;
- sarcasmo politico;
- aggettivi valutativi non necessari;
- titoli costruiti per suggerire al lettore cosa deve pensare.

La neutralità non significa nascondere le divergenze.

Significa attribuirle correttamente.

---

# 32. NIENTE META-COMMENTI

Il lettore non deve vedere il processo interno di costruzione della rassegna.

NON scrivere:

- "abbiamo trovato solo due notizie";
- "rispetta la finestra di 12-24 ore";
- "abbiamo fatto tre ricerche";
- "secondo le regole di Mario";
- "non abbiamo trovato altro";
- "per raggiungere quota quattro";
- "questa notizia è stata inserita perché serviva un quarto articolo".

I box editoriali devono parlare dei FATTI, non del processo redazionale.

---

# 33. TICKER

Il ticker deve contenere le principali notizie dell'edizione.

Deve essere aggiornato quotidianamente.

Selezionare titoli realmente rappresentativi delle sezioni e non riempirlo con titoli secondari.

---

# 34. MARKET BAR

Regola vincolante (Mario, 2/9/2026 e 31/8/2026): le card della market bar sono SEMPRE le stesse, ogni giorno, aggiornate con valori reali:

- benzina;
- diesel;
- petrolio;
- gas;
- oro;
- bitcoin;
- Palestinesi uccisi (dal 7 ottobre 2023, Gaza) — SEMPRE presente ogni giorno, non solo nei giorni in cui il Confronto tratta Gaza.

NON aggiungere la card dello spread Btp-Bund: Mario non la vuole. Aggiungere una card nuova, diversa da queste, SOLO quando una notizia specifica del giorno la giustifica chiaramente (es. un evento eccezionale con un numero-chiave associato); altrimenti l'elenco non va toccato.

Indicare fonte e data/ora di riferimento quando disponibili.

Non mescolare quotazioni riferite a momenti diversi senza indicarlo.

---

# 35. AGENDA — COSA SUCCEDE OGGI

Regola permanente (Mario, 3/9/2026): questa sezione contiene SOLO ED ESCLUSIVAMENTE notizie/eventi della data di pubblicazione della rassegna stessa, a livello mondiale — non scadenze, appuntamenti o decisioni previste per giorni successivi, e non eventi già passati.

Selezionare esattamente 5 voci: le 5 cose più importanti che accadono nel mondo in quella giornata specifica (possono includere, quando pertinenti quel giorno: eventi politici, decisioni prese o annunciate, dati economici pubblicati, appuntamenti internazionali, eventi tecnologici, scadenze normative che scadono proprio oggi). Non è un calendario di cose future: se un fatto non sta accadendo OGGI, non va in agenda, anche se è rilevante e imminente (va eventualmente nel corpo dell'articolo della sezione pertinente, non qui).

Non forzare a 5 se davvero non ci sono 5 fatti mondiali abbastanza rilevanti nella giornata: meglio 3-4 voci solide che riempire con notizie minori (stessa logica anti-filler della sezione 10).

---

# 36. CITAZIONE DEL GIORNO

Le citazioni devono essere:

- realmente pronunciate/scritte dalla persona indicata;
- attribuite correttamente;
- pertinenti alle notizie del giorno.

Non usare citazioni inventate o ricostruite.

---

# 37. STATISTICHE DEL GIORNALE

Le statistiche devono essere coerenti con l'edizione reale.

Esempi:

- numero di edizioni pubblicate;
- giorni consecutivi;
- numero di testate utilizzate;
- numero di fonti confrontate.

Non inventare valori.

---

# 38. CONTROLLO FINALE PRIMA DELLA PUBBLICAZIONE

Prima della pubblicazione verificare:

### Struttura
- template corretto;
- indice corretto;
- ordine corretto;
- nessun CSS alterato;
- layout senza spazi vuoti anomali.

### Contenuti
- numero articoli corretto;
- articoli sufficientemente corposi;
- nessun filler;
- titoli coerenti con gli articoli;
- nessuna duplicazione inutile.

### Freschezza
- data originale di ogni notizia verificata;
- nessuna notizia vecchia spacciata per nuova.

### Confronto
- fonti differenti realmente consultate;
- divergenze attribuite correttamente;
- nessuna falsa equivalenza;
- fatti separati da opinioni.

### Fonti
- fonti presenti;
- link funzionanti quando disponibili;
- numeri e citazioni verificati.

### Immagini
- nessuna immagine ripetuta nella stessa edizione (controllo obbligatorio, vedi sezione 8) — questo vale prima di tutto il resto;
- ogni articolo ha, quando possibile senza ripetere una foto già usata oggi, una propria immagine;
- soltanto immagini fornite da Mario;
- nessuna immagine generata autonomamente;
- nessun testo sopra le fotografie.

### Lingua
- tutto in italiano;
- traduzioni corrette;
- nomi propri e numeri verificati.

### Archivio
- archivio.html aggiornato con l'edizione del giorno precedente (mai con quella di oggi, che vive su index.html finché non viene sostituita domani);
- nessuna voce duplicata in archivio.html.

### Agenda
- "Cosa succede oggi" contiene solo fatti della data di pubblicazione odierna, a livello mondiale, non scadenze future né eventi passati;
- al massimo 5 voci, senza filler per raggiungere quel numero.

---

# 39. OBIETTIVO FINALE

Il risultato deve sembrare un vero quotidiano digitale:

- pieno;
- corposo;
- leggibile;
- aggiornato;
- ricco di informazioni;
- ricco di fonti;
- internazionale;
- comparativo.

Ma la quantità non deve mai prevalere sulla qualità.

La caratteristica che deve distinguere Il Contribuente da un normale aggregatore di notizie è sempre la stessa:

**non limitarsi a raccontare cosa è successo, ma mostrare come fonti diverse raccontano ciò che è successo.**

Il lettore deve uscire dalla pagina con:

- il fatto;
- il contesto;
- le fonti;
- le diverse prospettive;
- gli elementi verificabili;

e poter formare autonomamente il proprio giudizio.

---

# 40. ATTIVAZIONE

La skill si attiva quando Mario chiede:

- "rassegna stampa";
- "cosa succede oggi";
- "notizie del giorno";
- "aggiornami";
- "cosa succede in Italia";
- "cosa succede nel mondo";
- oppure una richiesta equivalente di aggiornamento dell'attualità.

Se Mario restringe il tema, utilizzare soltanto le sezioni pertinenti ma mantenere il template.

Per una rassegna completa, rispettare sempre l'intero indice sopra definito.


## STRUTTURA OBBLIGATORIA DI OGNI ARTICOLO

Questa struttura vale per ogni articolo di tutte le sezioni dell'indice, senza eccezioni per le normali card editoriali.

REGOLA AGGIORNATA E VINCOLANTE (Mario, 20/9/2026, sostituisce l'ordine precedente): il pulsante Continua a leggere/Mostra meno deve stare SEMPRE ALLA FINE DELL'ARTICOLO, MAI IN MEZZO. Non va mai messo subito dopo "Il fatto" e prima dell'approfondimento.

Ordine obbligatorio:

1. **Da sapere per capire** — breve contesto indispensabile per comprendere la notizia (vedi anche sezione 7: deve essere un paragrafo corposo, non una riga).
2. **Il fatto** — apertura immediata con **4-5 frasi** chiare e informative (sempre visibile).
3. **Approfondimento** — contenuto completo, dati, reazioni, contesto e confronto tra fonti (nascosto di default in `.body-extra`, compare quando l'articolo viene espanso).
4. **Fonte/i** — in fondo al contenuto, sempre visibile.
5. **Continua a leggere / Mostra meno** — UNICO pulsante, posizionato per ultimo, dopo la fonte: è l'ultimo elemento dell'articolo, non uno spartiacque a metà testo.

Il testo completo NON deve essere visibile tutto nella card iniziale. L'obiettivo è mantenere la pagina leggibile e compatta, evitando articoli infiniti che occupano verticalmente tutta la sezione.

Le 4-5 frasi iniziali devono essere sufficienti per capire subito cosa è successo. Il contenuto successivo deve aggiungere informazioni reali e non ripetere l'apertura.

**Da sapere per capire** non è un titolo ornamentale: deve contenere realmente il contesto necessario. **Il fatto** deve invece partire dall'aggiornamento attuale.

I pulsanti devono funzionare tramite JavaScript senza cambiare pagina. Quando l'articolo è aperto, **Continua a leggere** non deve più essere visibile e deve comparire **Mostra meno**, sempre in fondo. Quando viene richiuso, avviene il contrario.

La struttura HTML/CSS/JS deve essere uniforme in tutte le sezioni, così l'utente impara una sola interazione e la ritrova in tutto il giornale.

---

# 41. SEZIONI FISSE EXTRA (fuori indice) — MAI TOCCARE SENZA CHIEDERE

Oltre all'indice standard della sezione 5, il sito pubblicato include altre sezioni/dashboard fisse che Mario ha aggiunto nel tempo direttamente nelle edizioni, e che NON fanno parte dell'indice/della lista di sezioni da riscrivere ogni giorno:

- Sezione "Approfondimenti fissi" (sidebar, id `approfondimenti`) — link fissi (Geopolitica, Conflitti nel mondo, Immigrazione in Europa, Guerre, Dazi, Sanzioni, Glossario) e box "Termine del giorno"/statistiche;
- Dashboard "Sicurezza Pubblica" (id `sicurezza-pubblica`);
- Dashboard "Petrolio Basilicata" (id `petrolio-basilicata`), con la sotto-lista "Le ultime notizie" — REGOLA ASSOLUTA E PERMANENTE (ribadita 20/9/2026): tutte le notizie di questa sotto-lista devono SEMPRE essere affiancate in orizzontale, per sempre, su ogni dispositivo, senza alcuna eccezione futura.

Regola vincolante e assoluta (Mario, 16/9/2026, ribadita più volte): queste sezioni, e la dashboard "Dati Immigrazione" dell'indice standard, vanno copiate IDENTICHE da un'edizione all'altra — layout, HTML e CSS non vanno mai rigenerati, riscritti o "corretti" di propria iniziativa, nemmeno per sistemare un bug di stile evidente. Se emerge un problema (es. un layout che sembra rotto), or se Mario segnala che qualcosa in una di queste sezioni non va, si spiega la diagnosi e si PROPONE la correzione, ma si chiede sempre conferma esplicita prima di modificare il codice di queste sezioni. Aggiornare solo i dati/testo/date al loro interno quando esplicitamente richiesto.

## Nota tecnica nota (17/9/2026): grid a 5 articoli

La "regola universale di layout" della sezione 6 (1 articolo pieno, 2 impilati, 3 = lead + 2 affiancate, 4 = lead + 3 affiancate) è implementata in CSS con selettori `:has(> .article:nth-child(N):last-child)` che coprono solo i casi a 2, 3 o 4 articoli totali. La lista "Le ultime notizie" di Petrolio Basilicata ha 5 articoli: nessuna regola CSS li copre esplicitamente, quindi il grid di default (3 colonne fisse) li spezza in modo ibrido (3 affiancati + 1 isolato), né un vero affiancamento né uno stack pulito — probabile causa dei ripetuti cambi tra "verticale" e "orizzontale" chiesti da Mario in giorni diversi. Prima di toccare il CSS di questa sezione per "risolverlo", chiedere sempre conferma a Mario (vedi regola sopra): la soluzione tecnica più pulita è aggiungere una regola CSS dedicata al caso "5 articoli totali" in template.html, non forzare uno stack verticale né lasciare il comportamento di default.

---

# 42. PROCEDURA OPERATIVA QUOTIDIANA E CONSEGNA

Regola vincolante (Mario, 16/9/2026), procedura obbligatoria ogni mattina, sempre in quest'ordine:

1. Creare l'edizione del giorno (contenuti e date aggiornate, stesso layout/template di sempre).
2. Archiviare l'edizione del giorno precedente in `rassegne/` (e nella copia gemella `webapp/public/rassegne/`) con il nome `YYYY-MM-DD.html` corrispondente alla sua data.
3. Aggiungere in `archivio.html` (e nella copia gemella `webapp/public/archivio.html`) la voce mancante che punta all'edizione del giorno precedente appena archiviata.

Controlli obbligatori prima di consegnare, per non ripetere errori già fatti in passato:

- Tutte le date sul sito pubblicato sono aggiornate: `data-edition`/`data-published` nel body, data nel masthead, footer — e `index.html`/gli asset di `dist/` sono stati rigenerati con `npm run build` e ricopiati, non solo `edition.json`.
- Il link "Archivio edizioni" nel file HTML appena archiviato (dentro `rassegne/`) punta a `../archivio.html` (con `../`), mai a `archivio.html` senza prefisso.
- Consegnare sempre insieme alla rassegna del giorno anche il glossario `glossario.html` aggiornato con gli eventuali nuovi termini comparsi in quell'edizione (regola del 31/8/2026), rispettando la struttura/codice esistente senza reinventarla.

Il push su GitHub lo fa SEMPRE Mario manualmente: non va mai fatto in autonomia dalla rassegna automatica. Se il push automatico (o l'accesso al Mac) non dovesse riuscire per qualsiasi motivo, i file dell'edizione vanno comunque preparati e consegnati (in chat e/o sul Mac se raggiungibile) così che Mario possa pubblicarli lui stesso senza perdere tempo — non bloccarsi solo perché un passaggio automatico fallisce.
---

# 43. BACINO PERMANENTE DELLE FONTI — REGOLA VINCOLANTE

Regola vincolante e permanente (Mario, 20/9/2026).

Per ogni edizione de **Il Contribuente**, la ricerca delle notizie deve utilizzare prioritariamente il bacino di testate giornalistiche, agenzie, fonti scientifiche, istituzionali e specialistiche elencato in questa sezione.

## Regole operative

- Ogni articolo deve essere costruito tramite **confronto diretto tra testate/fonti diverse sullo stesso fatto**.
- Quando disponibili, utilizzare **almeno 3 fonti realmente consultate, pertinenti e utili** per ogni articolo.
- Le fonti devono apportare verifica, dettagli, dati, contesto, reazioni o prospettive utili. Non aggiungere una fonte soltanto per aumentare artificialmente il numero delle citazioni.
- **ANSA non deve essere utilizzata automaticamente come fonte principale o dominante** dell'edizione. Va usata quando pertinente, insieme alle altre fonti del bacino.
- Distribuire la ricerca tra fonti italiane, internazionali, locali, specialistiche, scientifiche e primarie in funzione dell'argomento.
- Quando le fonti concordano, indicare chiaramente la convergenza.
- Quando differiscono su fatti, numeri, ricostruzioni, responsabilità, interpretazioni o conseguenze, rendere visibile la divergenza e attribuirla alla fonte corretta.
- Non creare contrasti artificiali quando le fonti non divergono realmente.
- **Non attribuire etichette politiche o ideologiche alle testate.** Descrivere concretamente ciò che ciascuna fonte riporta.
- Per dati, documenti, normative e dichiarazioni ufficiali, privilegiare quando disponibili anche le fonti primarie o istituzionali presenti nel bacino.
- La presenza di una fonte in questo elenco non elimina le altre regole di qualità del presente `SKILL.md`: freschezza, verifica, attendibilità, pertinenza, confronto, attribuzione e distinzione tra fatti e interpretazioni restano obbligatorie.
- Se una notizia importante non è adeguatamente verificabile attraverso fonti di questo bacino, non inventare collegamenti o citazioni. È preferibile scegliere un'altra notizia solida. Fonti esterne al bacino possono essere usate eccezionalmente quando indispensabili per una fonte primaria, un documento originale o una verifica che le fonti elencate non consentono, specificandone chiaramente la natura.

## Elenco permanente delle fonti da utilizzare

- [ANSA](https://www.ansa.it)
- [LaPresse](https://www.lapresse.it)
- [Corriere della Sera](https://www.corriere.it)
- [Il Sole 24 Ore](https://www.ilsole24ore.com)
- [Tgcom24](https://www.tgcom24.mediaset.it)
- [Adnkronos](https://www.adnkronos.com)
- [Open](https://www.open.online)
- [Il Post](https://www.ilpost.it)
- [Il Fatto Quotidiano](https://www.ilfattoquotidiano.it)
- [Il Giornale](https://www.ilgiornale.it)
- [La Nazione](https://www.lanazione.it)
- [Il Mattino](https://www.ilmattino.it)
- [Il Giorno](https://www.ilgiorno.it)
- [RomaToday](https://www.romatoday.it)
- [Dire](https://www.dire.it)
- [RSI](https://www.rsi.ch)
- [Euronews](https://it.euronews.com)
- [Quotidiano Nazionale](https://www.quotidiano.net)
- [Globalist](https://www.globalist.it)
- [Panorama](https://www.panorama.it)
- [Il Tempo](https://www.iltempo.it)
- [Virgilio Notizie](https://www.virgilio.it)
- [CNN](https://www.cnn.com)
- [Bloomberg](https://www.bloomberg.com)
- [CNBC](https://www.cnbc.com)
- [Internazionale (Reuters)](https://www.internazionale.it)
- [El Español](https://www.elespanol.com)
- [laRegione.ch](https://www.laregione.ch)
- [Sky TG24](https://tg24.sky.it)
- [Il Giornale d'Italia](https://www.ilgiornaleditalia.it)
- [Yahoo Finanza Italia](https://it.finance.yahoo.com)
- [Il Sussidiario](https://www.ilsussidiario.net)
- [Agenzia Nova](https://www.agenzianova.com)
- [Journal du Net](https://www.journaldunet.com)
- [Public Sénat](https://www.publicsenat.fr)
- [The Objective](https://theobjective.com)
- [Times of Israel](https://www.timesofisrael.com)
- [CFR](https://www.cfr.org)
- [Tech Startups](https://techstartups.com)
- [Frontex](https://www.frontex.europa.eu)
- [FNSI](https://www.fnsi.it)
- [MilanoToday](https://www.milanotoday.it)
- [ScienceDaily](https://www.sciencedaily.com)
- [JAMA Network Open](https://jamanetwork.com)
- [Nature](https://www.nature.com)
- [UT Health San Antonio](https://news.uthscsa.edu)
- [University of Cambridge](https://www.cam.ac.uk)
- [Dataconomy](https://dataconomy.com)
- [TechCrunch](https://techcrunch.com)
- [Washington Post](https://www.washingtonpost.com)
- [Fortune](https://fortune.com)
- [Al Jazeera](https://www.aljazeera.com)
- [anews](https://www.anews.com.tr)
- [WTOP](https://wtop.com)
- [Axios](https://www.axios.com)
- [Adn24](https://www.adn24.it)
- [Arab News](https://www.arabnews.com)
- [Human Rights Watch](https://www.hrw.org)
- [Xinhua](https://english.news.cn)
- [Spaceflight Now](https://spaceflightnow.com)
- [Reuters](https://www.reuters.com)
- [Wall Street Journal](https://www.wsj.com)
- [LuccaInDiretta](https://www.luccaindiretta.it)
- [forzearmate.org](https://forzearmate.org)
- [RIA Novosti](https://ria.ru)
- [NPR](https://www.npr.org)
- [CBS News](https://www.cbsnews.com)
- [Anadolu Agency](https://www.aa.com.tr)
- [La Voce di New York](https://www.lavocedinewyork.com)
- [Federconsumatori](https://federconsumatori.it)
- [InfoCilento](https://www.infocilento.it)
- [SalernoToday](https://www.salernotoday.it)
- [Il Gallo](https://www.ilgallo.it)
- [Corriere Salentino](https://www.corrieresalentino.it)
- [l'Immediato](https://www.immediato.net)
- [Altarimini](https://altarimini.it)
- [Stato Quotidiano](https://www.statoquotidiano.it)
- [PBS NewsHour](https://www.pbs.org)
- [Pakistan Today](https://www.pakistantoday.com.pk)
- [Sudan Tribune](https://sudantribune.com)
- [MilanoFinanza](https://www.milanofinanza.it)
- [Eastern Herald](https://easternherald.com)
- [Spaziocrypto](https://en.spaziocrypto.com)
- [QuiFinanza](https://www.quifinanza.it)
- [Federal Reserve](https://www.federalreserve.gov)
- [Italpress](https://www.italpress.com)
- [Blitz Quotidiano](https://www.blitzquotidiano.it)
- [Teleacras](https://www.teleacras.it)
- [Imola Oggi](https://www.imolaoggi.it)
- [Yahoo Finance](https://finance.yahoo.com)
- [98Zero](https://www.98zero.com)
- [AGI](https://www.agi.it)
- [BleepingComputer](https://www.bleepingcomputer.com)
- [Borsa Italiana/Radiocor](https://www.borsaitaliana.it)
- [CatanzaroInforma](https://www.catanzaroinforma.it)
- [China Daily](https://www.chinadaily.com.cn)
- [CoinDesk](https://www.coindesk.com)
- [Cyprus Mail](https://cyprus-mail.com)
- [Engadget](https://www.engadget.com)
- [El País](https://english.elpais.com)
- [Fanpage](https://www.fanpage.it)
- [GrandangoloAgrigento](https://www.grandangoloagrigento.it)
- [Infobae](https://www.infobae.com)
- [Investing.com](https://www.investing.com)
- [MacRumors](https://www.macrumors.com)
- [OpenAI](https://openai.com)
- [TASS](https://tass.com)
- [Telenuova](https://www.telenuova.tv)
- [Tempo Stretto](https://www.tempostretto.it)
- [The Decoder](https://the-decoder.com)
- [The Guardian](https://www.theguardian.com)
- [Venezuelanalysis](https://venezuelanalysis.com)
- [WAFA](https://english.wafa.ps)

### Principio finale

L'elenco è un **bacino di ricerca**, non una lista da citare meccanicamente. Per ogni notizia vanno selezionate le fonti che hanno realmente pubblicato informazioni pertinenti sullo stesso fatto. Il risultato deve mostrare al lettore **come fonti diverse raccontano la stessa notizia**, senza classificare politicamente le testate e senza trasformare il confronto in una falsa contrapposizione.

## Regola toponomastica — KIEV

Regola vincolante e permanente (Mario, 20/09/2026).

- In tutti i contenuti de **Il Contribuente** utilizzare sempre la forma italiana **Kiev**.
- Non utilizzare mai la grafia **Kyiv** nei testi redazionali, nei titoli, nei sottotitoli, nelle didascalie, nei box, nelle copertine e nei post social.
- Se una fonte utilizza “Kyiv”, nella rielaborazione editoriale convertirlo in **Kiev**, salvo il caso di una citazione letterale in cui la grafia faccia parte del testo originale.
- La regola serve a mantenere una terminologia immediatamente riconoscibile e uniforme per i lettori italiani.
