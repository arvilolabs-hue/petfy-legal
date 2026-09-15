#!/usr/bin/env python3
"""Generate dependency-free GitHub Pages HTML from reviewed source copy.

Current legal content is a review draft. RELEASE_DECISIONS.md must be resolved
before changing DRAFT to an effective policy and publishing it.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

from content import PAGES

ROOT = Path(__file__).resolve().parent
DRAFT_VERSION = "2026-09-15-draft.3"


def localized(es: str, en: str, tag: str = "span") -> str:
    return (
        f'<{tag} class="lang-es" lang="es">{es}</{tag}>'
        f'<{tag} class="lang-en" lang="en">{en}</{tag}>'
    )


def svg_arrow() -> str:
    return '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def page_shell(title: str, description: str, body: str, current: str, es_title: str | None = None) -> str:
    robots_tag = '<meta name="robots" content="noindex,nofollow" />\n  ' if current == "legal" else ""
    nav = [
        ("index.html", "home", "Inicio", "Home"),
        ("index.html#documents", "documents", "Documentos", "Documents"),
        ("support.html", "support", "Ayuda", "Support"),
    ]
    nav_html = "".join(
        f'<a href="./{href}" {"aria-current=\"page\"" if current == key else ""}>{localized(es, en)}</a>'
        for href, key, es, en in nav
    )
    # A direct policy page lives under the Documents family, so the nav retains
    # straightforward destinations rather than falsely marking an anchor current.
    return f'''<!doctype html>
<html lang="en" data-language="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="color-scheme" content="light" />
  <meta name="description" content="{escape(description, quote=True)}" />
  <meta name="theme-color" content="#fcfaf8" />
  {robots_tag}<title data-title-en="{escape(title, quote=True)} · Petfy" data-title-es="{escape(es_title or title, quote=True)} · Petfy">{escape(title)} · Petfy</title>
  <link rel="icon" type="image/png" href="./assets/favicon.png" />
  <link rel="stylesheet" href="./style.css" />
  <script src="./language.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">{localized('Saltar al contenido', 'Skip to content')}</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="identity" href="./index.html" aria-label="Petfy, Arvilo Labs">
        <img src="./assets/petfy-mark.png" alt="" width="48" height="48" />
        <span class="identity-text"><strong>Petfy</strong><small>Arvilo Labs</small></span>
      </a>
      <nav class="primary-nav" aria-label="Main navigation">{nav_html}</nav>
      <div class="language-switcher" role="group" aria-label="Language">
        <button type="button" data-language-button="es" aria-label="Español">ES</button>
        <button type="button" data-language-button="en" aria-label="English">EN</button>
      </div>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand"><strong>Petfy</strong><span>{localized('Una app de Arvilo Labs para cuidar con claridad.', 'An Arvilo Labs app for clearer pet care.')}</span></div>
      <nav aria-label="Footer navigation">
        <a href="./privacy.html">{localized('Privacidad', 'Privacy')}</a>
        <a href="./terms.html">{localized('Condiciones', 'Terms')}</a>
        <a href="./delete-account.html">{localized('Eliminar cuenta', 'Delete account')}</a>
        <a href="./support.html">{localized('Ayuda', 'Support')}</a>
      </nav>
      <a class="footer-contact" href="mailto:arvilolabs@gmail.com">arvilolabs@gmail.com</a>
      <p class="footer-note">{localized('© 2026 Arvilo Labs · Petfy para iPhone y iPad.', '© 2026 Arvilo Labs · Petfy for iPhone and iPad.')}</p>
    </div>
  </footer>
</body>
</html>
'''


def draft_notice() -> str:
    return f'''<div class="draft-notice" role="note">
      <strong>{localized('Texto en revisión', 'Text under review')}</strong>
      <p>{localized('Esta propuesta aún no es la versión legal vigente. Faltan decisiones sobre menores, transferencias, conservación y otros puntos del lanzamiento internacional.', 'This proposal is not yet the effective legal version. Decisions about minors, transfers, retention, and other international launch details remain.')} · {DRAFT_VERSION}</p>
    </div>'''


def home_page() -> str:
    paths = [
        ("privacy.html", "01", "Entiende tus datos", "Understand your data", "Qué se usa, por qué y cómo pedir ayuda.", "What we use, why, and how to get help."),
        ("terms.html", "02", "Consulta las condiciones", "Read the terms", "Petfy Premium, uso de la app y cuidados.", "Petfy Premium, app use, and pet care."),
        ("delete-account.html", "03", "Elimina tu cuenta", "Delete your account", "Pasos desde la app y cómo cancelar Premium.", "Steps in the app and how to cancel Premium."),
    ]
    path_html = "".join(
        f'''<a class="path-row" href="./{href}">
          <span class="path-num">{num}</span>
          <span class="path-text"><strong>{localized(es, en)}</strong><small>{localized(desc_es, desc_en)}</small></span>
          <span class="path-arrow">{svg_arrow()}</span>
        </a>'''
        for href, num, es, en, desc_es, desc_en in paths
    )
    documents = [
        ("ai-notice.html", "Petfy AI", "Petfy AI", "Consentimiento, contexto y límites", "Consent, context, and limitations"),
        ("dmca.html", "Derechos de autor", "Copyright", "Cómo comunicar una posible infracción", "How to report a possible infringement"),
    ]
    document_html = "".join(
        f'''<a class="document-row" href="./{href}"><span><strong>{localized(es, en)}</strong><small>{localized(desc_es, desc_en)}</small></span>{svg_arrow()}</a>'''
        for href, es, en, desc_es, desc_en in documents
    )
    body = f'''
    <section class="home-hero outer">
      <div class="hero-copy">
        <div class="hero-signature"><span class="signature-line"></span> Petfy <span class="signature-cross">×</span> Arvilo Labs</div>
        <h1>{localized('Cuidar también es <em>tenerlo todo claro.</em>', 'Caring also means <em>having clarity.</em>')}</h1>
        <p>{localized('Petfy reúne la vida de tus mascotas en un solo lugar. Este es el espacio para conocer la app, entender tus datos y encontrar ayuda cuando la necesites.', 'Petfy brings your pets’ everyday life together in one place. Here you can explore the app, understand your data, and find help when you need it.')}</p>
        <div class="hero-actions">
          <a class="button button-primary" href="#documents">{localized('Explorar documentos', 'Explore documents')}{svg_arrow()}</a>
          <a class="button button-quiet" href="./support.html">{localized('Necesito ayuda', 'I need help')}</a>
        </div>
      </div>
      <div class="hero-art"><img src="./assets/petfy-guide.png" alt="" width="520" height="520" /><span>{localized('Para cada mascota, en cada etapa.', 'For every pet, at every stage.')}</span></div>
    </section>
    <section class="intro-band outer" id="about">
      <div><span class="eyeline">{localized('Conoce Petfy', 'Meet Petfy')}</span><h2>{localized('Más orden. Más tiempo para estar juntos.', 'Less clutter. More time together.')}</h2></div>
      <p>{localized('Organiza perfiles, vacunas, alimentación, recordatorios y documentos de tus mascotas. Encuentra veterinarias cercanas y, si eliges Premium, usa funciones adicionales como Petfy AI y reportes PDF.', 'Organize pet profiles, vaccines, feeding, reminders, and documents. Find nearby vets and, if you choose Premium, use additional features such as Petfy AI and PDF reports.')}</p>
    </section>
    <section class="journeys outer" id="documents" aria-labelledby="journeys-title">
      <div class="section-heading"><span class="eyeline">{localized('Encuentra lo que necesitas', 'Find what you need')}</span><h2 id="journeys-title">{localized('Tres caminos. Una respuesta clara.', 'Three paths. A clear answer.')}</h2><p>{localized('Las páginas jurídicas revisadas aún son borradores; te mostramos exactamente qué falta validar.', 'The revised legal pages are still drafts; we show exactly what remains to validate.')}</p></div>
      <div class="path-list">{path_html}</div>
    </section>
    <section class="support-feature outer" aria-labelledby="support-title">
      <div class="support-symbol" aria-hidden="true">?</div>
      <div><span class="eyeline">{localized('Estamos aquí', 'We are here')}</span><h2 id="support-title">{localized('Si algo no está claro, hablemos.', 'If something is unclear, let’s talk.')}</h2><p>{localized('Problemas de acceso, compras, datos o una pregunta sobre Petfy: escribe al correo público de Arvilo Labs.', 'Account, purchase, data, or Petfy questions: reach Arvilo Labs at its public email.')}</p></div>
      <a class="button button-light" href="./support.html">{localized('Ir a ayuda', 'Go to support')}{svg_arrow()}</a>
    </section>
    <section class="more-documents outer" aria-labelledby="more-documents-title"><div><span class="eyeline">{localized('Más información', 'More information')}</span><h2 id="more-documents-title">{localized('Conoce cada detalle', 'Explore the details')}</h2></div><div>{document_html}</div></section>
    '''
    return page_shell("Home", "Petfy by Arvilo Labs: app, support, privacy, terms, and account deletion.", body, "home", "Inicio")


def support_page() -> str:
    body = f'''
    <div class="page-intro outer"><a class="breadcrumb" href="./index.html">{localized('Inicio', 'Home')}</a><span class="breadcrumb-sep">/</span><span>{localized('Ayuda', 'Support')}</span><h1>{localized('Ayuda que llega a una persona.', 'Support that reaches a person.')}</h1><p>{localized('Escríbenos sobre Petfy y te orientaremos con la cuenta, los datos y las compras. Este es el canal público de Arvilo Labs.', 'Write to us about Petfy and we will help with your account, data, and purchases. This is the public Arvilo Labs contact channel.')}</p></div>
    <section class="support-layout outer">
      <div class="contact-panel"><span class="eyeline">{localized('Contacto directo', 'Direct contact')}</span><h2>arvilolabs@gmail.com</h2><p>{localized('Para ayudarnos a encontrar tu caso, escribe desde el correo vinculado a tu cuenta si se trata de acceso, datos o Premium.', 'For account, data, or Premium issues, email us from the address linked to your account so we can find your case.')}</p><a class="button button-primary" href="mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Support" data-href-es="mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Ayuda" data-href-en="mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Support">{localized('Escribir un correo', 'Send an email')}{svg_arrow()}</a></div>
      <div class="support-topics">
        <h2>{localized('Antes de escribir', 'Before you write')}</h2>
        <div class="topic"><strong>{localized('Cuenta y acceso', 'Account and sign-in')}</strong><p>{localized('Cuéntanos qué método usas (Apple, Google o correo) y qué mensaje aparece. Nunca envíes tu contraseña.', 'Tell us whether you use Apple, Google, or email and what message appears. Never send your password.')}</p></div>
        <div class="topic"><strong>{localized('Premium y pagos', 'Premium and payments')}</strong><p>{localized('Usa «Restaurar compras» dentro de Petfy. Para cambiar o cancelar una suscripción, abre las <a href="https://apps.apple.com/account/subscriptions">Suscripciones de Apple</a>. Apple gestiona los reembolsos.', 'Use “Restore purchases” inside Petfy. To change or cancel a subscription, open <a href="https://apps.apple.com/account/subscriptions">Apple Subscriptions</a>. Apple handles refunds.')}</p></div>
        <div class="topic"><strong>{localized('Privacidad y eliminación', 'Privacy and deletion')}</strong><p>{localized('Puedes <a href="./delete-account.html">eliminar tu cuenta</a> en la app. Si no tienes acceso, escríbenos desde el correo asociado. Para consultas sobre datos, lee primero la <a href="./privacy.html">página de privacidad</a>.', 'You can <a href="./delete-account.html">delete your account</a> in the app. If you cannot sign in, email us from the linked address. For data questions, read the <a href="./privacy.html">privacy page</a> first.')}</p></div>
      </div>
    </section>
    <section class="support-note outer"><strong>{localized('Tu seguridad importa', 'Your security matters')}</strong><p>{localized('No incluyas contraseñas, números de tarjeta o documentos de identidad en el primer mensaje. Podemos pedir una verificación segura si tu solicitud afecta datos de una cuenta.', 'Do not include passwords, card numbers, or government IDs in the first message. We may ask for secure verification if your request affects account data.')}</p></section>
    '''
    return page_shell("Support", "Contact Arvilo Labs for Petfy account, privacy, and subscription support.", body, "support", "Ayuda")


def legal_page(key: str) -> str:
    data = PAGES[key]
    toc = "".join(
        f'<a href="#{section_id}">{localized(escape(title["es"]), escape(title["en"]))}</a>'
        for section_id, title, _ in data["sections"]
    )
    sections = "".join(
        f'''<section id="{section_id}" class="legal-section"><h2>{localized(escape(title['es']), escape(title['en']))}</h2>{localized(body['es'], body['en'], 'div')}</section>'''
        for section_id, title, body in data["sections"]
    )
    body = f'''
    <div class="page-intro outer legal-intro"><a class="breadcrumb" href="./index.html">{localized('Inicio', 'Home')}</a><span class="breadcrumb-sep">/</span><span>{localized('Documentos', 'Documents')}</span><h1>{localized(escape(data['title']['es']), escape(data['title']['en']))}</h1><p>{localized(escape(data['summary']['es']), escape(data['summary']['en']))}</p></div>
    <div class="legal-layout outer">
      <aside class="legal-toc" aria-label="On this page"><strong>{localized('En esta página', 'On this page')}</strong><nav>{toc}</nav><a class="toc-help" href="./support.html">{localized('¿Necesitas ayuda?', 'Need help?')}{svg_arrow()}</a></aside>
      <article class="legal-prose">{draft_notice()}{sections}<div class="end-panel"><strong>{localized('¿Queda alguna pregunta?', 'Still have a question?')}</strong><p>{localized('Escríbenos y revisaremos tu caso.', 'Email us and we will look into it.')}</p><a href="./support.html">{localized('Ver canales de ayuda', 'See support options')}{svg_arrow()}</a></div></article>
    </div>'''
    return page_shell(data["title"]["en"], data["summary"]["en"], body, "legal", data["title"]["es"])


def main() -> None:
    (ROOT / "index.html").write_text(home_page(), encoding="utf-8")
    (ROOT / "support.html").write_text(support_page(), encoding="utf-8")
    for key, data in PAGES.items():
        (ROOT / data["file"]).write_text(legal_page(key), encoding="utf-8")


if __name__ == "__main__":
    main()
