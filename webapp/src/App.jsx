import edition from './data/edition.json'
import IntroOverlay from './components/IntroOverlay'
import Masthead from './components/Masthead'
import Ticker from './components/Ticker'
import MarketBar from './components/MarketBar'
import Sidebar from './components/Sidebar'
import Toc from './components/Toc'
import VerifyBadge from './components/VerifyBadge'
import QuoteDay from './components/QuoteDay'
import TopStats from './components/TopStats'
import AgendaBox from './components/AgendaBox'
import Section from './components/Section'
import Footer from './components/Footer'
import BackToTop from './components/BackToTop'

function formatUpdatedLabel(edizioneIso) {
  if (!edizioneIso) return ''
  const mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
  const [y, m, d] = edizioneIso.split('-').map(Number)
  if (!y || !m || !d) return edizioneIso
  return `${d} ${mesi[m - 1]} ${y}`
}

export default function App() {
  return (
    <>
      <IntroOverlay edition={edition.edition} published={edition.published} />
      <Masthead masthead={edition.masthead} badges={edition.badges} />
      <Ticker items={edition.ticker} />
      <MarketBar cards={edition.market} />
      <div className="wrap">
        <div className="page-grid">
          <Sidebar sidebar={edition.sidebar} />
          <div className="main-col">
            <Toc items={edition.toc} dashboards={edition.tocDashboards} />
            <VerifyBadge html={edition.verifyBadgeHtml} />
            <QuoteDay quotes={edition.quotes} />
            <TopStats stats={edition.topStats} />
            {edition.topStatsNote && (
              <div
                className="section-note"
                style={{ marginTop: '-32px', marginBottom: '44px' }}
                dangerouslySetInnerHTML={{ __html: edition.topStatsNote }}
              />
            )}
            <AgendaBox items={edition.agenda} />

            {edition.sections.map((s) => (
              <Section section={s} key={s.id} />
            ))}
          </div>
        </div>
      </div>
      <Footer updatedLabel={formatUpdatedLabel(edition.edition)} />
      <BackToTop />
    </>
  )
}
