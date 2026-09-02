'Restate: Ek Status enum banao (PENDING, DONE, FAILED).'

# example: PENDING = "pending" ; DONE = "done" ; FAILED = "failed"

# pseudocode:
            # 1.from enum import Enum
            # 2.create class Status inherit from Enum
            # 3.PENDING = "pending" ; DONE = "done" ; FAILED = "failed"
            # 4.print(Status.PENDING.value) ; print(Status.DONE.value) ; print(Status.FAILED.value)

# translate:
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"

print(Status.PENDING.value)
print(Status.DONE.value)
print(Status.FAILED.value)

# dry run:
# Pending
# done
# failed