# ---------------------------------------------------------------------------- #
#                            Working with CSV Files                            #
# ---------------------------------------------------------------------------- #

import csv

# Steps:  
    # 1. Open csv
    # 2. csv.reader
    # 3. Reformat it into a python object list of lists

# Open the file
with open("C:/Users/aiman/Downloads/example.csv", encoding='utf-8') as csv_file:
    # csv.reader
    csv_data = csv.reader(csv_file)

    # Reformat into python object
    data_lines = list(csv_data)

# print(data_lines)
    
# Column names - first row
""" print(data_lines[0]) """
    
""" for line in data_lines:
    print(line) """

# Getting row 10
""" print(data_lines[10]) """

# Getting email example
""" print(data_lines[10][3]) """

# Getting all emails
""" all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails) """

# Getting full names
""" full_names = []

for line in data_lines[1:]:
    full_names.append(line[1] + " " + line[2])

print(full_names) """

# ---------------------------- Writing to CSV File --------------------------- #

""" with open('C:/Users/aiman/Downloads/to_save_file.csv', mode='w', newline='') as file_to_output:
    csv_writer = csv.writer(file_to_output, delimiter=",")

    # First write is column heading
    csv_writer.writerow(['a','b','c'])
    csv_writer.writerow([['1','2','3'],['4','5','6']]) """

# --------------------------- Appending to CSV File -------------------------- #

# Won't overwrite, just append
""" with open('C:/Users/aiman/Downloads/to_save_file.csv', mode='a', newline='') as file_to_output:
    csv_writer = csv.writer(file_to_output)
    csv_writer.writerow([['1','2','3'],['4','5','6']]) """


