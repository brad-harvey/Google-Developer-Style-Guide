---
title: "Cross-references and linking"
source: "https://developers.google.com/style/cross-references"
section: "Linking"
---

# Cross-references and linking

## Core principles

1. Favor giving context directly on the page over sending readers away with a link.
2. Write link text that clearly describes what the destination contains.
3. Links should open in the current tab by default; tell the reader explicitly if a link opens a new tab.
4. Keep links consistent (site-root-relative URLs) and avoid duplicating the same link unnecessarily.
5. Use HTTPS for external links, and mention it in the text if the destination is on a different domain when that matters.

## Choose links selectively

Every link is a decision point for the reader and adds cognitive load. Give the definition, brief explanation, or basic steps directly on the page instead of linking, when that's feasible.

Avoid linking the same destination more than once on a page, except when:
- Linking to a specific section further down.
- The page is long enough that a repeated link genuinely helps.
- There are multiple natural entry points (e.g., separate procedure and troubleshooting sections).

Link to the single most relevant destination rather than offering several links that serve the same purpose.

## Write descriptive link text

Two good patterns:

- **Match the destination's title or heading** — "For more information, see [Load balancing and scaling]."
- **Use a descriptive phrase**, front-loading the important words, capitalized as it would be in running text, and kept short — e.g., "...use Cloud Scheduler and Cloud Functions to manage [task scheduling on Compute Engine]."

Avoid:
- Vague link text like "this document," "this article," or "click here."
- Using a bare URL as the link text — link the title or a description instead.
- Splitting an abbreviation from its link — e.g., write "[Google Kubernetes Engine (GKE)]," not "[Google Kubernetes Engine] (GKE)."

When linking a CLI command, include a description alongside the code unless it reads awkwardly — e.g., "run the `gcloud instances create` command with the [`--hostname` flag]."

## Write link introductions

Use a consistent lead-in: "For more information, see..." or "For more information about..., see...". Add the "about ..." clause when the link text alone doesn't make the destination's purpose clear. Use "see," not "on," before the link.

- Preferred: "For more information about task scheduling, see [Reliable task scheduling...]"
- Avoid: "For more information on indexes, see..."

## Make the link's purpose clear

The surrounding text or the link text itself should explain why the reader would want to follow it — e.g., "For more information about authentication and authorization, see [Using OAuth 2.0...]"

## Call out unexpected link behavior

- **File downloads or email links** — say so, and mention the file type: "[download the security features PDF]" or "[send email to Technical Support]."
- **Same-page section links** — tell the reader it's an in-page jump: "see the [Write descriptive link text](#descriptive-link-text) section of this document."
- **Section on another page** — use the normal cross-reference phrasing, e.g., "see [Create a table]."
- **New-tab links** — explicitly flag it, e.g., "[Accessible content (opens in a new tab)]"; don't force a new tab silently.
- **External domains** — mention it in the text when it matters; don't rely on an icon alone.

## Don't use external-link icons

Mention "external" in the text instead, when it's worth calling out — e.g., "see [OS-level virtualization]," or occasionally "see the Wikipedia page about [OS-level virtualization]."

## Punctuation around link text

Keep punctuation outside the link itself.
- Preferred: "see [Test your code]."
- Avoid: "see [Test your code.]"

## Quotation marks and italics

Don't wrap linked cross-reference text in quotation marks — e.g., "see [Meet Android Studio]," not "see [\"Meet Android Studio\"]."

For references that aren't linked: use quotation marks for short works or sections, and italics for full-length works like books or movies.

## Avoid external links in navigation

Don't put links to outside your documentation set inside nav/TOC elements — place them within the page content instead. If an external nav link is unavoidable, make clear to the reader that it leaves the current documentation set.

## Style link text

- Make link color contrast clearly with body text.
- Underline only actual links — don't underline non-link text.
- Distinguish visited links with a color-blind-friendly treatment.
