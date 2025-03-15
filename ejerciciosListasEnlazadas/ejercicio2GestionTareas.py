class Tarea:
    def __init__(self, descripcion, prioridad, fechaVencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fechaVencimiento = fechaVencimiento  
        self.siguiente = None
    
    def __str__(self):
        prioridad_str = {1: "Alta", 2: "Media", 3: "Baja"}.get(self.prioridad, "Desconocida")
        return f"{self.descripcion} | Prioridad: {prioridad_str} | Vence: {self.fechaVencimiento}"

class listaTareas:
    def __init__(self):
        self.cabeza = None
    
    def compararFechas(self, fecha1, fecha2):
        return fecha1 <= fecha2  
    
    def agregarTareas(self, descripcion, prioridad, fechaVencimiento):
        nuevaTarea = Tarea(descripcion, prioridad, fechaVencimiento)
        if not self.cabeza or (self.cabeza.prioridad > prioridad or 
                                (self.cabeza.prioridad == prioridad and self.compararFechas(fechaVencimiento, self.cabeza.fechaVencimiento))):
            nuevaTarea.siguiente = self.cabeza
            self.cabeza = nuevaTarea
        else:
            actual = self.cabeza
            while actual.siguiente and (actual.siguiente.prioridad < prioridad or 
                                        (actual.siguiente.prioridad == prioridad and self.compararFechas(actual.siguiente.fechaVencimiento, fechaVencimiento))):
                actual = actual.siguiente
            nuevaTarea.siguiente = actual.siguiente
            actual.siguiente = nuevaTarea
    
    def eliminarTareas(self, descripcion):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.descripcion == descripcion:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Tarea '{descripcion}' eliminada")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no se encuentra")
    
    def mostrarTareas(self):
        actual = self.cabeza
        if not actual:
            print("No hay tareas ingresadas")
            return
        while actual:
            print(actual)
            actual = actual.siguiente
    
    def buscarTarea(self, descripcion):
        actual = self.cabeza
        while actual:
            if actual.descripcion == descripcion:
                print("Tarea encontrada:", actual)
                return actual
            actual = actual.siguiente
        print("Tarea no se encuentra")
        return None
    
    def completarTarea(self, descripcion):
        self.eliminarTareas(descripcion)
        print(f"Tarea '{descripcion}' completada y eliminada")

def menu():
    tareas = listaTareas()
    while True:
        print("\nLista de tareas")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Buscar tarea")
        print("5. Completar tarea")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            descripcion = input("Ingrese descripcion de la tarea: ")
            print("Seleccione la prioridad: \n1. Alta\n2. Media\n3. Baja")
            prioridad = int(input("Ingrese la prioridad (1, 2 o 3): "))
            fechaVencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            tareas.agregarTareas(descripcion, prioridad, fechaVencimiento)

        elif opcion == "2":
            descripcion = input("Ingrese tarea a eliminar (descripcion): ")
            tareas.eliminarTareas(descripcion)

        elif opcion == "3":
            tareas.mostrarTareas()

        elif opcion == "4":
            descripcion = input("Ingrese tarea a buscar (descripcion): ")
            tareas.buscarTarea(descripcion)

        elif opcion == "5":
            descripcion = input("Ingrese tarea a completar (descripcion): ")
            tareas.completarTarea(descripcion)

        elif opcion == "6":
            print("Saliendo")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu()
