# Petfy · Arvilo Labs

Sitio estático de presentación, soporte y documentos públicos de Petfy. El lanzamiento vigente es **solo para iPhone y iPad en App Store**.

## Estructura

- `build_site.py` genera el HTML sin dependencias externas.
- `content.py` contiene los textos EN/ES de las páginas jurídicas.
- `style.css` y `language.js` contienen la presentación y el selector de idioma.
- `assets/` incluye ilustraciones oficiales de Petfy copiadas del repositorio de la app.
- `PRODUCT.md`, `DESIGN.md` y `RELEASE_DECISIONS.md` documentan el producto, el diseño y los hechos pendientes.

Páginas generadas: `index.html`, `support.html`, `privacy.html`, `terms.html`, `delete-account.html`, `ai-notice.html`, `dmca.html`.

## Desarrollo

```bash
python3 build_site.py
python3 -m http.server 8765
```

Abre `http://localhost:8765/index.html`. Antes de confirmar cambios, ejecuta `python3 check_site.py` y `git diff --check`.

## Estado de publicación

Las páginas jurídicas generadas muestran **«Texto en revisión»**. No se deben conectar a la ficha de App Store ni publicar como versión legal vigente hasta resolver los puntos de `RELEASE_DECISIONS.md`, fijar versión/fecha efectiva y revisar el mismo texto dentro de la app. La página de soporte usa el correo público elegido por el titular: `arvilolabs@gmail.com`.

El sitio público actual sigue en `https://arvilolabs-hue.github.io/petfy-legal/`; este repositorio local puede probarse antes de cambiar GitHub Pages.
