'pathlib se ek folder banao aur usme ek file likho (write_text).'

# restate:pathlib se new folder banao aur usme ek file likho jiska naam write_text ho.
# example:

# pseudocode:
            # 1.from pathlib import Path
            # 2.file_path = Path("week10_files_json_text/code/hw/write_text")
            # 3.with open(file_path,'r) as f: print(f.read())

from pathlib import Path


file_path = Path("week10_files_json_text/code/hw/write_text")
# print(file_path.exists())
with open(file_path,"r") as f:
    print(f.read())


# dry run:
# hi!