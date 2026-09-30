#!/usr/bin/env python3
"""Build the google-dev-style Claude skill from the consolidated guide/ files.

Copies each guide/ section into .claude/skills/google-dev-style/references/ under
a descriptive filename, strips repo-only navigation, splits the oversized
key-resources section away from the word list, and zips the result into a
distributable .skill bundle.

Run after scripts/build_guide.py so the references track the latest guide/ output.
"""
import os
import re
import shutil
import zipfile

ROOT = os.environ.get("GDS_ROOT") or os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
GUIDE_DIR = os.path.join(ROOT, "guide")
SKILL_DIR = os.path.join(ROOT, ".claude", "skills", "google-dev-style")
REFS_DIR = os.path.join(SKILL_DIR, "references")
DIST_DIR = os.path.join(ROOT, "dist")

# guide/ section file -> reference filename inside the skill
SECTION_TO_REFERENCE = {
    "01-introduction.md": "introduction.md",
    "02-key-resources.md": "key-resources.md",  # split below; word list is extracted
    "03-general-principles.md": "general-principles.md",
    "04-language-and-grammar.md": "language-and-grammar.md",
    "05-punctuation.md": "punctuation.md",
    "06-formatting-and-organization.md": "formatting-and-organization.md",
    "07-linking.md": "linking.md",
    "08-computer-interfaces.md": "computer-interfaces.md",
    "09-html-and-css.md": "html-and-css.md",
    "10-names-and-naming.md": "names-and-naming.md",
}

BACK_LINK = re.compile(r"^\[← Back to index\]\(\.\./STYLE_GUIDE\.md\)\n\n?", re.MULTILINE)
WORD_LIST_HEADING = "\n## Word list\n"


def clean(text):
    """Strip navigation that only makes sense inside the repo."""
    return BACK_LINK.sub("", text)


def split_word_list(text):
    """Return (key_resources_body, word_list_body).

    guide/02 concatenates product names, the text-formatting summary, and the
    full A-Z glossary. The glossary is over half the section and gets consulted
    on its own, so it ships as a separate reference file.
    """
    index = text.index(WORD_LIST_HEADING)
    head = text[:index].rstrip()
    # Drop the now-dangling table-of-contents entry.
    head = head.replace("- [Word list](#word-list)\n", "")
    head = head.rstrip().rstrip("-").rstrip() + "\n"

    tail = text[index:].lstrip("\n")
    tail = "# Word list\n\n" + tail.split("\n", 1)[1].lstrip("\n")
    return head, tail


def build_references():
    if os.path.isdir(REFS_DIR):
        shutil.rmtree(REFS_DIR)
    os.makedirs(REFS_DIR)

    written = []
    for section, reference in SECTION_TO_REFERENCE.items():
        with open(os.path.join(GUIDE_DIR, section), encoding="utf-8") as f:
            body = clean(f.read())

        if section == "02-key-resources.md":
            body, word_list = split_word_list(body)
            word_list_path = os.path.join(REFS_DIR, "word-list.md")
            with open(word_list_path, "w", encoding="utf-8") as f:
                f.write(word_list)
            written.append("word-list.md")

        with open(os.path.join(REFS_DIR, reference), "w", encoding="utf-8") as f:
            f.write(body)
        written.append(reference)

    return sorted(written)


def package():
    os.makedirs(DIST_DIR, exist_ok=True)
    bundle = os.path.join(DIST_DIR, "google-dev-style.skill")
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, _, filenames in os.walk(SKILL_DIR):
            for filename in sorted(filenames):
                full = os.path.join(path, filename)
                arcname = os.path.join(
                    "google-dev-style", os.path.relpath(full, SKILL_DIR)
                ).replace(os.sep, "/")
                zf.write(full, arcname)
    return bundle


if __name__ == "__main__":
    references = build_references()
    bundle = package()
    size = os.path.getsize(bundle)
    print(f"Wrote {len(references)} reference files to {REFS_DIR}")
    for reference in references:
        print(f"  {reference}")
    print(f"Packaged {bundle} ({size:,} bytes)")
