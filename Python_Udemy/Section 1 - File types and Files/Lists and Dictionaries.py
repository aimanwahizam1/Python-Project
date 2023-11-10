my_list = [1,2,3]

# ---------------------------------------------------------------------------- #
#                                 Dictionaries                                 #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                          Accessing Dictionary Values                         #
# ---------------------------------------------------------------------------- #

my_dict = {
    "name":"Aiman",
    "age":24
}

print(my_dict["name"])

# ---------------------------------------------------------------------------- #
#                      Accessing Dictionary Values Part 2                      #
# ---------------------------------------------------------------------------- #

# Can hold lists and dictionaries inside dictionaries
my_dict_two = {
    "name": "Aiman",
    "lived places": ["Malaysia", "Qatar", "UK", "UAE"],
    "siblings": [
        {
            "name": "Aisyah",
            "age": 21,
            "relation": "Sister"
        },
        {
            "name": "Akmal",
            "age": 13,
            "relation": "Brother"
        }
    ]
}

# NOTE: f statements are used to print WITH VALUES in more understandable way
print(f"Places I have lived: {my_dict_two['lived places']}")

# NOTE: calling a value of a dict inside a dict is NEXT TO and not in (nested)
print(f'Age of my sister is {my_dict_two["siblings"][0]["age"]}')

# More advanced example
print(f"Age of my {my_dict_two['siblings'][0]['relation'].lower()} is {my_dict_two['siblings'][0]['age']}")

# NOTE: calling a value of a list inside a dict is next to and not in 
print(f"Last placed I have lived is {my_dict_two['lived places'][-1]}")

# ---------------------------------------------------------------------------- #
#                      Accessing Dictionary Values Part 3                      #
# ---------------------------------------------------------------------------- #

# To get all keys
keys = my_dict_two.keys()
print(keys)

# To get all values
values = my_dict_two.values()
print(values)

# To get all pairs
items = my_dict_two.items()
print(items)

# ---------------------------------------------------------------------------- #
#                            Adding to a Dictionary                            #
# ---------------------------------------------------------------------------- #

# Adding new key value pair
my_dict_two["hobbies"] = ["gaming", "climbing"]
print(my_dict_two)

# Overwrite key value pair
my_dict_two["name"] = "Aiman Wahizam"
print(my_dict_two)

# Advanced example
my_dict_two["siblings"][0]["name"] = "Aisyah Wahizam"
print(my_dict_two)