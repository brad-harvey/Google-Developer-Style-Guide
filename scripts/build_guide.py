#!/usr/bin/env python3
"""Consolidate extracted per-page files into linked section files + master index."""
import os
import re
import glob

ROOT = os.environ.get("GDS_ROOT") or os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
PAGES_DIR = os.path.join(ROOT, "pages")
GUIDE_DIR = os.path.join(ROOT, "guide")
os.makedirs(GUIDE_DIR, exist_ok=True)

SECTION_TITLES = {
    "01-introduction": "Introduction",
    "02-key-resources": "Key resources",
    "03-general-principles": "General principles",
    "04-language-and-grammar": "Language and grammar",
    "05-punctuation": "Punctuation",
    "06-formatting-and-organization": "Formatting and organization",
    "07-linking": "Linking",
    "08-computer-interfaces": "Computer interfaces",
    "09-html-and-css": "HTML and CSS",
    "10-names-and-naming": "Names and naming",
}

def slugify(text):
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"')
    return fm, body.strip()

# Pass 1: collect all pages, build source-url -> (section_dir, anchor, guide_file) map
pages = []  # list of dicts: section_dir, path, fm, body
for section_dir in sorted(os.listdir(PAGES_DIR)):
    full_section = os.path.join(PAGES_DIR, section_dir)
    if not os.path.isdir(full_section):
        continue
    for fpath in sorted(glob.glob(os.path.join(full_section, "*.md"))):
        with open(fpath, encoding="utf-8") as f:
            raw = f.read()
        fm, body = parse_frontmatter(raw)
        pages.append({
            "section_dir": section_dir,
            "path": fpath,
            "fm": fm,
            "body": body,
        })

url_to_target = {}
for p in pages:
    src = p["fm"].get("source", "")
    guide_filename = f"{p['section_dir']}.md"
    anchor = slugify(p["fm"].get("title", os.path.basename(p["path"])))
    p["anchor"] = anchor
    p["guide_filename"] = guide_filename
    if src:
        # normalize both full URL and path-only forms
        path_only = src.replace("https://developers.google.com", "")
        url_to_target[src] = (guide_filename, anchor)
        url_to_target[path_only] = (guide_filename, anchor)

def relink(body, current_guide_filename, current_source=""):
    current_source_clean = current_source.split("#")[0].rstrip("/")

    def repl(match):
        full = match.group(0)
        link_text = match.group(1)
        url = match.group(2)
        url_clean = url.split("#")[0].rstrip("/")
        # A page linking to its own source URL means the live original, not a
        # pointer back to itself. Rewriting it would produce a useless anchor.
        if current_source_clean and url_clean in (
            current_source_clean,
            current_source_clean.replace("https://developers.google.com", ""),
        ):
            return full
        target = url_to_target.get(url_clean)
        if not target:
            # try with /style prefix normalization
            target = url_to_target.get(url_clean.replace("https://developers.google.com", ""))
        if target:
            guide_filename, anchor = target
            if guide_filename == current_guide_filename:
                return f"[{link_text}](#{anchor})"
            else:
                return f"[{link_text}]({guide_filename}#{anchor})"
        return full
    # matches [text](url) where url looks like a developers.google.com/style link
    pattern = re.compile(r"\[([^\]]+)\]\((https?://developers\.google\.com/style[^\s)]*|/style/[^\s)]*)\)")
    return pattern.sub(repl, body)

# Pass 2: write section files
section_order = sorted(SECTION_TITLES.keys())
master_toc_lines = []

for section_dir in section_order:
    section_title = SECTION_TITLES[section_dir]
    section_pages = [p for p in pages if p["section_dir"] == section_dir]
    guide_filename = f"{section_dir}.md"
    out_path = os.path.join(GUIDE_DIR, guide_filename)

    lines = [f"# {section_title}", "", "[← Back to index](../STYLE_GUIDE.md)", ""]
    toc = ["## On this page", ""]
    for p in section_pages:
        title = p["fm"].get("title", "Untitled")
        toc.append(f"- [{title}](#{p['anchor']})")
    lines.extend(toc)
    lines.append("")
    lines.append("---")
    lines.append("")

    master_toc_lines.append(f"### [{section_title}]({guide_filename})")
    for p in section_pages:
        title = p["fm"].get("title", "Untitled")
        source = p["fm"].get("source", "")
        body = relink(p["body"], guide_filename, source)
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"*Source: [{source}]({source})*")
        lines.append("")
        lines.append(body)
        lines.append("")
        lines.append("---")
        lines.append("")
        master_toc_lines.append(f"- [{title}]({guide_filename}#{p['anchor']})")
    master_toc_lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")

# Pass 3: write master index
master_lines = [
    "# Google Developer Documentation Style Guide — Condensed Reference",
    "",
    "A condensed, reorganized reference to the [Google Developer Documentation Style Guide]"
    "(https://developers.google.com/style), paraphrased from the original site and grouped to "
    "mirror its left-hand navigation. This is a working internal reference, not a verbatim copy — "
    "for exact original wording, follow the source link on any entry.",
    "",
    "The original guide is published by Google and, except as otherwise noted on its pages, its "
    "content is licensed under the [Creative Commons Attribution 4.0 License]"
    "(https://creativecommons.org/licenses/by/4.0/); code samples are licensed under the "
    "[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). This reference attributes "
    "all guidance to Google's original style guide accordingly.",
    "",
    "Per-page source extracts (one file per original page, mirroring the site's nav) live under "
    "[`pages/`](pages/). This index and the `guide/` section files are the condensed, cross-linked "
    "version of that same content.",
    "",
    "## Table of contents",
    "",
]
master_lines.extend(master_toc_lines)

with open(os.path.join(ROOT, "STYLE_GUIDE.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(master_lines).rstrip() + "\n")

print("Wrote", len(section_order), "section files and STYLE_GUIDE.md")
