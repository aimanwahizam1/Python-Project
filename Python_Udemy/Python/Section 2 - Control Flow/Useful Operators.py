from random import shuffle, randint

# ---------------------------------------------------------------------------- #
#                               Useful Operators                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------- range() --------------------------------- #

# 0 - 9 (up to and not including number)
""" for num in range(10):
    print(num) """

# Include starting number
""" for num in range(3,10):
    print(num) """

# Include step size
""" for num in range(0,11,2):
    print(num) """

# Quickly make a list with range
""" print(list(range(0,11,2))) """

# -------------------------------- enumerate() ------------------------------- #

# This gives a running count of loops
# A.K.A index counter

""" word ='abcde'

for index, letter in enumerate(word):
    print(index, letter)
    print(letter) """

# ----------------------------------- zip() ---------------------------------- #

# Pairs items in multiple lists

my_list = [1,2,3,4,5,6]
my_list2 = ['a','b','c']
my_list3 = [100,200,300]

# Will only zip to the length of shortest list - e.g. ignores post 3 in my_list
""" for item in zip(my_list, my_list2, my_list3):
    print(item) """

# ------------------------------------ in ------------------------------------ #

# Returns boolean 

print('x' in my_list)

# ------------------------------ random library ------------------------------ #

# NOTE: import at the top 

""" shuffle(my_list)
print(my_list) """

""" my_rand_num = randint(0,100)
print(my_rand_num) """

# ----------------------------------- input ---------------------------------- #

# Takes it in as a string
result = input('Enter a random number:')
print(f'You entered {int(result)}')