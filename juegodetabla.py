# Solicitar al usuario un número del 1 al 10
# numero = int(input("Por favor ingresa un número del 1 al 10: "))

# Validar que el número esté en el rango correcto
# if numero < 1 or numero > 10:
#     print("Por favor ingresa un número válido del 1 al 10.")
# else:
#     # Mostrar la tabla de multiplicar del número ingresado
#     print(f"Tabla de multiplicar del {numero}:")
 #    for i in range(1, 11):
  #       print(f"{numero} x {i} = {numero * i}")

# Definir una función para calcular el factorial de un número
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Solicitar al usuario un número
numero = int(input("Por favor ingresa un número para calcular su factorial: "))

# Validar que el número sea positivo
if numero < 0:
    print("El factorial solo está definido para números enteros no negativos.")
else:
    # Calcular y mostrar el factorial del número ingresado
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
