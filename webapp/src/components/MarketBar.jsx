import { parseStyle } from '../lib/styleUtil'

export default function MarketBar({ cards }) {
  return (
    <div className="market-bar">
      <div className="market-bar-inner">
        {cards.map((c, i) => (
          <div className="market-card" key={i} style={parseStyle(c.style)}>
            <div className="market-label">{c.label}</div>
            <div className="market-value" style={parseStyle(c.valueStyle)}>{c.value}</div>
            <div className={'market-delta' + (c.deltaDirection ? ' ' + c.deltaDirection : '')}>
              {c.delta}
            </div>
            <div className="market-source">{c.source}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
