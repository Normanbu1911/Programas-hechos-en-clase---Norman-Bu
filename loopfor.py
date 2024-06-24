import os
os.system('cls' if os.name == 'nt' else 'clear')

#Ejemplo 1


#ciclo for

#for i in range(10):
#    print(i)


#for i in range (1,20,2):
#    print(i)

#ciclo for con listas
lista = ("uno","dos","tres","cuatro","cinco")
for item in lista:
    print(item)

# ciclo for con tuplas

#tupla = ("uno","dos","tres","cuatro","cinco")
for item in tupla:
    print(item)

#ciclo for con diccionarios
diccionario =
{"curso":"Python TOTAL",
"clase": "ciclos",
"tema":"for",
"duracion":"1 trimestre",
"profesor":"Norman Alexis"}

print(diccionario)

for llave in diccionario:
    print(llave, ":", diccionario(llave))
