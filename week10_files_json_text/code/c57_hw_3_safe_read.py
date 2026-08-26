'safe_read jaise function banao jo ek allowed folder ke bahar ke path ko reject kare.'

# restate:ek function banao jo path ke aalava koi aur folder access na kare.
# example:

# pseudocode:
            # 1.from pathlib import Path
            # 2.create function safe_read():main_folder = Path("week10_files_json_text/code/data").resolve()
            # 3.create variable file_name = input("enter the file: ")
            # 4.create another variable file_path = (main_folder / file_name).resolve()
            # 5.if file_path.is_relative_to(main_folder): info = file_path.read() then print(info)
            # 6.else: print(access denied)
            # 7.call the function safe_read()

from pathlib import Path

def safe_read()->None:
    main_folder = Path("week10_files_json_text/code/data").resolve()

# print(main_folder.exists())

    file_name = input("enter the file: ")
    file_path = (main_folder / file_name).resolve()

    if file_path.is_relative_to(main_folder):
        info = file_path.read_text()
        print(info)

    else:
        print("Access denied")

safe_read()

# dry run:
# enter the file: ../my_utils.txt
# Access denied