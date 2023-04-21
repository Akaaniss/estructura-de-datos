import array
import random

num=random.randint(10,30)
arr=array.array("i",[0]*num)

for i in range(num):
    arr[i]=random.randint(1,100)
print(arr)

ElementoEnc= int(input("Ingrese elemento a buscar:"))
ElementoEnc= False

for i in range(num):
    if arr ==ElementoEnc:
        print(f"El elemento que busca se encuentra en 'i'")
        ElementoEnc = True
        break

if not ElementoEnc:
    print(f"El elemento no se encuentra en este arreglo.")