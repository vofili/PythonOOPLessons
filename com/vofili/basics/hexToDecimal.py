hexDict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):

    lenNum = len(hexNum)

    if lenNum > 3  or lenNum < 1:
        return "None"

    decimalValue = 0
    currentNumberIndex = 0
    while (lenNum > 0):

        currentNum=hexNum[currentNumberIndex]
        currentHexDigit=hexDict[currentNum]
        decimalValue = decimalValue + (currentHexDigit * (16 ** (lenNum-1)))
        currentNumberIndex += 1
        lenNum -= 1

    print(decimalValue)

hexToDec("ABC")

me="A00"
currIndex = len(me) - 1
print(currIndex)
print(me[0])