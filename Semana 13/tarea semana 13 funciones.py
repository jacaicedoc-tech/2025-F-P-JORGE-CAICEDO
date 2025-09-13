# Función para calcular el promedio de temperaturas de varias ciudades y semanas
def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio de cada ciudad,
    considerando varias semanas de registro.

    Parámetros:
        datos (dict): Diccionario donde la clave es el nombre de la ciudad
                      y el valor es una lista de semanas,
                      cada semana representada como una lista de temperaturas.

    Retorna:
        dict: Diccionario con el promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        # Unimos todas las temperaturas de todas las semanas en una sola lista
        todas_temperaturas = [temp for semana in semanas for temp in semana]

        if len(todas_temperaturas) > 0:
            promedio = sum(todas_temperaturas) / len(todas_temperaturas)
            promedios[ciudad] = round(promedio, 2)
        else:
            promedios[ciudad] = None  # Si no hay datos disponibles

    return promedios


# Ejemplo de uso: 3 ciudades con 4 semanas de temperaturas
temperaturas_ciudades = {
    "Quito": [
        [18, 19, 20, 21, 19, 20, 18],  # Semana 1
        [20, 21, 22, 21, 20, 19, 20],  # Semana 2
        [19, 20, 19, 18, 20, 21, 22],  # Semana 3
        [21, 20, 19, 20, 21, 20, 19]   # Semana 4
    ],
    "Guayaquil": [
        [28, 29, 30, 31, 32, 30, 29],  # Semana 1
        [30, 31, 32, 33, 34, 32, 31],  # Semana 2
        [29, 30, 31, 32, 33, 31, 30],  # Semana 3
        [31, 32, 33, 34, 35, 33, 32]   # Semana 4
    ],
    "Cuenca": [
        [15, 16, 15, 14, 15, 16, 15],  # Semana 1
        [14, 15, 14, 13, 14, 15, 14],  # Semana 2
        [16, 15, 16, 15, 16, 15, 16],  # Semana 3
        [15, 14, 15, 14, 15, 14, 15]   # Semana 4
    ]
}

resultado = calcular_promedio_temperaturas(temperaturas_ciudades)

print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio}°C")

