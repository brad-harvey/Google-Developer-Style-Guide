---
title: "Accessibility"
source: "https://developers.google.com/style/accessibility"
section: "General principles"
---

# Accessibility

Guidance for writing documentation that works for readers using screen readers, keyboard-only navigation, magnification, or other assistive tools.

## General dos and don'ts

- Avoid ableist language.
- Make sure every part of the document is reachable via keyboard alone.
- Test with a screen reader.
- Use semantic HTML (e.g., `<em>` for emphasis) rather than purely visual styling.
- Prefer native HTML elements over custom-styled equivalents.
- Limit heavy font formatting — screen readers call out formatting changes explicitly.
- Explicitly document any specialized accessibility features.
- Avoid hard line breaks inside sentences/paragraphs.
- Minimize camelCase and ALL CAPS — some screen readers spell these out letter by letter.
- Be mindful that not every screen reader announces every punctuation mark.
- Spell out "and" instead of "&" in headings, running text, and navigation (except inside code or literal UI text).

## Ease of reading

- Break up long blocks of text with paragraphs, headings, and lists.
- Keep sentences under roughly 26 words.
- Define acronyms on first use, and again if used rarely.
- Use parallel structure for parallel content.
- Front-load paragraphs with the most distinguishing information so they scan well.
- Avoid double negatives.
- Left-align text; don't center or justify.

## Headings and titles

- Make headings descriptive and unique so they work as navigation landmarks.
- Don't skip heading levels.
- Use CSS, not heading level, for visual styling.
- Don't leave headings empty.
- Use real heading elements (`h1`, `h2`, ...).
- Reserve `h1` for the page title/main content.

## Links

- Write link text that's understandable out of context — never "click here" or "read this."
- Refer to links with "see."
- Call out unexpected behavior (a download starts, a new tab opens, the page jumps to an anchor).
- Separate adjacent links so they aren't announced as one.

## Lists

- Give each instruction in a procedure its own list item.
- Use lists generally to improve scanability and step-following.

## Images

- Give every image an alt attribute; use empty alt text for purely decorative images.
- Alt text should describe the image's intent, not just its contents.
- Never make an image the sole carrier of information.
- Don't repeat information redundantly across image and text unless necessary.
- Never render code or terminal output as an image — use real text.
- Prefer SVG over PNG for readable-at-any-zoom images.

## Video, audio, and GIFs

- Provide captions, a transcript, or a description for audio/video content.
- Make sure captions can be translated.
- Avoid flickering/flashing visuals.

## Buttons and icons

- Use the native `<button>` element for form submission, not styled `<div>`s.
- Icons should represent their object/function unambiguously.

## UI navigation paths

- Add an `aria-label` to the `>` character in menu-path breadcrumbs so screen readers read it sensibly (effectively "and then").

## Tables

- Introduce a table in the text before it appears.
- Use `<th>` for header cells, limited to the first row/column.
- Use `scope` for more complex header relationships, and `headers` for multi-level header rows.
- Avoid putting a table inside a numbered procedure if you can avoid it.
- Never merge cells with `colspan`/`rowspan`.
- Use tables sparingly overall — they're hard on screen readers.
- Give any in-table images/symbols descriptive alt text.

## Interactive elements

- Introduce an interactive element (e.g., an expandable section) in the text before the reader reaches it.

## Forms

- Label every input with a real `<label>` element, placed outside the field.
- Write error messages that say what's wrong and how to fix it.

## Custom CSS and JavaScript

- Meet a 4.5:1 contrast ratio for text.
- Never use `visibility:hidden` or `display:none` to "hide" content that should still be announced — both hide from screen readers too.
- Minimize reliance on mouseover events; provide keyboard-accessible focus/blur equivalents.
- Keep visual styling order aligned with DOM order and natural reading flow.

## Document rendering / general testing

- Test the document without sound, without images, without color, keyboard-only, with magnification, and without relying on punctuation.
- Don't rely on color, size, or position alone to communicate meaning — pair with a secondary cue (text, icon+label).
- Refer to UI elements by their label, not by a visual description.
- Avoid directional language ("above," "below," "to the right") — it breaks for screen-reader users and doesn't localize well. Use "preceding"/"following" instead.
