# ---------------------------------------------------------------------------- #
#                                Special Methods                               #
# ---------------------------------------------------------------------------- #

# How do you use built in Python functions (len, print) with a user defined class?

class Book():

    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    # Special/Dunder/Magic methods:

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book was deleted")
    
b = Book("English 101", "Peter", 200)

# If you comment out the __str__ method, print will give you the memory location since this is the result of str(object instance)
# If you uncomment it, the special method allows you to print as the stated string representation
print(b)
print(str(b))

# Same thing with len
print(len(b))

# Same thing with del
del b