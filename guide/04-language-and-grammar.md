# Language and grammar

[← Back to index](../STYLE_GUIDE.md)

## On this page

- [Abbreviations](#abbreviations)
- [Active voice](#active-voice)
- [Anthropomorphism](#anthropomorphism)
- [Articles (a, an, the)](#articles-a-an-the)
- [Capitalization](#capitalization)
- [Contractions](#contractions)
- [Pluralization](#pluralization)
- [Possessives](#possessives)
- [Prepositions](#prepositions)
- [Present tense](#present-tense)
- [Pronouns](#pronouns)
- [Second person](#second-person)
- [Sentence structure](#sentence-structure)
- [Verbs in reference documents](#verbs-in-reference-documents)

---

## Abbreviations

*Source: [https://developers.google.com/style/abbreviations](https://developers.google.com/style/abbreviations)*

# Abbreviations

## Definitions and types
- **Acronyms** are pronounced as a word (NATO, scuba).
- **Initialisms** are pronounced letter by letter (CIA, FYI, PR).
- **Shortened words** drop part of the word, sometimes keeping a period (Dr., etc., min, CA).
- Contractions are a separate category, covered on their own page.

## Long vs. short forms
- Short informal forms like *app*, *demo*, or *sync* aren't true abbreviations, so they don't take periods.
- Use a "speaking test": if people naturally say it as a word, treat it as a word rather than an abbreviation.

## When to use abbreviations
- Prefer well-known acronyms/initialisms when they save the reader time.
- Spell the term out on first use.
- Avoid abbreviations that aren't related to the document's main subject.
- Avoid specialized abbreviations your audience won't recognize.

### Spelling out unfamiliar terms
- On first mention, spell out an unfamiliar term and put the abbreviation in parentheses; use just the abbreviation afterward.
- Consider whether the audience, translators, or non-native English readers will know the term.
- Some abbreviations rarely need spelling out at all: AI, API, DVD, PDF, XML, HTML, RAM, REST, URL, USB.

### Formatting the introduction of a term
- Italicize both the spelled-out phrase and the abbreviation when introducing them.
- Only capitalize the spelled-out form if it's a proper noun.
- If the term is a link, include the abbreviation in the link text.

## Abbreviations to avoid
- Don't use *i.e.* or *e.g.* — write "that is" or "for example" instead.
- Avoid internet shorthand like "tl;dr," "ymmv," or "RTFM."
- Prefer the full common word over an abbreviation (e.g., "approximately" rather than "approx.").
- Don't abbreviate simple substitutions — write "10 times," not "10x."

## Periods
- No periods in acronyms or initialisms.
- Shortened words generally keep a period, except for date/time abbreviations.
- No period when the shortened form is read as a word (app, sync).
- No periods on country, state, or "DC" abbreviations.

## Pluralizing abbreviations
- Follow normal pluralization rules.

## Don't use abbreviations as verbs
- Avoid turning an abbreviation into a verb — say "use SSH to log in," not "ssh into."

## Choosing "a" vs. "an"
- Base the choice on pronunciation, not spelling: "a SQL," "a FHIR," "an SAP."

---

## Active voice

*Source: [https://developers.google.com/style/voice](https://developers.google.com/style/voice)*

# Active voice

## Main principle
Use active voice — where the grammatical subject performs the action — instead of passive voice. Make it clear who or what is doing the action.

## Why it matters
Passive voice often hides who's responsible for an action, leaving the reader unsure whether the reader, the computer, the server, an end user, or someone else is meant to act.

**Preferred (active):** "Send a query to the service. The server sends an acknowledgment."
**Avoid (passive):** "The service is queried, and an acknowledgment is sent."

## When passive voice is acceptable

### To emphasize the object rather than the action
Preferred: "The file is saved."

### To de-emphasize the subject/actor
Preferred: "Over 50 conflicts were found in the file."
Avoid: "You created over 50 conflicts in the file."

### When the actor doesn't matter to the reader
Preferred: "The database was purged in January."

---

## Anthropomorphism

*Source: [https://developers.google.com/style/anthropomorphism](https://developers.google.com/style/anthropomorphism)*

# Anthropomorphism

## Main principle
Don't attribute human qualities to software or hardware. Anthropomorphic language is figurative, which reduces precision and makes content harder to understand and translate for a global audience.

## Examples

**Preferred:**
- A Delimiter object specifies where to split a string.
- The PC detects a new device.

**Avoid:**
- A Delimiter object tells the splitter where a string should be broken.
- The PC sees a new device.

## Takeaway
Favor direct, literal descriptions of what components do instead of giving them human abilities like "seeing" or "telling."

---

## Articles (a, an, the)

*Source: [https://developers.google.com/style/articles](https://developers.google.com/style/articles)*

# Articles (a, an, the)

## Main guidance
Include definite and indefinite articles (*a*, *an*, *the*) in your writing. Don't drop them for brevity — including in headings and titles.

**Preferred:** "Create a VM instance"
**Avoid:** "Create VM instance"

## Related considerations
- **Global audience:** standard English word order (with articles) is easier for international readers and translation tools to parse. See [Global audience](../03-general-principles/global-audience.md).
- **Headings and titles:** the same "don't drop articles" guidance applies. See [Headings and titles](../06-formatting-and-organization/headings-and-titles.md).
- **Product names:** there are separate rules for whether an article precedes a specific product name. See [Product names](../02-key-resources/product-names.md).
- **Abbreviations:** choosing *a* vs. *an* before an abbreviation depends on pronunciation. See [Abbreviations](abbreviations.md).

## Summary
Always include articles for clarity and translatability — don't drop them anywhere for the sake of brevity.

---

## Capitalization

*Source: [https://developers.google.com/style/capitalization](https://developers.google.com/style/capitalization)*

# Capitalization

## General principles
- Follow standard American English capitalization; avoid capitalizing things unnecessarily.
- Don't rely on capitalization alone to distinguish two terms (e.g., "Pod" vs. "pod") — pick clearer wording instead.
- Reserve all-caps for official names, standardized abbreviations, or literal code references.
- Avoid camelCase-style writing except in official names or actual code.

## Product names
- Capitalize product names according to the product's official branding.

## Titles and headings
- Use sentence case: capitalize the first word, proper nouns, and the first word after a colon.
- Don't end titles or headings with a period.
- When you reference another page's title from within this guide, render it in sentence case even if the source used different capitalization.

## After a colon
- Start the text following a colon in lowercase, unless what follows is a proper noun (e.g., "Open source software: Hadoop"), a heading, a quotation, or text following a label like "Caution" or "Note."

## Figures and images
- Use sentence case for captions, labels, and callouts.

## Glossaries and indexes
- Lowercase entries unless they're proper nouns; write definitions in sentence case.

## Hyphenated words
- At the start of a sentence or heading, capitalize only the first element of a hyphenated compound, unless a later element is itself a proper noun.

## Lists and tables
- Use sentence case throughout list items and table content.

## Naming capitalization styles
- Avoid naming a convention like "camel case" in reader-facing text; instead, show the requirement with an example.

---

## Contractions

*Source: [https://developers.google.com/style/contractions](https://developers.google.com/style/contractions)*

# Contractions

## General guidance
Common two-word contractions are fine in informal documentation — e.g., "you're," "don't," "there's."

## Negation contractions
- Prefer contractions like "isn't," "don't," and "can't" over the spelled-out negative.
- Reason: readers scanning text can easily miss a standalone "not," but a contraction like "don't" is harder to misread.
- If you need to emphasize a negation strongly, formatting such as *is <em>not</em>* is an option, though it's rarely necessary.

## Contractions to avoid
- Don't invent nonstandard contractions (e.g., "guides're," or using "'s" to mean "is" on an unusual word like "browser's").
- Don't use three-word contractions (e.g., "mightn't've").

---

## Pluralization

*Source: [https://developers.google.com/style/pluralization](https://developers.google.com/style/pluralization)*

# Pluralization

## Singular vs. plural agreement
- With long or complex subjects, make sure singular/plural agreement is still correct — e.g., "Confirm that the number of entries listed in the directory is accurate."
- When multiple subjects are joined by "and" or "or," match verb number accordingly — e.g., "The request payload and header information are logged."
- After "one or more," use the plural, not singular — e.g., "If one or more tests fail, a system warning is triggered."
- After "more than one," use the singular, not plural — e.g., "You can create more than one instance at a time."

## Plural abbreviations
- Pluralize acronyms/initialisms like ordinary words: "APIs, SKEs, and IDEs," not "API's, SKE's, IDE's."
- Add "es" to abbreviations ending in s, sh, ch, or x (e.g., OSes, DISHes, DCCHes, BMXes).
- Keep the spelled-out term and its abbreviation in matching number: "virtual machines (VMs)," not "virtual machines (VM)."
- Use the singular unit after "1," and plural for every other number: "1 degree" but "15 degrees" and "0 degrees."
- Don't pluralize an abbreviation used as a unit alongside a number: "64 GB," not "64 GBs."

## Plural product and feature names
- Don't pluralize trademarks or company/product names.
- Keep class names singular and add a plural noun after them instead — e.g., "`Intent` objects," not "`Intent`s."

## Parenthetical plurals
- Don't hedge with an optional plural in parentheses, like "port(s)."
- Pick one form (singular or plural) and use it consistently, or use "one or more" when both possibilities apply — e.g., "can contain one or more ports."

---

## Possessives

*Source: [https://developers.google.com/style/possessives](https://developers.google.com/style/possessives)*

# Possessives

## General formation
- Singular nouns (including ones ending in "s"): add "'s" — e.g., "Modify each vector's record," "Raise the storage class's quota."
- Plural nouns ending in "s": add only an apostrophe — e.g., "Extend the models' capabilities" (not "models's").
- Plural nouns not ending in "s": add "'s."
- If a possessive reads awkwardly, rewrite around it instead — e.g., "Analyze the business data" rather than "Analyze the businesses' data."
- Never use "'s" to form a plural.

## Product, feature, and company names
- Don't put product/feature/trademark names in possessive form when describing their function or performance; use the name as a modifier instead — e.g., "monitor Google Search performance," not "monitor Google Search's performance" (or rephrase with "of": "performance of Google Search").
- Company names can take "'s" when actual possession is meant, but not when the name is functioning as a trademark.

## Code items
- Never make a code item itself possessive. Form the possessive from the following noun instead — e.g., "the `wordCount` method's return value" — or rephrase entirely: "the value returned by the `wordCount` method."

---

## Prepositions

*Source: [https://developers.google.com/style/prepositions](https://developers.google.com/style/prepositions)*

# Prepositions

## Ending a sentence with a preposition is fine
- There's no rule against it — place a preposition wherever it reads most naturally and clearly, including at the end of a sentence.
- Preferred: "For details, see the client library documentation for the language you're interacting with."
- Avoid: "For details, see the client library documentation for the language with which you're interacting."

## Use prepositions deliberately
- Add a preposition when it clarifies meaning; drop one that's unnecessary.
- Don't overload a sentence with too many prepositions.
- Example of balanced usage: "The icon for the connector manager turns green within a few minutes, and the connector instance is displayed shortly after."

## Related page
- See [UI elements and interaction](../08-computer-interfaces/ui-elements-and-interaction.md) for preposition choices specific to referencing UI elements.

---

## Present tense

*Source: [https://developers.google.com/style/tense](https://developers.google.com/style/tense)*

# Present tense

## Main rule
Use present tense for general behavior that isn't tied to a specific point in time.

Preferred: "Send a query to the service. The server sends an acknowledgment."
Avoid: "Send a query to the service. The server will send an acknowledgment."

## Exception: genuinely future actions
Future tense ("will") is fine when describing something that truly happens later.

Preferred: "Add the filename to the backup list. The file will be archived the next time the backup process runs."

## Exception: asynchronous operations
Future tense is also appropriate for delayed delivery or async behavior.

Preferred: "A message is sent that will notify any Pub/Sub subscribers."
Avoid: "A message is sent that notifies any Pub/Sub subscribers."

## Don't use future tense for "after the next release"
Avoid describing how a product will behave after a future release or update using future tense — describe current behavior instead.

## Avoid hypothetical "would"
Don't use conditional language like "would" to describe ordinary procedural results.

Preferred: "If you send an unsubscribe message, the server removes you from the mailing list."
Avoid: "You can send an unsubscribe message. The server would then remove you from the mailing list."

---

## Pronouns

*Source: [https://developers.google.com/style/pronouns](https://developers.google.com/style/pronouns)*

# Pronouns

## Avoid ambiguous references
- Make sure every pronoun clearly points back to one antecedent.
- Preferred: "If you type text in the field, the text doesn't change."
- Avoid: "If you type text in the field, it doesn't change."
- Follow demonstratives ("this," "these") with a noun rather than leaving them dangling: "Set this value to true" rather than "Set this to true."

## Gender-neutral pronouns
- Don't use gendered pronouns (he, she, him, her, his) unless referring to an actual person of that gender.
- Avoid constructions like "he/she" or "(s)he."
- Use singular "they" as the gender-neutral option.

## Optional pronouns like "that"/"which"
- Keep pronouns such as "that" in a sentence when they add clarity.
- Preferred: "Right-click the link that you want to open."
- Avoid: "Right-click the link you want to open."

## First-person vs. second-person
- Avoid first-person pronouns (I, we, us, our) except in FAQs, author commentary, or references to the organization itself.
- Use "you" (second person) whenever possible.

## Relative pronouns: that / which / who / whose
- "That" introduces a restrictive clause and isn't preceded by a comma — e.g., "The echidna that has a long snout is furry."
- "Which" introduces a nonrestrictive clause and is preceded by a comma — e.g., "The echidna, which has a long snout, is furry."
- "Who" can replace "that" when referring to people.
- "Whose" is the possessive form, usable for people, animals, and things.

## See also
- [Second person](second-person.md) for more on addressing the reader as "you."

---

## Second person

*Source: [https://developers.google.com/style/person](https://developers.google.com/style/person)*

# Second person

## Address the reader as "you"
- Use "you"/"your" rather than "we"/"our"/"us" for directness and clarity.
- Assume the reader is the one performing the task or making the decision.
- Reserve "user" for the end-users of software that the reader builds, not for the reader themself.
- Preferred: "The following sections describe how you can create a website."
- Avoid: "The following sections describe how we can create a website."

## Imperative mood for instructions
- An implied "you" is fine for direct instructions, e.g., "Click **Submit**."
- Use the imperative sparingly in running prose; consider formatting the content as a numbered procedure instead. See [Procedures](../06-formatting-and-organization/procedures.md).

## Third person for software or end-user actions
- Reserve second person ("you") for actions the reader takes.
- Use third person to describe what software or end-users do, as opposed to what the reader (developer) does — e.g., in API reference text describing what code does.

## Using "we" carefully
- "We" is acceptable when clearly referring to the authoring organization, as long as the antecedent is unambiguous.
- Example uses: "Example Organization provides A and B, but we don't provide C and D." / "The support team regularly reviews tickets. Expect to hear from us in 2-3 business days."

## Be consistent about who "you" is
- Identify who "you" refers to (developer, sysadmin, etc.) early in the document, and keep that audience consistent throughout.

---

## Sentence structure

*Source: [https://developers.google.com/style/sentence-structure](https://developers.google.com/style/sentence-structure)*

# Sentence structure

## Main principle
When telling the reader to do something, state the circumstance, condition, or goal before the instruction itself. This lets readers quickly judge whether a sentence is relevant to them before reading the instruction.

## Put context before the instruction
Preferred: "For more information, see [link]."
Avoid: "See [link] for more information."

## Lead procedures with the goal
Preferred: "To delete the entire document, click Delete."
Avoid: "Click Delete if you want to delete the entire document."

## State the condition before the consequence
Preferred: "If your app is in certain regions, custom domains might add latency."
Avoid: "Custom domains might add latency if your app is in certain regions."

## Why this matters
Leading with circumstances and goals lets readers decide relevance immediately, which makes documentation faster to scan and use.

---

## Verbs in reference documents

*Source: [https://developers.google.com/style/reference-verbs](https://developers.google.com/style/reference-verbs)*

# Verbs in reference documents

## Main rule
Describe what a method does using a third-person singular verb (ending in "-s"), rather than an imperative form that instructs the developer.

The distinction is subtle — it comes down to whether the description's opening verb ends in "-s" or not.

## Example
Preferred: "tasks.insert: Creates a new task on the specified task list."
Avoid: "tasks.insert: Create a new task on the specified task list."

## Context
This applies specifically to method/endpoint descriptions in reference documentation, and lines up with the broader API design guidance used across Google Cloud's API design guide.

---
