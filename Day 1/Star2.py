sum = 0
column1 = list()
column2 = list()
with open("input.txt", "r") as input:
    for line in input.readlines():
        numbers = line.split()
        column1.append(numbers[0])
        column2.append(numbers[1])
    input.close()
length = len(column1)

for i in range(0, length):
    sum = sum + abs(int(column2[i]) - int(column1[i]))
print("Solucion = ", str(sum))
