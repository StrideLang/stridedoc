import DefaultTheme from 'vitepress/theme';
// @ts-ignore
import Mermaid from 'vitepress-plugin-mermaid/Mermaid.vue';
import './custom.css';

export default {
  extends: DefaultTheme,
  enhanceApp({ app }: { app: any }) {
    app.component('Mermaid', Mermaid);
  }
};
