---
name: rassegna-stampa-quotidiana

Rassegna stampa quotidiana — 5:00

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

Se Mario non fornisce una fotografia:

- lasciare l'articolo senza immagine;
- NON usare SVG generate da Claude;
- NON usare immagini segnaposto;
- NON inventare una fotografia.

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

Regola standard:

- pubblicazione della fonte originale entro le ultime 24-36 ore rispetto al momento della costruzione della rassegna.

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

Il formato può includere:

- "Prospettiva A";
- "Prospettiva B";
- eventuale "Terza voce";
- "Cosa sappiamo".

La sezione non deve essere costruita per creare artificialmente un equilibrio 50/50.

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

I dati periodici possono essere più vecchi della finestra 24-36 ore se sono gli ultimi dati ufficiali disponibili, purché siano chiaramente datati.

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
- "rispetta la finestra di 24-36 ore";
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

Aggiornare, quando previsto dal template:

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

