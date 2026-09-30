# Punctuation

## On this page

- [Colons](#colons)
- [Commas](#commas)
- [Dashes](#dashes)
- [Ellipses](#ellipses)
- [Hyphens](#hyphens)
- [Parentheses](#parentheses)
- [Periods and other end punctuation](#periods-and-other-end-punctuation)
- [Quotation marks](#quotation-marks)
- [Semicolons](#semicolons)
- [Slashes](#slashes)

---

## Colons

*Source: [https://developers.google.com/style/colons](https://developers.google.com/style/colons)*

# Colons

A colon signals that closely related information follows — usually a list, an explanation, or an elaboration of what came before.

## Lead-in text should be a complete sentence

When a colon introduces a list or explanation, the text before the colon should stand on its own as a complete sentence.

- Preferred: "The fields are defined as follows:"
- Avoid: "The fields are:"

## Capitalization after a colon

The word right after a colon is normally lowercase, with a few exceptions covered on the capitalization page (for example, when what follows is itself a complete, standalone sentence in some contexts).

Examples:
- "Tone: concise, conversational, friendly, respectful"
- "When you add or update content to an existing project, remember to take these steps: review the style guide, use checklists, enlist a fellow writer or an editor to copyedit your work, and request a developmental edit if you feel that it's warranted."

## See also

Related guidance covers introducing lists, introducing code samples, dashes, and using run-in headings.

---

## Commas

*Source: [https://developers.google.com/style/commas](https://developers.google.com/style/commas)*

# Commas

Key topics: serial commas, introductory phrases, independent clauses, nonrestrictive clauses, and conjunctive adverbs.

## Serial (Oxford) commas

Use a comma before the final "and" or "or" in a list of three or more items, to avoid ambiguity.

- Preferred: "Locations are divided into zones, regions, and multi-regions."
- Avoid: "Locations are divided into zones, regions and multi-regions."

## Commas after introductory words and phrases

Put a comma after an introductory word or phrase that opens a sentence.

- "Finally, only groups that contain parameters appear in this list."
- "Based on the requirements of your game, you can implement this method."

## Commas joining two independent clauses

Add a comma before a coordinating conjunction (and, but, or, nor, for, so, yet) that joins two independent clauses — unless both clauses are very short.

- "The libraries make feed creation easier, and they ensure that only valid feeds are produced."
- Short-clause exception, no comma needed: "Type your ID and click **OK**."

## Independent clause followed by a dependent clause

Only add a comma if it's needed to prevent misreading.

- No comma needed: "Direct-access flags are plain variables and can be read directly."
- Comma added for clarity: "The manager acknowledged the last team member who entered the room, and started the meeting."

## Other clauses that need commas

- **Nonrestrictive "which" clauses** — put a comma before "which" when it starts a nonrestrictive clause: "Name of the group, which has a maximum length of 200 characters."
- **Conjunctive adverbs** (otherwise, however, therefore) — use a semicolon, period, or dash before them, and a comma after: "The variable must have a value; otherwise, the server returns an error."
- **Causal "because" clauses** — generally skip the comma, unless "because" introduces a nonrestrictive clause: "You can use the same key name in multiple backend services and backend buckets, because each set of keys is independent of the others."

## See also

Related guidance covers commas and decimal points in numbers, and punctuating examples.

---

## Dashes

*Source: [https://developers.google.com/style/dashes](https://developers.google.com/style/dashes)*

# Dashes

## Em dashes

Use an em dash to mark a break in the flow of a sentence or an interruption. Don't put spaces before or after it.

How to type one:
- HTML: `&mdash;`
- macOS: Option+Shift+hyphen
- Linux: Compose key + three hyphens, or Ctrl+Shift+U then 2014
- Windows: Alt+0151 (numeric keypad)

Don't substitute a hyphen or en dash for an em dash.

## En dashes

Don't use en dashes at all. Use a hyphen, or spell out "to," instead.

## Don't use dashes to separate a term from its description

Avoid the "term - description" pattern in description-style lists. Instead:
- Use a colon: "Example: This is an example."
- Use a period: "Example. This is an example."
- Or use an HTML description list (`<dl>`) when there are multiple terms.

Avoid: "Example - This is an example."

---

## Ellipses

*Source: [https://developers.google.com/style/ellipses](https://developers.google.com/style/ellipses)*

# Ellipses

## General rule

Avoid using ellipses ("...") in technical documentation to show omission or hesitation.

## Don't use ellipses as suspension points

Don't use an ellipsis to convey a pause or uncertainty.

- Avoid: "The answer is ... wait for it ... that you shouldn't do this."

## UI text that contains ellipses

If a UI element's label includes an ellipsis (e.g., a button that reads "Save ..."), leave the ellipsis out when referring to it in documentation, unless dropping it would cause confusion — e.g., write "click **Save**."

## Ellipses in quoted text

An ellipsis can stand in for omitted material inside a quotation, but avoid using one at the very start or end of the quote.

If the omitted text spans a sentence boundary, use four periods (three for the ellipsis, one as the terminal period): "All the world's a stage, .... And one man in his time plays many parts."

## Punctuation and spacing

Use three literal periods (not a single ellipsis character), with one space before and one after — except drop the trailing space if punctuation follows immediately.

- Preferred: "...we'll explain it in class." or "...; we'll explain it in class."
- Avoid: "...we'll explain it in class" (missing the surrounding space)

---

## Hyphens

*Source: [https://developers.google.com/style/hyphens](https://developers.google.com/style/hyphens)*

# Hyphens

Use hyphens to avoid misreading, to combine terms, and to separate parts of words for clarity. In general: hyphenate certain prefixes and compound modifiers, write most compound nouns as one word, and don't put spaces around a hyphen except in suspended constructions.

## General approach

When deciding whether to hyphenate, check (in order): existing usage in your docs, the word list, then a dictionary such as Merriam-Webster. Deviate from the guidance when it serves your readers.

## Prefixes

Generally don't hyphenate a prefix and the noun that follows it — e.g., infrastructure, metadata, preprocessing.

Hyphenate when:
- The prefix is "self-" or "cross-": self-managing, cross-region
- The base word is capitalized or a number: non-Google, post-2000
- Omitting the hyphen would cause confusion: de-energize, re-mark
- The base word is already hyphenated: un-Google-like
- Consistency with existing docs calls for it: pre-processing, post-processing

Special note on "non-": this prefix can easily create hard-to-parse words and is often hyphenated; both "noncurrent" and "non-existence" style forms can be acceptable depending on context.

## Compounds

### Compound nouns
Write as one word (closed form) by default — webpage, hostname, tradeoff, workaround. The word list has exceptions that stay hyphenated or open, such as "multi-region" and "style sheet."

For measurement units where the components multiply together, hyphenate: 5 vCPU-hours, 40 person-hours.

### Compound modifiers before a noun
Hyphenate for clarity — well-designed app, Android-specific techniques.

With "more" or "most," add a hyphen to clarify what's being modified: more-reliable internet links.

Avoid stacking more than two words into a compound modifier; restructure the sentence instead.
- Preferred: "test cases specific to the 2023 edition"
- Avoid: "edition-2023-specific test cases"

Hyphenate spelled-out numbers and units used as modifiers: 64-bit system, five-minute wait. For abbreviated units, skip the hyphen and use a nonbreaking space instead unless clarity requires a hyphen: 200 GB disk.

Don't hyphenate "-ly" adverb + adjective modifiers: "Publicly available implementations."

### Compound terms after a verb
Generally don't hyphenate after a verb — "The app is well designed." "The logs are written in real time."

Exceptions per the word list stay hyphenated regardless of position: on-premises, cloud-based, customer-facing, user-friendly.

## Ranges of numbers

Use a hyphen (not an en dash) for a number range: "8-20 files," "5-10 minutes." Don't mix a hyphenated range with the word "from" — use either "8-20 files" or "from 8 to 20 files."

## Spacing around hyphens

Never put a space on either side of a hyphen, except with a suspended hyphen.

## Suspended hyphens

When multiple compound modifiers share a common base word, drop the base from the earlier modifiers and keep a hyphen with a following space:
- "one- or two-hour intervals"
- "one-, two-, or three-hour intervals"

---

## Parentheses

*Source: [https://developers.google.com/style/parentheses](https://developers.google.com/style/parentheses)*

# Parentheses

## Core guidance

Avoid putting critical information inside parentheses — some readers skip over parenthetical content entirely. Whenever you're inclined to reach for parentheses, ask whether they're actually necessary; a comma, dash, semicolon, or period is often a better choice.

Keep a mid-sentence parenthetical short. If the aside is long, split it into a separate sentence instead.

## Punctuation with parentheses

If a full, standalone sentence sits inside the parentheses, its period goes inside the closing parenthesis, not after it.

## Examples

Preferred approaches:
- Use an em dash: "Enter a name for the instance—for example, `my-instance-99`"
- Use two sentences: "Enter a six-digit hex number, and then click OK. For example, if you want forest green, enter `228B22`"
- Reserve parentheses for a minor aside: "Enter a six-digit hex number (for example, `228B22`), and then click OK"

Avoid:
- Putting essential instructions in parentheses
- Long parenthetical asides in the middle of a sentence

## Related

Don't use parentheses to mark an optional plural (e.g., "file(s)") — see the pluralization guidance for the recommended alternative.

---

## Periods and other end punctuation

*Source: [https://developers.google.com/style/periods](https://developers.google.com/style/periods)*

# Periods and other end punctuation

## Core rules

- End complete sentences with a period, except in some list items and in headings.
- Avoid ending a sentence with a URL.
- Put the period inside quotation marks.
- If parentheses enclose a full sentence, the period goes inside them.
- Use periods for decimal points and for abbreviations, but not for acronyms.

## Periods with lists

Whether a list item gets a period depends on the type of list — see the Lists page for the capitalization and end-punctuation rules.

## Periods with URLs

A period right after a URL is ambiguous — readers can't tell if it's part of the address. To avoid this:
- Avoid ending a sentence with a URL in running text where possible.
- Restructure the sentence so the URL isn't at the end.
- Put the URL on its own line, without a trailing period.
- If the URL is rendered as a link (typically colored/underlined), that visual distinction helps separate it from the punctuation.

## Periods with quotation marks

Place the period inside the quotation marks, even if it wasn't part of the original quoted text — except for literal code strings, which follow different rules (see quotation marks guidance). If the quoted text already ends in a question mark or exclamation point, don't add another period.

## Periods with parentheses

- Partial sentence in parentheses: period goes outside the closing parenthesis.
- Full sentence in parentheses: period goes inside.

## Periods with headings

Don't put a period at the end of heading text.

## Periods with numbers

Use a period as the decimal point (US convention — this varies internationally).

## Periods with abbreviations

Use a period after a shortened word (an abbreviation), but not after an acronym or initialism.

## Spacing

Use a single space between sentences, not two.

## Exclamation points

Use sparingly overall — they can read as unprofessional and often translate poorly.

By content type:
- Concept and reference docs: never use them.
- Procedural docs: avoid; use a period instead.
- Blog posts: occasional, sparing use for genuine enthusiasm is acceptable.

Acceptable uses regardless of content type:
- Required by code syntax (e.g., `!=`)
- Quoting an exact system error message that contains one
- Marking a genuine milestone in a tutorial, used sparingly

Translation note: some languages (e.g., Japanese, Korean) can read an exclamation point as shouting.

---

## Quotation marks

*Source: [https://developers.google.com/style/quotation-marks](https://developers.google.com/style/quotation-marks)*

# Quotation marks

## Use straight quotation marks

Always use straight double quotes and straight apostrophes, never curly/typographic ones — this keeps text consistent with code requirements and avoids errors.

## When to use quotation marks

- Titles of short works, such as articles or episodes — e.g., reference the "Deploying containers" section.
- A section within a larger document that can't be linked directly — e.g., the "Introduction to Vertex AI" guide.
- Direct quotations — e.g., "We are still learning the techniques..."
- Metaphorical or non-standard use of a term — e.g., a configuration that forms an "island."

## Commas and periods

Place commas and periods inside the quotation marks — except for a literal string shown in code font, where punctuation goes outside: `escape`, not "escape,".

## Single quotation marks

Reserve single quotes for:
- Code examples in languages that require single quotes.
- A quotation nested inside another quotation — double quotes outside, single quotes inside: "She said, 'Help,' and saw him floundering."

---

## Semicolons

*Source: [https://developers.google.com/style/semicolons](https://developers.google.com/style/semicolons)*

# Semicolons

## General principle

Avoid semicolons where possible.

## Three acceptable uses

1. **Joining closely related independent clauses**, when a period or comma wouldn't work as well:
   "You can easily test compatibility by computing the centroid; if it is on the opposite side of the planet, reverse the order of your vertices."

2. **Before a conjunctive adverb or transitional phrase** (such as "therefore" or "that is") that links two independent clauses:
   - "This setup places the head-tracked node below the Main Camera; therefore, only the stereo cameras are affected by the user's head motion."
   - "The URL from which a video ad loads; that is, the URL to use to fetch that video ad."

3. **Separating items in a complex list**, where individual items are long or already contain their own commas:
   "Review your document one more time, checking for the following: present tense and active voice; typos, punctuation, and grammar; and whether you can shorten anything."

---

## Slashes

*Source: [https://developers.google.com/style/slashes](https://developers.google.com/style/slashes)*

# Slashes

## General rule

Avoid slashes, except in actual code.

## Slashes with dates

Don't use slash-based date formats — see the Dates and times page for the recommended format.

## Slashes for alternatives

Don't use a slash to mean "or"/"and" — spell out the word instead.

- Preferred: "...developed and is hosted by a commercial entity" or "...developed or is hosted by a commercial entity"
- Avoid: "...developed/hosted by a commercial entity"
- Preferred: "Call this method five or six times"
- Avoid: "Call this method 5/6 times"

### "And/or"

Use "and" alone when it already implies "or." Reserve "and/or" for places where space is extremely tight, such as a table cell.
- Preferred: "You can view and edit your own data"
- Avoid: "You can view and/or edit your own data"

## Slashes in file paths and URLs

Use forward slashes for file paths and URLs; use backslashes only for Windows-style paths. When a URL needs to wrap onto a new line, break immediately after a slash — never insert an extra hyphen into a URL.

## Slashes in fractions

Avoid a slash in a fraction — it's ambiguous. Use "¾", "0.75", or "75%" instead of "3/4".

## Slashes in abbreviations

Don't use abbreviations built around a slash; spell the words out — "care of," "with" — instead of "c/o," "w/".

---
