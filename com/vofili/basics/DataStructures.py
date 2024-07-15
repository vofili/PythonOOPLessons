mySet =  {"2","9","19","11","5"}

stringVal = 'AAAAABBBBBCCCCC'

prevChar = None
for char in stringVal:
    counter = 0
    if char != prevChar:
        print(f'New character is {char}')
    prevChar = char
    counter += 1


