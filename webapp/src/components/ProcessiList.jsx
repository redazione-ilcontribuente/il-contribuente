// Schede dei procedimenti giudiziari. Ogni scheda ha una riga "Stato
// attuale" ben visibile in cima (per non lasciare mai intendere una
// responsabilita' penale che i gradi successivi hanno escluso) seguita
// dalle fasi del procedimento in ordine cronologico.
export default function ProcessiList({ items }) {
  if (!items || items.length === 0) return null
  return (
    <div className="pb-processi-list">
      {items.map((it, i) => (
        <div className="pb-processo-card" key={i}>
          <div className="pb-processo-title">{it.titolo}</div>
          {it.sottotitolo && <div className="pb-processo-sub">{it.sottotitolo}</div>}
          <div className="pb-processo-stato">
            <span className="pb-processo-stato-label">Stato attuale</span>
            <span dangerouslySetInnerHTML={{ __html: it.statoAttuale }} />
          </div>
          <div className="pb-processo-fasi">
            {it.fasi.map((f, j) => (
              <div className="pb-processo-fase" key={j}>
                <div className="pb-processo-fase-label">{f.label}</div>
                <div className="pb-processo-fase-testo" dangerouslySetInnerHTML={{ __html: f.testo }} />
              </div>
            ))}
          </div>
          {it.notaHtml && (
            <div className="pb-processo-nota" dangerouslySetInnerHTML={{ __html: it.notaHtml }} />
          )}
        </div>
      ))}
    </div>
  )
}
