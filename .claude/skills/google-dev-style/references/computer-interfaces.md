# Computer interfaces

## On this page

- [API reference code comments](#api-reference-code-comments)
- [Code in text](#code-in-text)
- [Code samples](#code-samples)
- [Command-line syntax](#command-line-syntax)
- [Placeholder formatting](#placeholder-formatting)
- [UI elements and interaction](#ui-elements-and-interaction)

---

## API reference code comments

*Source: [https://developers.google.com/style/api-reference-comments](https://developers.google.com/style/api-reference-comments)*

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

---

## Code in text

*Source: [https://developers.google.com/style/code-in-text](https://developers.google.com/style/code-in-text)*

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

---

## Code samples

*Source: [https://developers.google.com/style/code-samples](https://developers.google.com/style/code-samples)*

# Code samples

## Basic guidelines

- Follow the relevant language's style guide for indentation; generally prefer spaces over tabs, commonly two spaces per level (some ecosystems use four, or tabs — defer to that language's convention).
- Wrap code lines around 80 characters so they read well in narrow windows or printouts.
- Mark code blocks as preformatted: use `<pre>` in HTML, or indent every line by four spaces in Markdown (a fenced code block also works).
- To show omitted code, use a language-appropriate comment rather than an ellipsis or three literal dots, and don't make blocks with omissions "click to copy."

## Introducing a sample

- End the lead-in sentence with a colon when the code immediately follows it.
- Use a period instead if other content comes between the lead-in and the code, or if the lead-in's last sentence isn't directly describing the sample.

## Style guides to follow

Defer to the relevant public language style guide (Google publishes ones for C++, HTML/CSS, Java, JavaScript, Python, and more — see the full list on GitHub). Some projects use their own override, such as Android's AOSP Java style guide — follow the project-specific guide when one exists.

---

## Command-line syntax

*Source: [https://developers.google.com/style/code-syntax](https://developers.google.com/style/code-syntax)*

# Command-line syntax

## Best practices

- Link to the full command reference from your introductory text or step, e.g. "To connect to the instance, use the `gcloud compute ssh` command:"
- Keep non-reference examples minimal — include only the arguments needed for the common case, and point readers to the full reference for everything else.
- Make click-to-copy examples runnable as-is: avoid optional, mutually exclusive, or repeatable-argument syntax in them, and use placeholders instead of anything the reader would need to edit out.

## Formatting a command

- Use `<pre>` in HTML or a fenced code block in Markdown.
- If a line runs past ~80 characters, break it before certain characters and indent continuation lines four spaces, using the shell's continuation character (backslash-space on Linux/Cloud Shell, caret-space on Windows).
- Document placeholders in a following description list, and follow standard end-punctuation rules for that list.
- Follow Google's shell style guide for quoting conventions in bash/sh commands.

## Command prompt

- Start each line of a multi-line input with the prompt symbol; you can disable text selection on the prompt via CSS so it doesn't get copied along with the command.
- Don't show the current directory before the prompt, except when you need to signal a context change (e.g., moving from a local shell to a remote one).
- A prompt is optional for a single-line command, but be consistent about whether you use one throughout a document.
- Keep command input and its output in separate code blocks.

## Optional arguments

- Enclose an optional argument in square brackets; if there are several, bracket each separately, e.g. `gcloud dns GROUP [GLOBAL_FLAG] [FILENAME]`.
- Leave optional arguments out of click-to-copy examples, since unremoved brackets will break the command.

## Mutually exclusive arguments

- Show a forced choice with curly braces and pipes, e.g. `{FILE_1|FILE_2}`, meaning the reader must pick exactly one.
- Avoid this syntax in click-to-copy commands for the same reason as optional arguments.

## Repeatable arguments

- Use three dots with no surrounding spaces (`...`) to show a value can repeat, e.g. `gcloud dns GROUP [GLOBAL_FLAG ...]`.
- Leave the ellipsis notation out of click-to-copy examples.

## Handling optional arguments in click-to-copy commands

Four options, in rough order of preference:
1. Strip optional arguments down to what's needed for the common case, and link to the full reference.
2. Provide separate code blocks, one per common variation.
3. Split the variations into separate tasks/sections.
4. If none of the above fit, flag explicitly that optional arguments are present and explain what the reader needs to remove.

## Command output

- Include output only when it's useful — e.g. the reader needs to copy a value or verify a result — and skip it otherwise.
- Introduce it with something like "The output is similar to the following:" or "The output is the following:"
- Show omitted output lines with three dots on their own line.

## Command-line terminology

- Describe what a whole command accomplishes rather than walking through each token, unless the reader genuinely needs to know the individual element names.
- For `gcloud`: a **command group** organizes related commands (e.g. `ml-engine`); a **command** is the executable operation; a **flag** is any element other than the group/command names; an **argument** is a value passed to a command or flag. "Flag" is Google Cloud–specific terminology; "option" is the more general catch-all term used elsewhere.
- For Linux commands, keep terminology simple given how complex real command syntax can get. Rough vocabulary: **command name** (the operation), **argument/path** (a value or location), **option** (a hyphen-prefixed element, e.g. `-follow`), **metacharacter** (globbing symbols like `*`, `?`, `^`), **pipe** (`|`, sends output to another command), and **redirection symbols** (`>`, `<`, `<<`, `>>`).

## Linux signals — don't substitute alternate wording

- **SIGKILL**: kills a process immediately; can't be caught, blocked, or ignored. Don't call it cancel/end/exit/quit/stop/terminate.
- **SIGTERM**: requests termination, allowing child-process cleanup. Don't call it cancel/end/exit/quit/stop.
- **SIGQUIT**: sent from the keyboard to quit a process; some processes can catch/block/ignore it. Don't call it cancel/end/exit/quit/stop.
- **SIGINT**: interrupts a process immediately, terminating by default unless handled/ignored/caught. Don't call it suspend/end/exit/pause/terminate.
- **SIGPAUSE**: tells a process to sleep until a signal arrives. Don't call it cancel/interrupt.
- **SIGSUSPEND**: temporarily suspends execution, useful for blocking delivery during critical sections. Don't call it pause/exit.
- **SIGSTOP**: stops a process so it can be resumed later; can't be caught, blocked, or ignored. Don't call it cancel/end/exit/interrupt/quit/terminate.

---

## Placeholder formatting

*Source: [https://developers.google.com/style/placeholders](https://developers.google.com/style/placeholders)*

# Placeholder formatting

Placeholders stand in for values the reader must substitute with their own input.

## Avoid the letter "x" as a generic placeholder

Use a descriptive placeholder name instead of "x" or "xx." The one common exception is a case like HTTP status code ranges, where "xx" is already conventional (e.g. `5xx`).

## Placeholders inline in text

- For code samples/commands: wrap in `<code><var>PLACEHOLDER_NAME</var></code>` in HTML, or use backtick+italic styling in Markdown.
- For non-code text: just use `<var>PLACEHOLDER_NAME</var>`.

## Placeholders inside code blocks

- HTML: wrap the whole block in `<pre>` and tag each placeholder with `<var>`.
- Markdown: a fenced code block works, but note you can't apply bold/italic styling inside it, which limits how you can mark placeholders there.

## Naming placeholders

- Use uppercase words joined with underscores, e.g. `API_NAME`, `METHOD_NAME`.
- Avoid hyphens, lowercase, or camelCase forms like `API-name`, `api_name`, `apiName`.
- Leave out possessive adjectives — don't write `MY_API_NAME` or `YOUR_API_NAME`.
- Keep surrounding punctuation (brackets, braces, ellipses) outside the `<var>` tag.

## Explaining placeholders

- For a single placeholder: "Replace `PLACEHOLDER` with a description of what the placeholder represents."
- For multiple placeholders: introduce with "Replace the following:" then list each one in the order it appears, formatted as `PLACEHOLDER`: description (lowercase start), using an em dash or "such as" to add examples where useful.
- For placeholders that show up in sample output: introduce with "This output includes the following values:" and follow the same list format as above.

---

## UI elements and interaction

*Source: [https://developers.google.com/style/ui-elements](https://developers.google.com/style/ui-elements)*

# UI elements and interaction

## Focus on the task, not the widget

Prefer describing what the reader should accomplish over naming the exact control, which keeps instructions clear and resistant to UI changes:
- "Refresh the page" rather than naming a specific refresh control.
- "Expand the **Advanced options** section" rather than describing the click target.

Give more mechanical detail only when the interaction itself is the point (e.g. "Click **Refresh**") or when the gesture genuinely isn't obvious (e.g. "To expand **Advanced options**, click the expander arrow").

## Formatting UI element names

- Bold every UI element name — buttons, menus, dialogs, windows, list items — using `<b>`/`**`, not `<strong>`, since bold here means "draw the eye," not "this is important."
- Outside of step-by-step procedures, give UI element references enough surrounding context to be understood on their own (say where the element lives, not just its name).

## Capitalization

- Convert all-caps UI labels to sentence case in your writing.
- If a label's capitalization is inconsistent across the product, standardize how you refer to it; otherwise, match the on-screen capitalization.

## Don't verb the UI

Don't use a UI element's name as if it were an English verb or noun on its own — pair it with a real verb: "Click **Save**," not "Save the settings" when "Save" is a button name; "In the **Name** field, enter the account name," not "Name the account."

## Terminology by element type

- **Window**: the whole app window, or a modular sub-window that can be opened separately.
- **Page**: a web page, or a console subpage — the preferred term for web contexts.
- **Dialog**: a smaller detached window that appears in front of other content.
- **Pane/panel**: a distinct rectangular region inside a larger window.
- **Section**: a labeled grouping of options within a window or pane.
- **Menu bar** vs. **menu**: the menu bar is the top-level row; a menu (e.g. **File**) contains commands and submenus. Menu items are called "commands," not "choices," "options," or "items."
- Use angle-bracket notation for menu paths within a single bold span, with a nonbreaking space before each bracket and an `aria-label="and then"` for screen readers — e.g. **View > Tools > Developer Tools**. Don't use this notation to describe interactions across different kinds of UI elements.
- **Navigation menu**: use this term consistently; avoid "navigation bar/pane/panel/window."
- **Toolbar**: a set of buttons for common actions; a toolbar button that opens a menu is a "menu button."
- **Buttons**: refer to a button by its label alone — "Click **OK**," not "Click the OK button."
- **Icons**: pair the icon with the name from its tooltip (tooltips matter both for accessibility and for making an icon findable at all); if the label is unclear, inspect the element for its ARIA label. Drop any ellipsis from the icon's name, and avoid directional language like "above" or "on the right" — use a screenshot if location is genuinely hard to describe otherwise.
- **Tab**: "the **Edit** tab."
- **Text box**: "the **Owner** box" (Google Cloud/Workspace docs say "field" instead of "box"); show entered text in code font.
- **List box**: "the **X** list" or "box." **Combo box**: "the **X** box," paired with "type or select" / "enter." **Spin box**: "the **X** box," paired with "enter."
- **Checkbox**: "the **X** checkbox." Prefer "select"/"clear" over the ambiguous "check"/"uncheck." Describe state as "selected" or "not selected."
- **Radio button**: refer to the button's own label or its group label, e.g. "Select **Do not remember passwords**."
- **Expander arrow** / **expandable section**: use these terms, not "expando" or "zippy." Avoid calling it out explicitly unless necessary.
- **Toggle**: don't use "toggle" as a verb — describe the actual action, and state explicitly which position ("Click the **Magic mode** toggle to the on position") since the starting state may not be obvious.

## Keyboard keys

- Mark keys and combinations with `<kbd>`.
- Capitalize letter keys ("Press Control+S," not "Control+s").
- Use `code` font, not `<kbd>`, for characters the user types as literal input.
- Use the key's name ("press Esc"), adding "the ... key" only if it reduces ambiguity.
- Spell out modifier key names (Command, Control, Option, Shift) rather than using symbols.
- Format combinations as `MODIFIER+KEY_NAME`; when Shift is involved, use `MODIFIER+Shift+KEY_NAME`.
- Give the macOS equivalent in parentheses after a Windows/Linux shortcut, e.g. "Press Control+C (or Command+C on macOS)."
- Spell out easily-confused characters in shortcuts (comma, hyphen, period, plus) instead of using the symbol.
- "Keyboard shortcut" and "key combination" are both fine, interchangeably.
- Use "press" for triggering a key/shortcut, and "enter" or "type" for entering text.

## Prepositions with UI elements

- Use "in" with dialogs, fields, lists, menus, panes, and windows — "In the **Alert** dialog, click **OK**."
- Use "on" with pages, tabs, and toolbars — "On the **Create instance** page, click **Add**."

## Verbs in procedures

Approved action verbs include: Click, Choose, Drag, Enable, Enter/type, Go to, Hold the pointer over, Press, Select, Tap, Turn on/off. See the word list for definitions of each.

---
