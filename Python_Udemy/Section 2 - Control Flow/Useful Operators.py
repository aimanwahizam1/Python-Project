from random import shuffle, randint

# ---------------------------------------------------------------------------- #
#                               Useful Operators                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------- range() --------------------------------- #

""" for num in range(10):
    print(num) """

#now include starting number
""" for num in range(3,10):
    print(num) """

#can include step size
""" for num in range(0,11,2):
    print(num) """

#to quickly make a list with range
""" print(list(range(0,11,2))) """

# -------------------------------- enumerate() ------------------------------- #
#gives a running count of loops
#index counter

word ='abcde'

for index, letter in enumerate(word):
    print(index, letter)
    print(letter)

# ----------------------------------- zip() ---------------------------------- #
#pairs items in multiple lists

my_list = [1,2,3,4,5,6]
my_list2 = ['a','b','c']
my_list3 = [100,200,300]

#will only zip to the length of shortest list - e.g. ignores post 3 in my_list
for item in zip(my_list, my_list2, my_list3):
    print(item)

# ------------------------------------ in ------------------------------------ #
#returns boolean 

print('x' in my_list)

# ------------------------------ random library ------------------------------ #
#import at the top 

shuffle(my_list)
print(my_list)

my_rand_num = randint(0,100)
print(my_rand_num)

# ----------------------------------- input ---------------------------------- #

#input always takes it in as a string
result = input('Enter a random number:')
print(f'You entered {int(result)}')