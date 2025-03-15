# Listas enlazadas 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class listaEnlazada:
# # Constructor
#     def __init__(self):
#         self.cabeza = None        

from typing import Optional

class Node:
    def __init__(self, numero:int)->None:
        self.dato=numero
        self.next:Optional["Node"] = None

class listaEnlazada:
    def __init__(self)->None:
        self.cabeza:Optional["Node"] = None

    def agregar(self, numero:int)->None:
        nodo:Node = Node (numero)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

lista = listaEnlazada()

lista.agregar(5)
lista.agregar(6)

lista.agregar(7)
lista.agregar(58)