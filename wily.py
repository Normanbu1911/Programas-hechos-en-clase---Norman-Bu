#Imprime 10 valores con el ciclo while

import os
os.system('cls' if os.name == 'nt' else 'clear')


i=0
while 1<10:
    print(1)
    i +=1
   
#print("Ciclo controlado por banderin")
#
#while True:
#    entrada = input("Ingresa S para salir")
#    if entrada.upper == "S":
#        break
#    print("Escribiste:", entrada)

#print("Ciclo controlado por banderin 2")
#bandera = "x"
#while bandera != "S":
 #   bandera = input("Ingresa S para salir")
print("ciclo controlado por banderin")

bandera = True
while bandera != False:
    bandera = input("Ingresa S para salir")
    print(bandera.upper())
    salir = bandera.upper()
    if salir == "S":
        bandera = False
        print ("saliste del ciclo")