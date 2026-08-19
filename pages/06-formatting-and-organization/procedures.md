---
title: "Procedures"
source: "https://developers.google.com/style/procedures"
section: "Formatting and organization"
---

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
