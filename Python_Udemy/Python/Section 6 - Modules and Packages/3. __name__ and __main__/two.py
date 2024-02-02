# ---------------------------------------------------------------------------- #
#                             __name__ and __main__                            #
# ---------------------------------------------------------------------------- #

# Importing one.py in same directory
import one

print("Top Level in two.py")

one.myfunc()

if __name__ == "__main__":
    print("two.py is being run directly!")
else:
    print("two.py has been imported!")

# Print statement explanation:
    # 1. Prints out the top level of one.py (being called in the import line)
    # 2. Prints out the bottom else statement since one.py is imported (i.e. now __name__ is not __main__) (also being called in the import line)
    # 3. Prints out the top level of two.py
    # 4. Prints out one.myfunc() (being called explicitly in two.py)
    # 5. Prints out the condition of __name__ == "__main__" since this is being ran directly in two.py (if this was imported, you would get the case of the else statement)
