class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "Error: La pila está vacía"
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return "Error: La pila está vacía"
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)

# Pruebas de la pila
pila = Stack()
pila.push(10)
pila.push(20)
pila.push(30)
print("Pila después de inserciones:", pila)
print("Elemento en la cima (peek):", pila.peek())
print("Eliminar elemento (pop):", pila.pop())
print("Pila después de eliminación:", pila)
print("¿Está vacía?", pila.isEmpty())
