---
title: "Filenames"
source: "https://developers.google.com/style/filenames"
section: "Names and naming"
---

# Filenames

## Naming files and directories

- Use lowercase names (with occasional consistency-driven exceptions), since some filesystems are case-sensitive and this improves searchability.
- Separate words with hyphens rather than underscores (e.g. `query-data.html`) — search engines treat hyphens as word breaks but often don't treat underscores that way.
- Stick to plain ASCII alphanumeric characters; avoid accented or special characters.
- Avoid vague, generic names like `document1.html`.

### Exceptions

- If a directory already uses underscores, match that existing convention (e.g. adding `lesson_4.jd` alongside an existing `lesson_1.jd`) rather than fixing naming project-wide.
- Auto-generated reference docs may use non-standard filenames dictated by the product or API's own structure — that's acceptable.

## Referring to files in text

- Put a specific filename in code font, and follow it with the word "file."
- Keep the filename's exact spelling even if it doesn't follow the naming guidelines above.
- Introduce a code sample with text that names the file it belongs to, e.g. "In the following `build.sh` file, modify the default values for all parameters:"

## Referring to file interactions

Don't turn a file type into a verb — say "extract a zip file," not "unzip a zip file."

## Referring to file types

Use the full file-type name rather than the extension — "a PNG file," not "a `.png` file." These names are often written in all caps when they come from an acronym (e.g. `.sh` → "Bash file," `.csv` → "CSV file").
