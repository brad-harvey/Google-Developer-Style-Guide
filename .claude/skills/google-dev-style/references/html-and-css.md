# HTML and CSS

## On this page

- [HTML and semantic tagging](#html-and-semantic-tagging)
- [HTML formatting](#html-formatting)
- [Markdown versus HTML](#markdown-versus-html)

---

## HTML and semantic tagging

*Source: [https://developers.google.com/style/semantic-tagging](https://developers.google.com/style/semantic-tagging)*

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

---

## HTML formatting

*Source: [https://developers.google.com/style/html-formatting](https://developers.google.com/style/html-formatting)*

# HTML formatting

## Basic guidelines

- Indent with spaces, never tabs — editors interpret tabs inconsistently.
- Use two spaces per indentation level.
- Write elements and attributes in all lowercase.
- Don't leave trailing whitespace at line ends, except where Markdown syntax specifically requires it.
- Otherwise follow Google's published HTML/CSS style guide, with one deliberate override: keep optional HTML elements in your markup rather than omitting them.

## Line length

- Wrap at 80 characters as the default.
- Exceptions: `meta` elements near the top of a file stay on one line regardless of length, and a link whose URL alone exceeds 80 characters should go on its own line with the `href`.
- Inside `<pre>` blocks, still try to break code near 80 characters without changing its meaning; existing files using a different consistent width don't need a full reformat just for a small edit.

---

## Markdown versus HTML

*Source: [https://developers.google.com/style/markdown](https://developers.google.com/style/markdown)*

# Markdown versus HTML

## Choosing a format

- Either HTML or Markdown is an acceptable authoring format. Some of this style guide's advice assumes HTML markup; if you write in Markdown, treat those HTML-specific details as not applicable to you.
- Markdown is generally quicker to write and its source is easier for people to read than raw HTML.
- HTML is more expressive — especially for semantic tagging — and can produce effects that are difficult or impossible in Markdown (for example, using the HTML `code` element to represent a nonbreaking space inside code).
- Absent other constraints, the choice comes down to personal preference — but defer to your team's or template's existing convention over your own preference when one already exists.

---
