# ----------------------------------------------
# Trabajo con Archivos de Texto en Python
# Ejemplo 2: Uso de readlines() y bucle for
# ----------------------------------------------

# 1. Escritura de un archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Estoy practicando Python paso a paso.\n")
    file.write("Nota 2: Aprender a manejar archivos es muy importante.\n")
    file.write("Nota 3: La lectura y escritura de datos es fundamental.\n")

print("Archivo 'my_notes.txt' creado y escrito nuevamente.\n")

# 2. Lectura del archivo de texto con readlines()
with open("my_notes.txt", "r") as file:
    # readlines() devuelve una lista con todas las líneas
    lines = file.readlines()

    print("Contenido del archivo usando readlines():\n")
    # Recorremos la lista de líneas con un for
    for line in lines:
        print(line.strip())  # strip() elimina los saltos de línea extra
