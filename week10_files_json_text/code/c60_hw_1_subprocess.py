'restate: subprocess.run se python --version chalao (list form) aur output print karo.'

# example:python --version 

# pseudocode:
            # 1.import subprocess
            # 2.create variable money = subprocess.run(["python","--version"], capture_output=True, text=True)
            # 3.print(money.stdout.strip())

import subprocess

money = subprocess.run(["python","--version"], capture_output=True, text=True)

print(money.stdout.strip())

# dry run:
# Python 3.15.0b3