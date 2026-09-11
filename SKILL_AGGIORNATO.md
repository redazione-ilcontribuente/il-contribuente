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
2. Verificare che `index.html` esista nella stessa cartella.
3. Leggere integralmente l'`index.html` corrente: da 10 settembre 2026 è il MASTER permanente da aggiornare ogni giorno.
4. Verificare che l'index contenga almeno:
   - `.article-image`;
   - la logica di layout dinamico già prevista dal template;
   - l'overlay "Un modo diverso di leggere le notizie";
   - il blocco `.footer-legal`;
   - gli script permanenti del template.
5. Se l'index manca o è chiaramente incompleto, NON inventare una nuova struttura HTML.
6. Informare Mario di ciò che manca e chiedere il ripristino dell'index/backup.

Da 10 settembre 2026 `index.html` è la fonte di verità per struttura, CSS, collegamenti e comportamento della pagina. Gli altri file del progetto sono approfondimenti fissi e NON vanno aggiornati quotidianamente.

---

# 3. INDEX.HTML — REGOLA ASSOLUTA

Da 10 settembre 2026 `index.html` è il file master permanente del quotidiano "Il Contribuente".

Deve essere utilizzato come base di ogni nuova edizione e deve essere l'UNICO file aggiornato quotidianamente.

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

Quando Mario richiede una modifica strutturale, grafica o funzionale permanente, applicarla all'`index.html` master e aggiornare anche `SKILL.md` se la modifica introduce una nuova regola da conservare.

Gli approfondimenti e gli altri file del sito restano fissi salvo richiesta esplicita. Ogni nuova edizione deve aggiornare l'index, non reinventare il contenitore.

---

# 4. ORDINE DI COSTRUZIONE

L'ordine operativo corretto è:

1. controllo integrità;
2. lettura integrale dell'index master;
3. verifica dell'indice e delle sezioni;
4. ricerca delle notizie;
5. confronto e verifica delle fonti;
6. selezione dei titoli;
7. presentazione a Mario dell'elenco dei titoli;
8. dopo il passaggio titoli, scrittura degli articoli;
9. inserimento delle immagini fornite da Mario;
10. aggiornamento ticker, mercati, citazioni, agenda, statistiche, dashboard e TUTTE le card;
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
13. Sicurezza Pubblica

Inoltre, su tablet/mobile è presente la mini-card **Approfondimenti**, che porta alla colonna/sezione degli approfondimenti fissi.

Queste sono le voci e i collegamenti strutturali da rispettare.

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

Il CSS dell'index master decide automaticamente la disposizione delle card.

La prima notizia di una sezione a formato articoli è il lead e occupa tutta la larghezza.

Regola generale:

- 1 articolo → piena larghezza;
- 2 articoli → entrambi a piena larghezza, uno sotto l'altro;
- 3 articoli → lead pieno + due card affiancate;
- 4 articoli → lead pieno + tre card affiancate.

NON scegliere manualmente larghezze diverse per le singole card.

NON lasciare spazi vuoti intenzionali.

NON modificare il CSS dell'edizione per correggere manualmente la griglia, salvo una modifica strutturale esplicitamente richiesta da Mario e destinata a diventare permanente nell'index master.

Il primo articolo deve essere marcato come:

`class="article lead"`

e l'index master deve occuparsi del resto.

Dati Immigrazione utilizza il proprio formato dashboard e non segue la griglia `.articles`.

---

# 7. COMPONENTI E BOX

Devono essere mantenuti i componenti già presenti nell'index master, tra cui:

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

Non creare componenti alternativi quando l'index master possiede già quello necessario.

## Da sapere per capire

`context-box` deve spiegare il contesto del fatto.

Può contenere:

- precedenti;
- quadro normativo;
- dati storici;
- definizioni;
- spiegazioni necessarie.

Non deve diventare un resoconto del lavoro della redazione.

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

I colori, i bordi, gli sfondi, i font e le dimensioni sono quelli definiti nell'index master.

NON modificarli durante la produzione quotidiana.

Se Mario vuole cambiare la grafica, la modifica va applicata all'index master permanente.

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

Regola vincolante (Mario, 4/9/2026): la sezione Confronto deve avere OBBLIGATORIAMENTE tre voci, non due. Il formato è sempre:

- "Prospettiva A" (duel-side left);
- "Prospettiva B" (duel-side right);
- "Terza voce" (duel-side third) — indipendente, non allineata né a A né a B: una fonte neutrale, un'analisi critica, un dato verificabile di terze parti (agenzia neutrale, autorità/organizzazione internazionale, esperto di settore). Non è opzionale.

Markup di riferimento (già presente e testato nell'index master): due `.duel-side` (left/right) dentro il primo `.duel-grid`, poi un secondo `.duel-grid` con `style="grid-template-columns:1fr; border-top:1px solid var(--rule);"` contenente il solo `.duel-side.third` a piena larghezza. Non modificare il CSS: questo secondo `.duel-grid` con lo style inline è il modo corretto, già previsto dal template, per ottenere la terza voce senza toccare la regola `.duel-grid{grid-template-columns:1fr 1fr;}`.

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

Aggiornare ogni giorno, quando presenti nell'index:

- benzina;
- diesel;
- petrolio;
- gas;
- oro;
- bitcoin.

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
- index master corretto;
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

### File da aggiornare
- aggiornare quotidianamente SOLO `index.html`;
- NON aggiornare automaticamente `archivio.html`, dossier, pagine guerre, sanzioni, glossario o altri approfondimenti;
- modificare un approfondimento soltanto se Mario lo richiede esplicitamente.

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


# 40. REGOLE PERMANENTI DAL 10 SETTEMBRE 2026 — INDEX, CARD E COLLEGAMENTI

Questa sezione sostituisce qualsiasi istruzione precedente incompatibile.

## Unico file da aggiornare ogni giorno

Da oggi l'unico file da aggiornare quotidianamente è:

`index.html`

Le altre pagine del sito sono **approfondimenti fissi** e NON devono essere aggiornate ogni giorno, salvo richiesta esplicita di Mario.

Ogni nuova rassegna deve quindi partire dall'ultimo `index.html` master disponibile e produrre il nuovo `index.html` del giorno.

## Regola assoluta: aggiornare TUTTE le card

Ogni giorno devono essere controllate e aggiornate **TUTTE le card dinamiche presenti nell'index**, nessuna esclusa.

Questo comprende:

- ticker;
- market bar;
- citazioni del giorno;
- statistiche principali;
- agenda;
- card statistiche;
- dashboard;
- badge fonti/testate;
- eventuali numeri, date, percentuali, variazioni e note temporali.

Non lasciare una card con dati del giorno precedente solo perché la notizia principale è stata aggiornata.

Se il dato ufficiale non cambia, può restare uguale, ma deve essere verificato come ultimo dato disponibile e la data/fonte deve restare corretta.

## Market bar — card permanenti

Il market bar deve mantenere le categorie previste dall'index master:

- Benzina
- Diesel
- Petrolio
- Gas TTF
- Oro
- Bitcoin
- Palestinesi uccisi dal 7 ottobre 2023 (Gaza), se presente nel market bar dell'index master

Aggiornare ogni giorno valori, fonte e riferimento temporale quando esiste un dato più recente.

## Card statistiche principali — struttura corrente

L'index master contiene sei card statistiche principali:

1. **Calo degli sbarchi in Italia da inizio 2026**
2. **Raccolta di Mistral AI, il più grande round tech europeo**
3. **Record esposti nella fuga di dati vietnamita sui passeggeri aerei**
4. **Palestinesi uccisi dal 7 ottobre 2023 (Gaza)**
5. **Omicidi volontari in Italia**
6. **Donne vittime di omicidio volontario e femminicidio**

Le card possono cambiare contenuto in futuro soltanto su richiesta di Mario o quando la logica editoriale dell'index master lo prevede. Fino ad allora la loro presenza e struttura vanno mantenute.

## Card cliccabili — comportamento obbligatorio

Le seguenti card sono interamente cliccabili/toccabili, non soltanto il testo:

### Sbarchi
La card:

**Calo degli sbarchi in Italia da inizio 2026**

deve collegarsi a:

`#dati-immigrazione`

cioè alla dashboard con titolo:

**Immigrazione, i numeri del 2026**

### Omicidi
La card:

**Omicidi volontari in Italia**

deve collegarsi a:

`#reati-tipologia`

### Donne vittime di omicidio volontario e femminicidio
La card:

**Donne vittime di omicidio volontario e femminicidio**

deve collegarsi a:

`#reati-tipologia`

Il target è la chart-card con titolo:

**Reati per tipologia: primo semestre 2026 vs 2025**

### Gaza
La card:

**Palestinesi uccisi dal 7 ottobre 2023 (Gaza)**

deve collegarsi al dossier fisso:

`guerre/pi.html`

Questi collegamenti devono funzionare su desktop, tablet/iPad e smartphone.

NON trasformare solo il titolo in link: l'intera card deve restare cliccabile.

NON cambiare l'aspetto grafico delle card collegate.

## ID permanenti da non rinominare

Devono essere mantenuti:

`id="dati-immigrazione"`

`id="sicurezza-pubblica"`

`id="reati-tipologia"`

`id="approfondimenti"`

Non rinominare o rimuovere questi ID, perché sono usati dai collegamenti interni dell'index.

## Dashboard nell'indice

Nella zona dell'indice devono essere mantenute le mini-card:

- **Dati Immigrazione** → `#dati-immigrazione`
- **Sicurezza Pubblica** → `#sicurezza-pubblica`

Su tablet/mobile deve comparire anche:

- **Approfondimenti** → `#approfondimenti`

Ordine mobile obbligatorio:

1. Dati Immigrazione
2. Sicurezza Pubblica
3. Approfondimenti

Su desktop la mini-card Approfondimenti resta nascosta se così previsto dall'index master; la colonna Approfondimenti resta nella sua posizione laterale.

## Continua a leggere — posizione corretta

Per ogni normale articolo l'ordine visivo deve essere:

1. testo iniziale dell'articolo;
2. eventuale testo aggiuntivo nascosto/espandibile;
3. **Continua a leggere** su una nuova riga dopo il testo;
4. fonti.

Il pulsante NON deve comparire prima della conclusione del testo iniziale e NON deve essere spostato dopo le fonti.

Quando l'articolo viene aperto, il comportamento JavaScript già presente nell'index master deve essere mantenuto.

## Approfondimenti fissi

Le pagine come:

- guerre;
- sanzioni;
- dazi;
- glossario;
- immigrazione Europa;
- SuperPotenze;
- altri dossier fissi;

non vanno riscritte o aggiornate quotidianamente.

Devono essere toccate soltanto quando Mario chiede esplicitamente di modificarle.

## Controllo finale specifico delle card

Prima di consegnare l'index quotidiano verificare sempre:

- che tutte le card previste siano presenti;
- che TUTTI i valori dinamici siano stati controllati;
- che le date siano aggiornate;
- che le fonti siano aggiornate;
- che nessuna card conservi per errore un dato superato;
- che i link delle card cliccabili funzionino;
- che `#dati-immigrazione`, `#sicurezza-pubblica`, `#reati-tipologia` e `#approfondimenti` esistano;
- che `guerre/pi.html` resti il link della card Gaza;
- che desktop, tablet e mobile mantengano il comportamento previsto dall'index master.

---

# 41. ATTIVAZIONE

La skill si attiva quando Mario chiede:

- "rassegna stampa";
- "cosa succede oggi";
- "notizie del giorno";
- "aggiornami";
- "cosa succede in Italia";
- "cosa succede nel mondo";
- oppure una richiesta equivalente di aggiornamento dell'attualità.

Se Mario restringe il tema, utilizzare soltanto le sezioni pertinenti ma mantenere la struttura dell'index master.

Per una rassegna completa, rispettare sempre l'intero indice sopra definito.


## STRUTTURA OBBLIGATORIA DI OGNI ARTICOLO

Questa struttura vale per ogni articolo di tutte le sezioni dell'indice, senza eccezioni per le normali card editoriali.

Ordine obbligatorio:

1. **Da sapere per capire** — breve contesto indispensabile per comprendere la notizia.
2. **Il fatto** — apertura immediata con **4-5 frasi** chiare e informative.
3. **Continua a leggere** — pulsante che espande il resto dell'articolo.
4. **Approfondimento** — contenuto completo, dati, reazioni, contesto e confronto tra fonti.
5. **Fonte/i** — in fondo al contenuto espanso.
6. **Mostra meno** — pulsante finale che richiude l'articolo e riporta alla visualizzazione iniziale.

Il testo completo NON deve essere visibile tutto nella card iniziale. L'obiettivo è mantenere la pagina leggibile e compatta, evitando articoli infiniti che occupano verticalmente tutta la sezione.

Le 4-5 frasi iniziali devono essere sufficienti per capire subito cosa è successo. Il contenuto successivo deve aggiungere informazioni reali e non ripetere l'apertura.

**Da sapere per capire** non è un titolo ornamentale: deve contenere realmente il contesto necessario. **Il fatto** deve invece partire dall'aggiornamento attuale.

I pulsanti devono funzionare tramite JavaScript senza cambiare pagina. Quando l'articolo è aperto, **Continua a leggere** non deve più essere visibile e deve comparire **Mostra meno**. Quando viene richiuso, avviene il contrario.

La struttura HTML/CSS/JS deve essere uniforme in tutte le sezioni, così l'utente impara una sola interazione e la ritrova in tutto il giornale.

---

# 41. REGOLE PERMANENTI DAL 10 SETTEMBRE 2026 — INDEX, CARD E COLLEGAMENTI

Da questa data l'`index.html` corrente è l'unico file da aggiornare quotidianamente. Tutti gli altri file del progetto sono approfondimenti fissi e restano invariati, salvo richiesta esplicita di Mario.

## Aggiornamento quotidiano obbligatorio di TUTTE le card

Ogni giorno bisogna controllare e aggiornare TUTTE le card presenti nell'index, senza eccezioni. Nessuna card deve restare con un valore, una data o una fonte del giorno precedente se esiste un dato più recente verificabile. Questo vale sia per le card della market bar sia per le card statistiche grandi.

Le card statistiche attualmente previste sono 6:

1. **Calo degli sbarchi in Italia da inizio 2026**;
2. **Raccolta di Mistral AI, il più grande round tech europeo**;
3. **Record esposti nella fuga di dati vietnamita sui passeggeri aerei**;
4. **Palestinesi uccisi dal 7 ottobre 2023 (Gaza)**;
5. **Omicidi volontari in Italia**;
6. **Donne vittime di omicidio volontario e femminicidio**.

Le sei card vanno mantenute nello stesso stile visivo già presente nell'index master. Non ridisegnarle e non sostituirle con componenti diversi.

## Card cliccabili: comportamento permanente

Quando una card è collegata a un approfondimento o a un punto interno della pagina, deve essere cliccabile/toccabile su TUTTA la superficie della card, non soltanto sul testo. Il comportamento deve funzionare allo stesso modo su desktop, iPad e smartphone. Mantenere il testo senza sottolineature e i colori ereditati, come già implementato nell'index master.

Collegamenti permanenti attuali:

- **Calo degli sbarchi in Italia da inizio 2026** → `#dati-immigrazione`, cioè la sezione **Dati Immigrazione — “Immigrazione, i numeri del 2026”**;
- **Omicidi volontari in Italia** → `#reati-tipologia`, cioè il grafico **“Reati per tipologia: primo semestre 2026 vs 2025”** nella sezione Sicurezza Pubblica;
- **Donne vittime di omicidio volontario e femminicidio** → `#reati-tipologia`, stesso grafico della sezione Sicurezza Pubblica;
- **Palestinesi uccisi dal 7 ottobre 2023 (Gaza)** → `guerre/pi.html`, dossier fisso **“Palestina e Israele: dalle origini a oggi”**.

I target/ID esistenti non devono essere rinominati senza richiesta esplicita, altrimenti i collegamenti delle card si rompono.

## Card Omicidi e Femminicidi

Le due card devono mostrare il dato corrente verificato senza inserire automaticamente un confronto con l'anno precedente nel testo della card. Il confronto storico resta nel grafico di Sicurezza Pubblica raggiungibile con il click/tap.

## Dashboard dell'indice e Approfondimenti su mobile

Sotto l'indice devono restare le mini-card dashboard già presenti:

1. Dati Immigrazione;
2. Sicurezza Pubblica;
3. Approfondimenti — visibile come mini-card nell'indice sui dispositivi mobili/tablet secondo le media query già presenti.

La colonna Approfondimenti resta nella sidebar su desktop; su schermi stretti scorre dopo il contenuto principale, come previsto dall'index master. Non modificare questo comportamento.

## Pulsante “Continua a leggere”

Nelle normali card articolo l'ordine visivo attuale deve essere preservato: testo iniziale dell'articolo → eventuale contenuto espandibile → ultimo periodo visibile → pulsante **Continua a leggere** su una nuova riga → blocco fonti. Non spostare il pulsante sopra l'ultimo testo visibile e non metterlo dopo le fonti.

## Controllo finale specifico delle card

Prima di consegnare l'HTML quotidiano verificare sempre:

- che tutte le card presenti nell'index siano state controllate una per una;
- che valori, date e fonti siano aggiornati quando esiste un dato nuovo;
- che nessuna card dinamica riporti per errore il dato del giorno precedente;
- che i quattro collegamenti permanenti sopra indicati funzionino;
- che l'intera superficie delle card collegate sia cliccabile/toccabile;
- che `#dati-immigrazione` e `#reati-tipologia` esistano ancora;
- che il link `guerre/pi.html` non venga trasformato in un link esterno o rinominato;
- che layout, hover e comportamento responsive siano rimasti identici.

