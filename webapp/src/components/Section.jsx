import Article from './Article'
import Duel from './Duel'
import KpiSection from './KpiSection'

export default function Section({ section }) {
  return (
    <div className="section" id={section.id}>
      <div className="section-head">
        <span className={'section-tag' + (section.tagClass ? ' ' + section.tagClass : '')}>
          {section.tag}
        </span>
        <h2 className="section-title" dangerouslySetInnerHTML={{ __html: section.title }} />
      </div>

      {section.note && (
        <div className="section-note" dangerouslySetInnerHTML={{ __html: section.note }} />
      )}

      {section.context.length > 0 && (
        <div className="context-box">
          <div className="context-box-label">Da sapere per capire</div>
          {section.context.map((p, i) => (
            <p key={i} dangerouslySetInnerHTML={{ __html: p }} />
          ))}
        </div>
      )}

      {section.type === 'duel' && (
        <Duel duel={section.duel} divergence={section.divergence} />
      )}

      {section.type === 'articles' && (
        <div className="articles">
          {section.articles.map((a, i) => (
            <Article article={a} key={i} />
          ))}
        </div>
      )}

      {section.type === 'kpi' && (
        <KpiSection blocks={section.blocks} />
      )}
    </div>
  )
}
