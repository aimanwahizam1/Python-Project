# ---------------------------------------------------------------------------- #
#                                      Map                                     #
# ---------------------------------------------------------------------------- #

# Example function
def square_number(num):
    return num ** 2

# Example list
numbers = [1,2,3]

# To work on this list with the function:
""" for number in numbers:
    print(square_number(number)) """

# Or you can use Map
# Map takes a function and an iterable list and loops list into function
""" squareNumberList = list(map(square_number,numbers))
print(f'{squareNumberList = }') """

# Example 2
""" def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    return string[0]

names = ['Andy', 'Eve', 'Sally']

splicedNames = list(map(splicer,names))
print(f'{splicedNames = }') """

# ---------------------------------------------------------------------------- #
#                                    Filter                                    #
# ---------------------------------------------------------------------------- #

# Similar to a map but returns a value based on TRUE or FALSE (boolean)
""" def check_even(num):
    return num % 2 == 0

myNumbers = [1,2,3,4,5]

filteredNumbers = list(filter(check_even,myNumbers)) """

# Returns numbers that gives TRUE in function
""" print(f'{filteredNumbers = }') """

# ---------------------------------------------------------------------------- #
#                                    Lambda                                    #
# ---------------------------------------------------------------------------- #

# Lambda expressions are anonymous - used ONE time and not given name or keyword

# Normal example
def square(num):
    return num ** 2

# Lambda example
lambda num: num ** 2

# Can combine map and lambda since it will be used once
""" squaredMapLambda = list(map(lambda num: num ** 2, myNumbers))
print(f'{squaredMapLambda}') """

# Can combine filter and lambda since it will be used once
""" filteredLambda = list(filter(lambda num: num % 2 == 0, myNumbers))
print(f'{filteredLambda = }') """




