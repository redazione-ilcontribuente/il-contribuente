// Converte una stringa style="border-color:#7c1d16;" (cosi' come esce
// dal parser Python) in un oggetto utilizzabile da React (style={...}).
export function parseStyle(styleStr) {
  if (!styleStr) return undefined
  const out = {}
  styleStr.split(';').forEach((decl) => {
    const [prop, val] = decl.split(':')
    if (!prop || !val) return
    const camel = prop.trim().replace(/-([a-z])/g, (_, c) => c.toUpperCase())
    out[camel] = val.trim()
  })
  return out
}
