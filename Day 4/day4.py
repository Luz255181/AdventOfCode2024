import re

# Inicializar la variable que llevará la cuenta
sum = 0
word = "XMAS"
reverseWord = "SAMX"


def obtener_diagonales(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    diagonales_principales = []
    diagonales_inversas = []

    # Diagonales principales (↘)
    for d in range(-(filas - 1), columnas):
        diag = [matriz[i][i - d]
                for i in range(filas) if 0 <= i - d < columnas]
        diagonales_principales.append(''.join(diag))

    # Diagonales inversas (↙)
    for d in range(filas + columnas - 1):
        diag = [matriz[i][d - i]
                for i in range(filas) if 0 <= d - i < columnas]
        diagonales_inversas.append(''.join(diag))

    return diagonales_principales, diagonales_inversas


with open("input.txt", "r") as input:
    matrix = list()

    # Leer la matriz del archivo y buscar en las filas
    for line in input.readlines():
        # Buscar "XMAS" y "SAMX" en la fila
        finds = len(re.findall(word, line))
        sum += finds
        finds = len(re.findall(reverseWord, line))
        sum += finds

        # Convertir la línea a una lista y agregarla a la matriz
        # Usamos strip() para eliminar saltos de línea innecesarios
        l = list(line.strip())
        matrix.append(l)

# Buscar en las columnas
# Número de columnas, suponiendo que todas las filas tienen el mismo número de columnas
num_columns = len(matrix[0])
for col in range(num_columns):
    # Construir la columna como una cadena
    column = ''.join([matrix[row][col] for row in range(len(matrix))])
    finds = len(re.findall(word, column))
    sum += finds
    finds = len(re.findall(reverseWord, column))
    sum += finds

# Buscar en las diagonales
diagonales_principales, diagonales_inversas = obtener_diagonales(matrix)

# Buscar en las diagonales principales e inversas
for diag in diagonales_principales + diagonales_inversas:
    finds = len(re.findall(word, diag))
    sum += finds
    finds = len(re.findall(reverseWord, diag))
    sum += finds

print(f"Total de 'XMAS' y 'SAMX': {sum}")
