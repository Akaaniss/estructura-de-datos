import random

fila1=int(input("Ingrese la cantidad de filas para la primera matriz:\n"))
columna1=int(input("Ingrese la cantidad de columnas para la primera matriz:\n"))
matriz1=[[random.randint(0,5) for j in range(columna1)for i in range(fila1)]]


fila2=int(input("ingrese la cantidad de filas para la segunda matriz:\n"))
columna2=int(input("ingrese la cantidad de columnas para la segunda matriz:\n"))
matriz2=[[random.randint(0,5) for j in range(columna2) for i in range(fila2)]]

print("Matriz 1:")
for fila1 in matriz1:
    print(fila1)

print ("Matriz 2:")
for fila2 in matriz2:
    print(fila2)

if fila1 == fila2 and columna1 == columna2:
    matrizResultante= [[matriz1[i][j] + matriz2[i][j] for j in range(columna1)] for i in range(fila1)]
    
else:
    print("las dimensiones de las matrices no coinciden, por tanto no se pueden sumar")
    exit()

print("El resultado de la suma de Matricez es:")
for fila in matrizResultante:
    print(fila)
