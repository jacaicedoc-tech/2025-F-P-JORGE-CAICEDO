# ----------------------------------------------
# Trabajo con Archivos de Texto en Python
# Escritura y Lectura de archivos
# ----------------------------------------------

# 1. Escritura de un archivo de texto
# Creamos (o sobrescribimos si ya existe) el archivo "my_notes.txt"
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Primera nota: Hoy aprendi a trabajar con archivos en Python.\n")
    file.write("Segunda nota: Los métodos write() y readline() son muy útiles.\n")
    file.write("Tercera nota: La práctica constante mejora mis habilidades.\n")

print("Archivo 'my_notes.txt' creado y escrito correctamente.\n")

# 2. Lectura de un archivo de texto
# Abrimos el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo línea por línea:\n")

    # Usamos un bucle para leer cada línea una por una
    line = file.readline()  # lee la primera línea
    while line:  # mientras haya contenido
        print(line.strip())  # mostramos la línea (strip() quita saltos de línea extra)
        line = file.readline()  # leemos la siguiente línea
