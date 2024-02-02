# ---------------------------------------------------------------------------- #
#                          Timing Code for Performance                         #
# ---------------------------------------------------------------------------- #

# Example code (same functionality):
def func1(n):
    return [str(num) for num in range(n)]

print(func1(10))

def func2(n):
    return list(map(str, range(n)))

print(func2(10))

# ------------------------- 1. Tracking Time Elapsed ------------------------- #

import time

# Steps:
    # 1. Find current time before
    # 2. Run code
    # 3. Find current time after
    # 4. Find difference in time

# 1.
start_time = time.time()

# 2.
result = func1(1000000)

# 3.
end_time = time.time()

# 4. 
elapsed_time = end_time - start_time

print(f'For function 1, the time to calculate is {elapsed_time}s.')

# 1.
start_time = time.time()

# 2.
result = func2(1000000)

# 3.
end_time = time.time()

# 4. 
elapsed_time = end_time - start_time

print(f'For function 2, the time to calculate is {elapsed_time}s.')

# NOTE: not as accurate

# ----------------------------- 2. timeit module ----------------------------- #

import timeit

# Statement is the code you want to time (note it is in 3" string)
    # NOTE: It will be run over and over again, so no need to use 1000000 to see non-negligible difference
stmt = """
func1(100)
"""

# Setup is the code you want to run before the statement
    # NOTE: It will only be ran once
setup = """
def func1(n):
    return [str(num) for num in range(n)]
"""

func1_timeit = timeit.timeit(stmt, setup, number=1000000)

# For func2:
stmt2 = """
func2(100)
"""

setup2 = """
def func2(n):
    return list(map(str, range(n)))
"""

func2_timeit = timeit.timeit(stmt2, setup2, number=1000000)

print(f'\nUsing timeit:\nfun1: {func1_timeit}s.\nfunc2: {func2_timeit}s.')