import { useEffect, useState } from 'react'

export default function BackToTop() {
  const [show, setShow] = useState(false)

  useEffect(() => {
    function onScroll() {
      setShow(window.scrollY > 400)
    }
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  return (
    <a href="#top" id="backToTop" className={'back-to-top' + (show ? ' show' : '')} aria-label="Torna su">
      &#8593;
    </a>
  )
}
