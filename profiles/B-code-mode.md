```typescript
// profile.ts — last deployed: today
import { Engineer, Contact } from "./types";

export const yarooq: Engineer = {
  name: "Yarooq Anwar",
  title: "Software Engineer",

  builds: {
    backend:  ["llm chat engines", "tts streaming", "REST APIs", "microservices"],
    frontend: ["next.js", "react", "react native", "markdown workspaces"],
    infra:    ["docker", "linux", "release automation (ios + android)"],
    ai:       ["streaming inference", "embeddable agents", "workspace integrations"],
  },

  stack: {
    languages: ["typescript", "python", "go", "sql"],
    runtime:   ["node.js", "nest.js", "fastapi"],
    storage:   ["postgres", "mongodb"],
  },

  shipped: [
    { name: "headless-curator",   desc: "automated content pipeline",      stack: ["python", "next.js", "docker"] },
    { name: "llama2-inference-ui", desc: "domain-specific llm interface",  stack: ["python", "fastapi"] },
    { name: "tabstack",            desc: "chromium tab memory saver",      link: "chrome web store" },
    { name: "keyloom",             desc: "wip — ask me about it" },
  ],

  currentFocus: ["llm-agent-toolkit (open source)", "go", "systems design"],

  reachableAt: {
    email:    "yarooq1@gmail.com",
    linkedin: "linkedin.com/in/YarooqAnwar",
    guestbook: "github.com/YarooqH/YarooqH/issues",
  } satisfies Contact,

  availability: "open to interesting problems · remote-friendly" as const,
};

export default yarooq;
```

<!-- run it: npx tsx profile.ts → expect output: a useful human -->
