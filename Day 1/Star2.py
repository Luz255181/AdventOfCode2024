sum = 0
column1 = list()
column2 = list()
with open("input.txt", "r") as input:
    for line in input.readlines():
        numbers = line.split()
        column1.append(numbers[0])
        column2.append(numbers[1])
    input.close()
for i in column1:
    sum = sum + (int(i) * column2.count(i))
print("Solucion = ", str(sum))
