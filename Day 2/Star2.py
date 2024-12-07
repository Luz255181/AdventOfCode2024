def isSafe(numbers):
    length = len(numbers) - 1
    for i in range(0, length):
        diference = abs(int(numbers[i]) - int(numbers[i+1]))
        if (diference > 3) or (diference == 0):
            return False
    is_increasing = all(numbers[i] <= numbers[i + 1]
                        for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] >= numbers[i + 1]
                        for i in range(len(numbers) - 1))
    return is_decreasing or is_increasing


safe = 0
with open("input.txt", "r") as input:
    for line in input.readlines():
        numbers = line.split()
        booleanSafe = isSafe(numbers)
        auxiliar = numbers.copy()
        if not booleanSafe:
            i = 0
            while (i < (len(numbers)-2) and not booleanSafe):
                auxiliar = numbers.copy()
                auxiliar.pop(i)
                booleanSafe = isSafe(auxiliar)
                i += 1
        if booleanSafe:
            safe += 1
input.close()
print("Solucion = ", safe)
