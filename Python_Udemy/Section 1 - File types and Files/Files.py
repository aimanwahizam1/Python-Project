# ---------------------------------------------------------------------------- #
#                                     Files                                    #
# ---------------------------------------------------------------------------- #

#Working with test.txt
#print(os.getcwd())
#Statement below means we do not need to .close() at end of code when we first .open()
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File typs and Files/test.txt') as myfile:
    contents = myfile.read()
    print(myfile.read())

    #to read again you need to reset cursor
    myfile.seek(0)
    print('Reading for the second time:\n' + myfile.read())

    #print as seperate lines
    myfile.seek(0)
    print('Separate lines:\n', myfile.readlines())

#Variables are global
print(contents) """

# ------------------------- Files reading and writing ------------------------ #

#Reading
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/test.txt', mode='r') as myfile_read:
    contents_read = myfile_read.read()
    print(contents_read) """

#Writing
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/test.txt', mode='w') as myfile_read:
    #.read will fail since we are in write mode (vice versa)
    contents_read = myfile_read.read()
    print(contents_read) """

#Append
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/test.txt', mode='a') as myfile_read:
    #.read will fail since we are in write mode (vice versa)
    contents_read = myfile_read.read()
    print(contents_read) """

# ---------------------------------- Part 2 ---------------------------------- #

""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test.txt', mode='r') as my_new_file:
    print(my_new_file.read()) """

#Append new line
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test.txt', mode='a') as my_new_file:
    my_new_file.write('\nFOUR ON FOURTH') """

#Read will have new line 
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test.txt', mode='r') as my_new_file:
    print(my_new_file.read()) """

#If file didnt exist, this would make a new one with mode 'w'
""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test_write.txt', mode='w') as my_new_file_write:
    my_new_file_write.write('I created this file!') """

""" with open('/c/Users/aiman/Python Project/Python_Udemy/Section 1 - File types and Files/my_new_test_write.txt', mode='r') as my_new_file_write:
    print(my_new_file_write.read()) """
