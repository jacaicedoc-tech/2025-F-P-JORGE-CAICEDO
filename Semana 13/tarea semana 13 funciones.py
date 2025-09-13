# Función para calcular la temperatura promedio por ciudad
def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio de cada ciudad.

    Parámetros:
        datos (dict): Diccionario donde las claves son nombres de ciudades
                      y los valores son listas con temperaturas semanales.

    Retorna:
        dict: Diccionario con cada ciudad y su temperatura promedio.
    """

    promedios = {}

    for ciudad, temperaturas in datos.items():
        if len(temperaturas) > 0:  # Evitamos división por cero
            promedio = sum(temperaturas) / len(temperaturas)
            promedios[ciudad] = round(promedio, 2)  # Redondeamos a 2 decimales
        else:
            promedios[ciudad] = None  # Si no hay datos, dejamos None

    return promedios


# Ejemplo de uso
temperaturas_ciudades = {
    "Quito": [18, 20, 19, 21, 22, 20, 19],  # Temperaturas de 1 semana
    "Guayaquil": [28, 29, 30, 31, 32, 33, 29],
    "Cuenca": [15, 16, 15, 14, 15, 16, 15]
}

resultado = calcular_promedio_temperaturas(temperaturas_ciudades)

print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio}°C")
