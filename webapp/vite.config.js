import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Il sito e' pubblicato su GitHub Pages nella root del dominio,
// quindi la base resta '/'. Se in futuro pubblichi sotto un sotto-percorso
// (es. username.github.io/il-contribuente/), cambia base qui.
export default defineConfig({
  plugins: [react()],
  base: '/',
})
