# Introduction

## On this page

- [About this guide](#about-this-guide)
- [Highlights](#highlights)
- [Philosophy of this guide](#philosophy-of-this-guide)
- [What's new](#whats-new)

---

## About this guide

*Source: [https://developers.google.com/style](https://developers.google.com/style)*

# About this guide

This is Google's house style guide for developer documentation: a reference for keeping technical writing clear and consistent across projects. It targets people writing documentation for software developers.

## How to use it alongside other references

When guidance conflicts, follow this order:

1. Your own project's style guidelines (if any)
2. This guide
3. Third-party references, split by topic:
   - Spelling: Merriam-Webster.com
   - General (non-technical) style: *The Chicago Manual of Style*, 17th edition
   - Technical style: the *Microsoft Writing Style Guide*

Other style guides worth consulting: the Apple Style Guide, and Red Hat's supplementary style guide.

## Platform-specific annotations

Content that only applies to a specific platform is marked with a small logo — Android or Google Cloud — next to the relevant guidance.

## These are guidelines, not hard rules

The guide expects deviation when it serves the audience better, as long as you stay internally consistent once you do. It borrows Orwell's line that it's fine to break any of these rules sooner than write something outright barbarous.

## What's covered

The left navigation spans: the introduction and philosophy behind the guide, the word list and product-name reference, general writing principles (accessibility, inclusive language, tone, etc.), language/grammar rules, punctuation, formatting and document organization, linking conventions, guidance for documenting computer interfaces and code, HTML/CSS conventions, and naming conventions.

---

## Highlights

*Source: [https://developers.google.com/style/highlights](https://developers.google.com/style/highlights)*

# Highlights

A quick-reference summary of the guide's most load-bearing points, spanning tone, language, grammar, formatting, punctuation, organization, and imagery.

## Tone and content

- Be conversational and friendly, but not frivolous.
- Don't document unreleased/unannounced features.
- Write descriptive link text instead of "click here"-style generic phrases.
- Write for accessibility.
- Write with a global/international audience in mind.

## Language and grammar

- Use second person ("you"), not first-person plural ("we").
- Prefer active voice so it's clear who/what is performing an action.
- Follow American spelling and punctuation conventions.
- Put conditions before instructions in a sentence.
- Check the word list for specific term usage.

## Formatting, punctuation, and organization

- Use sentence case for titles and headings.
- Use numbered lists for sequential steps.
- Use bulleted lists for non-sequential items.
- Use description lists for term/definition-style pairs.
- Use the Oxford (serial) comma.
- Set code-related text in a monospace/code font.
- Bold UI element names.
- Write dates in an unambiguous format.

## Images

- Give every image meaningful alt text.
- Use high-resolution or vector images where possible.

---

## Philosophy of this guide

*Source: [https://developers.google.com/style/philosophy](https://developers.google.com/style/philosophy)*

# Philosophy of this guide

## Scope and intent

This guide records Google's *preferred* house style for the sake of internal consistency — it does not claim to define an industry standard, and it isn't a substitute for a general writing guide or other established style guides.

It favors being concise. It only explains the reasoning behind a rule when that reasoning is itself useful (often when it touches accessibility or localization) — not everywhere, because that would get repetitive and clutter pages that readers are scanning for a quick answer to a specific question.

## What it explicitly is not

- Not an industry standard.
- Not a competitor or replacement for other style guides.
- Not a complete guide to basic writing.
- Not legal advice.

## Disclaimers worth noting

- Guidance here doesn't constrain what changes Google itself may make to its own documentation.
- Following (or not following) this guide doesn't change a writer's underlying ethical and legal responsibilities in what they publish.
- The guide itself is expected to change over time.

## Where explanations do appear

When the "why" behind a rule is genuinely useful, it sometimes gets called out on the [What's new](../01-introduction/whats-new.md) page rather than cluttering the main rule pages.

---

## What's new

*Source: [https://developers.google.com/style/whats-new](https://developers.google.com/style/whats-new)*

# What's new

A running changelog of updates to the style guide since its public release in June 2017. Entries are chronological, most recent first. This file summarizes the changelog at a point in time (fetched 2026-08-19); see the source URL for the current list — a changelog like this is inherently a live document and will keep growing.

## Recent changes (most recent entries)

- **2026-07-07** — Softened guidance on inconsistent terminology/translation cost; cross-referenced optional procedure steps with headings guidance; clarified that inclusive-documentation guidance covers figurative language; updated custom heading-anchor guidance; added UI-element contextualization guidance; added word-list entry for "managed instance group (MIG)."
- **2026-04-07** — Clarified list-item punctuation consistency; added the "do the following" lead-in phrase for lists; clarified ordered-list usage and step-number referencing; consolidated italics guidance onto its own page; standardized "selected"/"not selected" checkbox terminology; added code-font guidance for IP addresses, port numbers, and package names; expanded pane/panel/section definitions; added the `.wasm` extension; reorganized abbreviation-introduction formatting; consolidated pluralization guidance; restructured global-audience writing guidance; expanded exclamation-mark guidance; created a dedicated mathematical-notation page; changed temperature-formatting guidance; added "AI" word-list entry; clarified "can" for permission vs. ability; distinguished "page" vs. "document"; expanded "style sheet"/"stylesheet" and compound-word guidance; expanded the "first class" entry; enhanced "like/such as/for example/for instance" entries; added Compute Engine instance-naming guidance.
- **2025-05-08** — Added a prescriptive-documentation page; simplified contractions and articles guidance; generalized future-features and jargon guidance; consolidated cross-references/linking guidance; added accessibility rationale against directional language; new word-list entries including "choose," "confidential," "sensitive," "image," "FHIR."
- **2025-01-17** — Consolidated spelling guidance into the word-list intro; extended dictionary-usage guidance; generalized code-sample indentation guidance; changed phone-number formatting; extended guidance against "i.e.," "e.g.," "etc."
- **2024-10-29** — Consolidated hyphen/closed-compound guidance; added "hotspot."
- **2024-08-15** — Added binary-vs-decimal unit distinction; corrected "kB" abbreviation; expanded figure-reference guidance; added "curl," "whitepaper," "long-running operation"; updated several networking/content-type terms.
- **2024-05-16** through **2024-01-22** — Added "generative AI" and "rehost"; clarified placeholder rendering and directional-language avoidance; cleaned up redundant word-list entries; changed code-snippet omission convention to comments instead of an ellipsis.

## Earlier history (2017–2023)

The changelog continues back to the guide's original public release on **2017-06-08**, covering hundreds of smaller entries: individual word-list additions/changes, page reorganizations (e.g., separate pages created over time for footnotes, third-party content, timeless documentation, units of measurement, filenames, semantic tagging), and terminology shifts (e.g., "GCP" → "Google Cloud," "command-line tool" → "CLI" for gcloud, "master/slave" → "active/standby" and similar inclusive-language substitutions). For the full, exact list of dated entries, see the source page directly — this history section is condensed here rather than reproduced entry-by-entry.

## Footer

- License: Creative Commons Attribution 4.0 (guide text); Apache 2.0 (code samples).

---
