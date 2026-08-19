---
title: "Present tense"
source: "https://developers.google.com/style/tense"
section: "Language and grammar"
---

# Present tense

## Main rule
Use present tense for general behavior that isn't tied to a specific point in time.

Preferred: "Send a query to the service. The server sends an acknowledgment."
Avoid: "Send a query to the service. The server will send an acknowledgment."

## Exception: genuinely future actions
Future tense ("will") is fine when describing something that truly happens later.

Preferred: "Add the filename to the backup list. The file will be archived the next time the backup process runs."

## Exception: asynchronous operations
Future tense is also appropriate for delayed delivery or async behavior.

Preferred: "A message is sent that will notify any Pub/Sub subscribers."
Avoid: "A message is sent that notifies any Pub/Sub subscribers."

## Don't use future tense for "after the next release"
Avoid describing how a product will behave after a future release or update using future tense — describe current behavior instead.

## Avoid hypothetical "would"
Don't use conditional language like "would" to describe ordinary procedural results.

Preferred: "If you send an unsubscribe message, the server removes you from the mailing list."
Avoid: "You can send an unsubscribe message. The server would then remove you from the mailing list."
