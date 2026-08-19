---
title: "Prescriptive documentation"
source: "https://developers.google.com/style/prescriptive-documentation"
section: "General principles"
---

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
