def isSafe(numbers):
    for i in range(0, len(numbers)-1):
        difference = abs(int(numbers[i]) - int(numbers[i+1]))
        if (difference > 3) or (difference < 1):
            return False
    is_increasing = all(int(numbers[i]) <= int(numbers[i + 1])
                        for i in range(len(numbers) - 1))
    is_decreasing = all(int(numbers[i]) >= int(numbers[i + 1])
                        for i in range(len(numbers) - 1))
    return is_decreasing or is_increasing


safe = 0
with open("input.txt", "r") as input:
    for line in input.readlines():
        numbers = line.split()
        booleanSafe = isSafe(numbers)
        if not booleanSafe:
            for i in range(len(numbers)):
                newNumbers = numbers[:i] + numbers[i + 1:]
                booleanSafe = isSafe(newNumbers)
                if booleanSafe:
                    safe += 1
                    break
        else:
            safe += 1
input.close()
print("Solucion = ", safe)
