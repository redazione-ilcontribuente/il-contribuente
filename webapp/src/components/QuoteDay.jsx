export default function QuoteDay({ quotes }) {
  return (
    <>
      {quotes.map((q, i) => (
        <div className="quote-day" key={i}>
          <div className="quote-day-inner">
            <div className="quote-day-label">{q.label}</div>
            <div className="quote-day-text">{q.text}</div>
            <div className="quote-day-author">{q.author}</div>
          </div>
        </div>
      ))}
    </>
  )
}
