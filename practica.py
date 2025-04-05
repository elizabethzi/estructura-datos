from collections import deque
from typing import Optional

# Listas enlazadas

# class Datos:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.cabeza = None

#     def insertarDatos(self, nombre, apellido, edad):
#         nuevoDato = Datos(nombre, apellido, edad)
#         if (self.cabeza is None):
#             self.cabeza = nuevoDato
#             return
        
#         nuevoDato.next = self.cabeza
#         self.cabeza = nuevoDato

#     def insertarDatosFinal(self, nombre, apellido, edad):
#         nuevoDato = Datos(nombre, apellido, edad)
#         if self.cabeza == None:
#             self.cabeza = nuevoDato
#             return
#         actual = self.cabeza
#         while (actual.next is not None):
#             actual = actual.next    

#         actual.next = nuevoDato

#     def eliminarDatos (self):
#         if(self.cabeza is None):
#             print("esta vacio")
#             return
#         self.cabeza = self.cabeza.next

#     def eliminarDatosFinal (self):
#        if(self.cabeza is None):
#             print("esta vacio")
#             return
#        if(self.cabeza.next is None):
#            self.head = None
#            return
       
#        actual = self.cabeza

#        while actual.next.next:
#            actual = actual.next

#        actual.next = None    

#     def Imprimir(self):
#         actual = self.cabeza
#         while actual:
#             print(actual.nombre, actual.apellido, actual.edad)
#             actual = actual.next


# miLista = LinkedList()     

# miLista.insertarDatos("Pepe", "Papa", 5)
# miLista.insertarDatos("Pepe", "Papa", 4)
# miLista.insertarDatosFinal("Pepe", "Papa", 6)
# miLista.eliminarDatos()
# miLista.eliminarDatosFinal()
# miLista.eliminarDatosFinal()
# miLista.Imprimir()



# Cola FIFO / First in first out

class Queue:

    def __init__(self):
        self.head=None
        self.final=None
        self.Queue= []

    def geHead(self):
        return self.head
    def getFinal(self):
        return self.final
    def agregarItems(self, item):
        self.Queue.append(item)
        self.final = item
        return self.final
    def eliminarItems(self):
        self.Queue.pop(0)
        self.head = self.Queue[0]
        return self.head

    def longitud(self):
            return len(self.Queue)


# Pilas LIFO / Last in First out

class PilaStack:


    def __init__(self):
        self.listaNumeros = []

    def siVacio(self):
        return self.listaNumeros == []
    def insertarNumeros(self, numero):
        self.listaNumeros.append(numero)
    def eliminarNumeros(self):
        return self.listaNumeros.pop()   
    def top(self):
        return self.listaNumeros[len(self.listaNumeros)-1]
    def longitud(self):
        print("Long")
        return len(self.listaNumeros)
    def imprimir(self):
        print(self.listaNumeros)

nuevaLista = PilaStack() 


nuevaLista.insertarNumeros(3)
nuevaLista.insertarNumeros(2)
nuevaLista.insertarNumeros(1)


# nuevaLista.imprimir()


# nuevaLista.eliminarNumeros()
# nuevaLista.imprimir()

# nuevaLista.eliminarNumeros()
# nuevaLista.imprimir()

# nuevaLista.eliminarNumeros()
# nuevaLista.imprimir()


# nuevaLista.insertarNumeros(3)
# nuevaLista.insertarNumeros(2)
# nuevaLista.insertarNumeros(1)

# nuevaLista.imprimir()
# nuevaLista.insertarNumeros(3)
# nuevaLista.insertarNumeros(2)
# nuevaLista.insertarNumeros(1)

# nuevaLista.imprimir()
print(nuevaLista.longitud())


nuevaLista.eliminarNumeros()
nuevaLista.imprimir()

print(nuevaLista.longitud())

class otroStack:

    def __init__(self):
        self.head = None
        self.otroStack=[]

    def getHead(self):
        return self.head
    def agrearElemento(self, item):
        self.head = item
        self.otroStack.append(item)
        return self.head
    def eliminarElemento(self):
        self.otroStack.pop()
        self.head = self.otroStack[-1]
        return self.head
    

nuevoStack = otroStack()

