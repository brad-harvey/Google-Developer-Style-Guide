---
title: "Figures and other images"
source: "https://developers.google.com/style/images"
section: "Formatting and organization"
---

# Figures and other images

## When to use an image
- Use images only when they add a visual explanation that's genuinely hard to convey in words.
- In screenshots, capture only the UI elements relevant to the discussion.
- Never use an image to show text that could just be text — code samples, terminal output, etc. should stay as real, selectable/searchable text.

## Creating images
- Prefer SVG for diagrams (scales cleanly); fall back to PNG if SVG isn't available.
- Avoid transparent backgrounds — they can misbehave with the site's lightbox viewer.
- For motion, prefer an efficient video format (e.g., MP4) over animated GIFs.
- Keep screenshots visually consistent across a doc set: same OS, same look, same drop-shadow treatment.
- Crop tightly to relevant content; exclude unrelated UI.
- Redact any personal/identifying information with a solid opaque overlay (not a blur or mosaic).
- Flatten layered export formats (PDF, TIFF) before use.
- Avoid image maps — accessibility and mobile-scaling problems; use a text list of links instead.
- Give image files descriptive filenames.

## Introducing images in text
- Precede most images with a full sentence that ends in a colon (if the image immediately follows) or a period (if other content, like a note, sits between the sentence and the image).
- Screenshots that immediately follow a step-by-step UI description can skip a separate intro sentence.

## Alt text
- Every image needs an `alt` attribute, even if it's empty (`alt=""`) for purely decorative images.
- Alt text should be a concise description (roughly 155 characters or less), written as a full sentence or noun phrase, punctuated normally.
- Don't prefix alt text with "Image of" or "Photo of," and avoid all-caps (some screen readers spell out capitalized words letter by letter).
- Don't put a diagram's introductory framing inside the alt text — that belongs in the surrounding paragraph.
- Alt text should describe the image's function in context, not just its literal contents.
- If 155 characters isn't enough, pair a short alt text with a longer visible text description nearby.
- Reuse identical alt text for the same recurring icon/control/status indicator across a document.

## Captions and figure numbers
- Captions and figure numbers are optional.
- If used, wrap the image and its caption together in a `figure`/`figcaption` structure.
- Format numbered captions as "Figure N. Description." with a complete sentence and closing punctuation.
- When numbering figures, refer back to them by number ("figure 2"), lowercase except at the start of a sentence — avoid spatial references like "the image above."
- Keep the caption text and any in-text reference to the figure separate rather than combined into one sentence.

## Figure descriptions
- Add a fuller text description near the image when the caption alone doesn't convey everything the figure shows.
- Any information the reader needs must also exist in surrounding text — don't let the image be the sole carrier of information.

## Text embedded in the image itself
- Minimize text baked into graphics — it hurts accessibility, search, and localization.
- Keep any embedded text brief; avoid full sentences, punctuation, invented abbreviations, and detailed callout annotations.
- Follow normal capitalization rules for any in-image titles, and use full/trademarked product names.

## High-resolution images
- Use `srcset` to serve higher-resolution versions to capable browsers, while keeping a standard-resolution `src` for compatibility.
- Point `src` at the 1x image; name the 2x version `basename_2x.ext`.
- The 2x image must be exactly double the width and height of the 1x image (within a pixel) — never just upscale the 1x version.
- Set the `width` attribute to the CSS display size; let height scale proportionally.
- If maintenance overhead is a concern, it's acceptable to use the 2x image for both `src` and `srcset`.

## Layout
- Use the site's standard CSS/layout rather than manual inline positioning.
- Don't shrink images excessively; consider how they'll look printed.
- Keep images within the page's column-width constraints, and get appropriately pre-sized images from designers when needed.
- Avoid linking to a same-page figure unless the page is long enough that the link travels a real distance.
- Left-align images rather than centering them, and don't nest `img` elements inside `p` elements.
