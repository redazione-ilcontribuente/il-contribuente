export default function AgendaBox({ items }) {
  return (
    <div className="agenda-box">
      <h3 className="agenda-title">Cosa succede oggi</h3>
      <div className="agenda-list">
        {items.map((item, i) => (
          <div className="agenda-item" key={i}>
            <span className="agenda-time">{item.time}</span>
            <span className="agenda-event">{item.event}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
