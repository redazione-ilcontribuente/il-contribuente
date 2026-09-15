export default function Footer({ updatedLabel }) {
  return (
    <>
      <div className="footer">
        <span>Rassegna stampa — fonti multiple, tradotte e sintetizzate in italiano</span>
        <span>Aggiornata: {updatedLabel}</span>
      </div>
      <div className="footer-note">
        "Il Contribuente" perché sei tu che paghi, in un modo o nell'altro, quasi tutta l'informazione.
        Questa pubblicazione prova a restituirti qualcosa mettendo a confronto i fatti, raccontati da più voci — l'idea te la fai tu.
      </div>
      <div className="footer-legal">
        <p>Pubblicazione indipendente e personale, priva di finalità commerciali. Non sono presenti pubblicità, abbonamenti, sponsorizzazioni o finanziamenti di alcun tipo, pubblici o privati.</p>
        <p>I contenuti pubblicati costituiscono sintesi originali e rielaborazioni redazionali di notizie di pubblico dominio, diffuse da testate giornalistiche terze regolarmente citate accanto a ciascun contenuto. Non viene riprodotto integralmente alcun testo, titolo, fotografia o materiale protetto da diritto d'autore appartenente alle testate citate. Si invita alla consultazione delle fonti originali, di cui vengono sempre indicati nome e riferimento.</p>
        <p>Tutti i marchi, i loghi, i nomi e i segni distintivi delle testate menzionate restano di proprietà esclusiva dei rispettivi editori; la loro citazione ha esclusivo scopo informativo e di attribuzione della fonte, senza alcuna affiliazione, patrocinio o approvazione da parte delle testate stesse.</p>
        <p>Questa pubblicazione non costituisce prodotto editoriale ai sensi dell'art. 1 della legge 7 marzo 2001, n. 62, non avendo carattere di periodicità regolarmente garantita né organizzazione redazionale strutturata, e non è pertanto soggetta a registrazione presso il Tribunale.</p>
        <p>Le sintesi comparative tra testate riportano posizioni e opinioni riconducibili esclusivamente alle fonti citate, non a chi cura questa pubblicazione, il cui intento è offrire un quadro informativo comparato e non esprimere posizioni editoriali proprie.</p>
        <p>Eventuali richieste di rettifica o rimozione di contenuti possono essere inoltrate a <a href="mailto:redazione.ilcontribuente@protonmail.com" style={{ color: 'var(--ink-soft)' }}>redazione.ilcontribuente@protonmail.com</a> e saranno evase con la massima tempestività.</p>
        <p style={{ marginTop: '14px', paddingTop: '12px', borderTop: '1px solid var(--rule)' }}>
          &copy; 2026 Il Contribuente. Tutti i diritti riservati. Le sintesi, le rielaborazioni redazionali, i confronti tra fonti e l'impaginazione originale di questa pubblicazione sono opera dell'autore e tutelati dalla legge sul diritto d'autore (l. 633/1941 e succ. mod.), anche in forma anonima o pseudonima ai sensi dell'art. 8. È vietata la riproduzione, copia integrale o parziale, ridistribuzione o pubblicazione altrove dei contenuti originali di questa testata senza autorizzazione, fatto salvo l'uso di brevi citazioni con obbligo di attribuzione alla fonte.
        </p>
        <div className="footer-cc">
          <span className="footer-cc-icon">CC BY-NC-ND</span>
          <span>
            Informazione senza padroni &middot; Licenza{' '}
            <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it" target="_blank" rel="noopener noreferrer">
              Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0
            </a>
          </span>
        </div>
      </div>
    </>
  )
}
