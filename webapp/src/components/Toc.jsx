export default function Toc({ items, dashboards }) {
  return (
    <div className="toc">
      <div className="toc-inner">
        <div className="toc-kicker">Indice</div>
        <div className="toc-links">
          {items.map((item, i) => (
            <a href={item.href} className="toc-link" key={i}>{item.label}</a>
          ))}
        </div>
      </div>
      {dashboards && dashboards.length > 0 && (
        <div className="toc-dashboards">
          {dashboards.map((d, i) => (
            <a
              href={d.href}
              className={'toc-dashboard-card' + (d.mobileOnly ? ' toc-dashboard-mobile-only' : '')}
              key={i}
            >
              <span className="toc-dashboard-tag">{d.tag}</span>
              <span className="toc-dashboard-label">{d.label}</span>
            </a>
          ))}
        </div>
      )}
    </div>
  )
}
