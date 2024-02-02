# ---------------------------------------------------------------------------- #
#                             Importing from Module                            #
# ---------------------------------------------------------------------------- #

""" from mymodule import my_func

# Calling imported function
my_func() """

# ---------------------------------------------------------------------------- #
#                            Importing from Package                            #
# ---------------------------------------------------------------------------- #

# NOTE: To create a package you need to make a __init__.py
# This tells python that this is a package
# This is seen in MyMainPackage and MyMainPackage.SubPackage

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

some_main_script.report_main()
my_sub_script.sub_report()