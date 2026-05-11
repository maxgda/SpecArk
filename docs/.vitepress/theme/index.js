import DefaultTheme from "vitepress/theme";
import { h } from "vue";
import HeroAnimation from "./components/HeroAnimation.vue";
import Terminal from "./components/Terminal.vue";
import ArtifactFlow from "./components/ArtifactFlow.vue";
import "./custom.css";

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      "home-hero-image": () => h(HeroAnimation)
    });
  },
  enhanceApp({ app }) {
    app.component("Terminal", Terminal);
    app.component("ArtifactFlow", ArtifactFlow);
    app.component("HeroAnimation", HeroAnimation);
  }
};
