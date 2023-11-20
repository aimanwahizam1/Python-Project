# ---------------------------------------------------------------------------- #
#                                  Inheritance                                 #
# ---------------------------------------------------------------------------- #

# Inheritance is a way to FORM NEW CLASSES from PRE-DEFINED CLASSES
# NOTE: allows to reuse code and reduce complexity

# Creating a base class

class Animal():

    def __init__(self) -> None:
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

""" my_animal = Animal() """

""" my_animal
my_animal.eat()
my_animal.who_am_i() """

# New classes can use the base class to inherit some of its method you want to use again
# E.g. making an inherited class
# NOTE: this is known as a "Derived Class"

class Dog(Animal):

    def __init__(self) -> None:
        super().__init__()
        print("Dog Created")

    # NOTE: You can overwrite existing methods:
    def who_am_i(self):
        print("I am a dog")

    # NOTE: You can also add on new methods:
    def bark(self):
        print("Woof!")

""" my_dog = Dog() """

""" my_dog
my_dog.eat()
my_dog.who_am_i()
my_dog.bark() """

# ---------------------------------------------------------------------------- #
#                                 Polymorphism                                 #
# ---------------------------------------------------------------------------- #

# This is the way that different object classes can SHARE method names

class Cow():

    def __init__(self, name) -> None:
        self.name = name

    def speak (self):
        return f"{self.name} says Moo!"
    
class Sheep():

    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        return f"{self.name} says Baa!"
    
""" belle = Cow("Belle")
shaun = Sheep("Shaun") """

""" print(belle.speak())
print(shaun.speak()) """

# To call the same method you can make a function that calls that method
# NOTE: We call in different objects but execute the specific object methods

""" def animal_speak(animal):
    print(animal.speak()) """

""" animal_speak(belle)
animal_speak(shaun) """

# ------------------------------- Best Practice ------------------------------ #

# We first make an ABSTRACT class
# I.E a class that is not expected to not have any instance, just inherited

class FarmAnimal():

    def __init__(self, name) -> None:
        self.name = name

    # This method does nothing unless a subclass inherit and overwrite
    # NOTE: Further reinforces the fact this class is abstract/base and is not meant to have instances
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
# How the above abstract class is meant to be used:

class Chicken(FarmAnimal):
    
    # NOTE: Child classes do not need to call __init__, unless needs to be overwritten

    def speak(self):
        return f"{self.name} says Buck!"

class Duck(FarmAnimal):

    def speak(self):
        return f"{self.name} says Quack!"    
    
clark = Chicken("Clark")
donald = Duck("Donald")

print(clark.speak())
print(donald.speak())