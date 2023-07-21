#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
s_words = [word for word in st.split() if word[0].lower() == 's']
#print(s_words)

#Use range() to print all the even numbers from 0 to 10.
even_numbers = [number for number in range(0,11,2)]
#print(even_numbers)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
numbers_divisible_3 = [number for number in range(0,50) if number%3==0]
#print(numbers_divisible_3)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
even_words = []

for word in st.split():
    if len(word) % 2 == 0:
        even_words.append("even!")
        continue
    even_words.append(word)

#print(even_words)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
numbers_list = [number for number in range(0,101)]
numbers_list_output =[]

for number in numbers_list:
    if number % 3 == 0:
        if number % 5 == 0:
            numbers_list_output.append("FizzBuzz")
        else:
            numbers_list_output.append("Fizz")
    elif number % 5 == 0:
      numbers_list_output.append("Buzz")
    else:
        numbers_list_output.append(number)

#print(numbers_list_output)

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
first_letters = [word[0] for word in st.split()]

print(first_letters)