# Shutil and OSModule allows you to work with files

# NOTE: This is the way to open files as seen before
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/test/test.txt', mode='w') as myfile_read:
    contents_read = myfile_read.write('test write')  """

# ---------------------------------------------------------------------------- #
#                              OSModule and shutil                             #
# ---------------------------------------------------------------------------- #

import os
import shutil

# --------------------------- Get working directory -------------------------- #
print(os.getcwd())

# -------------------------- List items in directory ------------------------- #
print(os.listdir("c:/Users/aiman/Python Project/Python_Udemy"))

# -------------------------------- Move items -------------------------------- #
# Originally test.txt is in test folder 
    # Moves it to test2
# shutil.move("C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/test/test.txt", "C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/test2")

# ------------------------------ Deleting items ------------------------------ #
# NOTE: deleting functions are irreversible
    # So good to use send2trash, this will send to trashbin 

import send2trash

# Originally test had trash.txt
# send2trash.send2trash("C:\\Users\\aiman\\Python Project\\Python_Udemy\\Section 11 - Advanced Python Modules\\test\\trash.txt")

# --------------------------- Get files and folders -------------------------- #
for folder, sub_folders, files in os.walk("c:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/test"):
    print(f"Currently looking at {folder}\n")
    print("The subfolders are: ")
    for sub_folder in sub_folders:
        print(f"\t Subfolder: {sub_folder}")
    print("The files are: ")
    for f in files:
        print(f"\t File: {f}")

    print("\n")
    