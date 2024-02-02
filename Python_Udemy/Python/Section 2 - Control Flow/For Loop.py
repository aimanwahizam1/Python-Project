# ---------------------------------------------------------------------------- #
#                                   For Loop                                   #
# ---------------------------------------------------------------------------- #

# ----------------------------------- List ----------------------------------- #

my_list = [1,2,3,4,5,6,7,8,9,10]

# Example for loop
""" for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}') """


# Example 2
list_sum = 0

""" for num in my_list:
    list_sum += num

print(list_sum) """

# ---------------------------------- String ---------------------------------- #

my_string = 'Hello World'

# This prints individual letter
""" for letter in my_string:
    print(letter) """

# ---------------------------------- Tuples ---------------------------------- #

#List of tuples
my_tuple_list = [(1,2),(3,4),(5,6),(7,8)]

# Tuple impacting
""" for a,b in my_tuple_list:
    print(a)
    print(b) """

# Different examples of printing tuples using for loops
""" for a in my_tuple_list:
    print(a) """

""" for a,b in my_tuple_list:
    print(a) """

# ------------------------------- Dictionaries ------------------------------- #

my_dict = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}

# Returns keys
for key in my_dict:
    print(key)

# Returns items
for item in my_dict.items():
    print(item)

# Tuple impacting in dictionary 
for key, value in my_dict.items():
    print(key, value)

# Return values
for value in my_dict.values():
    print(value)