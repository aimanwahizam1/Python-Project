# ---------------------------------------------------------------------------- #
#                               Working with PDF                               #
# ---------------------------------------------------------------------------- #

# NOTE: we primarily only READ PDF files, writing is rare and problematic

import PyPDF2

# NOTE: mode is read binary 
""" with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/PDF Folder/Working_Business_Proposal.pdf", mode='rb') as f:
    # Reading the PDF
    pdf_reader = PyPDF2.PdfReader(f)
    
    # Getting number of pages:
    # print(len(pdf_reader.pages))

    # Getting pages
    page_one = pdf_reader.pages[0]

    # Getting text on page
    page_one_text = page_one.extract_text() """

# print(page_one_text)
    
# ---------------------------- Adding to PDF file ---------------------------- #
    
# NOTE: can add pages but not amend text in existing pages
    
""" with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/PDF Folder/Working_Business_Proposal.pdf", mode='rb') as f:
    # Reading the PDF
    pdf_reader = PyPDF2.PdfReader(f)
    
    # Get the page
    first_page = pdf_reader.pages[0]

    # Initialise writer
    pdf_writer = PyPDF2.PdfWriter()

    # Add page to writer
    pdf_writer.add_page(first_page)

with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/PDF Folder/Some_Brand_New_File.pdf", mode='wb') as f:
    # Write into file what pdf writer has in it
    pdf_writer.write(f) """


# ------------------------------ Example Problem ----------------------------- #

# Get all the text in pdf file
""" pdf_text = []

with open("C:/Users/aiman/Python Project/Python_Udemy/Python/Section 14 - Working with PDF and Spreadsheet CSV/PDF Folder/Working_Business_Proposal.pdf", mode='rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)

    for num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[num]

        pdf_text.append(page.extract_text())

print(pdf_text) """






