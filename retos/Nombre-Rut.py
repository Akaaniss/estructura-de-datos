Nombres=[ ]
Ruts=[ ]

for i in range(5):
    nombre=input("Ingrese nombre {}:".format(i+1))
    rut= input("ingrese Rut {}:".format(i+1))

    Nombres.append(nombre)
    Ruts.append(rut)

print("Nombres sin orden especifico:",Nombres)
print("Ruts sin orden especifico:",Ruts)

Nombres.sort()
Ruts.sort()
print("Nombres en orden alfabetico:",Nombres)
print("Ruts en orden ascendente:",Ruts)
