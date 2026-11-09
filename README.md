# Stride Documentation & Website (`stridedoc`)

This repository contains the official website, documentation, and the **`stride-docgen`** automated reference extractor for the [Stride programming language](https://github.com/StrideLang/Stride).

The site is built with [VitePress](https://vitepress.dev/) and deployed automatically to **GitHub Pages**.

---

## Repository Structure

```text
stridedoc/
├── .github/workflows/
│   └── deploy.yml              # GitHub Pages CI/CD workflow
├── scripts/
│   └── docgen.py               # stride-docgen: Automatic metadata & API extractor
├── docs/
│   ├── .vitepress/
│   │   ├── config.mts          # VitePress config (Shiki Stride grammar, search, nav)
│   │   └── theme/              # Custom brand styling & badge CSS
│   ├── grammars/
│   │   └── stride.tmLanguage.json # Official Stride syntax grammar
│   ├── public/
│   │   └── logo.svg            # Stride vector logo
│   ├── index.md                # Marketing Landing Page
│   ├── learn/                  # Narrative guides & tutorials
│   │   ├── why-stride.md
│   │   ├── getting-started.md
│   │   ├── language-tour.md
│   │   ├── systems-and-domains.md
│   │   └── audio-dsp.md
│   └── reference/              # Extracted Standard Library documentation
│       └── library/
├── package.json
└── README.md
```

---

## Development Workflow

### 1. Extract API Reference Docs
To re-extract the latest standard library definitions from `$STRIDEROOT`:

```bash
npm run docs:extract
# or manually:
python scripts/docgen.py --strideroot ../Stride/strideroot --output docs
```

This scans `strideroot/library`, extracts module signatures, `meta:` docstrings, ports, and default values, and automatically generates:
- Markdown pages for all modules under `docs/reference/library/`
- VitePress sidebar configuration at `docs/.vitepress/sidebar-reference.json`

### 2. Local Preview & Development
Start the local VitePress development server with live reload:

```bash
npm run docs:dev
```

Open `http://localhost:5173/stridedoc/` in your browser.

### 3. Production Build
To test the production build locally:

```bash
npm run docs:build
npm run docs:preview
```

---

## Deployment

Pushes to `main` (or `master`) automatically trigger the GitHub Actions workflow in `.github/workflows/deploy.yml`, building and publishing the static site directly to **GitHub Pages**.

---

## License

Released under the 3-Clause BSD License.
