# ---------------------------------------------------------------------------- #
#                              Collections Module                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Counter --------------------------------- #

""" from collections import Counter

my_list = [1,1,1,1,1,2,2,2,3]
 
my_list_counter = Counter(my_list)
print(my_list_counter)

# NOTE: also works with strings
print(Counter("Hello Aiman".lower().split()))

letters = "aaaaaaabbbbcccccccccccccc"

c = Counter(letters)
# Return most common by ranking
print(c.most_common())
# Return unique elements
print(list(c))
 """

# -------------------------------- DefaultDic -------------------------------- #

""" from collections import defaultdict

normal_dict = {
    "a": 10
}

print(normal_dict["a"])
# The below should give you KeyError
# print(normal_dict["b"])

# NOTE: DefaultDic assigns default value to KeyError
    # Default value given by lambda
default_dict = defaultdict(lambda: 0)

default_dict["correct"] = 100
print(default_dict["correct"])

# The below will give default value for missing key
    # NOTE: will also make the missing key value pair
print(default_dict["wrong"])
print(default_dict) """

# -------------------------------- Namedtuple -------------------------------- #

from collections import namedtuple

# This creates a class based tuple
    # Where tuple values are given a "label" under that class
Dog = namedtuple("Dog", ["age", "breed", "name"])

sammy = Dog(age=5,breed="Husky", name="Sammy")

print(sammy)

# Calling tuple values
print(sammy.age)
# Same as above
print(sammy[0])

print(sammy.breed)
print(sammy.name)

