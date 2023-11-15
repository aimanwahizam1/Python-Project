# ---------------------------------------------------------------------------- #
#                                    Warmup                                    #
# ---------------------------------------------------------------------------- #

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

""" def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
            return min(a,b)
    else:
        return max (a,b) """
    
""" print(lesser_of_two_evens(2,10))
print(lesser_of_two_evens(2,17)) """

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

""" def animal_crackers(text):
    first_letters = [word[0].lower() for word in text.split()]
    return first_letters[0] == first_letters [1] """

""" print(animal_crackers("Levelheaded Llama"))
print(animal_crackers('Crazy Kangaroo')) """

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

""" def makes_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20 """
    
""" print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(12,8)) """

# ---------------------------------------------------------------------------- #
#                               Level 1 Problems                               #
# ---------------------------------------------------------------------------- #

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# Old solution - very lengthy

""" def old_macdonald(name):
    output = ''

    for letter in range(len(name)):
        if letter == 0 or letter == 3:
            output += name[letter].upper()
        else:
            output += name[letter]

    return output """

# New and improved solution
""" def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:] """

""" print(old_macdonald('macdonald'))
print(old_macdonald('aiman')) """

# MASTER YODA: Given a sentence, return a sentence with the words reversed

""" def master_yoda(text):
    words = text.split()
    return " ".join(words[::-1]) """

""" print(master_yoda('I am home'))
print(master_yoda('We are ready')) """

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

""" def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10 """

""" print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209)) """

# ---------------------------------------------------------------------------- #
#                               Level 2 Problems                               #
# ---------------------------------------------------------------------------- #

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# Old solution - holds unnecessary memory

""" def has_33(nums):
    current = 0

    for number in nums:
        if number == 3:
            while current == 3:
                return True
        current = number
    return False """

# New and improved solution

""" def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False """

""" print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3])) """

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

""" def paper_doll(text):
    output = ''

    # NOTE: to iterate over each letter just need to do this for loop
    for letter in text:
        output += letter*3

    return output """

""" print(paper_doll('Hello'))
print(paper_doll('Mississippi')) """

#BLACKJACK: Given three integers between 1 and 11, 
# if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# NOTE: Rewritten for readability 

""" def blackjack(a,b,c):
    total = a + b + c   

    if total > 21 and 11 in (a,b,c):
        total -= 10

    if total > 21:
        return "BUST"
    
    return total """
        
""" print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11)) """

# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.

# Old solution - holds too many memories

""" def summer_69(arr):
    sliced_array = []
    memory = 0
    output = 0

    for i in range(len(arr)):
        if arr[i] == 6:
            memory = arr[i]
        else:
            if memory == 6:
                if arr[i] == 9:
                    memory = arr[i]
            else:
                sliced_array.append(arr[i])

    if len(sliced_array) != 0:
        for number in sliced_array:
            output += number
        return output
    
    return 0 """

# New and improved solution

""" def summer_69(arr):
    total = 0
    current_6 = False
    
    for number in arr:
        if number == 6:
            current_6 = True
        
        if number == 9 and current_6:
            current_6 = False
        
        if not current_6:
            total += number
    
    return total """

""" print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([1, 2, 6, 9, 3])) """

# ---------------------------------------------------------------------------- #
#                             Challenging Problems                             #
# ---------------------------------------------------------------------------- #

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# Old solution - too complicated 

""" def spy_game(nums):
    array = []
    output = ''

    for number in nums:
        if number == 0 or number == 7:
            array.append(number)

    for number in array:
        output += str(number)

    if output == '007':
        return True
    return False """

# New and improved solution

""" def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False """

""" print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) """

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_prime(num):
    numbers = [number for number in range(2,num + 1)]
    counter = 0
    
    for number in numbers:
        for i in range(2, number + 1):
            if i != number:
                if number % i == 0:
                    break
            else:
                counter += 1
    return counter

#print(count_prime(500))

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

my_dict = {
    'A': '  *  \n * * \n*****\n*   *\n*   *',
    'B': '***  \n*  **\n***  \n*  **\n***  '
}

def print_big(letter):
    if letter.upper() in my_dict.keys():
        return(my_dict[letter.upper()])
        
print(print_big('a'))
print(print_big('b'))

