---
title: "Timeless documentation"
source: "https://developers.google.com/style/timeless-documentation"
section: "General principles"
---

# Timeless documentation

## Core idea

Write about the current state of the product, not about how it got there or where it's going — avoid language that ties the text to a specific point in time, or that assumes the reader knows the product's history.

## Why

- Less maintenance burden — the doc doesn't go stale just because time passes.
- Doesn't assume the reader is familiar with a previous version.
- Especially important for reference/technical docs meant to stay accurate for a long time.

## Where time-based language is fine

- Blog posts and announcements.
- Release notes.
- Procedural steps that describe an actual state transition in the moment (e.g., "the status changes to Running").

## Words to avoid in ordinary product documentation

- **Time-projecting:** "currently," "presently," "at present," "as of this writing."
- **Obsolescence-prone:** "new," "newer," "old," "older," "latest," "soon."
- **Speculative:** "eventually," "future," "in the future," "does not yet," "existing."
- **Vague-contextual:** "now" (usually implied and unnecessary).

## Examples

| Instead of | Write |
|---|---|
| "new subcommands let you..." | "These subcommands let you..." |
| "options aren't currently supported" | "The following options aren't supported" |
| "now supports the following filters" | "supports the following filters" |

If you truly need to flag something as new, anchor it to a concrete date instead of a relative word — e.g., "The January 14, 2021 release includes a new resource panel."
