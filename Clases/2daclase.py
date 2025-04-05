# Listas

# numeros = list()

# continuar : bool = True

# # Funciones

# def agregarLista(numero: int)->None:
#  numero = int(input('Ingresa el numero: '))
#  numeros.append(numero)

# def quitarLista()->None:
#     numeros.pop()


# # Ciclo 

# while continuar:

#  accion = int(input('Escoge la acción: 1. Agregar / 2. Eliminar / 3. Salir: '))


#  if accion == 1:
#   agregarLista(numeros)

#  if accion == 2:
#   quitarLista()

#  if accion == 3:
#   print('Adios')
#   continuar = False

# print('Lista')
# print(numeros)


 

# 
# 
# 
# 
# 
# 
# 
# 
#Diccionario

# persona = {
#     'clave': '123456789',
#     'nombre': 'Elizabeth',
#     'edad': 21,

# }

# print(persona['clave'])

# persona = {}

# def agregarPersona (clave:str, valor: str):
#     persona.update({clave : valor})
#     print(persona)

# agregarPersona('123', 'Pepe')   



# Ejercicio

mascotas = {}
continuar : bool = True

def agregarMascota (clave: str, valor:str):
    mascotas.update({clave:valor})



def quitarMascota (clave: str):
      mascotas.pop(clave)
      
    


while continuar:
    accion = int(input('Escoge la acción: 1. Agregar / 2. Eliminar / 3. Salir: '))

    if accion ==1:
            print('Agrega clave')
            clave :str = input()
            print('Agrega valor')
            valor :str = input()
            agregarMascota(clave, valor)
            print(mascotas)
    if accion ==2:   
            print('Agrega clave')
            clave :str = input()
            quitarMascota(clave)
            print('Eliminado con exito')
            print(mascotas)
    if accion ==3:
        print('Adios')
        continuar = False

print(mascotas)