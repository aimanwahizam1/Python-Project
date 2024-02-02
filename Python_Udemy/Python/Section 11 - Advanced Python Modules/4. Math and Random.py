# ---------------------------------------------------------------------------- #
#                                     Math                                     #
# ---------------------------------------------------------------------------- #

import math

value = 4.45
print(math.floor(value))
print(math.ceil(value))

pi = math.pi
e = math.e
infinity = math.inf

result = math.log(100,10)
print(result)

# ---------------------------------------------------------------------------- #
#                                    Random                                    #
# ---------------------------------------------------------------------------- #

import random

print(random.randint(1,100))

# To get the same random number, you need to set a seed
# random.seed(42)
print(random.randint(1,100))

# Get a random item in a list
my_list = [1,2,3,4,5,6]
print(random.choice(my_list))

# Getting multiple items
# With replacement (can get same number again)
print(random.choices(population=my_list, k=10))

# Without replacement
print(random.sample(population=my_list, k=4))

# Distributions
# Uniform distribution
print(random.uniform(1,100))

# Gaussian
print(random.gauss(1,1))