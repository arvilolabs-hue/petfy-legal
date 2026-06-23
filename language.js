(function () {
  const STORAGE_KEY = "petfyLegalLanguage";
  const supported = new Set(["en", "es"]);

  function getInitialLanguage() {
    const stored = window.localStorage.getItem(STORAGE_KEY);
    if (supported.has(stored)) {
      return stored;
    }

    const browserLanguage = (navigator.language || "en").slice(0, 2).toLowerCase();
    return supported.has(browserLanguage) ? browserLanguage : "en";
  }

  function setLanguage(language) {
    const nextLanguage = supported.has(language) ? language : "en";
    document.documentElement.dataset.language = nextLanguage;
    document.documentElement.lang = nextLanguage;
    window.localStorage.setItem(STORAGE_KEY, nextLanguage);

    document.querySelectorAll("[data-language-button]").forEach((button) => {
      const isActive = button.getAttribute("data-language-button") === nextLanguage;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });
  }

  window.addEventListener("DOMContentLoaded", function () {
    setLanguage(getInitialLanguage());

    document.querySelectorAll("[data-language-button]").forEach((button) => {
      button.addEventListener("click", function () {
        setLanguage(button.getAttribute("data-language-button"));
      });
    });
  });
})();
