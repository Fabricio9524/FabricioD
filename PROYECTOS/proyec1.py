def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional y devuelve su posición si se encuentra.
    :param matriz: Lista de listas que representa la matriz.
    :param valor: Valor a buscar en la matriz.
    :return: Tupla con la posición (fila, columna) si se encuentra, o None si no está.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

# Definir una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Ejecutar la búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
