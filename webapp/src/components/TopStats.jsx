import { parseStyle } from '../lib/styleUtil'

export default function TopStats({ stats }) {
  return (
    <div className="stats">
      {stats.map((s, i) => {
        const className = 'stat' + (s.extraClass ? ' ' + s.extraClass : '')
        const style = parseStyle(s.style)
        const inner = (
          <>
            <div className="stat-label">{s.label}</div>
            <div className="stat-value">{s.value}</div>
            <div className="stat-delta">{s.delta}</div>
          </>
        )
        return s.href ? (
          <a className={className} href={s.href} style={style} key={i}>
            {inner}
          </a>
        ) : (
          <div className={className} style={style} key={i}>
            {inner}
          </div>
        )
      })}
    </div>
  )
}
