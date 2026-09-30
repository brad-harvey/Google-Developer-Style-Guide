---
name: google-dev-style
description: Google-style conventions for technical writing — voice, grammar, punctuation, formatting, code and command-line conventions, and a full A–Z terminology glossary. Use whenever writing or editing technical documentation, READMEs, API references, release notes, tutorials, code comments, or answering a technical question where the response will read as documentation. Also use when asked to tighten, clarify, or professionalize existing technical prose, even if the user doesn't mention a style guide.
---

# Google Developer Documentation style

Write technical content the way Google's developer documentation team writes it:
clear, direct, conversational-but-professional, and built for a global audience
of readers who are scanning for an answer, not reading for pleasure. Every rule
below serves the same goal — reduce the reader's effort. Active voice, short
sentences, "you," and present tense all exist because they make text faster to
parse, easier to translate, and harder to misread.

This applies to any technical output: documentation, READMEs, API references,
code comments, explanations of how code works, tutorials, error-message copy, or
a plain conversational answer about a technical topic. Apply the voice and
formatting rules in chat responses too, not just in generated files.

## The core moves (apply these by default)

**Voice and tone.** Conversational, friendly, respectful — never slangy, cutesy,
or full of buzzwords. Skip filler ("please note," "simply," "just," "let's"),
pop-culture references, and exclamation marks. Clarity beats personality every
time they conflict. Don't overuse "please" — a plain imperative ("Click
**Submit**") is already polite enough.

**Active voice, present tense, second person.** The subject performs the action;
describe how things behave now, not how they'll behave later; call the reader
"you," not "the user" or "we" (reserve "we" for the organization itself, and
only when the referent is unambiguous).

- "Send a query to the service. The server sends an acknowledgment." — not "The
  service is queried, and an acknowledgment is sent" or "...the server will
  send..."

**Lead with context, then the instruction.** State the circumstance, condition,
or goal before telling the reader what to do — it lets them judge relevance
before they read the action.

- "To delete the entire document, click **Delete**." — not "Click **Delete** if
  you want to delete the entire document."

**Write timeless, prescriptive content.** Describe the current state of the
product, not its history or its future. Avoid "currently," "now," "new," "soon,"
"eventually" — if something is genuinely new, anchor it to a real date instead of
a relative word. Recommend *one* good way to do something rather than cataloging
every option. Match certainty language to reality: "must" for requirements, "we
recommend" for suggestions, "can" for optional paths, plain present tense for
what actually happens ("the process returns 10 items," not "the process should
return 10 items").

**Keep sentences short and plain.** Roughly 26 words or fewer. Prefer the simple
word over the fancy one ("use" not "utilize," "start" not "commence"). Don't
stack more than two modifiers on a noun. One idea per paragraph; split anything
past 5–6 sentences.

**Don't overclaim.** Avoid superlatives ("best," "fastest," "never," "always")
and unverifiable performance or security claims — say a feature "helps with" or
"is designed for" security rather than claiming it prevents something outright,
since an absolute claim becomes false the moment reality disagrees with it.

**Be inclusive and accessible by default.** Gender-neutral language (singular
"they," not "he/she"); no ableist or violent-metaphor idioms ("doesn't respond"
not "hangs," "final check" not "sanity-check"); diverse, non-US-centric example
names; no directional language like "above," "below," or "on the right" (use
"preceding" and "following" — direction doesn't hold up for screen readers,
translation, or reflowed layouts).

## Formatting defaults

- **Headings**: sentence case, no ending period. Task headings start with a bare
  infinitive ("Create an instance," not "Creating an instance"); conceptual
  headings are noun phrases, not "-ing" forms. Don't skip heading levels.
- **Lists**: introduce with a full sentence ending in a colon (or a period if
  other content intervenes). Numbered lists for sequence, bullets when order
  doesn't matter, description lists for term/definition pairs. Keep items
  grammatically parallel.
- **Procedures**: one clear instruction per step, imperative verbs ("Clone the
  repository," not "You need to retrieve..."), state where the action happens
  before the action itself. A single-step "procedure" is just one sentence, not
  a numbered list.
- **Notes, cautions, and warnings**: use sparingly, and only for genuinely
  skippable asides — never for prerequisites, cross-references, or actual steps,
  which belong in the main flow.
- **Code font** for anything the reader enters or that names a real code element
  — commands, filenames, class and method names, placeholders, literal values,
  flags — never for product names or plain-prose domain names. Placeholders are
  `UPPER_SNAKE_CASE`, never a bare "x".
- **Numbers**: spell out zero through nine, use numerals for 10 and above;
  always use numerals for versions, sizes, and other technical quantities
  regardless of magnitude.
- **Dates**: write as Month Day, Year (March 5, 2026), never numeric-only forms
  that are ambiguous across locales.
- **Articles**: never drop "a," "an," or "the" for brevity, including in
  headings ("Create a VM instance," not "Create VM instance").
- **Contractions** are fine and often preferred for negation ("doesn't,"
  "can't") — a spelled-out "not" is easy to miss when scanning.
- Straight quotes and apostrophes only, never curly ones. Em dashes with no
  surrounding spaces; no en dashes; avoid semicolons, parentheses for essential
  information, and ellipses.

Full detail on any of these lives in the reference files below. Consult one when
you need the specifics — exact hyphenation rules, table formatting, exception
lists, UI-element terminology — rather than guessing.

## Reference files

Load these as needed rather than all at once. Each covers one area in depth.

| File | Covers |
|---|---|
| [references/general-principles.md](references/general-principles.md) | Voice and tone, accessibility, inclusive language, jargon, prescriptive and timeless writing, excessive claims, third-party content |
| [references/language-and-grammar.md](references/language-and-grammar.md) | Active voice, present tense, second person, pronouns, possessives, pluralization, capitalization, contractions, articles, sentence structure |
| [references/punctuation.md](references/punctuation.md) | Colons, commas, dashes, hyphens, parentheses, periods, quotation marks, semicolons, slashes |
| [references/formatting-and-organization.md](references/formatting-and-organization.md) | Headings, lists, procedures, tables, notes, numbers, dates and times, units, images, paragraphs |
| [references/computer-interfaces.md](references/computer-interfaces.md) | Code in text, code samples, command-line syntax, placeholders, API reference comments, UI element terminology |
| [references/word-list.md](references/word-list.md) | A–Z glossary of specific terms — check here before using any word you're unsure about (jargon, ambiguous UI terms, deprecated phrasing) |
| [references/key-resources.md](references/key-resources.md) | Product-name conventions and the text-formatting summary (which markup to use for what) |
| [references/linking.md](references/linking.md) | Cross-references, link text, heading anchors |
| [references/names-and-naming.md](references/names-and-naming.md) | Example domains and names, filenames, trademarks |
| [references/html-and-css.md](references/html-and-css.md) | Semantic HTML, HTML versus Markdown formatting choices |
| [references/introduction.md](references/introduction.md) | Background and philosophy of the source guide |

**Check the word list first for terminology.** Many common developer words have a
preferred form or are flagged as avoid-entirely — "allowlist" and "denylist" over
"whitelist" and "blacklist," "primary" and "replica" over "master" and "slave,"
"extract" over "unzip" or "untar." When a term isn't in the list, default to the
plainest, most literal word a reader unfamiliar with internal jargon would
understand.

## When this guidance doesn't apply

If the user's own project has an established style — existing docs, a
CONTRIBUTING guide, or an explicit instruction — that conflicts with a rule here,
follow the project's convention instead. This skill is a sensible default, not an
override.
