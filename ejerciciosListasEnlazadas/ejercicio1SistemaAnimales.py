class Animal:

    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None  
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) tiene {self.edad} años"

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def existeAnimal(self, nombre, tipo):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre and actual.tipo == tipo:
                return True
            actual = actual.siguiente
        return False    
    
    def agregarAnimal(self, nombre, tipo, edad):
   
        if self.existeAnimal(nombre, tipo):
            print(f"El animal {nombre} ({tipo}) ya esta registrado")
            return
        
        nuevoAnimal = Animal(nombre, edad, tipo)
        if not self.cabeza:
            self.cabeza = nuevoAnimal
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevoAnimal
    
    
    def mostrarAnimalesIterativo(self):
        actual = self.cabeza
        if not actual:
            print("No hay animales registrados")
            return
        while actual:
            print(actual)
            actual = actual.siguiente
    
    def mostrarAnimalesRecursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
            if not nodo:
                print("No hay animales registrados")
                return
        print(nodo)
        if nodo.siguiente:
            self.mostrarAnimalesRecursivo(nodo.siguiente)


animales = ListaEnlazada()

animales.agregarAnimal("Pepe", "Aguila", 5)
animales.agregarAnimal("Negro", "Felino", 7)
animales.agregarAnimal("Pepe", "Aguila", 5)  

print("\nLista de animales (iterativo): ")
animales.mostrarAnimalesIterativo()

print("\nLista de animales (recursivo): ")
animales.mostrarAnimalesRecursivo()