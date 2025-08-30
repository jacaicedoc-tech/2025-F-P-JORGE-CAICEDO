# Programa 2: Ordenación de una fila en matriz bidimensional (3x3) con Bubble Sort

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Definimos una matriz 3x3
matriz = [
    [5, 8, 3],
    [9, 2, 7],
    [6, 1, 4]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionamos la fila que queremos ordenar (ejemplo: la fila 1 → segunda fila)
indice_fila = 1
matriz[indice_fila] = bubble_sort(matriz[indice_fila])

print("\nMatriz después de ordenar la fila", indice_fila, ":")
for fila in matriz:
    print(fila)
