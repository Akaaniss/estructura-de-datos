class Video:
    def __init__(self,titulo,autor,duracion):
        self.titulo=titulo
        self.autor=autor
        self.duracion=duracion
class Nodo:
    def __init__(self,video):
        self.video=video
        self.siguiente=None

class lista_reproduccion:
    def __init__(self):
        self.primero=None   
        self.ultimo=None

#este def verifica si la lista de videos se encuentra vacia
    def esta_vacia(self):
        return self.primero is None
    
    #este def agrega videos a la lista de reproduccion
    def agregar_video(self,video):
        nuevoNodo=Nodo(video)
        if self.esta_vacia():
            self.primero=nuevoNodo
            self.ultimo=nuevoNodo
            self.ultimo.siguiente=self.primero
        else:
            nuevoNodo.siguiente=self.primero
            self.ultimo.siguiente=nuevoNodo
            self.ultimo=nuevoNodo

#este def muestra la lista de videos con titulo,autor y duracion
    def mostrar_videos(self):
        if self.esta_vacia():
            print("La lista está vacía")
        else:
            actual=self.primero
            while True:
                print("Titulo",actual.video.titulo)
                print("Autor",actual.video.autor)
                print("Duracion",actual.video.duracion)
                actual=actual.siguiente
                if actual==self.primero:
                    break
    
    #este def busca un video en la lista por el titulo y muestra su info
    def buscar_video(self,titulo):
        if self.esta_vacia():
            print("La lista de videos está vacía")
        else:
            actual=self.primero
            while True:
                if actual.video.titulo==titulo:
                    print("Titulo",actual.video.titulo)
                    print("Autor",actual.video.autor)
                    print("Duracion",actual.video.duracion)
                    return
                actual=actual.siguiente
                if actual==self.primero:
                    break
            print("El video no se encontró")
    
    #este elimina un video de la lista por su titulo
    def eliminar_video(self,titulo):
        if self.esta_vacia():
            print("La lista de videos está vacía")
        elif self.primero.video.titulo==titulo:
            if self.primero==self.ultimo:
                self.primero=None
                self.ultimo=None
            else:
                self.primero=self.primero.siguiente
                self.ultimo.siguiente=self.primero
        else:
            anterior=self.primero
            actual=self.primero.siguiente
            while actual!=self.primero:
                if actual.video.titulo==titulo:
                    anterior.siguiente=actual.siguiente
                    if actual==self.ultimo:
                        self.ultimo=anterior
                    return
                anterior=actual
                actual=actual.siguiente
            print("El video no se encontró")

lista=lista_reproduccion()

#para agregar videos de forma manual
while True:
    titulo=input("Ingrese el titulo del video:")
    if titulo.lower()=="salir":
        break
    autor=input("Ingrese el nombre del autor:")
    duracion=input("Ingrese la duración del video:")

    video=Video(titulo,autor,duracion)
    lista.agregar_video(video)
    
#ahora mostrar la lista de videitos
print("----------lista de videos----------")
lista.mostrar_videos()
print("-----------------------------")

#para buscar video
print("---------Buscar video-------")
titulo_buscar=input("Ingrese el titulo del video:")
lista.buscar_video(titulo_buscar)
print("-----------------------------")

#para eliminar video
print("---------Eliminar video-------")
titulo_eliminar=input("Ingrese el titulo del video que desea eliminar:")
lista.eliminar_video(titulo_eliminar)
print("-----------------------------")

#lista de videos actualizada
print("---------Eliminar video-------")

lista.mostrar_videos()
print("-----------------------------")