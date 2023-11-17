# ---------------------------------------------------------------------------- #
#                                    Classes                                   #
# ---------------------------------------------------------------------------- #

# ---------------------------- Self and Attributes --------------------------- #

# NOTE: Use camel casing for class names
""" class Dog():

    # NOTE: A function inside a class is called a METHOD
    # Self refers any attributes to any instances of the class
    # NOTE: init is like a constructor in other languages
    # NOTE: -> None means that it will return None type
    def __init__(self, breed, name, spots) -> None:

        # This is an example of an ATTRIBUTE
        # We take in the argument and assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # This attribute is a BOOLEAN type (attributes can be any type)
        self.spots = spots """

# Creating an INSTANCE of a class
""" my_dog = Dog("Lab", "Archie", True) """
 
# This shows that the type of my_dog is Dog
""" print(type(my_dog)) """

# This shows that we have assigned an attribute from the __init__ method
""" print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots) """

# -------------------------- Class Object Attributes ------------------------- #

# NOTE: This is a continuation of the above
# Pasted above with new comments and learning specific to this section

""" class Dog():

    # Class Object Attributes are the SAME for ANY INSTANCE
    # NOTE: Don't need self keyword since this is true for any instance
    species = "Mammal"

    def __init__(self, breed, name, spots) -> None:

        self.breed = breed
        self.name = name
        self.spots = spots """

""" my_dog2 = Dog("Huskie", "Peter", False)
print(my_dog2.species) """

# ---------------------------------- Methods --------------------------------- #

""" class Dog():

    species = "Mammal"

    def __init__(self, breed, name, spots) -> None:

        self.breed = breed
        self.name = name
        self.spots = spots

    # Methods are functions inside a class
    # Takes the object into account by SELF
    # NOTE: To call "name" we connect it to the instance by self.name
    # NOTE: We can also call in an outside parameter by using that argument (it wont be part of self)
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and my dogtag number is {number}.") """
""" my_dog3 = Dog("Wolf", "Ben", False) """

# Calling the method
""" my_dog3.bark(10) """

# ---------------------------------- Summary --------------------------------- #

""" class Circle():

    # Class object attribute
    pi = 3.14

    # Constructor
    def __init__(self, radius) -> None:
        self.radius = radius

        # We can also give it an attribute that is not passed in
        # NOTE: calling pi (class object attribute) we use Circle.pi (class_name.class_attribute)
        self.area = (radius**2) * Circle.pi

    # Method
    def calculate_circumference(self):
        return self.radius * Circle.pi * 2 """
    

""" my_circle = Circle(10) """

""" print(my_circle.calculate_circumference())
print(my_circle.area) """
