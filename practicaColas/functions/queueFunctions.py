from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    
    # Add a ticket to the queue, using the TicketController class to manage the queue.
    # you need order the tickets by type and priority. (dudas, asesor, caja, otros)
   
    tipo = ticket.type

    if tipo not in ticketTypes:
        print("Error: Tipo de turno no válido")
        return

    print(f"Añadiendo ticket: {ticket.dict()} a la cola de {tipo}")
    print(f"ID de la instancia de {tipo} antes de encolar: {id(ticketTypes[tipo])}")

    ticketTypes[tipo].enqueue(ticket)

    print("Cola actual después de añadir:")
    ticketTypes[tipo].print_queue()
