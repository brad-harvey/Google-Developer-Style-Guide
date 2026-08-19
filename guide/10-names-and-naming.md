# Names and naming

[← Back to index](../STYLE_GUIDE.md)

## On this page

- [Example domains and names](#example-domains-and-names)
- [Filenames](#filenames)
- [Trademarks](#trademarks)

---

## Example domains and names

*Source: [https://developers.google.com/style/examples](https://developers.google.com/style/examples)*

# Example domains and names

## Key principle

Never use real or personally identifiable information in examples — including domain names, email addresses, and phone numbers. Always use fictitious placeholders instead.

## Domains to use in examples

- IANA-reserved documentation domains: `example.com`, `example.org`, `example.net`
- Additional Google-owned example domains: `altostrat.com`, `examplepetstore.com`, `example-pet-store.com`, `myownpersonaldomain.com`, `my-own-personal-domain.com`, `cymbalgroup.com`
- For internationalized examples, use an IDN Test TLD and Punycode-encode non-ASCII characters (e.g. `xn--kgbechtv`).

## Email addresses

Pair one of the example domains above with a name from the example person-name list (e.g. `dana@example.com`). Generic mailbox names like `support@example.net` are fine too. Don't build example addresses out of real product names or invented brand-like names.

## Person names

- A pool of 30 gender-neutral given names is provided for use in examples: Alex, Amal, Ariel, Bola, Charlie, Cruz, Dana, Dani, Hao, Ira, Izumi, Jie, Kai, Kalani, Kim, Kiran, Lee, Lucian, Luka, Mahan, Noam, Nur, Quinn, Raha, Rosario, Sasha, Tal, Taylor, Tristan, Yuri.
- When a surname is needed, use just an initial after the given name (e.g. "Quinn N.").
- Use they/their/theirs rather than gendering example people, and avoid specifying gender unless the example genuinely requires it. Don't default to a gender binary, and be mindful that some names carry cultural gender connotations. Don't let names imply stereotypes about job role or ethnicity.
- Reserve "Alice" and "Bob" for cases that are specifically referencing the classic cryptography/security-protocol characters.

## Company names

Use "Example Organization" as a generic company name; when you need to distinguish two, qualify it, e.g. "Enterprise Example Organization" vs. "Startup Example Organization."

## Phone numbers

Use US numbers in the reserved fictional range 800-555-0100 through 800-555-0199. Never use a real phone number in an example.

## IP addresses

- IPv4 (RFC 5737 documentation ranges): `192.0.2.0`–`192.0.2.255`, `198.51.100.0`–`198.51.100.255`, `203.0.113.0`–`203.0.113.255` (as CIDR: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`).
- IPv6 (RFC 3849 documentation range): addresses like `2001:db8::` and `2001:db8:1:1:1:1:1:1`, within the `2001:db8::/32` block.

## Street addresses

The guide supplies a few ready-made fictional addresses (in Mountain View, CA; Lisbon; and Paris) for use in examples.

## Project names

Give example projects meaningful, descriptive names relevant to the reader's own context — avoid empty placeholders like "foo," "bar," or "baz." When you need several related examples, a numbered scheme works (e.g. "staging," "production-1," "production-2").

## Service account IDs

Use the numeric placeholder `123456789012345678901` when a unique-looking service account ID is needed.

---

## Filenames

*Source: [https://developers.google.com/style/filenames](https://developers.google.com/style/filenames)*

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

---

## Trademarks

*Source: [https://developers.google.com/style/trademarks](https://developers.google.com/style/trademarks)*

# Trademarks

## Follow the owner's usage rules

Always follow whatever usage guidelines the trademark's owner publishes. For Google's own trademarks, defer to Google's official trademark/permissions guidance.

## Use trademarks only as modifiers

- A trademark should modify a noun, not stand in for one — e.g. write "a Chromebook notebook computer," not "a Chromebook" on its own.
- Never turn a trademark into a possessive or plural, or otherwise alter its form (avoid something like "Chromebook's features...").
- Never use a trademark as a verb (avoid something like "google it").

---
