// Sequenza temporale generica per le sezioni dashboard (es. Petrolio Basilicata).
// Puramente presentazionale, nessuna interazione richiesta: deve restare
// leggibile identica su telefono, tablet, laptop e TV.
export default function Timeline({ items }) {
  if (!items || items.length === 0) return null
  return (
    <div className="pb-timeline">
      {items.map((it, i) => (
        <div className="pb-timeline-item" key={i}>
          <div className="pb-timeline-dot" />
          <div className="pb-timeline-year">{it.year}</div>
          <div className="pb-timeline-text" dangerouslySetInnerHTML={{ __html: it.text }} />
        </div>
      ))}
    </div>
  )
}
