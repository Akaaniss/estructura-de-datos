class Pila:
    def __init__(self):
        self.libros=[]

    def vacio(self):
        return len(self.libros)==0
    
    def Apilar(self,libro):
        self.libros.append(libro)

    def desapilado(self):
        if self.vacio():
            return None
        return self.libros.pop()
    
pila_De_libros=Pila()

pila_De_libros.Apilar("Libro 1")
pila_De_libros.Apilar("Libro 2")
pila_De_libros.Apilar("Libro 3")

libro=pila_De_libros.desapilado()
while libro is not None:
    print("Se ha desapilado el libro",libro)
    libro=pila_De_libros.desapilado()
