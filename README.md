# Week 7 Assignment: Shopping List Manager

- `list_warmup.py`: demonstrates list indexing, appending, removing, and length checks.
- `shopping_list.py`: runs a small interactive shopping list manager with add, remove, show, and done options.
- `list_report.py`: prints the numbered list, counts long item names, and finds the longest item.

It is safer to check `in` before calling `.remove()` because removing an item that is not in the list raises a `ValueError` and crashes the program. This check keeps the program running smoothly and lets the user know the item is missing instead of stopping unexpectedly.
