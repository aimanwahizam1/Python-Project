# ---------------------------------------------------------------------------- #
#                                  While Loop                                  #
# ---------------------------------------------------------------------------- #

x = [1,2,3]

for item in x:
    #can use Pass as filler so no syntax error when coding
    #pass does nothing at all
    pass

my_string = 'Aiman'

for letter in my_string:
    if letter.lower() == 'a':
        #Use continue to go back to top of while loop
        continue
    print(letter)

for letter in my_string:
    if letter.lower() == 'm':
        #Use break to go get out of while loop
        break
    print(letter)