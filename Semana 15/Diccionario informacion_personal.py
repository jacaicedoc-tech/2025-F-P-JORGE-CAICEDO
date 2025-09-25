# Crear un Diccionario con informacion personal
informacion_personal = {"nombre": "Kiara Ortiz","edad": 33,"ciudad": "Quito","profesion": "Sociologa"}

informacion_personal["ciudad"] = "Esmeraldas"
informacion_personal["profesion"] = "Abogada"

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

del(informacion_personal["edad"])

print("Diccionario final:")
print(informacion_personal)
