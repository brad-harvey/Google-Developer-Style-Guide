---
title: "Example domains and names"
source: "https://developers.google.com/style/examples"
section: "Names and naming"
---

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
