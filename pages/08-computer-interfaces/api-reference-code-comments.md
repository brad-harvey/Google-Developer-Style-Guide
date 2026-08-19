---
title: "API reference code comments"
source: "https://developers.google.com/style/api-reference-comments"
section: "Computer interfaces"
---

# API reference code comments

## Documentation basics

- Every class, interface, struct, and similar API member needs a description.
- Every constant, field, enum, and typedef needs a description.
- Every method needs a description covering its parameters, return value, and any exceptions it throws.
- Consider including a short code sample (roughly 5–20 lines) near the top of each unique reference page.
- Put API names, classes, methods, constants, and parameters in code font, linked where possible.
- Format string literal values in code font with double quotes, e.g. `"wrap_content"`.
- Match the spelling/casing of class names exactly as they appear in code.
- Don't pluralize a class name directly — instead say something like "Intent objects."
- Lowercase generic/common terms that aren't literal code identifiers (e.g., "activities").

## Classes, interfaces, and structs

- Open with a short sentence stating the class's purpose without just repeating its name, and without filler like "this class does/will."
- Avoid mid-sentence abbreviations like "e.g." — spell out "for example."
- Keep the opening sentence unique, descriptive, and short enough to work well if extracted into a class list.
- After the opening sentence, explain how to instantiate/invoke the type, describe key features, and note best practices or pitfalls.

## Members

- Keep member (constant/field) descriptions as brief as possible.
- Link to methods that make use of the constant or field.

## Methods

### Description
Pick an opening verb based on what the method does:
- Returns data → "Adds a new bird ... and returns ..."
- Boolean getter → "Checks whether ..."
- Non-boolean getter → "Gets the ..."
- Setter with no return value → "Sets the ..."
- Update → "Updates the ..."
- Delete → "Deletes the ..."
- Registers a callback → "Registers ..."
- Is itself a callback → "Called by ..." (with more detail on when subclasses implement it)
- Convenience constructor → "Creates a ..."

Always write method descriptions in present tense.

### Parameters
- Capitalize the first word and end with a period.
- Non-boolean parameters: start with "The" or "A."
- Boolean parameters that trigger an action: "If true, [does X]. If false, [does Y]."
- Boolean parameters that describe state: "True if ...; false otherwise."
- When there's a default, explain each possible value, then note the default explicitly.

### Return values
- Non-boolean: start with "The ..."
- Boolean: "True if ...; false otherwise."
- Keep it brief — put detailed explanation in the class description instead.

### Exceptions
- If the doc generator auto-inserts a "Throws" label, start the description with "If ..."
- Otherwise, start with "Thrown when ..."

## Deprecation notices

- Always name the recommended replacement — tell readers exactly what to use instead.
- Include a version number if your project tracks those.
- Give guidance on how to migrate existing code.
- Put the most important information first, since the first sentence is often surfaced in summaries; later sentences can explain why and add context.
- Example patterns: "Deprecated. Use `#CameraPose` instead." / "Deprecated. Access this field using the `getField` method."
