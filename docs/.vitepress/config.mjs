const skills = [
  {
    text: "spdd-orchestrator",
    link: "/skills/spdd-orchestrator"
  },
  {
    text: "spdd-story",
    link: "/skills/spdd-story"
  },
  {
    text: "spdd-analysis",
    link: "/skills/spdd-analysis"
  },
  {
    text: "spdd-reasons-canvas",
    link: "/skills/spdd-reasons-canvas"
  },
  {
    text: "spdd-generate",
    link: "/skills/spdd-generate"
  },
  {
    text: "spdd-prompt-update",
    link: "/skills/spdd-prompt-update"
  },
  {
    text: "spdd-sync",
    link: "/skills/spdd-sync"
  },
  {
    text: "spdd-api-test",
    link: "/skills/spdd-api-test"
  }
];

const workflowSidebar = [
  {
    text: "Workflow Overview",
    link: "/workflow/"
  },
  {
    text: "Orchestrator Modes",
    link: "/workflow/orchestrator-modes"
  },
  {
    text: "Phase Handoffs",
    link: "/workflow/phase-handoffs"
  }
];

export default {
  title: "SpecArk",
  description: "Developer documentation for the SpecArk Codex plugin and SPDD workflow",
  base: "/SpecArk/",
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    logo: {
      text: "SpecArk"
    },
    nav: [
      { text: "Guide", link: "/getting-started" },
      { text: "Workflow", link: "/workflow/" },
      { text: "Skills", link: "/skills/" },
      { text: "References", link: "/references/" }
    ],
    search: {
      provider: "local"
    },
    sidebar: {
      "/": [
        {
          text: "Overview",
          items: [
            { text: "What Is SpecArk?", link: "/" },
            { text: "Getting Started", link: "/getting-started" },
            { text: "Installation", link: "/installation" },
            { text: "Plugin Layout", link: "/plugin-layout" },
            { text: "Limitations", link: "/limitations" },
            { text: "Next Steps", link: "/next-steps" },
            { text: "Release Notes", link: "/release-notes" },
            { text: "Maintainer Notes", link: "/maintainer-notes" },
            { text: "Contributing", link: "/contributing" }
          ]
        },
        {
          text: "Workflow",
          items: workflowSidebar
        },
        {
          text: "Skills",
          items: [
            { text: "Skill Index", link: "/skills/" },
            ...skills
          ]
        },
        {
          text: "References",
          items: [
            { text: "Reference Index", link: "/references/" },
            { text: "Orchestrator Contract", link: "/references/orchestrator-contract" },
            { text: "Skill Authoring Guide", link: "/references/high-quality-skill-authoring" },
            { text: "REASONS Canvas Notes", link: "/references/reasons-canvas" }
          ]
        }
      ]
    },
    footer: {
      message: "Structured Prompt-Driven Development for Codex plugin workflows.",
      copyright: "SpecArk"
    },
    outline: {
      level: [2, 3]
    }
  }
};
