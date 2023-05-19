import numpy as np

filas1 = np.random.randint(2, 6)
columnas1 = np.random.randint(2, 6)
filas2 = np.random.randint(2, 6)
columnas2 = np.random.randint(2, 6)

print("Ingrese los elementos de la primera matriz")
matriz1= []
for i in range(filas1):
    fila=[]
    for j in range(columnas1):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz1.append(fila)   

print("Ingrese los elementos de la segunda matriz:")
matriz2= []
for i in range(filas2):
    fila = []
    for j in range(columnas2):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz2.append(fila)

#restar las matrices
if filas1 == filas2 and columnas1 == columnas2:
    matriz_resultante = []
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            elemento = matriz1[i][j] - matriz2[i][j]
            fila.append(elemento)
        matriz_resultante.append(fila)
    print("Matriz resultado de la resta:")
    for fila in matriz_resultante:
        print(fila)
else:
    print("No se puede restar las matrices debido a sus dimensiones diferentes.")

#nueva matriz
print("Ingrese elementos de una nueva matriz:") 
filas_n=int(input("Ingrese la cantidad de filas:"))
columnas_n=int(input("ingrese la cantidad de columnas:"))
matriz_n=np.zeros(filas_n,columnas_n)  
for i in range(filas_n):
    for j in range(columnas_n):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        matriz_n[i][j] = elemento

#multiplicar
if columnas1== filas_n:
    resultado_final = np.dot(matriz_resultante, matriz_n)
    print("Resultado de la multiplicación:")
    print(resultado_final)
else:
    print("No se puede multiplicar la matriz")
