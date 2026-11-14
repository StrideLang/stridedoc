import { defineConfig } from 'vitepress';
import { withMermaid } from 'vitepress-plugin-mermaid';
import fs from 'node:fs';
import path from 'node:path';

// Load Stride TextMate Grammar
const grammarPath = path.resolve(__dirname, '../grammars/stride.tmLanguage.json');
let strideGrammar: any = null;
if (fs.existsSync(grammarPath)) {
  strideGrammar = JSON.parse(fs.readFileSync(grammarPath, 'utf-8'));
}

// Load Auto-generated Reference Sidebar
import referenceCategories from './sidebar-reference.json';

const docSidebar = [
  {
    text: 'Guides',
    items: [
      { text: 'Design Rationale', link: '/learn/why-stride' },
      { text: 'Getting Started', link: '/learn/getting-started' },
      { text: 'Language Tour', link: '/learn/language-tour' }
    ]
  },
  {
    text: 'Architecture',
    items: [
      { text: 'Systems, Frameworks & Domains', link: '/learn/systems-and-domains' }
    ]
  },
  {
    text: 'Reference',
    items: [
      { text: 'Standard Library Overview', link: '/reference/library/' },
      { text: 'Symbol Index (A–Z)', link: '/reference/library/symbols' },
      ...referenceCategories
    ]
  }
];

export default withMermaid(
  defineConfig({
    title: "Stride",
    description: "A domain-specific programming language for declarative dataflow streams, finite state machines, and multi-rate embedded systems",
    base: "/stridedoc/", // Ready for GitHub Pages deployment under https://<org>.github.io/stridedoc/

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/stridedoc/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#18181b' }],
    ['meta', { name: 'og:title', content: 'The Stride Programming Language' }],
    ['meta', { name: 'og:description', content: 'A domain-specific programming language for declarative dataflow streams, finite state machines, and multi-rate embedded systems.' }]
  ],

  markdown: {
    math: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    },
    languages: strideGrammar ? [
      {
        ...strideGrammar,
        name: 'stride',
        aliases: ['strd']
      }
    ] : []
  },

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'Stride',

    nav: [
      { text: 'Documentation', link: '/learn/getting-started', activeMatch: '^/(learn|reference)/' },
      {
        text: 'Ecosystem',
        items: [
          { text: 'Toolchain (stridelang)', link: 'https://github.com/StrideLang/stridelang' },
          { text: 'VS Code Extension', link: 'https://github.com/StrideLang/vscode-stride-lang' },
          { text: 'Core Runtime (strideroot)', link: 'https://github.com/StrideLang/strideroot' }
        ]
      }
    ],

    sidebar: {
      '/learn/': docSidebar,
      '/reference/': docSidebar
    },

    search: {
      provider: 'local'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/StrideLang/Stride' }
    ],

    footer: {
      message: 'Released under the 3-Clause BSD License.',
      copyright: 'Copyright © 2017-present The Regents of the University of California & Stride Contributors.'
    }
  }
}));
