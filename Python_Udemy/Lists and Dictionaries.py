my_list = [1,2,3]

# ---------------------------------------------------------------------------- #
#                                 Dictionaries                                 #
# ---------------------------------------------------------------------------- #

my_dict = {
    "name":"Aiman",
    "age":24
}

print(my_dict["name"])

# Can hold lists and dictionaries inside dictionaries
my_dict_two = {
    "name": "Aiman",
    "lived places": ["Malaysia", "Qatar", "UK"],
    "siblings": {
        "Aisyah": 21,
        "Akmal": 13
    }
}

print(f"Places I have lived: {my_dict_two['lived places']}")

#Note calling a value of a dict inside a dict is next to and not in 
print(f"Age of my sister is {my_dict_two['siblings']['Aisyah']}")

#Note calling a value of a list inside a dict is next to and not in 
print(f"Last placed I have lived is {my_dict_two['lived places'][-1]}")

#adding new key value pair
my_dict_two["hobbies"] = ["gaming", "climbing"]
print(my_dict_two)

#overwrite key value pair
my_dict_two["name"] = "Aiman Wahizam"
print(my_dict_two)

#to get all keys
keys = my_dict_two.keys()
print(keys)

#to get all values
values = my_dict_two.values()
print(values)

#to get all pairs
items = my_dict_two.items()
print(items)