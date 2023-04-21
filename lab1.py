import random
#creamos las filas
fila1=int(input("Ingrese la cantidad de filas para la primera matriz:\n"))
columna1=int(input("Ingrese la cantidad de columnas para la primera matriz:\n"))

fila2=int(input("ingrese la cantidad de filas para la segunda matriz:\n"))
columna2=int(input("ingrese la cantidad de columnas para la segunda matriz:\n"))

matriz1=[[random.randint(0,5) for j in range(columna1)for i in range(fila1)]]
matriz2=[[random.randint(0,5) for j in range(columna2) for i in range(fila2)]]

#imprimimos las matrices
print("Matriz 1:")
for fila in matriz1:
    print(fila1)

print ("Matriz 2:")
for fila in matriz2:
    print(fila2)

if fila1 == fila2 and columna1 == columna2:
    matriz_resultante = [[matriz1[i][j] + matriz2[i][j] for j in range(columna1)] for i in range(fila1)]

else:
    print("las dimensiones de las matrices no coinciden, por tanto no se pueden sumar")
    exit()


print("El resultado de la suma de Matrices2 es:")
for fila in matriz_resultante:
    print(fila)


fila3= int(input("ingrese la cantidad de filas para la tercera matriz:\n"))
columna3= int(input("Ingrese la cantidad de columnas para la tercera matriz:\n"))
matriz3=[[random.randint(0,5)for j in range(columna3)for i in range(fila3)]]

print("Matriz 3:")
for fila3 in matriz3:
    print(fila3)


if fila1 == fila3 and columna1==columna3:
    matriz_final = [[matriz_resultante[i][j] - matriz3[i][j] for j in range(columna1)] for i in range(fila1)]

else:
    print("Las dimensiones de las matrices no coinciden y no se pueden restar")
    exit()

print("Matriz final:")
for fila in matriz_final:
    print(fila)