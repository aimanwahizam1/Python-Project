# ---------------------------------------------------------------------------- #
#                         Errors and Exception Handling                        #
# ---------------------------------------------------------------------------- #

# E.g. We write a script that READS a txt file with mode="r"
# BUT a user may try to WRITE to a file with this script
# This will give an error - NOW THE ENTIRE SCRIPT WILL STOP!

# NOTE: We can use Error Handling to let the script CONTINUE even with an error!

# --------------------------------- Keywords --------------------------------- #

# Try: block of code to be ATTEMPTED (may lead to an error)
# Except: block of code that will execute if there is an ERROR in the try block
# Finally: block of code EXECUTED REGARDLESS OF ERROR OR NOT

# ----------------------------- Example of Error ----------------------------- #

""" def add(n1,n2):
    print(n1+n2)

number1 = 10
number2 = input("Please provide a number:")

# NOTE: Calling this will give you an error, since number2 will be a string from input
add(number1,number2)

# NOTE: Any further code will not execute. See print statement below
print("I know there's an error above. So this won't print!") """

# ------------------------- Example of Error Handling ------------------------ #

""" def add(n1,n2):
    print(n1+n2)

try:
    # We want to attempt this code
    # It might have an error

    # Same code as above, and seen to provide an error (str + int)
    number1 = 10
    number2 = int(input("Please provide a number:"))
    add(number1,number2)
except:
    # NOTE: Will execute if THERE IS AN ERROR
    print("Hey it looks like you aren't adding correctly!")

# NOTE: Can add an else block to execute IF THERE ARE NO ERRORS
else:
    print("Adding successful!") """

# ------------------ Example of Error Handling with Finally ------------------ #

# If there is no testfile.txt in the directory, run the below block
""" try:
    f = open("C:/Users/aiman/Python Project/Python_Udemy/Section 7 - Errors and Exceptions Handling/testfile.txt", mode="w")
    f.write("Write a test line")

# NOTE: We can give a specific error in except block
except TypeError:
    print("There was a type error!")
except OSError:
    # NOTE: This is a permissions error (reading on a writing permission vice versa)
    print("Hey you have an OS Error!")

# NOTE: Finally block will always execute NO MATTER WHAT
finally:
    print("I always run!") """

# Once the above code has been ran once, testfile.txt would have been created
# If so run the below code to induce an error (OS Error)
""" try:
    f = open("C:/Users/aiman/Python Project/Python_Udemy/Section 7 - Errors and Exceptions Handling/testfile.txt", mode="r")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
except:
    print("All other exception!")
finally:
    print("I always run!") """

# --------------------- Error Handling inside a Function --------------------- #

# NOTE: Optional to mix else and finally block - sometimes its not needed!
""" def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number:"))
        except:
            print("Whoops that is not a number!")
            continue
        else:
            print("Thank you for your number!")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")

ask_for_int() """






