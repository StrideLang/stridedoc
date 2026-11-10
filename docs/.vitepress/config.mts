import { defineConfig } from 'vitepress';
import fs from 'node:fs';
import path from 'node:path';

// Load Stride TextMate Grammar
const grammarPath = path.resolve(__dirname, '../grammars/stride.tmLanguage.json');
let strideGrammar: any = null;
if (fs.existsSync(grammarPath)) {
  strideGrammar = JSON.parse(fs.readFileSync(grammarPath, 'utf-8'));
}

// Load Auto-generated Reference Sidebar
const sidebarRefPath = path.resolve(__dirname, 'sidebar-reference.json');
let referenceCategories: any[] = [];
if (fs.existsSync(sidebarRefPath)) {
  try {
    referenceCategories = JSON.parse(fs.readFileSync(sidebarRefPath, 'utf-8'));
  } catch (e) {
    console.error("Failed to parse sidebar-reference.json", e);
  }
}

export default defineConfig({
  title: "Stride",
  description: "A domain-specific programming language for dataflow streams, real-time digital signal processing, and embedded systems",
  base: "/stridedoc/", // Ready for GitHub Pages deployment under https://<org>.github.io/stridedoc/

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/stridedoc/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#0284c7' }],
    ['meta', { name: 'og:title', content: 'The Stride Programming Language' }],
    ['meta', { name: 'og:description', content: 'A domain-specific programming language for dataflow streams, real-time digital signal processing, and embedded systems.' }]
  ],

  markdown: {
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
      { text: 'Documentation', link: '/learn/getting-started' },
      { text: 'Language Tour', link: '/learn/language-tour' },
      { text: 'Reference', link: '/reference/library/' },
      { text: 'Architecture', link: '/learn/systems-and-domains' },
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
      '/learn/': [
        {
          text: 'Introduction',
          items: [
            { text: 'Design Rationale', link: '/learn/why-stride' },
            { text: 'Getting Started', link: '/learn/getting-started' },
            { text: 'Language Tour', link: '/learn/language-tour' }
          ]
        },
        {
          text: 'Architecture & Specifications',
          items: [
            { text: 'Systems, Frameworks & Domains', link: '/learn/systems-and-domains' },
            { text: 'Digital Signal Processing', link: '/learn/audio-dsp' }
          ]
        }
      ],
      '/reference/': [
        {
          text: 'Standard Library',
          items: [
            { text: 'Overview & Namespaces', link: '/reference/library/' }
          ]
        },
        ...referenceCategories
      ]
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
});
