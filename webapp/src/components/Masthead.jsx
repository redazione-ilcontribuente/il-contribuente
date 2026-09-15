import { useState } from 'react'

const BADGE_LIMIT = 15

export default function Masthead({ masthead, badges }) {
  const [expanded, setExpanded] = useState(false)
  const showToggle = badges.length > BADGE_LIMIT

  return (
    <div className="masthead">
      <div className="masthead-top">
        {masthead.topLine.map((line, i) => (
          <span key={i}>{line}</span>
        ))}
      </div>
      <h1
        className="masthead-title"
        dangerouslySetInnerHTML={{ __html: masthead.titleHtml }}
      />
      <div
        className="masthead-sub"
        dangerouslySetInnerHTML={{ __html: masthead.subtitle }}
      />
      <div className="masthead-badges">
        {badges.map((b, i) => (
          <a
            key={i}
            className={'badge' + (i >= BADGE_LIMIT && !expanded ? ' badge-hidden' : '')}
            href={b.href}
            target="_blank"
            rel="noopener noreferrer"
          >
            {b.label}
          </a>
        ))}
      </div>
      {showToggle && (
        <button
          type="button"
          className="badges-toggle-btn"
          onClick={() => setExpanded((v) => !v)}
        >
          {expanded ? 'Mostra meno' : 'Vedi altri'}
        </button>
      )}
      <a href="archivio.html" className="back-link">Archivio edizioni &rarr;</a>
    </div>
  )
}
