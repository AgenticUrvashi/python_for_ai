'Current folder ki saari .txt files list karo (glob).'

# restate: current folder me se txt file ki list banao.
# example:

# pseudocode:
            # 1.from pathlib import Path
            # 2.create variavle file_path = "week10_files_json_text/code"
            # 3.create another variable parent_folder = Path(file_path)
            # 4.create another variable txt_files = parent_folder.glob("*.txt")
            # 5.use for loop for file_path in txt_files: print(file_path.name)

from pathlib import Path

file_path = "week10_files_json_text/code"
parent_folder = Path(file_path)
# print(parent_folder.exists())

txt_files = parent_folder.glob("*.txt")

for file_path in txt_files:
    print(file_path.name)


# dry run:
# diary.txt
# my_first_file.txt