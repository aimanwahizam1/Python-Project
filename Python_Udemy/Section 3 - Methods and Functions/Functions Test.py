# Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
    return (4/3)*math.pi*(rad**3)

#print(vol(2))

# Write a function that checks whether a number is in a given range (inclusive of high and low)

#Returns statement version
def ran_check_1(num,low,high):
    if num >= low and num <= high:
        return f'{num} is in the range between {low} and {high}'
    
#print(ran_check_1(5,2,7))
#print(ran_check_1(3,1,10))

#Returns boolean version
def ran_check_2(num,low,high):
    return num >= low and num <= high

#print(ran_check_2(5,2,7))
#print(ran_check_2(3,1,10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    counter_dictionary = {
        'upper': 0,
        'lower': 0
    }

    for character in s:
        if character.isalpha():
            if character.isupper():
                counter_dictionary['upper'] += 1
            else:
                counter_dictionary['lower'] += 1
    
    return f'Original String: {s} \nNo. of Upper case characters: {counter_dictionary["upper"]} \nNo. of Lower case characters: {counter_dictionary["lower"]} '

#print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))

#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
    output = 1

    for number in numbers:
        output *= number

    return output

#print(multiply([1, 2, 3, -4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    return s.replace(" ","") == s[::-1].replace(" ","")

#print(palindrome('nurses run'))
#print(palindrome('hello'))

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    letters = set(str1.lower().replace(" ",""))

    if len(alphabet) == len(letters.intersection(alphabet)):
        return True

#print(ispangram("The quick brown fox jumps over the lazy dog"))
#print(ispangram("Pack my box with five dozen liquor jugs"))







