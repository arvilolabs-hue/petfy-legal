# Petfy · Arvilo Labs

Sitio estático de presentación, soporte y documentos públicos de Petfy. El lanzamiento vigente es **solo para iPhone y iPad en App Store**.

## Estructura

- `build_site.py` genera el HTML sin dependencias externas.
- `content.py` contiene los textos EN/ES de las páginas jurídicas.
- `style.css` y `language.js` contienen la presentación y el selector de idioma.
- `assets/` incluye ilustraciones oficiales de Petfy copiadas del repositorio de la app.
- `PRODUCT.md`, `DESIGN.md` y `RELEASE_DECISIONS.md` documentan el producto, el diseño y las verificaciones pendientes antes del lanzamiento internacional.

Páginas generadas: `index.html`, `support.html`, `privacy.html`, `terms.html`, `delete-account.html`, `ai-notice.html`, `dmca.html`.

## Desarrollo

```bash
python3 build_site.py
python3 -m http.server 8765
```

Abre `http://localhost:8765/index.html`. Antes de confirmar cambios, ejecuta `python3 check_site.py` y `git diff --check`.

## Estado de publicación

Las páginas jurídicas muestran **versión 1.0, vigente desde el 15 de septiembre de 2026**. La identidad visual pública es Arvilo Labs; privacidad y condiciones identifican a Brandon Stevens Aragón Mejía como titular y responsable. Soporte, privacidad y eliminación de cuenta usan `arvilolabs@gmail.com`. `RELEASE_DECISIONS.md` conserva las comprobaciones de lanzamiento internacional y la app debe enlazar la misma versión antes de presentarse a revisión.

El sitio público actual sigue en `https://arvilolabs-hue.github.io/petfy-legal/`; este repositorio local puede probarse antes de cambiar GitHub Pages.
