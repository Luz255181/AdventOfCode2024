def isSafe(numbers):
    length = len(numbers) - 1
    booleanSafe = True
    i = 0
    if (int(numbers[0]) > int(numbers[1])):
        while (booleanSafe and i < length):
            number1 = int(numbers[i])
            number2 = int(numbers[i+1])
            diference = number1 - number2
            if (number1 < number2) or (diference > 3) or (diference == 0):
                booleanSafe = False
            i += 1
    else:
        while (booleanSafe and i < length):
            number1 = int(numbers[i])
            number2 = int(numbers[i+1])
            diference = number2 - number1
            if (number1 > number2) or (diference > 3) or (diference == 0):
                booleanSafe = False
            i += 1
    return booleanSafe


safe = 0
with open("input.txt", "r") as input:
    for line in input.readlines():
        numbers = line.split()
        booleanSafe = isSafe(numbers)
        if not booleanSafe:
            i = 0
            while (i < (len(numbers)-1) and not booleanSafe):
                auxiliar = numbers.copy()
                newNumbers = auxiliar.pop(i)
                booleanSafe = isSafe(newNumbers)
                i += 1
        if booleanSafe:
            safe += 1
input.close()
print("Solucion = ", safe)
