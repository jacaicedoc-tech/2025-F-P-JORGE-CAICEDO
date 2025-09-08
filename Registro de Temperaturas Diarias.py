# Registro de temperaturas diarias con matriz 3D
# Dimensiones:
# Ciudades -> Semanas -> Días

# Definimos las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Creamos una matriz 3D con temperaturas (ejemplo inventado)
# [ciudad][semana][día]
temperaturas = [
    # Quito
    [
        [15, 16, 17, 18, 16, 15, 14],  # Semana 1
        [17, 18, 16, 15, 14, 15, 16]  # Semana 2
    ],
    # Guayaquil
    [
        [28, 29, 30, 31, 32, 30, 29],  # Semana 1
        [27, 28, 29, 30, 31, 30, 28]  # Semana 2
    ],
    # Cuenca
    [
        [12, 13, 14, 15, 13, 12, 11],  # Semana 1
        [14, 15, 13, 12, 11, 12, 13]  # Semana 2
    ]
]

# Calcular promedio por ciudad y semana
for i in range(len(ciudades)):  # Recorre ciudades
    print(f"\nPromedios de temperaturas en {ciudades[i]}:")

    for j in range(len(temperaturas[i])):  # Recorre semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # Recorre días
            suma += temperaturas[i][j][k]

        promedio = suma / len(temperaturas[i][j])
        print(f"  Semana {j + 1}: {promedio:.2f} °C")
