import { parseStyle } from '../lib/styleUtil'
import Timeline from './Timeline'
import RegionMap from './RegionMap'
import Article from './Article'
import DenunceList from './DenunceList'
import ProcessiList from './ProcessiList'

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
        if (b.kind === 'timeline') {
          return <Timeline items={b.items} key={i} />
        }
        if (b.kind === 'map') {
          return <RegionMap points={b.points} note={b.note} key={i} />
        }
        if (b.kind === 'subhead') {
          return (
            <div className="pb-subhead" key={i}>
              <span className="pb-subhead-tag" style={parseStyle(b.style)}>{b.label}</span>
            </div>
          )
        }
        if (b.kind === 'articles') {
          return (
            <div className="articles" key={i}>
              {b.articles.map((a, j) => (
                <Article article={a} key={j} />
              ))}
            </div>
          )
        }
        if (b.kind === 'denunce') {
          return <DenunceList items={b.items} key={i} />
        }
        if (b.kind === 'processi') {
          return <ProcessiList items={b.items} key={i} />
        }
        return null
      })}
    </>
  )
}
