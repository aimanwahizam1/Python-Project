import csv
import PyPDF2
import re

# Step 1. Get link from csv file diagonal

with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/CVS Folder/find_the_link.csv") as f:
    csv_data = csv.reader(f)

    data_lines = list(csv_data)

# print(data_lines)

link = ""
n = 0

for i in range(len(data_lines)):
    link += data_lines[i][n]
    n += 1

print(link)

# Step 2. Getting phone number in PDF
with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/PDF Folder/Find_the_Phone_Number.pdf", mode='rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)

    phone_number_format = r'\d{3}\.\d{3}\.\d{4}'

    for num in range(len(pdf_reader.pages)):
        match = re.search(phone_number_format, pdf_reader.pages[num].extract_text())

        if match:
            print(match.group())
            print(f'Found on page {num}')
            break



