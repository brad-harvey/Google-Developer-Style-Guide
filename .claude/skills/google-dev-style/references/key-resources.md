# Key resources

## On this page

- [Product names](#product-names)
- [Text-formatting summary](#text-formatting-summary)

---

## Product names

*Source: [https://developers.google.com/style/product-names](https://developers.google.com/style/product-names)*

# Product names

## Capitalization

Capitalize Google product names in title case, except when matching a UI label or when the official name itself starts lowercase.

Feature names are generally lowercase unless they're officially capitalized or match a UI label. When unsure, follow existing precedent in current documentation.

## Use full names

Use the complete, trademarked product name rather than an abbreviation, unless the abbreviation matches a UI label. Be careful to make clear which product is being referenced.

## Articles ("the")

Don't put "the" before a product name unless it's modifying something else. Exception: tool and API names generally do take "the" (e.g., "The Transcoder API").

## Never use product names as verbs

Product and feature names should never be verbed.

## Other guidelines

- Follow the official capitalization used by the brand, company, or open-source community that owns the name.
- For names that officially start lowercase (e.g., macOS-style names), restructure the sentence so it doesn't begin with that name.
- "Service" (singular) is fine to describe multiple products collectively when "services" wouldn't cause confusion.
- When a product name modifies another noun and takes an article, match it grammatically (e.g., "An Anthos Service Mesh environment").

## Examples

- Preferred: "The Cloud Datastore options page"
- Preferred: "Using Cloud Datastore with Cloud Dataproc"
- Avoid: "Using the Cloud Datastore with Cloud Dataproc"

---

## Text-formatting summary

*Source: [https://developers.google.com/style/text-formatting](https://developers.google.com/style/text-formatting)*

# Text-formatting summary

A quick-reference table of when to use each text style.

## Bold
- Reserve for UI element names and run-in headings.
- HTML: `<b>`; Markdown: `**text**`.
- Avoid double-underscore (`__`) bold in Markdown for consistency.

## Italic
- Use sparingly — mainly to introduce or discuss a term.
- HTML: `<i>`; Markdown: `_text_` (prefer underscores over asterisks so it's visually distinct from bold).
- Italicize titles of full-length works (books, movies, web series).
- Italicize mathematical variables and version-number variables.

## Underline
- Reserve exclusively for link text — don't use it for emphasis.

## Code font
- HTML: `<code>`; Markdown: backticks.
- Use for filenames, class names, method names, HTTP status codes, console/command output, and similar literal strings.
- Use a code block (`<pre>` or triple backticks) for multi-line sample code.
- Never manually restyle code font (size/color) — let the semantic tag do it.

## Capitalization
- Standard American English conventions in running text.
- Sentence case for headings, titles, and navigation labels.
- All-uppercase for placeholder text.

## Quotation marks
- Follow American English punctuation conventions (e.g., punctuation inside closing quotes).
- Use for titles of shorter works (articles, episodes) — not full-length works (those are italicized).
- Keep quotation marks outside of link text and outside end punctuation.

## Font type, size, and color
- Don't override the site/theme's default styles — rely on semantic HTML or Markdown rather than manual styling.

## Other
- Don't use "&" as a stand-in for "and" in running text; spell out "and" (exception: literal UI element names that contain "&").
