// Elenco di denunce/esposti/dichiarazioni di associazioni e comitati.
// Ogni scheda distingue sempre chi, cosa, quando e l'esito (o la sua
// assenza) — e se si tratta di un esposto formale o solo di una
// dichiarazione pubblica, cosi' il lettore non confonde le due cose.
export default function DenunceList({ items }) {
  if (!items || items.length === 0) return null
  return (
    <div className="pb-denunce-list">
      {items.map((it, i) => (
        <div className="pb-denuncia-card" key={i}>
          <div className="pb-denuncia-top">
            <span className="pb-denuncia-chi">{it.chi}</span>
            <span className={'pb-denuncia-tipo' + (it.formale ? ' formale' : ' dichiarazione')}>
              {it.formale ? 'Esposto formale' : 'Dichiarazione pubblica'}
            </span>
          </div>
          <div className="pb-denuncia-meta">{it.quando}</div>
          <div className="pb-denuncia-testo" dangerouslySetInnerHTML={{ __html: it.cosa }} />
          <div className={'pb-denuncia-esito' + (it.esitoStato ? ' ' + it.esitoStato : '')}>
            Esito: <span dangerouslySetInnerHTML={{ __html: it.esito }} />
          </div>
          {it.fonteHtml && (
            <div className="pb-denuncia-fonte" dangerouslySetInnerHTML={{ __html: it.fonteHtml }} />
          )}
        </div>
      ))}
    </div>
  )
}
