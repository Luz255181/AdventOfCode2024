import re

sum = 0
with open("input.txt", "r") as input:
    pattern = r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)'
    enable = True
    numbers = r'\d{1,3}'
    for line in input.readlines():
        multiplications = re.findall(pattern, line)
        for i in range(len(multiplications)):
            match multiplications[i]:
                case "do()":
                    enable = True
                case "don't()":
                    enable = False
                case _:
                    if (enable):
                        num = re.findall(numbers, multiplications[i])
                        sum = sum + (int(num[0]) * int(num[1]))
input.close()
print("Solucion = ", sum)
