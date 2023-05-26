import numpy as np

matrizA= np.random.randint(0,11, size=(4,4))

matrizB= np.random.randint(0,11, size=(4,4))

matrizC= np.random.randint(0,11, size=(4,4))

matrizA_alcubo= np.linalg.matrix_power(matrizA, 3)

matrizB_menos1= np.linalg.inv(matrizB)

#(A^3· B^-1· C)
resultado= np.dot(np.dot(matrizA_alcubo, matrizB_menos1),matrizC)

#(A^3)^-1
matrizA_alcubo_inv= np.linalg.inv(matrizA_alcubo)

#(A^3· B^-1· C) y (A^3)^-1
resultado += matrizA_alcubo_inv

#menos decimales en el resultado:D
resultadoReal= np.round(resultado,2)

print("matriz resultante")
print(resultadoReal)
