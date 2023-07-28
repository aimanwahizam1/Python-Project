def myfunc(string):
    output = ''

    for i in range(len(string)):
        if i % 2 == 0:
            output += string[i].upper()
        else:
            output += string[i].lower()

    return output

print(myfunc('aiman'))
print(myfunc('penis'))