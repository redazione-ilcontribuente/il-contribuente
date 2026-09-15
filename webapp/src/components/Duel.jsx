import { useState } from 'react'

function DuelSide({ side }) {
  const [expanded, setExpanded] = useState(false)
  const hasMore = side.bodyExtra && side.bodyExtra.length > 0

  return (
    <div className={'duel-side ' + side.variant + (expanded ? ' expanded' : '')}>
      <span className="duel-tag">{side.tag}</span>
      <div className="duel-headline" dangerouslySetInnerHTML={{ __html: side.headline }} />
      <p className="body" dangerouslySetInnerHTML={{ __html: side.body }} />
      {hasMore && (
        <div className="body-extra">
          {side.bodyExtra.map((p, i) => (
            <p className="body" key={i} dangerouslySetInnerHTML={{ __html: p }} />
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
      <span className="source" dangerouslySetInnerHTML={{ __html: side.sourceHtml }} />
    </div>
  )
}

export default function Duel({ duel, divergence }) {
  const mainSides = duel.sides.filter((s) => s.variant === 'left' || s.variant === 'right')
  const thirdSides = duel.sides.filter((s) => s.variant === 'third')

  return (
    <>
      <div className="duel">
        <div className="duel-fact">
          <div className="duel-fact-label">Il fatto</div>
          <div className="duel-fact-text" dangerouslySetInnerHTML={{ __html: duel.fact }} />
        </div>
        <div className="duel-grid">
          {mainSides.map((s, i) => (
            <DuelSide side={s} key={i} />
          ))}
        </div>
        {thirdSides.length > 0 && (
          <div className="duel-grid" style={{ gridTemplateColumns: '1fr', borderTop: '1px solid var(--rule)' }}>
            {thirdSides.map((s, i) => (
              <DuelSide side={s} key={i} />
            ))}
          </div>
        )}
      </div>
      {divergence && (
        <div className="context-box" style={{ marginTop: '20px' }}>
          <div className="context-box-label">Dove le fonti divergono</div>
          <p dangerouslySetInnerHTML={{ __html: divergence }} />
        </div>
      )}
    </>
  )
}
