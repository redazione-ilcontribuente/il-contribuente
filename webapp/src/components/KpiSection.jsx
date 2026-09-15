import { parseStyle } from '../lib/styleUtil'

function ChartCard({ card }) {
  return (
    <div className="chart-card" id={card.id || undefined}>
      <div className="chart-title">{card.title}</div>
      <div className="chart-period" dangerouslySetInnerHTML={{ __html: card.period }} />
      {card.bars.map((bar, i) => (
        <div className="bar-row" key={i}>
          <div className="bar-label">{bar.label}</div>
          <div className="bar-track">
            <div
              className={'bar-fill' + (bar.fillClass ? ' ' + bar.fillClass : '')}
              style={parseStyle(bar.style)}
              data-tooltip={bar.tooltip}
            />
          </div>
          <div className="bar-value" dangerouslySetInnerHTML={{ __html: bar.value }} />
        </div>
      ))}
      {card.sideNotes && card.sideNotes.map((note, i) => (
        <div className="side-note" key={i} dangerouslySetInnerHTML={{ __html: note }} />
      ))}
      {card.tableHtml && (
        <div dangerouslySetInnerHTML={{ __html: `<details class="table-view">${card.tableHtml}</details>` }} />
      )}
      {card.sources && <div className="dv-sources" dangerouslySetInnerHTML={{ __html: card.sources }} />}
    </div>
  )
}

function KpiRow({ kpis }) {
  return (
    <div className="kpi-row">
      {kpis.map((k, i) => (
        <div className={'kpi' + (k.extraClass ? ' ' + k.extraClass : '')} key={i}>
          <div className="kpi-label">{k.label}</div>
          <div className="kpi-value">{k.value}</div>
          <div className="kpi-note" dangerouslySetInnerHTML={{ __html: k.note }} />
        </div>
      ))}
    </div>
  )
}

// Rende in sequenza esatta i blocchi di una sezione 'dati' (note, righe di
// kpi, grafici a barre) cosi' come compaiono nell'HTML originale: una
// sezione come "Sicurezza pubblica" ne ha piu' di uno, con sotto-titoli
// numerati in mezzo.
export default function KpiSection({ blocks }) {
  return (
    <>
      {blocks.map((b, i) => {
        if (b.kind === 'note') {
          return (
            <div
              className="section-note"
              style={parseStyle(b.style)}
              key={i}
              dangerouslySetInnerHTML={{ __html: b.html }}
            />
          )
        }
        if (b.kind === 'kpiRow') {
          return <KpiRow kpis={b.kpis} key={i} />
        }
        if (b.kind === 'chartCard') {
          return <ChartCard card={b.card} key={i} />
        }
        return null
      })}
    </>
  )
}
