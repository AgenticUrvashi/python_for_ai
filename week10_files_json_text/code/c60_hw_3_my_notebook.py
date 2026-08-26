'restate: Notes app mein ek note add karo aur ek keyword se search karo.'

# example: text = Hi! my name is Urvashi.

# pseudocode:
            # 1.import my_notebook
            # 2.call my_notebook.save_notes("Hi! my name is Urvashi.")
            # 3.call my_notebook.search_notes("Hi! my name is Urvashi.")

# translate:
import my_notebook

my_notebook.save_notes("Hi! my name is Urvashi.")

my_notebook.search_notes("Hi! my name is Urvashi.")

# dry run:
# 2026-08-26 18:48:19,038 - INFO - Notes file notes.json loaded
# 2026-08-26 18:48:19,040 - INFO - Note saved to notes.json
# 2026-08-26 18:48:19,052 - INFO - Notes file notes.json loaded