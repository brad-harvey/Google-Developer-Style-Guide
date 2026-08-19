---
title: "HTML formatting"
source: "https://developers.google.com/style/html-formatting"
section: "HTML and CSS"
---

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
