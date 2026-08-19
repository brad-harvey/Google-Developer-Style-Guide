---
title: "Headings as link targets (make headings into link targets)"
source: "https://developers.google.com/style/headings-targets"
section: "Linking"
---

# Headings as link targets

## Why use a custom anchor

- It creates a shorter, cleaner anchor ID than an auto-generated one.
- It protects a frequently-linked heading from breaking if its wording changes later.
- In systems that auto-generate anchors from heading text, a custom anchor keeps existing links working even after the heading is edited.

## HTML

Three ways to set a custom anchor, in order of preference:
1. Wrap the heading in `<section id="anchor-id"></section>`.
2. Place `<a name="anchor-id"></a>` before or inside the heading.
3. Put an `id` attribute directly on the heading tag (works, but least preferred).

## Markdown

Append the anchor syntax to the end of the heading line: `{: #anchor-id }`.

## Naming an anchor

- Use lowercase letters only.
- Separate words with hyphens.
- Keep it short but meaningful — e.g., `conserve-habitat` rather than `help-conserve-habitat-for-pollinators`.

## Changing a heading that already has an anchor

If your system auto-generates anchors and you edit the heading text:
- Explicitly set the original anchor ID so it's preserved.
- Keep the existing custom anchor unless it contains wording you need to remove.
- Check your CMS for internal links that reference the old anchor if you do need to change it.
