# Crear un Diccionario
informacion_personal = {
    "nombre": "Kiara Ortiz",
    "edad": 33,
    "ciudad": "Esmeraldas",
    "profesion": "Sociologa"
}

# Cambiar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar (o modificar) la clave "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

informacion_personal.pop("edad", None)  # None evita error si la clave no existe

print("Diccionario final:")
print(informacion_personal)
