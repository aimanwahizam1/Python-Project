# ---------------------------------------------------------------------------- #
#                          Unzipping and Zipping Files                         #
# ---------------------------------------------------------------------------- #

# Creating the files 

""" with open("C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/zip/fileone.txt", mode= "w") as my_file:
           contents = my_file.write("Test file for unzipping and zipping lesson!")

with open("C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/zip/filetwo.txt", mode= "w") as my_file:
           contents = my_file.write("Test file two for unzipping and zipping lesson!") """

# ------------------------------- Zipping Files ------------------------------ #
           
import zipfile

# Creating a compressed file
""" compressed_file = zipfile.ZipFile("comp_file.zip", "w")

# Writing to compressed file
compressed_file.write("fileone.txt", compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write("filetwo.txt", compress_type=zipfile.ZIP_DEFLATED)

# NOTE: remember to close the file
compressed_file.close() """

# ------------------ Extracting Files from Compressed Folder ----------------- #

""" zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content") """



# ---------------------------------------------------------------------------- #
#                                    shutil                                    #
# ---------------------------------------------------------------------------- #

# NOTE: you would use shutil more often!

# ------------------- Using shutil to Zip an entire folder ------------------- #

import shutil

dir_to_zip = "C:/Users/aiman/Python Project/Python_Udemy/Section 11 - Advanced Python Modules/zip/extracted_content"

output_filename = "example"

shutil.make_archive(output_filename, "zip", dir_to_zip)

# ------------------------- Extracting zipped content ------------------------ #

shutil.unpack_archive("example.zip", "final_unzip", "zip")