def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operacion == "suma":
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)
elif operacion == "resta":
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)

elif operacion == "division":
    resultadodiv = division(num1, num2)
    print("El resultado de la division es:", resultadodiv)

elif operacion == "multiplicacion":
    resultadomulti = multiplicacion(num1, num2)
    print("El resultado de la multiplicacion es:", resultadomulti)


else:
    print("Operación inválida")

    
num1= float (input("num1: ") )
num2= float (input("num2: ") )

if num1 == 0:
    print("no se puede dividir entre 0")
else:
    print(num1/num2)
    
