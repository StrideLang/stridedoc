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
│   │   └── systems-and-domains.md
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

The website is 100% statically generated and hosted for **free** on **GitHub Pages** using GitHub Actions (zero external servers or paid services required).

### One-Time Setup in GitHub Repository

1. Open your repository on GitHub.
2. Navigate to **Settings** &rarr; **Pages** (in the left sidebar).
3. Under **Build and deployment** &rarr; **Source**, select **GitHub Actions**.

### Automated CI/CD

Whenever changes are pushed to `main` (or `master`), the workflow in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) automatically:
1. Checks out the repository and installs dependencies with `npm ci`.
2. Compiles the static site and pre-builds the client-side search index with `npm run docs:build`.
3. Publishes the site directly to GitHub Pages at:
   ```text
   https://<username-or-org>.github.io/stridedoc/
   ```

### Custom Domain (Optional)

To host the documentation under a custom domain (e.g. `docs.stridelang.org` or `stridelang.org`):
1. In `docs/.vitepress/config.mts`, change `base: "/stridedoc/"` to `base: "/"`.
2. In GitHub repository **Settings** &rarr; **Pages**, enter your custom domain under **Custom domain** and enable **Enforce HTTPS** (free SSL certificate is provisioned automatically via Let's Encrypt).

---

## License

Released under the 3-Clause BSD License.
