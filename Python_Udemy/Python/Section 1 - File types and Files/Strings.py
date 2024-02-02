# ---------------------------------------------------------------------------- #
#                                    Strings                                   #
# ---------------------------------------------------------------------------- #

# Example String
string = "hello"

# --------------------------- Slicing and Indexing --------------------------- #

first_letter = string[0]
print(first_letter)

# You can use negative index to go from the back
all_but_last_letter = string[:-1]
print(all_but_last_letter)

# ---------------------------------------------------------------------------- #
#                                   Printing                                   #
# ---------------------------------------------------------------------------- #

# --------------------------------- .format() -------------------------------- #

# Gives places where values will slot in in print statements

print("The {} {} {}".format("fox", "brown", "quick"))

# Make .format ref the in the correct order
print("The {2} {1} {0}".format("fox", "brown", "quick"))

# Use variables for .format
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# Using variables as inputs
result = 10/3
print("10/3 = {result}".format(result=result))

# Or
print("10/3 = {}".format(result))

# NOTE: you can also edit the number of decimals places used in .format => {value called:width.precision f}
# Width is how wide the result will be (normally 1)
# Precision is decimal places (rounded up if needs be)
print("10/3 to the nearest 2 decimal places is {result:1.2f}".format(result=result))

# --------------------------------- fstrings --------------------------------- #

# Same as .format but different way (clearer)
name = "Aiman"
age = 24

# NOTE: In .format...
print("{name} is {age} years old".format(name=name, age=age))

# Or 
print("{} is {} years old".format(name, age))

# NOTE: In fstring...
print(f"{name} is {age} years old")
print(f"10/3 = {result:1.2f}")

# NOTE: For debugging its useful to do this:
# (this gives variable name and value) 
# (also works for lists and dictionaries)
print(f'{name=}')