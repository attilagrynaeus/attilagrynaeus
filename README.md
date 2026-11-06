<div align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/header-mobile.svg" />
    <img src="assets/header.svg" width="100%" alt="Attila Grynaeus — Java and Spring engineer; software architecture and AI tools" />
  </picture>
  <img src="assets/typing.svg" width="480" alt="25+ years of building software." />
  <p>
    <a href="https://www.linkedin.com/in/attila-grynaeus">LinkedIn ↗</a> &nbsp; · &nbsp;
    <a href="https://mindjourneylabs.com">MindJourney Labs ↗</a> &nbsp; · &nbsp;
    <a href="mailto:attila@grynaeus.dev">Email ↗</a>
  </p>
</div>

I'm Attila, a **senior Java/Spring engineer** with **25+ years in enterprise software**. I work across backend design, delivery and the awkward bugs between services. I also lead and mentor engineers.

Alongside my enterprise work, I'm building a multiplayer farming game and experimenting with tools that make development less repetitive.

**Sun-certified:** Java Programmer (SCJP) · Business Component Developer (SCBCD)

## R.A.M. FARM

A multiplayer farming world I'm building. The interesting engineering problem isn't drawing a crop: it's making sure two players cannot harvest it twice, and that reconnecting doesn't bring old state back.

<a href="docs/ram-farm.md">
  <picture>
    <source media="(max-width: 900px)" srcset="assets/system-mobile.svg" />
    <img src="assets/system.svg" width="100%" alt="R.A.M. FARM architecture: browser clients, Node.js gameplay runtime, Java/Spring transactions and PostgreSQL persistence" />
  </picture>
</a>
<br />

The client handles input and presentation. The server validates shared actions; persistent inventory and ownership changes are transactional. Browser-driven gameplay tests exercise the same paths a player uses.

**[Read the engineering notes →](docs/ram-farm.md)**

<sub>Private project · In development</sub>

## Public code

<div align="center">
  <a href="https://github.com/attilagrynaeus/Promptee"><img src="profile/promptee.svg" width="395" alt="PrompTee public repository" /></a>
  <a href="https://github.com/attilagrynaeus/ai-test-generator"><img src="profile/ai-test-generator.svg" width="395" alt="AI Test Generator public Java demo repository" /></a>
</div>

**[PrompTee](https://github.com/attilagrynaeus/Promptee)** — A shared workspace for saving, finding and reusing prompts. React, Supabase and a serverless backend. [A small UI regression test](https://github.com/attilagrynaeus/Promptee/blob/main/src/__tests__/PromptCard.deleteConfirm.test.jsx).

**[AI Test Generator](https://github.com/attilagrynaeus/ai-test-generator)** — A Java/Spring experiment that turns API descriptions into JUnit test scaffolding. [Start with the input validator](https://github.com/attilagrynaeus/ai-test-generator/blob/main/server/src/main/java/com/ag/server/validation/ApiSpecValidator.java). A demo, not a maintained service.

Also: **[WildFly AI Assist](https://github.com/attilagrynaeus/troubleshoot-ai-assist)** connects application errors with relevant internal documentation using retrieval-augmented generation.

## Working stack

<p align="center">
  <img src="profile/stack.svg" width="440" alt="Java, Spring, PostgreSQL, Docker, Kubernetes, TypeScript, React and Python" />
</p>

Java and Spring are my core. Around them: PostgreSQL, containers, CI/CD and TypeScript. Python is useful for the AI tooling.

## GitHub activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile/activity-dark.svg" />
  <img src="profile/activity-light.svg" width="100%" alt="My actual GitHub contribution history, rendered as a 3D calendar" />
</picture>

<details>
  <summary>Activity details</summary>
  <br />
  <img src="profile/stats.svg" width="440" alt="GitHub activity statistics, generated from the GitHub API" />
</details>

<sub>Updated daily. Only activity exposed by GitHub is shown; private project details stay private.</sub>

---

I write at **[MindJourney Labs](https://mindjourneylabs.com)**. For a conversation about Java/Spring engineering, architecture or developer tooling: **[LinkedIn](https://www.linkedin.com/in/attila-grynaeus)** or **[attila@grynaeus.dev](mailto:attila@grynaeus.dev)**.
