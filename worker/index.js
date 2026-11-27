// Il Contribuente — reindirizzamento al dominio ufficiale (Mario, 27/11/2026).
// Chi apre il vecchio indirizzo (*.workers.dev) o www.ilcontribuente.com
// viene portato con un redirect 301 su https://ilcontribuente.com, stessa pagina.
// Tutto il resto è servito normalmente dai file del sito.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.endsWith(".workers.dev") || url.hostname === "www.ilcontribuente.com") {
      url.protocol = "https:";
      url.hostname = "ilcontribuente.com";
      url.port = "";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
