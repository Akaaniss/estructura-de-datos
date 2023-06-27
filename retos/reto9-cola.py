class Banco:
    def __init__(self):
        self.clientes=[]

    def agregarClientes(self,nombre):
        self.clientes.append(nombre)

    def atenderClientes(self):
        if len(self.clientes)>0:
            cliente=self.clientes.pop(0)
            print("Atendiendo al cliente",cliente)
        else:
            print("No hay clientes esperando")
        
    def mostrarClientes(self):
        print("Clientes en espera:")
        for clientes in self.clientes:
            print(clientes)

banco=Banco()

while True:
    print("1: agregar cliente")
    print("2: atender cliente")
    print("3: mostrar clientes en espera")
    print("4: salir")
    opcion=input("seleccione una opcion:")

    if opcion =="1":
        nombre=input("Ingrese nombre de cliente:")
        banco.agregarClientes(nombre)
        print("Cliente",nombre,"agregado en la lista")
    
    elif opcion=="2":
        banco.atenderClientes()
    
    elif opcion=="3":
        banco.mostrarClientes()

    elif opcion=="4":
        break

    else:
        print("Opcion no valida, intentelo denuevo")