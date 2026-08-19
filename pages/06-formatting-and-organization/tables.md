---
title: "Tables"
source: "https://developers.google.com/style/tables"
section: "Formatting and organization"
---

# Tables

## When to use a table
- Use a table when each item has three or more related pieces of data worth comparing.

## When not to use a table
- Don't use a table purely for page layout — use CSS.
- Don't use a table for single-row content, or for what's really a single column (that should be a list).
- Never use a table to display code snippets, and don't split a simple one-dimensional list across table columns just to fit space.
- Avoid dropping a table into the middle of a numbered procedure.

## Structure
- Use `<p>` elements rather than `<br>` for multiple paragraphs inside a cell.
- Introduce a table with a full sentence describing its purpose, ending in a colon (if immediately before the table) or a period.
- A single-table document doesn't need a caption; with multiple tables, caption each as "Table N. Description," in sentence case with no trailing period, and refer to tables by number in the text (not capitalized).
- Use sentence case for column headers, keep them concise, and don't end them with punctuation; mark header cells with `<th>` (and a `scope` attribute) rather than faking a header look with styling.
- Don't style the table element itself, and never merge cells with `colspan`/`rowspan`.
- Sort rows in a logical or alphabetical order, and give any images/symbols in cells proper `alt` text.
- Split up a table that's grown too large or complex.
- Use responsive CSS so tables adapt to different viewport sizes.
- Refer to a table by its number rather than linking directly to it.
