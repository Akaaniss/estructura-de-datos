import random

fila=int(input("Ingrese la cantidad de filas:\n"))
columnas=int(input("Ingrese la cantidad de columnas:\n"))

escalar=int(input("Ingrese un escalar:"))
matriz=[]

for i in range(fila):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(0,10))
    matriz.append(fila)

for i in range(fila):
    for j in range(columnas):
        matriz[i][j]*=escalar

print(matriz)