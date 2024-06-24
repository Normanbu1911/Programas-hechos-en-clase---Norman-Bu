def calcular_precio_total(cantidad, precio_balon):
    descuento = 0
    if cantidad >= 10:
        descuento = 0.1
    precio_total = cantidad * precio_balon
    if descuento > 0:
        precio_total -= precio_total * descuento
    return precio_total

cantidad = int(input("Ingrese la cantidad de balones de futbol a vender: "))
precio_balon = 600  

precio_total = calcular_precio_total(cantidad, precio_balon)
print("El precio total a pagar es:", precio_total)