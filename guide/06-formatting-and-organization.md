# Formatting and organization

[← Back to index](../STYLE_GUIDE.md)

## On this page

- [Dates and times](#dates-and-times)
- [Examples](#examples)
- [Figures and other images](#figures-and-other-images)
- [Footnotes](#footnotes)
- [Headings and titles](#headings-and-titles)
- [Italics with terms](#italics-with-terms)
- [Lists](#lists)
- [Mathematical notation](#mathematical-notation)
- [Notes and other notices](#notes-and-other-notices)
- [Numbers](#numbers)
- [Paragraphs](#paragraphs)
- [Phone numbers](#phone-numbers)
- [Procedures](#procedures)
- [Tables](#tables)
- [Units of measurement](#units-of-measurement)

---

## Dates and times

*Source: [https://developers.google.com/style/dates-times](https://developers.google.com/style/dates-times)*

# Dates and times

## Times
- Use the 12-hour clock unless a 24-hour format is required for the context.
- Capitalize AM/PM and put a space before it: `3:45 PM`.
- Drop `:00` for round hours: `3 PM`, not `3:00 PM`.
- In time ranges, use a hyphen with no surrounding spaces: `5-10 minutes ago`.
- Prefer exact times, but `noon` and `midnight` are acceptable as words.

## Time zones
- Avoid mentioning a time zone unless it's necessary.
- When possible, express times in the reader's local time (e.g., "10 AM your local time") instead of naming a zone.
- If a zone must be named, spell out the region and give the UTC/GMT offset parenthetically, e.g., "US and Canadian Pacific Standard Time (UTC-8)."
- Don't abbreviate time zone names (avoid things like "PST").

## Dates
- Spell out month names and weekday names in full.
- Always use a four-digit year, not a two-digit shorthand: `January 19, 2017`.
- If including the weekday, put it before the month: `Tuesday, April 27, 2021`.
- Month + year with no day doesn't take a comma: `She was hired in January 2017`.
- Three-letter abbreviations for month/weekday are acceptable only when space is tight (headings, tables), e.g., `Mon, Sep 3, 2018` — don't mix abbreviated and spelled-out forms in the same date.
- When a full "Month Day, Year" date sits mid-sentence, add a comma after the year: "The January 19, 2017, release of...". A month-and-year-only date mid-sentence takes no such comma: "The January 2017 release of...".
- For numeric dates, use ISO 8601 (`YYYY-MM-DD`) with hyphens, e.g., `2017-04-15`. Avoid other numeric date formats (`02.12.2017`, `12/02/2017`) unless there's no alternative.
- In made-up examples, pick a day-of-month greater than 12 so the date can't be misread as ambiguous (day vs. month).

## Combined date and time
- State the date before the time: `2017-04-15 at 3 PM`, `May 4, 2009, at 6 PM`.

## Seasons and year divisions
- Avoid naming seasons, since they're reversed across hemispheres and vary by climate. Use months, quarters, or general temperature language instead — e.g., "during warmer months" rather than "during summer."

---

## Examples

*Source: [https://developers.google.com/style/format-examples](https://developers.google.com/style/format-examples)*

# Examples

## Introducing an example at the end of a sentence
- Set it off with a comma, parentheses, or an em dash — not a semicolon.
- e.g., "Choose a strong encryption algorithm, such as AES-256."
- e.g., "Enter a name for the instance, for example, `my-instance-99`."

## Short examples mid-sentence
- Keep them brief and set them off with commas, parentheses, or dashes rather than a long aside.
- e.g., "Enter a six-digit hex number (for example, `228B22`), and then click **OK**."

## Longer examples
- If an example needs more explanation than fits comfortably mid-sentence, give it its own sentence starting with "For example,".
- e.g., "You can assign tags to your virtual machine instances to categorize them. For example, you could tag instances by environment with `env:prod` or `env:dev`."

---

## Figures and other images

*Source: [https://developers.google.com/style/images](https://developers.google.com/style/images)*

# Figures and other images

## When to use an image
- Use images only when they add a visual explanation that's genuinely hard to convey in words.
- In screenshots, capture only the UI elements relevant to the discussion.
- Never use an image to show text that could just be text — code samples, terminal output, etc. should stay as real, selectable/searchable text.

## Creating images
- Prefer SVG for diagrams (scales cleanly); fall back to PNG if SVG isn't available.
- Avoid transparent backgrounds — they can misbehave with the site's lightbox viewer.
- For motion, prefer an efficient video format (e.g., MP4) over animated GIFs.
- Keep screenshots visually consistent across a doc set: same OS, same look, same drop-shadow treatment.
- Crop tightly to relevant content; exclude unrelated UI.
- Redact any personal/identifying information with a solid opaque overlay (not a blur or mosaic).
- Flatten layered export formats (PDF, TIFF) before use.
- Avoid image maps — accessibility and mobile-scaling problems; use a text list of links instead.
- Give image files descriptive filenames.

## Introducing images in text
- Precede most images with a full sentence that ends in a colon (if the image immediately follows) or a period (if other content, like a note, sits between the sentence and the image).
- Screenshots that immediately follow a step-by-step UI description can skip a separate intro sentence.

## Alt text
- Every image needs an `alt` attribute, even if it's empty (`alt=""`) for purely decorative images.
- Alt text should be a concise description (roughly 155 characters or less), written as a full sentence or noun phrase, punctuated normally.
- Don't prefix alt text with "Image of" or "Photo of," and avoid all-caps (some screen readers spell out capitalized words letter by letter).
- Don't put a diagram's introductory framing inside the alt text — that belongs in the surrounding paragraph.
- Alt text should describe the image's function in context, not just its literal contents.
- If 155 characters isn't enough, pair a short alt text with a longer visible text description nearby.
- Reuse identical alt text for the same recurring icon/control/status indicator across a document.

## Captions and figure numbers
- Captions and figure numbers are optional.
- If used, wrap the image and its caption together in a `figure`/`figcaption` structure.
- Format numbered captions as "Figure N. Description." with a complete sentence and closing punctuation.
- When numbering figures, refer back to them by number ("figure 2"), lowercase except at the start of a sentence — avoid spatial references like "the image above."
- Keep the caption text and any in-text reference to the figure separate rather than combined into one sentence.

## Figure descriptions
- Add a fuller text description near the image when the caption alone doesn't convey everything the figure shows.
- Any information the reader needs must also exist in surrounding text — don't let the image be the sole carrier of information.

## Text embedded in the image itself
- Minimize text baked into graphics — it hurts accessibility, search, and localization.
- Keep any embedded text brief; avoid full sentences, punctuation, invented abbreviations, and detailed callout annotations.
- Follow normal capitalization rules for any in-image titles, and use full/trademarked product names.

## High-resolution images
- Use `srcset` to serve higher-resolution versions to capable browsers, while keeping a standard-resolution `src` for compatibility.
- Point `src` at the 1x image; name the 2x version `basename_2x.ext`.
- The 2x image must be exactly double the width and height of the 1x image (within a pixel) — never just upscale the 1x version.
- Set the `width` attribute to the CSS display size; let height scale proportionally.
- If maintenance overhead is a concern, it's acceptable to use the 2x image for both `src` and `srcset`.

## Layout
- Use the site's standard CSS/layout rather than manual inline positioning.
- Don't shrink images excessively; consider how they'll look printed.
- Keep images within the page's column-width constraints, and get appropriately pre-sized images from designers when needed.
- Avoid linking to a same-page figure unless the page is long enough that the link travels a real distance.
- Left-align images rather than centering them, and don't nest `img` elements inside `p` elements.

---

## Footnotes

*Source: [https://developers.google.com/style/footnotes](https://developers.google.com/style/footnotes)*

# Footnotes

- Avoid footnotes in general — they're not accessible to screen-reader users and complicate localization.
- Prefer alternatives: a cross-reference to related content, a formatted note, or a parenthetical aside within the sentence.
- If a footnote truly is necessary, mark it with a superscript number (`<sup>1</sup>`) and place the footnote text at the bottom of the same page.

---

## Headings and titles

*Source: [https://developers.google.com/style/headings](https://developers.google.com/style/headings)*

# Headings and titles

- Use sentence case for all headings and titles.
- For task-based headings, start with a bare infinitive verb: "Create an instance," not "Creating an instance."
- For conceptual headings, use a noun phrase rather than an "-ing" form: "Migration to Google Cloud," not "Migrating to Google Cloud." ("Billing" and "Pricing" are accepted exceptions to the no-"-ing" rule.)
- Prefix a heading with "Optional:" when the section only applies in some scenarios, e.g., "Optional: Customize your alias."
- Each page should have exactly one H1, and it shouldn't be repeated verbatim as a subheading.
- Keep abbreviations in headings to well-known ones, and spell out terms in full where possible — full terms help both readability and SEO.
- Don't number headings to show sequence; let the heading hierarchy (H1/H2/H3) carry that structure.
- Avoid putting code elements or links directly in headings; if code must appear, add plain-language context around it.
- Maintain a proper heading hierarchy — don't skip from H1 straight to H3.
- Never leave a heading with no content under it.
- When referring readers to related subsections, say "the following sections" rather than the ambiguous "this section" or "these sections."

---

## Italics with terms

*Source: [https://developers.google.com/style/italics-terms](https://developers.google.com/style/italics-terms)*

# Italics with terms

- When you introduce a new term along with its definition, italicize the term on first use rather than bolding it or putting it in quotes.
- When referring to a word, letter, or phrase as itself (a metalinguistic mention, not its meaning), use italics rather than bold or quotation marks — e.g., discussing the word *and* itself, or the character *'s* used to form a possessive.

---

## Lists

*Source: [https://developers.google.com/style/lists](https://developers.google.com/style/lists)*

# Lists

## Choosing a list vs. a table
- Use a table when items have multiple properties worth comparing; use a list for sequential steps or a simple collection.
- Don't use a "list" of just one item.

## Types of lists
- **Numbered lists** — for items where order matters (steps, ranked priorities). Nested sequential sub-items can use lowercase letters or roman numerals.
- **Bulleted lists** — for items where order doesn't matter; make clear whether each bullet is required or optional.
- **Description lists** (`dl`/`dt`/`dd`) — for term/definition pairs.
- **Run-in description lists** — a bulleted list where each item starts with a bolded term, saving vertical space while still highlighting terms.

## Introducing a list
- Introduce a list with a complete sentence.
- End that sentence with a colon if the list follows immediately, or a period if other content comes between the intro and the list.
- Prefer a full lead-in like "Use the Submit button for any of the following purposes:" over a fragment like "Use the Submit button to:".

## Capitalization and punctuation within items
- Capitalize the first word of numbered/bulleted items (unless case is meaningful for that content).
- End items with sentence-ending punctuation, except single words, verb-less fragments, code-only items, or link text — and apply that choice consistently across the whole list.
- In description lists: capitalize the term, don't put a period after it, and do end the definition with a period.
- In run-in lists: capitalize the bolded lead term and end it consistently with either a period or colon; text after a period starts a new capitalized sentence, text after a colon stays lowercase unless it's a new sentence. Avoid using a dash to separate the term from its description.

## Other rules
- Keep grammatical structure parallel across all items in a list.
- For multi-paragraph list items, use separate `p` elements rather than line breaks (`br`).
- In comma-separated in-line lists, use the serial (Oxford) comma and avoid trailing off with "etc." or "and so on."

---

## Mathematical notation

*Source: [https://developers.google.com/style/mathematical-notation](https://developers.google.com/style/mathematical-notation)*

# Mathematical notation

- Use proper HTML entities for math symbols rather than keyboard look-alikes (an exception is made for `+`, `=`, and `/`) — e.g., use a real minus-sign entity instead of a hyphen.
- Put non-breaking spaces around binary operators within an expression.
- Keep operators/symbols upright; italicize only the variables (e.g., *x* ≠ *y*).
- Short expressions can sit inline in a sentence; move longer ones onto their own line so they don't break awkwardly.
- Prefer decimal form over a written fraction when practical (`0.02` rather than a fraction).
- If a fraction must be spelled out in words, hyphenate it: "three-sevenths," "one and one-half."
- Use `<sup>`/`<sub>` tags for exponents and subscripts rather than a caret or plain adjacent characters — e.g., `2<sup>3</sup>`, not `2^3`.
- When unambiguous, prefer symbolic notation over spelled-out comparisons in running text (*a* > *b* rather than "*a* is greater than *b*").
- For complex or multiline equations, use a diagram, image, or dedicated math-rendering tool instead of trying to force it into plain text.

---

## Notes and other notices

*Source: [https://developers.google.com/style/notices](https://developers.google.com/style/notices)*

# Notes and other notices

## General principles
- Use notices sparingly — readers can skip over content that's pulled out of the normal flow, so overusing them dilutes their value.
- Don't stack multiple notices back to back; restructure the content instead.
- Before adding a notice, consider whether the information could just be regular body text.

## The four notice types
- **Note** — relevant but non-essential information the reader could skip without harm (e.g., a tangential tip).
- **Caution** — signals the reader should proceed carefully because something could go wrong (e.g., warning against an overly broad `0.0.0.0/0` network range).
- **Warning** — for serious or irreversible risks; stronger than a caution, essentially a "don't do this" (e.g., never pass a password on the command line).
- **Success** — confirms something completed correctly; only appropriate in interactive/dynamic contexts (like a console flow), not static reference pages.

## When a note is appropriate
Use a note only when all of the following are true: the information is relevant but not required for the reader to succeed, it doesn't interrupt the reader's task if skipped, and it doesn't naturally belong in the main flow of text.

## When not to use a note
Don't use a note for: cross-references, prerequisites (put those before the step instead), actual procedural steps, information the reader needs to succeed, or content that would read naturally as part of the surrounding paragraph.

---

## Numbers

*Source: [https://developers.google.com/style/numbers](https://developers.google.com/style/numbers)*

# Numbers

- Spell out ordinal numbers in text ("first," "fifth," "twelfth") rather than using "1st," "5th," "12th."
- Spell out zero through nine as words; use numerals for 10 and up.
- If a number would start a sentence, either spell it out or rewrite the sentence so the numeral falls later.
- Technical quantities — version numbers, memory/disk sizes, query limits, and similar measurements — always use numerals, even below 10.
- When a spelled-out number directly precedes a numeral quantity, keep both as written, e.g., "fifteen 100,000-byte files."
- Round, imprecise quantities like "millions" or "billions" can stay as words.
- If a sentence mixes numbers under and over 10, it's fine to use numerals throughout for consistency.
- For numbers less than one, include the leading zero before the decimal point: "0.3 inches."
- Prefer decimal form for fractions when practical; if spelled out, hyphenate ("two-fifths").
- Write percentages as a numeral plus the percent sign with no space: "40%."
- Use a hyphen with no spaces for number ranges: "2012-2016."
- Format currency with commas for thousands and a period for decimals: "$10,000," "$0.006653."
- Write dimensions with a lowercase "x" and no spaces: "192x192."
- Format exponents using standard mathematical notation, without extra spacing.

---

## Paragraphs

*Source: [https://developers.google.com/style/paragraph-structure](https://developers.google.com/style/paragraph-structure)*

# Paragraphs

- Break content into shorter paragraphs so pages stay scannable rather than becoming walls of text.
- Give each paragraph one main idea, using as few sentences as that idea needs.
- Treat a paragraph longer than 5-6 sentences as a sign it should be split.
- Single-sentence paragraphs are fine, and a longer paragraph is fine too, as long as it stays focused on one idea.
- Lead with the most important information — don't bury a paragraph's key point at the end.
- Left-align body text; avoid centered, fully justified, or right-aligned text.
- Don't insert manual/hard line breaks inside a sentence or paragraph — they break badly on resized windows, different devices, or larger text settings.

---

## Phone numbers

*Source: [https://developers.google.com/style/phone-numbers](https://developers.google.com/style/phone-numbers)*

# Phone numbers

- Never use a real phone number in an example. For US examples, use a number in the reserved range 800-555-0100 through 800-555-0199.
- Use a non-breaking hyphen (`&#8209;` in HTML/Markdown) between the number groups so a phone number doesn't wrap across lines.
- For North American (NANP) numbers, separate area code, exchange, and number with non-breaking hyphens, e.g., 415‑555‑0132.
- For non-NANP countries, include the country and area code, with a plus sign immediately before the country code and no space: +1‑415‑555‑0132.
- For an extension, follow the number with the word "extension" and the extension digits: "415-555-0132, extension 987."

---

## Procedures

*Source: [https://developers.google.com/style/procedures](https://developers.google.com/style/procedures)*

# Procedures

## Introducing a procedure
- Give a procedure an introductory sentence beyond the heading. Use a colon if the steps follow right after, or a period if other content (like a note) intervenes — e.g., "Customize the buttons:" versus "To customize the buttons, follow these steps."

## Structuring steps
- A one-step procedure should be a single bulleted item written as a full sentence, not a numbered list — e.g., "To clear the entire log, click **Clear logcat**."
- For sub-steps, use lowercase letters, and lowercase roman numerals for a further level below that; punctuate the parent step with a colon or period as appropriate.
- Combine a short sequence of clicks with angle brackets, e.g., "Click **File > New > Document**," but don't let a single step become excessively long.
- When there's more than one way to do something, document the single best approach where possible (favoring keyboard-accessible, shortest, or most broadly familiar method); if multiple approaches genuinely need documenting, separate them by page, heading, or tab rather than interleaving them.
- Don't repeat the same procedure in multiple places — link to a single canonical version instead.
- Mark optional steps by starting with "Optional:" e.g., "Optional: Type an arbitrary string...".

## Context and goals
- State where an action happens before describing the action itself, e.g., "In Google Docs, click **File > New > Document**." Restate that location context if the procedure continues under a new heading.
- Where useful, state the goal of a step before the action, e.g., "To start a new document, click **File > New > Document**."
- If a step has a result or a reason, state the action first and the result immediately after in the same step, e.g., "Click **Run**. The query results appear after the query runs."

## Wording steps
- Start steps with an imperative/action verb ("Clone the repository") rather than describing the requirement indirectly ("You need to retrieve the project ID").
- Keep verb forms parallel across related steps.
- Write steps as complete sentences.
- Avoid directional language like "above," "below," or "on the right" — it doesn't hold up for accessibility or across localized/re-flowed layouts.
- Don't say "please," and describe what a command accomplishes rather than just instructing the reader to "run the following command."
- If pressing Enter/Return is required to complete an action, say so as part of the step; don't document unrelated keyboard shortcuts.
- State any prerequisite hardware, software, or materials up front, before the procedure starts.

## Documenting commands
When documenting a command, follow this order: what the command does, the command itself, an explanation of any placeholders, further command detail, then the output (if relevant) and results as a separate paragraph if needed.

---

## Tables

*Source: [https://developers.google.com/style/tables](https://developers.google.com/style/tables)*

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

---

## Units of measurement

*Source: [https://developers.google.com/style/units-of-measure](https://developers.google.com/style/units-of-measure)*

# Units of measurement

- Put a non-breaking space between a number and its unit for most measurements, e.g., `64 GB`.
- Skip the space for currency, percentages, and angle degrees: `$10`, `65%`, `180°`.
- For temperature, put a non-breaking space between the number and the degree symbol, but no space between the symbol and the scale letter: `50 °C`, `50 °F`.
- Kelvin has no degree symbol, but still gets a non-breaking space: `300 K`.
- For a range of measurements, repeat the unit on both numbers and join them with "to" rather than a hyphen: "-40 °C to 85 °C," not "-40-85 °C."
- Hyphenate compound/multiplied units: "5 vCPU-hours," "40 person-hours."
- For thousands, a lowercase "k" with no space is fine alongside a noun: "55k download operations."
- Use a currency indicator when the currency could be ambiguous, e.g., "US$10" instead of a bare "$10."
- Spell out "per" for rates when there's room; reserve the division-slash notation for tight spaces like table cells.
- Match decimal vs. binary unit prefixes to what the underlying system actually uses (kB vs. KiB, MB vs. MiB, GB vs. GiB).

---
