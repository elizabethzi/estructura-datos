class Node:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Stack:
    def __init__(self): 
        self.cabeza = Node("cabeza")
        self.tamano = 0

    def printStack(self):
        actual = self.cabeza.siguiente  # Corrección aquí
        if not actual:
            print("Pila vacía")
            return
        print("Contenido de la pila:")
        while actual:
            print(actual.valor)
            actual = actual.siguiente

    def getSize(self):
        return self.tamano

    def isEmpty(self): 
        return self.tamano == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.cabeza.siguiente.valor

    def push(self, valor):
        nodo = Node(valor)
        nodo.siguiente = self.cabeza.siguiente
        self.cabeza.siguiente = nodo
        self.tamano += 1

    def pop(self):
        if self.isEmpty():
            print("No se puede eliminar, pila vacía")
            return None
        remover = self.cabeza.siguiente
        self.cabeza.siguiente = remover.siguiente
        self.tamano -= 1
        return remover.valor

# Prueba
stack = Stack()


# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.printStack()


# print(stack.getSize(), "tamaño")
# print(stack.isEmpty(), "Si esta vacio? False = esta lleno / True = esta vacio")
# print(stack.peek(), "Elemento superior")
# stack.push(5)
# print(stack.peek(), "Elemento superior")


print(stack.pop())
print(stack.isEmpty())