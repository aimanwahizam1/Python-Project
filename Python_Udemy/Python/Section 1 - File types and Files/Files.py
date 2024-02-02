# ---------------------------------------------------------------------------- #
#                                     Files                                    #
# ---------------------------------------------------------------------------- #

# --------------------------- Working with test.txt -------------------------- #

#print(os.getcwd())
#Statement below means we do not need to .close() at end of code when we first .open()
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt') as myfile:
    contents = myfile.read()
    print('Reading for the first time:')
    print(contents + '\n')

    #to read again you need to reset cursor
    myfile.seek(0)
    print('Reading for the second time:\n' + contents)
    print('\n')

    #print as separate lines
    myfile.seek(0)
    print('Separate lines:\n', myfile.readlines())
    print('\n')

# #Variables are global
print('Global Reading:')
print(contents) """

# ---------------------------------------------------------------------------- #
#                           Files reading and writing                          #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Reading --------------------------------- #

""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt', mode='r') as myfile_read:
    contents_read = myfile_read.read()
    print(contents_read) """

# ---------------------------------- Writing --------------------------------- #

# NOTE: any writing will overwrite any existing text in the current file - Don't run this (illustration purpose only)
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt', mode='w') as myfile_read:
    contents_read = myfile_read.write('test write') """

# Fail Writing Case (also applies to Append)
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt', mode='r') as myfile_read:
    #.read will fail since we are in write mode (vice versa)
    contents_read = myfile_read.read()
    print(contents_read) """

# ---------------------------------- Append ---------------------------------- #

""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt', mode='a') as myfile_append:
    #.read will fail since we are in write mode (vice versa)
    contents_append = myfile_append.write('\n' + 'test append') """

# Read the append to see it in action
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/test.txt') as myfile:
    print(myfile.read()) """


# ---------------------------------------------------------------------------- #
#                       Files Part 2 - Methods in Action                       #
# ---------------------------------------------------------------------------- #

# 1. Read File (Original will only have 3 lines)
""" with open('C:/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/Text files/my_new_test.txt', mode='r') as my_new_file:
    print(my_new_file.read()) """

# 2. Append new line
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test.txt', mode='a') as my_new_file:
    my_new_file.write('\nFOUR ON FOURTH') """

# 3. Read will have new line 
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test.txt', mode='r') as my_new_file:
    print(my_new_file.read()) """

# NOTE: If file doesn't exist, this would make a new one with mode 'w'
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test_write.txt', mode='w') as my_new_file_write:
    my_new_file_write.write('I created this file!') """

""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test_write.txt', mode='r') as my_new_file_write:
    print(my_new_file_write.read()) """