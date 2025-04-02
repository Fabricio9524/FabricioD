def bubble_sort(fila):
    """
    Ordena una lista utilizando el algoritmo de ordenación Bubble Sort.
    :param fila: Lista de números a ordenar.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def ordenar_fila_matriz(matriz, fila_index):
    """
    Ordena una fila específica de la matriz en orden ascendente.
    :param matriz: Lista de listas representando la matriz.
    :param fila_index: Índice de la fila a ordenar.
    """
    if 0 <= fila_index < len(matriz):
        print("Matriz original:")
        for fila in matriz:
            print(fila)
        
        bubble_sort(matriz[fila_index])
        
        print("\nMatriz con la fila ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila fuera de rango.")


# Definir una matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 6],
    [3, 8, 1]
]

# Fila a ordenar (por ejemplo, la fila con índice 1)
fila_a_ordenar = 1

# Ejecutar la función
ordenar_fila_matriz(matriz, fila_a_ordenar)
