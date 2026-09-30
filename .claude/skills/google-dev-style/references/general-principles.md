# General principles

## On this page

- [Accessibility](#accessibility)
- [Excessive claims](#excessive-claims)
- [Future features](#future-features)
- [Global audience](#global-audience)
- [Inclusive documentation](#inclusive-documentation)
- [Jargon](#jargon)
- [Prescriptive documentation](#prescriptive-documentation)
- [Third-party content](#third-party-content)
- [Timeless documentation](#timeless-documentation)
- [Voice and tone](#voice-and-tone)

---

## Accessibility

*Source: [https://developers.google.com/style/accessibility](https://developers.google.com/style/accessibility)*

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

---

## Excessive claims

*Source: [https://developers.google.com/style/excessive-claims](https://developers.google.com/style/excessive-claims)*

# Excessive claims

## What counts as an excessive claim

- An unverifiable statement about performance or cost.
- A security claim that a future incident could disprove.
- Subjective or disparaging language about another product.

## Guidance

**Avoid superlatives** — words like "best," "simplest," "fastest," "never," "always." Use "ensure" and "guarantee" cautiously.

**Performance claims** need a verifiable data source behind them, and should hold up even as future circumstances change.

**Security language** — say a feature "helps with security" or "is designed for security" rather than claiming it prevents something outright; an absolute claim becomes false the moment an incident occurs.

**Competitive comparisons** are risky for two reasons: you may be misrepresenting a competitor's product, and either product's future releases could make the comparison false.

## Bottom line

Write factually and objectively — limit claims to verifiable information that stays true for the life of the documentation.

## Examples

- Performance, preferred approach: describe how the product works, then explain why it performs well in specific, referenced scenarios.
- Performance, avoid: flatly claiming your product is faster than a named competitor's.
- Security, preferred: describing a security product as part of a broader strategy that helps prevent a category of attack.
- Security, avoid: flatly claiming a security product prevents that category of attack.

---

## Future features

*Source: [https://developers.google.com/style/future](https://developers.google.com/style/future)*

# Future features

## Core rule

Don't document future features or products, even in a low-key or oblique way. Don't pre-announce anything in documentation unless your legal counsel has approved it.

## In practice

- Keep documentation limited to what's actually released/current.
- Don't hint at, tease, or reference unreleased functionality.

## Related pages

- [Present tense](../04-language-and-grammar/present-tense.md) — write about the current state, not the future.
- [Timeless documentation](timeless-documentation.md) — write so the content doesn't need constant date-based updates.

---

## Global audience

*Source: [https://developers.google.com/style/translation](https://developers.google.com/style/translation)*

# Writing for a global audience

Localization, clarity, and consistency all make documentation easier for both international readers and translators.

## Use clear, concise, unambiguous language

- Prefer simple words over complex ones ("start" over "commence," "so" over "consequently," "use" over "utilize").
- Prefer a single word over a wordy phrase ("many" over "a number of").
- Keep sentences short — it eases translation.
- Avoid stacking phrasal verbs where a single verb works (exceptions that are fine as-is: "set up," "log in," "sign in").
- Limit yourself to at most two modifiers stacked on a noun.
- Place modifiers immediately next to the word they modify (e.g., "Request only one token," not "Only request one token").
- Use active voice and present tense — subject-performs-action sentences are easier to parse and translate.
- Don't reuse the same word with two different meanings in close proximity.
- Avoid directional language ("above," "below") in procedures.
- Add qualifying nouns for clarity ("the `example.yaml` file," not just "example.yaml").
- It's fine to repeat a word rather than vary it, if repetition removes ambiguity; use "then," "that," "of" to disambiguate where needed.
- Define abbreviations on first use.
- Make sure pronoun antecedents are unambiguous — mistranslation risk otherwise.

## Address users directly

- Say "you," not "the user" or "they."
- Give the reader the context they need.
- Minimize negative constructions.

## Be consistent

- Once you pick a term for a concept, keep using that exact term (and capitalization) everywhere.
- Use the same sentence patterns for the same kind of content.
- Subject + verb + object order; put conditional clauses first.
- Keep list items parallel in structure.
- Apply bold/italic and capitalization consistently.

## Be inclusive

- Write dates and times unambiguously.
- Avoid culturally specific references and holidays.
- Use a diverse set of example names.
- Skip colloquialisms, idioms, slang, and humor — they often don't translate.
- Skip references tied to a specific hemisphere/season.

## Images

- Use screenshots sparingly.
- Convey new information in text, not only in a screenshot.

---

## Inclusive documentation

*Source: [https://developers.google.com/style/inclusive-documentation](https://developers.google.com/style/inclusive-documentation)*

# Write inclusive documentation

## Avoid unnecessarily gendered language

Use gender-neutral alternatives — e.g., "person-hours" instead of "man-hours," "humanity" instead of "mankind."

## Avoid figurative language

Use precise, literal terminology instead of idioms, metaphors, or slang, since figurative language often doesn't translate and can obscure meaning.

### Avoid ableist language

Replace words that trivialize disability with neutral alternatives — e.g., "final check" instead of "sanity-check," "baffling" instead of "crazy," "slows down" instead of "cripples," "placeholder" instead of "dummy variable."

### Avoid graphic or violent metaphors

Use precise, non-graphic terms — e.g., "doesn't respond" instead of "hangs," "click" instead of "hit." For industry jargon that is graphic (like "STONITH"), minimize its use and explain it clearly when necessary.

## Write diverse and inclusive examples

- Use gender-neutral pronouns consistently.
- Avoid US-centric cultural references.
- Choose a diverse mix of example names.
- Say "older adults" rather than "elderly" or "seniors."

## Write about features and users inclusively

- Avoid unnecessary "native" vs. "non-native" speaker distinctions.
- Replace "blacklist"/"whitelist" with "allowlist"/"blocklist" (or similarly precise alternatives).
- Avoid "first-class citizen" and similar loaded phrasing.

### Replacing established but non-inclusive terms

On first mention, you can acknowledge the older non-inclusive term in parentheses, then use the inclusive term for the rest of the document.

### Writing around non-inclusive terms baked into code

Put the non-inclusive term in code font when you must reference it literally (e.g., an existing API parameter name), minimize how often you use it, and use the inclusive term everywhere else.

## Avoid bias when discussing disability

- Don't describe non-disabled people as "normal" or "healthy" (implying disabled people aren't).
- Research and respect the terminology a given community actually prefers.
- Some communities (e.g., autistic, blind, Deaf communities) commonly prefer identity-first language — honor that instead of defaulting to person-first phrasing everywhere.
- Avoid "victim" framing ("suffering from," "wheelchair-bound").
- Avoid patronizing euphemisms ("physically challenged," "special").

---

## Jargon

*Source: [https://developers.google.com/style/jargon](https://developers.google.com/style/jargon)*

# Jargon

## What counts as jargon

Specialized, often figurative terminology used by a particular group to stand in for a larger concept (e.g., "camel case," "swim lane," "break-glass procedure"). Vague catch-all terms like "solution," "support," or "workload" have a similar effect.

## Why it's a problem

- Readers outside the group won't understand it.
- It hurts clarity and limits how broad an audience the doc can reach.
- It complicates translation.
- It creates a knowledge barrier for readers at different experience levels.
- It can inadvertently exclude particular groups or cultures.

## A decision path for handling a jargon term

1. **Can you write around it entirely?** Do, unless you need to keep the term for SEO. (E.g., replace "hold a postmortem" with "when finished, review what worked.")
2. **Is there a more specific/plain-language replacement?** Use the word list's suggested alternative (e.g., "affected area" instead of "blast radius"), and drop anything offensive or non-inclusive.
3. **Used only once in the document?** Give a plain-language explanation inline, in parentheses, or link to a trusted definition.
4. **Used repeatedly throughout the document?** Define it briefly on first use (or link to a trusted definition), then use it normally afterward.
5. **Appears inside a code sample?** Only put the actual code tokens in code font — don't let the jargon bleed into surrounding prose formatting, and make clear what you're referring to.

---

## Prescriptive documentation

*Source: [https://developers.google.com/style/prescriptive-documentation](https://developers.google.com/style/prescriptive-documentation)*

# Prescriptive documentation

## Core idea

Prescriptive (opinionated) documentation recommends *one* way to accomplish a task, rather than laying out every possible option and letting the reader choose.

## Where this shows up

- **Purpose and structure** — state a clear, specific purpose for the document, and let headings map to that purpose.
- **Examples and procedures** — build scenarios around the reader's most common/relevant use case.
- **Sample commands** — pick commands and arguments that match the most common use case, rather than showing every flag.

## Word choice by certainty level

- **Required action:** "must," or an imperative like "Do the following before you continue."
- **Recommended action:** "We recommend..." / "Google recommends...". "Should" is acceptable for a generally-recognized recommendation (e.g., established security practice).
- **Optional/alternative action:** "can."
- **Expected (typical) outcome:** describe it as a fact — "The process returns 10 items."
- **Possible (uncertain) outcome:** "might" or "can."
- **Actual current state:** avoid "should be" here — say what actually happens ("the server sets...," "you must set...") rather than implying an expectation that might not hold.

## Example

- Preferred: "Ensure that the button conforms to the guidelines."
- Avoid: "The button should conform to the guidelines." (Ambiguous between a requirement and a description of current state.)

---

## Third-party content

*Source: [https://developers.google.com/style/other-sources](https://developers.google.com/style/other-sources)*

# Third-party content

## Core rule

Don't copy content — text, images, code, logos, or speech — from another source. Paraphrase it in your own words and link to the original.

## Sources this applies to

- Third-party documentation, websites, books, blogs, videos, images, podcasts.
- Reference sources — dictionaries, encyclopedias, Wikipedia.
- Open-source project documentation (licensing varies project to project — don't assume you can reuse it freely).
- Content on GitHub (same caveat — different repos carry different licenses).

## When you're not sure

If you're unsure who owns something or what its license allows, don't use it. Paraphrase the underlying idea and link back to the source for attribution instead of quoting it directly.

## Example pattern

- Preferred: paraphrase the concept in your own words, and link the defined term to the original source (e.g., explaining what a "recovery point objective" is in your own sentence, with the term linked out).
- Avoid: lifting a source's exact definition verbatim and just adding a citation — that's still a copyright problem even with attribution.

---

## Timeless documentation

*Source: [https://developers.google.com/style/timeless-documentation](https://developers.google.com/style/timeless-documentation)*

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

---

## Voice and tone

*Source: [https://developers.google.com/style/tone](https://developers.google.com/style/tone)*

# Voice and tone

## The target

Conversational, friendly, and respectful — without sliding into slang. Prioritize clarity: simple, consistent language that works for a global audience. Personality is fine, but clear and useful information comes first.

## Avoid

- Technical buzzwords and jargon.
- Cutesy or "entertaining" language.
- Figurative language, metaphors, and ableist phrasing.
- Filler phrases ("please note," "at this time").
- Choppy or overly verbose sentences.
- Repeating the same sentence-starter over and over.
- Pop-culture references.
- Exclamation marks.
- Anything that insults or denigrates a group.
- Minimizing phrases like "simply," "it's easy," "just," "let's."
- Internet slang and abbreviations.

## Techniques

- Ask yourself plainly, "What am I actually trying to say?" before polishing the wording.
- Get a colleague's read on tone.
- Read the passage aloud — awkward phrasing tends to surface that way.
- Use real transitions between sentences rather than choppy fragments.
- When tone and clarity conflict, clarity wins.

## "Please"

Don't overuse "please" in instructions — a direct imperative reads fine on its own ("Click **View**," not "Please click **View**").

## Calibrating tone

Think of tone on a spectrum from too informal to too formal, and aim for the appropriate middle: professional, but still human and approachable — not stiff, and not chatty.

---
