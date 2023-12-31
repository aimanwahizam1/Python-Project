# ---------------------------------------------------------------------------- #
#                                    Functions                                 #
# ---------------------------------------------------------------------------- #

# ------------------------------ Default Values ------------------------------ #

# You can provide a default value
""" def say_hello(name='Aiman'):
    print(f'Hello {name}') """

# NOTE: giving a value will overwrite default value
""" say_hello('Peepee') """

# NOTE: giving no value will print out default value
""" say_hello() """

# ---------------------------- Multiple Arguments ---------------------------- #

""" def add_num(num1, num2):
    return num1+num2 """

""" result = add_num(1,2)
print(result) """

# Example: Return all even numbers in a given list
""" def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(check_even_list([1,2,3])) """

# NOTE: as seen before, can use list comprehension
""" def even_list(num_list):
    return [number for number in num_list if number % 2 == 0]

print(even_list([1,2,3])) """

# ------------------------------ Tuple Unpacking ----------------------------- #

""" stock_prices = [('APPL',100), ('GOOG',200), ('MSFT',300)]

for ticker, price in stock_prices:
   print(f'{ticker = }')
   print(f'{price = }') """

# Example: Make a function where it returns the employee of the month based on their work hours
""" work_hours = [('Aiman',100), ('Bill', 200), ('Tanya', 300)]

def employee_of_the_month(work_hours):
    current_max = 0
    employee_of_month = ''

    # Iterate through list and keep memory of highest hours and the employee name
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)

name, hours = employee_of_the_month(work_hours)
print(name, hours) """

# -------------------- Example of Using Multiple Functions ------------------- #

# Ball in Cup Game
# NOTE: Redid the game in a separate py file 
# User has to guess which cup has a ball - e.g. which index of a list has 'O'

""" from random import shuffle

def shuffle_list(my_list):
    #Built in shuffle does not return
    shuffle(my_list)
    return my_list

three_cups = [' ', 'O', ' ']

def player_guess():
    guess = ''
    
    #check correct input
    #input takes in strings
    while guess not in ['0','1','2']:
        guess = input('Pick a number between 0 - 2')

    return int(guess)

def check_guess(shuffled_list, guess):
    if shuffled_list[guess] == 'O':
        print('Correct') 
    else:
        print('Wrong')
        print(shuffled_list)

#step 1. shuffle list
shuffled_list = shuffle_list(three_cups)

#step 2. player guess
input_guess = player_guess()

#step 3. check guess
check_guess(shuffled_list,input_guess) """

# ---------------------------- *args and **kwargs ---------------------------- #

# *args allows you to take in any number of arguments as a tuple
# Variable name DOESN'T have to be args, e.g. could be *num

""" def myfunc(*args):
    for item in args:
        print(item)
    return sum(args) * 0.1

print(myfunc(1,2))
print(myfunc(1,2,3))
print(myfunc(1,2,3,4)) """

# **kwargs allows you to take in any number of arguments as a dictionary
""" def myfunc2(**kwargs):
    print(f'{kwargs = }')
    if 'fruit' in kwargs:
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print('I did not find any fruits')

myfunc2(fruit='Apple', veggie='Lettuce') """

# Can use both in combination
# Since args is first you need to provide args first
""" def myfunc3(*args, **kwargs):
    print(f'{args = }')
    print(f'{kwargs = }')
    print(f'I would like {args[0]} {kwargs["food"]}')

myfunc3(10,2,3,4,fruit='orange',animal='cat',food='pizza') """