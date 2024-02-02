import random

# -------------------------------- Question 1 -------------------------------- #

# Create a generator that generates the squares of numbers up to some number N.

""" def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x) """

# -------------------------------- Question 2 -------------------------------- #

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).

""" def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for number in rand_num(1,10,12):
    print(number) """

# -------------------------------- Question 3 -------------------------------- #

# Use the iter() function to convert the string below into an iterator:

""" s = 'hello'

s_iterable = iter(s)

print(next(s_iterable))
print(next(s_iterable))
print(next(s_iterable))
print(next(s_iterable))
print(next(s_iterable)) """
