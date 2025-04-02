import random

def calcular_promedio_temperaturas(matriz):
    """
    Calcula el promedio de temperaturas para cada ciudad en cada semana.
    :param matriz: Lista 3D con temperaturas [ciudad][semana][día].
    :return: Diccionario con promedios por ciudad y semana.
    """
    promedios = {}
    
    for ciudad_idx, ciudad in enumerate(matriz):
        promedios[ciudad_idx] = []
        for semana_idx, semana in enumerate(ciudad):
            promedio = sum(semana) / len(semana)
            promedios[ciudad_idx].append(round(promedio, 2))
    
    return promedios

# Definir dimensiones
ciudades = 3
semanas = 2
DiasSemana = 7

# Crear matriz 3D con temperaturas aleatorias entre 15 y 35 grados
matriz_temperaturas = [[[random.randint(15, 35) for _ in range(DiasSemana)] for _ in range(semanas)] for _ in range(ciudades)]

# Calcular promedios
promedios = calcular_promedio_temperaturas(matriz_temperaturas)

# Mostrar resultados
for ciudad, semanas in promedios.items():
    print(f"Ciudad {ciudad + 1}:")
    for semana, promedio in enumerate(semanas):
        print(f"  Semana {semana + 1}: {promedio}°C")
