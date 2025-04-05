from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, ticket: Ticket) -> None:
        node = Node(ticket, 1 if ticket.priority_attention else 0)  # Prioridad 1 si es prioridad
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            if current.priority < node.priority:
                node.next = current
                self.head = node
            else:
                while current.next and current.next.priority > node.priority:
                    current = current.next
                node.next = current.next
                current.next = node

       
        print(f"Turno añadido: {ticket.dict()} con prioridad {node.priority}")
        self.print_queue()

    def dequeue(self) -> Ticket:
        if self.is_empty():
            print("Intento de dequeue pero la cola está vacía")
            return None

        ticket = self.head.data
        print(f"Atendiendo turno: {ticket.dict()}")  
        self.head = self.head.next
        self.print_queue()
        return ticket

    def print_queue(self) -> None:
        current = self.head
        print("Cola actual:")
        while current:
            print(f"Turno: {current.data.dict()}, Prioridad: {current.priority}")
            current = current.next
        print("Fin de la cola")
