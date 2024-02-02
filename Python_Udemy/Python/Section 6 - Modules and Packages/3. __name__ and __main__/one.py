# ---------------------------------------------------------------------------- #
#                             __name__ and __main__                            #
# ---------------------------------------------------------------------------- #

def myfunc():
    print("Function in one.py")

print("Top Level in one.py")

# NOTE: If we are running code that is in this file (i.e DIRECTLY)
# Then python assigns __name__ to be __main__

# NOTE: This is a common code structure

if __name__ == "__main__":
    print("one.py is being run directly!")
else:
    print("one.py has been imported!")