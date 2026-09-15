import { useEffect, useState } from 'react'

const TWENTY_FOUR_HOURS_MS = 24 * 60 * 60 * 1000

export default function IntroOverlay({ edition, published }) {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const storageKey = 'ilcontribuente_overlay_seen_' + (edition || 'ignota')
    let expired = false
    if (published) {
      const publishedDate = new Date(published)
      if (!isNaN(publishedDate.getTime())) {
        expired = Date.now() - publishedDate.getTime() > TWENTY_FOUR_HOURS_MS
      }
    }
    let alreadySeen = false
    try {
      alreadySeen = localStorage.getItem(storageKey) === '1'
    } catch (e) {
      alreadySeen = false
    }
    if (!alreadySeen && !expired) {
      setVisible(true)
      document.body.classList.add('overlay-open')
    }
  }, [edition, published])

  function close() {
    setVisible(false)
    document.body.classList.remove('overlay-open')
    try {
      localStorage.setItem('ilcontribuente_overlay_seen_' + (edition || 'ignota'), '1')
    } catch (e) {
      /* ignora: storage non disponibile */
    }
  }

  if (!visible) return null

  return (
    <div className="overlay" id="introOverlay" onClick={(e) => { if (e.target.id === 'introOverlay') close() }}>
      <div className="overlay-box">
        <button className="close-x" id="closeOverlay" aria-label="Chiudi" onClick={close}>&times;</button>
        <h3>Un modo diverso di leggere le notizie</h3>
        <p>
          Ogni notizia ha tante voci quante sono le penne che la scrivono.<br /><br />
          Un giornale sceglie un titolo, un altro ne sceglie uno opposto; uno mette la notizia in prima pagina, un altro la nasconde in fondo.<br /><br />
          Nessuno mente del tutto, ma nessuno racconta tutto.<br /><br />
          "Il Contribuente" nasce per mettere queste voci una accanto all'altra — italiane e straniere — senza sceglierne una al posto tuo.<br /><br />
          I fatti restano fatti. Il pensiero, quello, resta tuo.
        </p>
      </div>
    </div>
  )
}
