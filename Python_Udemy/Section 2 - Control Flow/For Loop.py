# ---------------------------------------------------------------------------- #
#                                   For Loop                                   #
# ---------------------------------------------------------------------------- #

# ----------------------------------- List ----------------------------------- #

my_list = [1,2,3,4,5,6,7,8,9,10]

""" for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}') """

list_sum = 0

for num in my_list:
    list_sum += num

#print(list_sum)

# ---------------------------------- String ---------------------------------- #

my_string = 'Hello World'

""" for letter in my_string:
    print(letter) """

# ---------------------------------- Tuples ---------------------------------- #

#List of tuples
my_tuple_list = [(1,2),(3,4),(5,6),(7,8)]

#tuple impacting
""" for a,b in my_tuple_list:
    print(a)
    print(b) """

# ------------------------------- Dictionaries ------------------------------- #

my_dict = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}

#Returns keys
for item in my_dict:
    print(item)

#Returns items
for item in my_dict.items():
    print(item)

#tuple impacting 
for key,value in my_dict.items():
    print(key, value)

#Return values

for value in my_dict.values():
    print(value)