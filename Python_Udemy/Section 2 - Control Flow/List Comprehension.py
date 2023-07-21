# ---------------------------------------------------------------------------- #
#                              List Comprehension                              #
# ---------------------------------------------------------------------------- #

#e.g. example on how to add to a list
my_string = 'Hello'
my_list = []

for letter in my_string:
    my_list.append(letter)

#print(my_list)

# ---------------------------- More efficient way ---------------------------- #

my_list2 =[letter for letter in my_string]
#print(my_list2)

my_list3 = [x for x in "word"]
#print(my_list3)

my_list4 = [number for number in range(0,11)]
#print(my_list4)

#You can perform operations on the element
my_list5 = [number**2 for number in range(0,11)]
#print(my_list5)

celsius = [0,25,40,100,-40]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
#print(fahrenheit)

#You can also add if statements
my_list6 = [number for number in range(0,11) if number%2==0]
#print(my_list6)

#You can also add if and else statements - WARNING the statement placement is flipped
my_list7 = [number if number%2==0 else 'ODD' for number in range(0,11)]
#print(my_list7)

# ------------------------------- Nested Lists ------------------------------- #

#e.g.
my_nested_list =[]

for x in [1,2,3]:
    for y in [1,10,100]:
        my_nested_list.append(x*y)

#print(my_nested_list)

# ------------------------------- Efficient way ------------------------------ #

my_nested_list2 = [x*y for x in [1,2,3] for y in [1,10,100]]
print(my_nested_list2)