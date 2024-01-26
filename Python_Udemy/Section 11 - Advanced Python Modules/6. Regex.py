# ---------------------------------------------------------------------------- #
#                                     Regex                                    #
# ---------------------------------------------------------------------------- #

import re

# text = "The agent's phone number is 323-313-2456."

# ------------------------------- Find using re ------------------------------ #

""" pattern = "phone"
match = re.search(pattern, text)
print(match)
# NOTE: can get the exact location of the span
print(match.span())
# Start
print(match.start())
#End
print(match.end())

# Not found example
    # Returns None
not_in_text = "aaaa"
print(re.search(not_in_text,text)) """

# -------------------- Finding multiple instances using re ------------------- #

""" # NOTE: if there are multiple matches, we will get the FIRST
text2 = "hello aiman hello"
print(re.search("hello", text2))
# To find all matches:
    # This will return a list of instances
print(re.findall("hello", text2))

# NOTE: we can get the match for each iteration
for match in re.finditer("hello", text2):
    print(match)
    print(match.span()) """

# ---------------------------------------------------------------------------- #
#                               Building Patterns                              #
# ---------------------------------------------------------------------------- #
    
# e.g. phone number
my_phone_number = "My phone number is +971-058-536-3368."

# NOTE: assume we know the format but not the actual phone number
    # \d - digit
    # \w - alphanumeric (inc _)
    # \s - whitespace
    # \D - non digit (ABC)
    # \W - non alphanumeric (*-+=))

# NOTE: Quantifiers
    # + - Occurs one or more times (\w-\w+ -> A-B_1)
    # {3} - Occurs exactly 3 times (\d{3} -> 123)
    # {2,4} - Occurs 2 to 4 times (\d{2,3} -> 12 or 123 or 1234)
    # {3,} - Occurs 3 or more times (\d{3,} - 123 or 1234 or ...)
    # * - Occurs zero or more times (A*B*C* -> AACCCC)
    # ? - Occurs once or none (plurals? -> plural (s occurs none times))   

""" # Format for phone number in regex:
    # the {3} shows that it is \d\d\d (three in a row)
phone_number = r"\W\d{3}-\d{3}-\d{3}-\d{4}"
number_in_text = re.search(phone_number, my_phone_number)
print(number_in_text)

# NOTE: now we have found it, to find the number itself:
print(number_in_text.group()) """

# ---------------------------------- Compile --------------------------------- #

phone_pattern = re.compile(r'(\W\d{3})-(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, my_phone_number)
print(results)

# NOTE: With Compile since the regex expression are in "groups", we can call specific groups
# Good for pulling specific data points (e.g. country code from phone number)
    # NOTE: index starts at 1

# Calling whole number:
print(results.group())
# Calling specific groups
print(results.group(1))
print(results.group(2))
print(results.group(3))
print(results.group(4))

# ---------------------------------------------------------------------------- #
#                               Additional Syntax                              #
# ---------------------------------------------------------------------------- #

# -------------------------------- Or Operator ------------------------------- #

# This is used to search for x OR y in dataset
print(re.search(r'cat | dog', 'The dog is here'))

# ----------------------------- Wildcard Operator ---------------------------- #

# . replaces any character
print(re.findall(r'.at', 'The cat in the hat sat.'))
# Can use multiple
print(re.findall(r'...at', 'The cat in the hat sat.'))

# ------------------------- Starts and Ends Operators ------------------------ #

# This is used for "starts with" and "ends with"

# Starts with
print(re.findall(r'^\d', "2 is a number"))

# Ends with
print(re.findall(r'\d$', 'The number is 2'))

# ---------------------------- Exclusion Operator ---------------------------- #

# Exclude operator: [^...]
phrase = "There are 3 numbers 34 inside 5 this sentence"

pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

# NOTE: this is a common way of removing punctuations
test = "This is a string! But it has punctuation. How can we remove it?"
exclude_punctuation = r'[^!.?]+'

print(re.findall(exclude_punctuation, test))

# Exercise: return test phrase but cleaned
clean = re.findall(r'[^!.? ]+', test)
clean_phrase = " ".join(clean)
print(clean_phrase)

# ---------------------------- Inclusion Operator ---------------------------- #

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are!'

pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))


