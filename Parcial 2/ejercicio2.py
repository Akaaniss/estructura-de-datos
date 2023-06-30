class Tarea:
    def __init__(self,identificador,titulo,descripcion,estado):
        self.identificador=identificador
        self.titulo=titulo
        self.descripcion=descripcion
        self.estado=estado

class Gestion_tareas:
    def __init__(self):
        self.tareas[]#tareas como lista vacia

    def agregar_tarea(self,tarea):
        self.tarea.append(tarea)#agregar tarea a la lista de tareas

    def eliminar_tarea(self,identificador):
        for tarea in self.tareas:
            if tarea.identificador==identificador:#buscar tarea con el identificador
                self.tareas.remove(tarea)#con esto se puede eliminar la tarea
                return True#si se eliminó
            return False#no se eliminó
        
    def buscar_tarea(self,identificador):
        for tarea in self.tareas:
            if tarea.identificador==identificador:
                return tarea#retornar en tarea 
            return None#si no se encuentra retorna en none
        
    def cambiar_estadoTarea(self,identificadot,nuevoestado):
        tarea=self.buscar_tarea(identificador)
        if tarea:
            tarea.estado=nuevoestado
            return True
        return False
    
    def mostrar_tareasOrdenadas(self):
        tareasOrdenadas=sorted(self.tareas,key=lambda tarea: tarea.identificador)
        print(f"Indentificador:{tarea.identificador},Titulo:{tarea.titulo},Estado:{tarea.estado}")
