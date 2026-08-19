---
name: google-dev-style
description: Google-style conventions for technical writing — voice, grammar, formatting, code, and terminology. Use whenever writing or editing technical documentation, READMEs, API references, tutorials, comments, or answering technical questions where the response will read as documentation.
---

# Writing in Google Developer Documentation style

Apply these conventions to any technical writing task: documentation, READMEs,
API references, tutorials, code comments, or explanatory answers to technical
questions. This skill distills the rules in this repo's condensed style guide
(`STYLE_GUIDE.md` and `guide/`) into direct instructions. For the full
rationale or edge cases behind any rule, check the matching section there —
in particular `guide/02-key-resources.md` for the terminology word list.

## Voice and tone

- Write like a knowledgeable colleague talking to another engineer: direct,
  clear, and warm, not stiff or bureaucratic.
- Skip marketing language, hype, and unnecessary superlatives ("blazing
  fast," "seamlessly," "simply" — that last one especially, since a step is
  rarely simple for the reader currently stuck on it).
- Don't be cute or jokey in reference material; light personality is fine in
  intros or tutorials, not in procedures or API docs.
- Address the reader directly as "you." Never refer to the reader in third
  person ("the user should...").
- Don't anthropomorphize software ("the script wants," "the API decides").
  Say what the system does mechanically instead.

## Grammar defaults

- **Active voice** by default. Reserve passive voice for when the actor is
  unknown, irrelevant, or the object is genuinely the point.
- **Present tense** by default, even for describing what code or a system
  does ("the function returns," not "the function will return").
- **Second person** ("you"), not first person plural ("we") and not an
  implied/absent subject.
- Use **they/them** as the default singular gender-neutral pronoun. Never
  guess a specific person's gender.
- Contractions (it's, don't, you're) are fine in prose for a natural tone;
  avoid them in formal reference material like legal text or precise
  specifications.
- Use "a" before consonant *sounds* and "an" before vowel *sounds* (e.g., "a
  URL," "an SQL query" — judge by pronunciation, not spelling).
- Avoid jargon and unnecessary abbreviations; spell out an acronym on first
  use, then abbreviate.

## Punctuation

- Use the serial (Oxford) comma in lists of three or more items.
- Use a colon to introduce a list or explanation, not a comma or dash.
- Avoid semicolons in prose; prefer two clear sentences.
- One space after a period.
- Avoid exclamation points in reference documentation.
- Hyphenate compound modifiers before a noun ("a well-known issue") but not
  after ("this issue is well known").
- Use straight/plain quotation marks (`"`, `'`) in code and file paths, never
  typographic "curly" quotes.

## Formatting and structure

- **Headings**: sentence case ("Configure the client library," not "Configure
  The Client Library"), and make each heading descriptive enough to work as a
  link target or table-of-contents entry on its own.
- **Lists**: numbered lists only for steps that must happen in order;
  bulleted lists for unordered items. Keep list items parallel in structure.
- **Paragraphs**: short — one idea per paragraph. Lead with the point, then
  support it.
- **Notices**: flag exceptions or warnings clearly and consistently, e.g. a
  bolded label like **Note:** or **Caution:** at the start of the callout,
  not buried mid-paragraph.
- **Numbers**: spell out zero through nine in prose; use digits for 10 and
  above, and always use digits when paired with a unit (5 GB, 3 ms).
- **Dates**: write as Month Day, Year (March 5, 2026), not numeric-only
  formats, to avoid day/month ambiguity for a global audience.
- **Tables**: use for genuinely tabular/comparative data, not as a layout
  hack; every table needs a header row.

## Linking

- Write descriptive link text that stands on its own ("see the
  authentication guide"), never "click here" or a bare URL.
- Give the reader the key information directly instead of forcing a click,
  when it's feasible to do so in a sentence or two.
- Don't repeat the same link target multiple times on one page unless it
  points to a different section or genuinely helps at that spot.

## Code, commands, and UI

- Put code font (backticks / `<code>`) around: commands, filenames, literal
  values, variable and function names, keys and values, and any text a
  reader would type verbatim.
- Format placeholders distinctly (e.g., `<PROJECT_ID>` or *italicized*) and
  explain each one the first time it appears.
- Use realistic, descriptive placeholder names, not `foo`/`bar`/`baz`.
- Name UI elements exactly as they appear on screen, and mark them clearly
  (commonly bold) so instructions like "click **Save**" are unambiguous.
- Prefer "select" for choosing a UI item generally; reserve "click" for an
  explicit mouse action and "tap" for touchscreens — don't mix them for the
  same audience/platform.
- Every code sample should be runnable and minimal — no unrelated setup, no
  dead code, no commented-out alternatives left in.

## Global audience and accessibility

- Avoid idioms, wordplay, and culturally specific references that don't
  translate ("hit it out of the park").
- Avoid directional or purely visual references ("the button on the right,"
  "the red text") since layout and color perception both vary; name the
  element instead.
- Write alt text for meaningful images; skip decorative ones.
- Avoid absolute claims and superlatives ("the fastest," "impossible to
  break") — they age badly and are rarely defensible.

## Timeless writing

- Avoid words that date the content: "now," "currently," "soon," "new," "in
  this release." State the current behavior as a plain fact instead of
  contrasting it with the past.
- Don't reference "today's date" relative language; use explicit versions or
  dates only when a fact genuinely depends on them.

## Terminology

- Check `guide/02-key-resources.md` (the word list) for a specific term
  before using it — many common developer words have a preferred form,
  a preferred alternative, or are flagged as avoid-entirely (e.g., prefer
  "allowlist/denylist" over "whitelist/blacklist," "primary/replica" over
  "master/slave," "extract" over "unzip/untar/uncompress").
- When a term isn't in the list, default to the plainest, most literal word
  a reader unfamiliar with internal jargon would understand.

## Applying this skill

When producing documentation, a README, a code comment, or an explanatory
answer to a technical question, follow the rules above by default. If the
user's own project already has an established style (existing docs,
CONTRIBUTING guide, or explicit instruction) that conflicts with a rule here,
follow the project's convention instead — this skill is a sensible default,
not an override.
