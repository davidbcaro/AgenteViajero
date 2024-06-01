import itertools

# Definimos las distancias entre las ciudades en una matriz de distancias
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Número de ciudades
n = len(distancias)

# Generar todas las permutaciones posibles de las ciudades (excepto la ciudad de origen)
permutaciones = itertools.permutations(range(1, n))

# Función para calcular la longitud de un recorrido
def calcular_longitud_recorrido(permutacion):
    longitud = 0
    # Añadir la distancia desde la ciudad de origen a la primera ciudad en la permutación
    longitud += distancias[0][permutacion[0]]
    # Añadir las distancias entre las ciudades en la permutación
    for i in range(len(permutacion) - 1):
        longitud += distancias[permutacion[i]][permutacion[i + 1]]
    # Añadir la distancia desde la última ciudad en la permutación de vuelta a la ciudad de origen
    longitud += distancias[permutacion[-1]][0]
    return longitud

# Encontrar el recorrido más corto
mejor_recorrido = None
mejor_longitud = float('inf')

for permutacion in permutaciones:
    longitud_actual = calcular_longitud_recorrido(permutacion)
    if longitud_actual < mejor_longitud:
        mejor_longitud = longitud_actual
        mejor_recorrido = permutacion

# Imprimir el resultado
mejor_recorrido = (0,) + mejor_recorrido + (0,)
print(f"El mejor recorrido es: {mejor_recorrido} con una longitud de: {mejor_longitud}")
