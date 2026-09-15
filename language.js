(function () {
  "use strict";
  const STORAGE_KEY = "petfySiteLanguage";
  const supported = new Set(["es", "en"]);

  function storedLanguage() {
    try { return window.localStorage.getItem(STORAGE_KEY); }
    catch (_) { return null; }
  }

  function initialLanguage() {
    const requested = new URLSearchParams(window.location.search).get("lang");
    if (supported.has(requested)) return requested;
    const stored = storedLanguage();
    if (supported.has(stored)) return stored;
    const browser = (navigator.language || "en").slice(0, 2).toLowerCase();
    return supported.has(browser) ? browser : "en";
  }

  function setLanguage(language) {
    const next = supported.has(language) ? language : "en";
    document.documentElement.lang = next;
    document.documentElement.dataset.language = next;
    try { window.localStorage.setItem(STORAGE_KEY, next); } catch (_) { /* Optional preference. */ }

    const title = document.querySelector("title[data-title-es]");
    if (title) document.title = title.dataset[next === "es" ? "titleEs" : "titleEn"];
    const group = document.querySelector(".language-switcher");
    if (group) group.setAttribute("aria-label", next === "es" ? "Idioma" : "Language");
    const navigation = document.querySelector(".primary-nav");
    if (navigation) navigation.setAttribute("aria-label", next === "es" ? "Navegación principal" : "Main navigation");
    const footer = document.querySelector(".site-footer nav");
    if (footer) footer.setAttribute("aria-label", next === "es" ? "Navegación del pie" : "Footer navigation");
    const toc = document.querySelector(".legal-toc");
    if (toc) toc.setAttribute("aria-label", next === "es" ? "En esta página" : "On this page");

    document.querySelectorAll("[data-href-es]").forEach((link) => {
      link.setAttribute("href", link.dataset[next === "es" ? "hrefEs" : "hrefEn"]);
    });

    document.querySelectorAll("[data-language-button]").forEach((button) => {
      const active = button.dataset.languageButton === next;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    setLanguage(initialLanguage());
    document.querySelectorAll("[data-language-button]").forEach((button) => {
      button.addEventListener("click", () => setLanguage(button.dataset.languageButton));
    });
  });
})();
