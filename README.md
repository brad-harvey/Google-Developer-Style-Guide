# Google Developer Style Guide — Extracted & Condensed Reference

A local, reorganized reference derived from the [Google Developer Documentation Style Guide](https://developers.google.com/style).

## Structure

- **[`STYLE_GUIDE.md`](STYLE_GUIDE.md)** — start here. Master index and table of contents linking into the condensed section files.
- **[`guide/`](guide/)** — condensed, cross-linked section files (one per left-nav section), each combining that section's pages with working internal links.
- **[`pages/`](pages/)** — one file per original page, organized in a folder structure that mirrors the site's left-hand navigation. This is the raw extraction layer the condensed guide was built from.
- **`scripts/build_guide.py`** — regenerates `STYLE_GUIDE.md` and `guide/` from the contents of `pages/`.
- **[`.claude/skills/google-dev-style/`](.claude/skills/google-dev-style/SKILL.md)** — a Claude skill that distills this guide into actionable instructions, so Claude follows Google-style conventions when writing documentation or answering technical questions. `SKILL.md` holds the always-loaded rules; `references/` holds the full guide, loaded on demand.
- **`scripts/build_skill.py`** — regenerates the skill's `references/` from `guide/` and packages `dist/google-dev-style.skill` for upload to Claude. Run it after `build_guide.py`.

## Rebuilding the skill

```
uv run scripts/build_guide.py
uv run scripts/build_skill.py
```

The second command writes `dist/google-dev-style.skill` (ignored by git, since it's reproducible). Upload that file in Claude's skill settings to replace the installed version.

## Nature of the content

Page content here is paraphrased/condensed in our own words, organized under the same headings and structure as the source, rather than copied verbatim — this is meant as a practical internal reference, not a mirror of the site. For exact original wording, each entry links back to its source page.

The original guide is published by Google. Except as otherwise noted on its pages, its content is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and its code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

## Known gaps

None currently. The word list (`pages/02-key-resources/word-list.md`) covers the full A–Z glossary; entries were parsed directly from the page's HTML rather than through model summarization, to avoid the risk of invented guidance.
