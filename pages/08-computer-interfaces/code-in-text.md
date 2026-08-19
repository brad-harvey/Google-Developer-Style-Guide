---
title: "Code in text"
source: "https://developers.google.com/style/code-in-text"
section: "Computer interfaces"
---

# Code in text

## Overview

Use code font (HTML `<code>` or Markdown backticks) to mark up code-related terms inside ordinary prose. It tells readers something must be entered verbatim, marks the boundaries of a code term, and visually separates it from surrounding words.

## Use code font for

- Attribute names and values — e.g. the `imageURL` attribute, an `e2-highcpu-16` machine type
- Class names — e.g. the `SnapshotDiskOperator` class
- Command output / terminal responses
- Command-line utility names — `gcloud`, `gsutil`, `kubectl`, `bq`
- Data types — e.g. `STRUCT`
- Database column/row/table names
- Defined constants and their values — e.g. a `city` constant set to `"San Francisco"`
- DNS record types — e.g. `AAAA` records
- Element names (HTML/XML tags) — `script`, `body`, `ClinicalDocument`
- Enum names/values
- Environment variable names
- Filenames and paths
- Folder/directory names
- HTTP content-type values
- HTTP status codes — "an HTTP `400 Bad Request` status code"
- HTTP verbs — `POST`, `GET`
- IAM role names
- IP addresses
- Language keywords (e.g. SQL's `FROM`)
- Method and function names
- Namespace aliases
- Placeholder variables
- Package names
- Port numbers
- Query parameters
- Literal strings used as command input, including URLs/domains typed as input
- Text a reader types into a UI field
- A UI value that echoes prior code-font input

## Don't use code font for

- Domain names mentioned in ordinary narrative (example.com)
- Product or service names (Google Docs, Google Sheets)
- URLs meant for the reader to navigate to in a browser

## Conditional cases

- **Booleans**: use code font for the literal values `true`/`false`/`1`/`0`, but not when just discussing a boolean condition in the abstract.
- **Command-line tools**: code-font the command itself (`gcc`, `curl`, `apt`), but use regular text for the name of the broader software project.
- **Email addresses**: code font when shown as literal input/output (`alex@example.com`); plain text with a link when it's a contact address.

## Code that's also a UI element

When a term is both a code element and a UI label, apply both code font and bold, e.g.: "In the **Network** list, select **`my-net-2`**."

## Method names

Skip the class name when referencing a method unless it's needed for clarity — prefer "call its `get` method" over spelling out `animal.get`.

## HTTP status codes

- Single code: "an HTTP `400 Bad Request` status code"
- Range shorthand: "an HTTP `2xx` or `400` status code"
- Explicit range: "HTTP status code in the `200`–`299` range"
- Always say "status code," not "response code" or "error code."

## Grammar around code elements

Don't inflect a code element itself (don't add 's or plural endings directly to it). Instead add a plain noun after it and inflect that noun:
- Preferred: "The `ADDRESS` constant's value is defined ..."
- Avoid: "`ADDRESS`'s value is defined ..."

Don't use a code element as if it were an English verb.

## Linking Android API terms

Link the first mention of an Android API element (in code font, via an HTML link); later mentions stay in code font without a link. Don't link very common classes like `Activity` or `Intent` every time. Link an attribute to the specific widget/layout reference entry, and link a method using its fragment identifier (e.g. `#onCreate(android.os.Bundle)`).
