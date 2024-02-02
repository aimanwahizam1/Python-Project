# ---------------------------------------------------------------------------- #
#                                   Challenge                                  #
# ---------------------------------------------------------------------------- #

import shutil
import re
import os

# --------------------------- 1. Unzip instructions -------------------------- #

# shutil.unpack_archive("unzip_me_for_instructions.zip", "challenge_instructions", "zip")

# ----------------------- 2. Find phone number in files ---------------------- #

for folder, sub_folders, files in os.walk("c:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/challenge_instructions/extracted_content"):
    for f in files:
        with open(folder+"/"+f, "r") as new_file:
            contents = new_file.read()
            search = re.findall(r'\d{3}-\d{3}-\d{4}', contents)
            if search:
                print(search)
                print(f'The phone number is found in: {folder+"/"+f}')