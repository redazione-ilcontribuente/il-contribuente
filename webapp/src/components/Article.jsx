import { useState } from 'react'

export default function Article({ article }) {
  const [expanded, setExpanded] = useState(false)
  const hasMore = article.bodyExtra && article.bodyExtra.length > 0

  return (
    <div className={'article' + (article.lead ? ' lead' : '') + (expanded ? ' expanded' : '')}>
      <h3>{article.title}</h3>
      <p dangerouslySetInnerHTML={{ __html: article.leadParagraph }} />
      {hasMore && (
        <div className="body-extra">
          {article.bodyExtra.map((p, i) => (
            <p key={i} dangerouslySetInnerHTML={{ __html: p }} />
          ))}
        </div>
      )}
      {hasMore && (
        <button
          type="button"
          className="read-more-btn"
          onClick={() => setExpanded((v) => !v)}
        >
          {expanded ? 'Mostra meno' : 'Continua a leggere'} <span className="rm-arrow">&#8595;</span>
        </button>
      )}
      <span className="source" dangerouslySetInnerHTML={{ __html: article.sourceHtml }} />
    </div>
  )
}
