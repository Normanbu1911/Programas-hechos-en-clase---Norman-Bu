import os   
os.system('cls' if os.name == 'nt' else 'clear')

mibool = True

a = 6 < 5
b = 30 == 15*3

#Comparaciones

print(not (mibool == a and mibool != b))
