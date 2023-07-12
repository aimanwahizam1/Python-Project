string = "hello"
first_letter = string[0]
all_but_last_letter = string[:-1]
print(first_letter)
print(all_but_last_letter)

#.format()
print("The {} {} {}".format("fox", "brown", "quick"))

#you can also make it .format ref the in the correct order
print("The {2} {1} {0}".format("fox", "brown", "quick"))