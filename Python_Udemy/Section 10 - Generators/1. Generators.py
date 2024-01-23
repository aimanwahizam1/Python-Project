# ---------------------------------------------------------------------------- #
#                                  Generators                                  #
# ---------------------------------------------------------------------------- #

# Generators allows us to write a function that can send back a value
    # Then resume to pick up where it left off
# NOTE: Generates a sequence of values over time
# The difference in syntax is the use of "yield"

# Generators will automatically stop and resume execution around the last point of value generation
    # Advantage: instead of calculating all values upfront, generators will compute 1 and then wait until next value is called for

# --------------------------- "Normal Way" Example --------------------------- #

""" def create_cubes(n):
    result = []
    
    for x in range(n):
        result.append(x**3)

    return result

# NOTE: this has created a giant list in memory
print(create_cubes(10))

# Here we see that the print values are printed one by one
    # So no longer need a list in memory like above
for x in create_cubes(10):
    print(x)
 """

# ----------------------------- Generator Example ---------------------------- #

""" def create_cubes(n):
    for x in range(n):
        yield(x**3)

# NOTE: printing generator now won't give result
print(create_cubes(10))
# If we want to get a list like above then need to cast to list
print(list(create_cubes(10)))

# To get results, you need to ITERATE through the generator
# NOTE: same result as above
    # Now a lot more memory efficient!
for x in create_cubes(10):
    print(x) """

# ---------------------------- Generator Example 2 --------------------------- #
    
""" def generate_fib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

for number in generate_fib(10):
    print(number) """

# ---------------------------------------------------------------------------- #
#                                 Next Function                                #
# ---------------------------------------------------------------------------- #
    
""" def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

# We can assign the generator and get values one by one
    # Not holding anything in memory!
g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g)) """

# ---------------------------------------------------------------------------- #
#                                 Iter Function                                #
# ---------------------------------------------------------------------------- #

s = "hello"

""" for letter in s:
    print(letter) """
 
# We can iterate over a string using a for loop
    # But we cannot iterate using next()
# next(s)
    
# To iterate, we need to turn string into a generator
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))