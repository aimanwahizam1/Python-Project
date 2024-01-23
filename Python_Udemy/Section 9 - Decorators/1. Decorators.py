# IDEA: Say you have a function and then you want to add an EXTRA functionality
# Running the edited function will run old and new functionality
# NOTE: Decorators allows you to toggle functionalities within functions 
    # Run function with just old or with old and new functionalities
# Decorators allow you to add extra functionalities to an existing function
    # They use an @ operator

# ---------------------------------------------------------------------------- #
#                                  Decorators                                  #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                              Returning Functions                             #
# ---------------------------------------------------------------------------- #

# --------------------------------- Example 1 -------------------------------- #

""" def hello(name="Aiman"):
    print("The hello() function has been executed.")

    # A function inside another function
    def greet():
        return "\t This is the greet() function inside hello()"
    
    def welcome():
        return("\t This is welcome() function inside hello()")
    
    print("I am going to return a function")

    if name == "Aiman":
        return greet
    else:
        return welcome

new_func = hello("Aiman")

# NOTE: this shows that I have returned a function within a function to a variable function
print(new_func()) """

# --------------------------------- Example 2 -------------------------------- #

""" # Function
def wow():
    # Function in a function
    def super_wow():
        return "I am super wow"
    
    # Returning a function
    return super_wow

# Assigning embedded function
some_func = wow()
print(some_func()) """

# ---------------------------------------------------------------------------- #
#                            Functions as Arguments                            #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Example --------------------------------- #

""" def hello():
    return "Hi Aiman"

# Passing in a function as an argument
def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

# NOTE: passing in function - NOT EXECUTING (i.e. passing hello not hello())
other(hello) """

# ---------------------------------------------------------------------------- #
#                                  Decorators                                  #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Example --------------------------------- #

# NOTE: think of decorators as "decorations"/"wrapping paper" for functions
    # They add extra code/functionalities to an existing functions either before or after

""" def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_function = new_decorator(func_needs_decorator)
decorated_function() """

# ------------------------------- Proper Syntax ------------------------------ #

# Same logic as above but with proper syntax

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

# NOTE: the difference is there is no assignment or use of argument
        # Since decorator function takes in func as argument can use @ operator
        # If you want to "toggle off" just comment out the @new_decorator line
func_needs_decorator()

# NOTE: Decorators are mainly used in web frameworks
    # Normally, we just need to understand pre-written funcs in libraries and we decorate our own functions