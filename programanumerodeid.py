def obtener_departamento_y_municipio1(numero_identidad):
    departamentos = {
        "0101": "La Ceiba",
        "0102": "El Porvenir",
        "0103": "Esparta",
        "0104": "Jutiapa",
        "0105": "La Masica",
        "0106": "San Francisco",
        "0107": "Tela",
        "0108": "Arizona"
        
    }

    departamento = departamentos.get(numero_identidad[:4])
    if departamento:
        return departamento
    else:
        return "No se encontró el departamento"

nombre = input("Ingrese su nombre: ")
numero_identidad = input("Ingrese su número de identidad: ")

departamento = obtener_departamento_y_municipio1(numero_identidad)

print("Nombre:", nombre)
print("Número de identidad:", numero_identidad)
print("Departamento:", departamento)
print("Municipio:", departamento)