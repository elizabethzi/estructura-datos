from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}


@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    if turno.type not in ticketTypes:
        return {"mensaje": "Tipo de turno inválido"}

    print(f"Recibiendo turno: {turno.dict()}")
    print(f"ID antes de encolar: {id(ticketTypes[turno.type])}")  

    add_queue(turno, ticketTypes)

    print(f"ID después de encolar: {id(ticketTypes[turno.type])}")  
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno.dict()}

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    if tipo in ticketTypes:
        print(f"Obteniendo el siguiente turno de {tipo}, ID de la instancia: {id(ticketTypes[tipo])}")
        ticket = ticketTypes[tipo].dequeue()
        if ticket:
            return {"mensaje": "El siguiente turno es", "datos_turno": ticket.dict()}
        return {"mensaje": "No hay turnos en la cola", "datos_turno": None}
    return {"mensaje": "Tipo de turno inválido"}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    if tipo in ticketTypes:
        print(f"Listando turnos de {tipo}, ID de la instancia: {id(ticketTypes[tipo])}")
        queue = []
        current = ticketTypes[tipo].head
        print(f"Estado de la cola antes de listar: {current}") 

        while current:
            queue.append(current.data.dict())
            current = current.next

        print(f"Cola después de listar: {queue}")  
        return {"mensaje": "Lista de turnos en cola", "datos_turnos": queue}
    return {"mensaje": "Tipo de turno inválido"}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}