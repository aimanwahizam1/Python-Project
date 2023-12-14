# ---------------------------------------------------------------------------- #
#                        Errors and Exceptions Homework                        #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                   Problem 1                                  #
# ---------------------------------------------------------------------------- #

# Handle the exception thrown by the code below by using try and except blocks.

""" for i in ['a','b','c']:
    print(i**2) """

""" ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int' """

# --------------------------------- Answer 1 --------------------------------- #

""" for i in ["a", "b", "c"]:
    try:
        print(i*2)
    except TypeError:
        print("TypeError!") """

# ---------------------------------------------------------------------------- #
#                                   Problem 2                                  #
# ---------------------------------------------------------------------------- #
        
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
        
""" x = 5
y = 0

z = x/y """

""" ---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero """

# --------------------------------- Answer 2 --------------------------------- #

""" x = 5
y = 0

try: 
    z = x/y
    print(z)
except ZeroDivisionError:
    print("You can't divide by Zero!")
finally:
    print("All Done.") """

# ---------------------------------------------------------------------------- #
#                                   Problem 3                                  #
# ---------------------------------------------------------------------------- #

# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

""" def ask():
    while True:
        try:
            number = int(input("Input an integer:"))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, your number squared is: ", number**2)
            break

ask() """