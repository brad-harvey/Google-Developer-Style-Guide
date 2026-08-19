---
title: "HTML and semantic tagging"
source: "https://developers.google.com/style/semantic-tagging"
section: "HTML and CSS"
---

# HTML and semantic tagging

## Core principle

Choose HTML elements for what they mean, not just how they look — reserve visual styling for CSS.

## Semantic elements

- Use `cite` for the title of a standalone work like a book or film.
- When there's no element that semantically fits, it's fine to fall back on a purely presentational HTML/CSS approach (see MDN's guide on HTML semantics for more background).

## Layout and structure

- Don't use frames or tables to lay out a page — use CSS.
- Only use heading elements (`h1`, `h2`, ...) for actual document hierarchy, never purely for visual size/weight.

## Emphasis and styling elements

- `em` means semantic emphasis, not "make it italic" — use `i` for italics that carry no emphasis.
- `strong` means strong importance, not "make it bold" — use `b` for bold text that isn't semantically important.
- Reserve `br` for line breaks that are genuinely part of the content, like in a poem or a mailing address; use `p` plus CSS spacing for other visual gaps.
