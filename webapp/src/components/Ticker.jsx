export default function Ticker({ items }) {
  // raddoppiato per lo scorrimento continuo via CSS (stesso trucco usato in index.html)
  const doubled = [...items, ...items]
  return (
    <div className="ticker-wrap">
      <div className="ticker">
        {doubled.map((t, i) => (
          <span key={i}>&#9733; {t.replace(/^★\s*/, '')}</span>
        ))}
      </div>
    </div>
  )
}
