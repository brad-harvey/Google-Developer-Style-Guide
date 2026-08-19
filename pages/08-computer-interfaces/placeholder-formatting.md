---
title: "Placeholder formatting"
source: "https://developers.google.com/style/placeholders"
section: "Computer interfaces"
---

# Placeholder formatting

Placeholders stand in for values the reader must substitute with their own input.

## Avoid the letter "x" as a generic placeholder

Use a descriptive placeholder name instead of "x" or "xx." The one common exception is a case like HTTP status code ranges, where "xx" is already conventional (e.g. `5xx`).

## Placeholders inline in text

- For code samples/commands: wrap in `<code><var>PLACEHOLDER_NAME</var></code>` in HTML, or use backtick+italic styling in Markdown.
- For non-code text: just use `<var>PLACEHOLDER_NAME</var>`.

## Placeholders inside code blocks

- HTML: wrap the whole block in `<pre>` and tag each placeholder with `<var>`.
- Markdown: a fenced code block works, but note you can't apply bold/italic styling inside it, which limits how you can mark placeholders there.

## Naming placeholders

- Use uppercase words joined with underscores, e.g. `API_NAME`, `METHOD_NAME`.
- Avoid hyphens, lowercase, or camelCase forms like `API-name`, `api_name`, `apiName`.
- Leave out possessive adjectives — don't write `MY_API_NAME` or `YOUR_API_NAME`.
- Keep surrounding punctuation (brackets, braces, ellipses) outside the `<var>` tag.

## Explaining placeholders

- For a single placeholder: "Replace `PLACEHOLDER` with a description of what the placeholder represents."
- For multiple placeholders: introduce with "Replace the following:" then list each one in the order it appears, formatted as `PLACEHOLDER`: description (lowercase start), using an em dash or "such as" to add examples where useful.
- For placeholders that show up in sample output: introduce with "This output includes the following values:" and follow the same list format as above.
