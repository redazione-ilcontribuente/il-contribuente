export default function Sidebar({ sidebar }) {
  return (
    <div className="side-col" id="approfondimenti">
      <div className="sidebar-block">
        <div className="sidebar-kicker">Approfondimenti fissi</div>
        {sidebar.fixedLinks.map((link, i) => (
          <a href={link.href} className="sidebar-item" key={i}>
            <span className="sidebar-item-title">{link.title}</span>
            <span className="sidebar-item-desc">{link.desc}</span>
          </a>
        ))}
      </div>

      <div className="sidebar-block">
        <div className="sidebar-kicker">Termine del giorno</div>
        <div className="sidebar-term-name">{sidebar.term.name}</div>
        <div className="sidebar-term-def">{sidebar.term.def}</div>
        <a href="glossario/glossario.html" className="sidebar-mini-link">Tutti i termini &rarr;</a>
      </div>

      <div className="sidebar-block">
        <div className="sidebar-kicker">Il Contribuente in cifre</div>
        <div className="sidebar-stats">
          {sidebar.stats.map((s, i) => (
            <div key={i}>
              <div className="sidebar-stat-value">{s.value}</div>
              <div className="sidebar-stat-label">{s.label}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
