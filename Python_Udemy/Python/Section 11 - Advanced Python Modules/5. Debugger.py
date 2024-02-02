# ---------------------------------------------------------------------------- #
#                                   Debugger                                   #
# ---------------------------------------------------------------------------- #

import pdb

x = [1,2,3]
y = 2
z = 3

# ------------------------------ Inducing Error ------------------------------ #

# No error
# result = y + z

# Below should give an error
# result2 = x + y

# --------------------------------- Debugging -------------------------------- #

# No error
result_one = y + z

# Debugging result2
# When running with set_trace: in console you are able to call variables to see what they are
    # Useful since in long script you might lose track of what variable gives the error
        # NOTE: press q in console to get out of debugger
pdb.set_trace()
result_two = y + x



