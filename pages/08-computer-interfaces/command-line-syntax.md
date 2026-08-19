---
title: "Command-line syntax"
source: "https://developers.google.com/style/code-syntax"
section: "Computer interfaces"
---

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
