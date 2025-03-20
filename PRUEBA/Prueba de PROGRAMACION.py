def es_numero_perfecto(n):
    """Retorna True si n es un número perfecto."""
    return sum([i for i in range(1, n) if n % i == 0]) == n

def numeros_perfectos_en_rango(inicio, fin):
    """Encuentra todos los numeros perfectos en el rango dado."""
    return [n for n in range(inicio, fin + 1) if es_numero_perfecto(n)]

# Pedir al usuario dos numeros
try:
    inicio = int(input("Ingresa el numero inicial del rango: "))
    fin = int(input("Ingresa el numero final del rango: "))

    if inicio > fin:
        print("El numero inicial debe ser menor o igual al número final.")
    else:
        perfectos = numeros_perfectos_en_rango(inicio, fin)
        if perfectos:
            print("numeros perfectos en el rango:", perfectos)
        else:
            print("No hay numeros perfectos en este rango.")

except ValueError:
    print("Por favor, ingresa numeros enteros validos.")



