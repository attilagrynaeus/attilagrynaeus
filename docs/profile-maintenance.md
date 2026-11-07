# Profile maintenance

The profile is a native GitHub README, not a separately hosted application. SHARDFORGE FARM is a public engineering codename; the original game source remains private.

## Editing

- `README.md`: public copy, project links and section order.
- `assets/header*.svg`: original responsive hero panels with restrained animated cyan/violet filaments. No embedded fonts or JavaScript; motion respects reduced-motion settings.
- `assets/cta-*.svg`: small visual labels wrapped by real README links; the SVGs themselves contain no interactive controls.
- `assets/system*.svg`: original simplified system diagram used only by the engineering notes. It is not a screenshot or performance claim.
- `docs/shardforge-farm.md`: public architectural overview only. Keep private source, internal endpoints, customer information and production assets out.
- `config/profile-3d.json`: the two contribution-calendar palettes. The calendar is intentionally static to avoid competing with the animated header.

Run from the repository root:

```sh
python3 -m unittest discover -s tests -p test_profile.py
python3 tools/validate_profile.py
```

Check the rendered README at desktop and mobile widths, in dark and light mode. Verify the hero text, both linked CTA labels and mobile art at narrow widths. The light-trail animation must not hide text when reduced motion is enabled. XML validation alone cannot catch clipping.

## Generated graphics

`Refresh profile visuals` runs daily at 04:37 UTC, on relevant pushes, and manually from Actions. It generates the six SVG files under `profile/`. The first generation was run successfully on the review branch; these are not placeholder cards.

The workflow uses the repository-scoped `GITHUB_TOKEN`, not a personal token. Do not widen its access to private repositories just to improve a profile statistic. It stages only the six generated outputs and never force-pushes. Data-fetch or SVG-validation failures stop the update instead of publishing an error card.

Contribution counts reflect the activity GitHub exposes to the generator. They are not a complete record of a professional career. Repository cards are linked code samples, not endorsements or claims of production readiness.

## Sources and attribution

Visual techniques were studied from [Om Lahore's profile](https://github.com/omlahore/omlahore). The header, wording and system diagram here are original; no personal achievements or product artwork were copied.

Generated graphics use [GitHub Profile 3D Contrib](https://github.com/yoshi389111/github-profile-3d-contrib), [GitHub Readme Stats Action](https://github.com/stats-organization/github-readme-stats-action), and [Skill Icons](https://github.com/tandpfun/skill-icons). The top-level GitHub Actions references are pinned to complete commit SHAs. Review upstream updates before changing those pins.

Experience and certification wording comes from the previously published profile. Public project descriptions are grounded in their repositories; the Java validator and React test are linked directly from the profile. Reconfirm role, experience and maintenance-status wording when updating the profile.
