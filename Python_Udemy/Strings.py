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