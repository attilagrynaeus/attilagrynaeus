# Profile maintenance

## One canonical portfolio

`README.md` is the complete public portfolio: positioning, three case studies, diagrams, code samples, stack and contact. The two case-study documents are compatibility links to the corresponding README sections. Do not fork the stories into parallel copies.

The approved contact is `attila.grynaeus@gmail.com`. Every email CTA must use `mailto:attila.grynaeus@gmail.com`; keep the address visible and copyable as text. Link validation does not prove mailbox delivery.

## Assets and layout

- `assets/header.svg` and `assets/header-mobile.svg`: compact professional introduction, with searchable text repeated in Markdown.
- `assets/system.svg` and `assets/system-mobile.svg`: the same logical multiplayer architecture at desktop and mobile widths. The direct browser-to-Spring path is mandatory on both. PostgreSQL persistence and Redis routing remain separate; the gateway is application infrastructure, not an AWS API Gateway claim.
- `assets/velyndra-architecture*.svg`: the read-only AI integration and its business-data boundary, shown inline.
- All six are original, self-contained SVGs with original schematic icons, descriptive titles, explicit viewBoxes, system fonts and no external resources, scripts or embedded fonts.
- The supplied light architecture reference informs spacing, icon-led cards and hierarchy; it does not establish a deployed AWS topology.
- Generated `profile/` graphics and their refresh workflow remain available but are not the main portfolio evidence. Existing unused decorative assets are retained to avoid unrelated deletions.

## Content and evidence

Professional experience and certifications retain the owner-approved profile wording. The AI engagement is anonymized under a fictional client alias. SHARDFORGE FARM is a public codename for a private engineering/game project; never publish the original brand, private source links, internal endpoints, credentials or unpublished game assets.

Describe observed implementation, design intent and executed test evidence distinctly. A test contract is not proof that a release passed. Do not infer throughput, latency, coverage, active users or business impact from repository size, test-file counts or CI badges. New numbers require a dated, reproducible measurement and an explicit environment.

Keep outcomes specific and attribution accurate: the enterprise modernization work is a contribution, not a claim to have led the whole program. Target roles are presented as interests, not invented job titles.

## Validation

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tools/validate_profile.py
```

Check desktop and mobile layouts, both color schemes, reduced motion, local anchors, contact targets and responsive image selection. Inspect the actual rendered diagrams for clipped text and incorrect edges; XML checks cannot prove the drawing is correct. A local GitHub-like Markdown preview is useful but is not the live GitHub page.

Existing Actions pins and generated-graphics workflows are unchanged. Their repository token must not be widened to private repositories for vanity statistics.

## Account-level alignment (manual settings)

The repository does not own GitHub bio/pins, LinkedIn or a CV. Suggested GitHub bio:

> Software Architect | Java/Spring, Distributed Systems & AI/MCP | 27+ years | Hands-on delivery from design to deployment.

Suggested public pins: PrompTee and AI Test Generator. Retain their proof-of-concept or project status; pinning is not a production-readiness claim.
