string = "hello"

#####Slicing and indexing
first_letter = string[0]

#This shows that you can use negative index to go from the back
all_but_last_letter = string[:-1]
print(first_letter)
print(all_but_last_letter)

#####.format()
print("The {} {} {}".format("fox", "brown", "quick"))

#you can also make it .format ref the in the correct order
print("The {2} {1} {0}".format("fox", "brown", "quick"))

#you can also use variables for .format
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

#you can also do this with variables
result = 10/3
print("10/3 = {result}".format(result=result))
#or
print("10/3 = {}".format(result))

#you can also edit the number of decimals places used in .format => {value called:width.precision f}
#width is how wide the result will be (normally 1)
#precision is decimal places (rounded up if needs be)
print("10/3 to the nearest 2 decimal places is {result:1.2f}".format(result=result))

#####fstrings
#same as above but different way
name = "Aiman"
age = 24
#Can write print("{name} is {age} years old".format(name=name, age=age))
#or print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")