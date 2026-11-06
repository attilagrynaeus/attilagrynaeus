<div align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/header-mobile.svg" />
    <img src="assets/header.svg" width="100%" alt="Hi, I'm Attila. Senior software engineer working in Java, Spring, developer tools and multiplayer systems." />
  </picture>
  <p>
    <a href="#selected-work"><img src="assets/cta-work.svg" width="176" alt="Explore my work" /></a>&nbsp;
    <a href="mailto:attila@grynaeus.dev"><img src="assets/cta-contact.svg" width="152" alt="Get in touch by email" /></a>
  </p>
  <p>
    <a href="https://www.linkedin.com/in/attila-grynaeus">LinkedIn</a> &nbsp;·&nbsp;
    <a href="https://mindjourneylabs.com">Writing</a> &nbsp;·&nbsp;
    <a href="#working-stack">Stack</a>
  </p>
</div>

I'm a **software architect and hands-on engineer with 27+ years in enterprise software**. Java, Spring and cloud systems are my foundation. Today, much of my work is in **LLM application architecture**: connecting AI agents to business APIs through well-defined, secure tools.

I've built production systems in event technology, retail/ERP, banking and public services. I care about clear contracts, tests, and services that people can actually operate.

**Sun certifications:** Java Programmer (SCJP) · Business Component Developer (SCBCD).

## Selected work

### Eventfrog — ChatGPT app and MCP integration (2026)

As Eventfrog's sole AI integration engineer, I designed, built and shipped its **public ChatGPT integration** end to end. I developed the MCP server and three typed tools for event categories, event search and event details, connected them through an API gateway and deployed the services on **Google Cloud Kubernetes**.

The challenge was making agent tool calls reliable: validated inputs, localized results, controlled access and responses grounded in Eventfrog data. The integration is live, not a concept demo.

**[Eventfrog in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6a3a779388f48191b85e9d2f28b8c95d)** · **[Official product information](https://eventfrog.de/en/help/organizer/boostprofits/promotion/ai-search.html)**

### R.A.M. FARM — multiplayer farming world

I'm building a multiplayer farming game. The difficult part isn't growing a crop on screen; it's making sure two players can't harvest the same crop twice, and that an old update cannot undo a newer one after reconnecting.

The game uses server-owned gameplay state, transactional persistence and browser-driven gameplay tests. It's an engineering project as much as a game.

**[Read the technical notes](docs/ram-farm.md)** · Private project, in development. No private source or gameplay screenshots are published here.

### Bison Schweiz AG — cloud pricing and ERP modernization

I built Spring Boot pricing services on **Azure and Kubernetes**, worked on REST and messaging integrations, and helped bring GitOps, automated testing and production observability into the delivery process.

### Public projects

<div align="center">
  <a href="https://github.com/attilagrynaeus/Promptee"><img src="profile/promptee.svg" width="395" alt="PrompTee GitHub repository card, generated from live repository data" /></a>
  <a href="https://github.com/attilagrynaeus/ai-test-generator"><img src="profile/ai-test-generator.svg" width="395" alt="AI Test Generator GitHub repository card, generated from live repository data" /></a>
</div>

**[PrompTee](https://github.com/attilagrynaeus/Promptee)** — A collaborative prompt workspace built with React, Supabase and serverless functions. [Example: UI regression test](https://github.com/attilagrynaeus/Promptee/blob/main/src/__tests__/PromptCard.deleteConfirm.test.jsx).

**[AI Test Generator](https://github.com/attilagrynaeus/ai-test-generator)** — A Java/Spring proof of concept that generates JUnit test scaffolding from API descriptions. [Example: input validator](https://github.com/attilagrynaeus/ai-test-generator/blob/main/server/src/main/java/com/ag/server/validation/ApiSpecValidator.java). This is a demo, not a maintained product.

**[WildFly AI Assist](https://github.com/attilagrynaeus/troubleshoot-ai-assist)** — An experiment using internal documentation to suggest fixes for WildFly application errors.

## Working stack

<div align="center">
  <img src="profile/stack.svg" width="440" alt="Java, Spring, PostgreSQL, Docker, Kubernetes, TypeScript, React, Python" />
</div>

**AI and LLM systems:** MCP, ChatGPT Apps, tool/function calling, typed tool schemas, agent workflows, RAG and secure API access. I test tool outcomes and failure cases, not just whether a model produces fluent text.

**Backend and cloud:** Java 17–25, Spring Boot, PostgreSQL, REST/OpenAPI, Kafka, Redis, Node.js, TypeScript, Kubernetes, Docker, Azure, Google Cloud, GitOps and OpenTelemetry.

## GitHub activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile/activity-dark.svg" />
  <img src="profile/activity-light.svg" width="100%" alt="3D calendar generated from GitHub's actual contribution history" />
</picture>

<details>
  <summary>Detailed GitHub statistics</summary>
  <p><img src="profile/stats.svg" width="440" alt="GitHub activity statistics based on API data" /></p>
</details>

<sub>Generated daily from GitHub data. Private repository names and source remain private.</sub>

---

I'm interested in engineering teams building reliable platforms and practical AI-enabled products — beyond prototypes and chatbot demos. **[Connect on LinkedIn](https://www.linkedin.com/in/attila-grynaeus)** or **[send me an email](mailto:attila@grynaeus.dev)**.
