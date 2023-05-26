import numpy as np

matriz1 =np.random.randint(1,11, size=(3,3))
print("matriz 1:")
print(matriz1)
print()

matriz2= np.random.randint(11,31, size=(3,3))
print("matriz 2:")
print(matriz2)
print()

matriz3=np.random.randint(-10,0, size=(3,3))
print("matriz 3:")
print(matriz3)
print()


resultado1 = np.dot(matriz1 + matriz2, matriz3)

resultado2=np.dot(matriz1, matriz3) + np.dot(matriz2, matriz3)

print("(A+B)*C")
print(resultado1)
print()

print("A*C+B*C")
print(resultado2)
print()

if np.array_equal(resultado1,resultado2):
    print("la propiedad '(A+B)*C=A*C+B*C' si se cumple")
else:
    print("la propiedad no se cumple")