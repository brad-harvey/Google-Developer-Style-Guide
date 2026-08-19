---
title: "UI elements and interaction"
source: "https://developers.google.com/style/ui-elements"
section: "Computer interfaces"
---

# UI elements and interaction

## Focus on the task, not the widget

Prefer describing what the reader should accomplish over naming the exact control, which keeps instructions clear and resistant to UI changes:
- "Refresh the page" rather than naming a specific refresh control.
- "Expand the **Advanced options** section" rather than describing the click target.

Give more mechanical detail only when the interaction itself is the point (e.g. "Click **Refresh**") or when the gesture genuinely isn't obvious (e.g. "To expand **Advanced options**, click the expander arrow").

## Formatting UI element names

- Bold every UI element name — buttons, menus, dialogs, windows, list items — using `<b>`/`**`, not `<strong>`, since bold here means "draw the eye," not "this is important."
- Outside of step-by-step procedures, give UI element references enough surrounding context to be understood on their own (say where the element lives, not just its name).

## Capitalization

- Convert all-caps UI labels to sentence case in your writing.
- If a label's capitalization is inconsistent across the product, standardize how you refer to it; otherwise, match the on-screen capitalization.

## Don't verb the UI

Don't use a UI element's name as if it were an English verb or noun on its own — pair it with a real verb: "Click **Save**," not "Save the settings" when "Save" is a button name; "In the **Name** field, enter the account name," not "Name the account."

## Terminology by element type

- **Window**: the whole app window, or a modular sub-window that can be opened separately.
- **Page**: a web page, or a console subpage — the preferred term for web contexts.
- **Dialog**: a smaller detached window that appears in front of other content.
- **Pane/panel**: a distinct rectangular region inside a larger window.
- **Section**: a labeled grouping of options within a window or pane.
- **Menu bar** vs. **menu**: the menu bar is the top-level row; a menu (e.g. **File**) contains commands and submenus. Menu items are called "commands," not "choices," "options," or "items."
- Use angle-bracket notation for menu paths within a single bold span, with a nonbreaking space before each bracket and an `aria-label="and then"` for screen readers — e.g. **View > Tools > Developer Tools**. Don't use this notation to describe interactions across different kinds of UI elements.
- **Navigation menu**: use this term consistently; avoid "navigation bar/pane/panel/window."
- **Toolbar**: a set of buttons for common actions; a toolbar button that opens a menu is a "menu button."
- **Buttons**: refer to a button by its label alone — "Click **OK**," not "Click the OK button."
- **Icons**: pair the icon with the name from its tooltip (tooltips matter both for accessibility and for making an icon findable at all); if the label is unclear, inspect the element for its ARIA label. Drop any ellipsis from the icon's name, and avoid directional language like "above" or "on the right" — use a screenshot if location is genuinely hard to describe otherwise.
- **Tab**: "the **Edit** tab."
- **Text box**: "the **Owner** box" (Google Cloud/Workspace docs say "field" instead of "box"); show entered text in code font.
- **List box**: "the **X** list" or "box." **Combo box**: "the **X** box," paired with "type or select" / "enter." **Spin box**: "the **X** box," paired with "enter."
- **Checkbox**: "the **X** checkbox." Prefer "select"/"clear" over the ambiguous "check"/"uncheck." Describe state as "selected" or "not selected."
- **Radio button**: refer to the button's own label or its group label, e.g. "Select **Do not remember passwords**."
- **Expander arrow** / **expandable section**: use these terms, not "expando" or "zippy." Avoid calling it out explicitly unless necessary.
- **Toggle**: don't use "toggle" as a verb — describe the actual action, and state explicitly which position ("Click the **Magic mode** toggle to the on position") since the starting state may not be obvious.

## Keyboard keys

- Mark keys and combinations with `<kbd>`.
- Capitalize letter keys ("Press Control+S," not "Control+s").
- Use `code` font, not `<kbd>`, for characters the user types as literal input.
- Use the key's name ("press Esc"), adding "the ... key" only if it reduces ambiguity.
- Spell out modifier key names (Command, Control, Option, Shift) rather than using symbols.
- Format combinations as `MODIFIER+KEY_NAME`; when Shift is involved, use `MODIFIER+Shift+KEY_NAME`.
- Give the macOS equivalent in parentheses after a Windows/Linux shortcut, e.g. "Press Control+C (or Command+C on macOS)."
- Spell out easily-confused characters in shortcuts (comma, hyphen, period, plus) instead of using the symbol.
- "Keyboard shortcut" and "key combination" are both fine, interchangeably.
- Use "press" for triggering a key/shortcut, and "enter" or "type" for entering text.

## Prepositions with UI elements

- Use "in" with dialogs, fields, lists, menus, panes, and windows — "In the **Alert** dialog, click **OK**."
- Use "on" with pages, tabs, and toolbars — "On the **Create instance** page, click **Add**."

## Verbs in procedures

Approved action verbs include: Click, Choose, Drag, Enable, Enter/type, Go to, Hold the pointer over, Press, Select, Tap, Turn on/off. See the word list for definitions of each.
