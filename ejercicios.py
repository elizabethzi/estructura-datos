# Triangulo de numeros


# numeros = list()

# def trianguloNumeros(numero: int)->None:
#     numero = int(input('Ingresa hasta que numero debe llegar el triangulo: '))
    
#     for i in range(0, numero):
#         numeros.append(i+1)
#         print(numeros)

# trianguloNumeros(numeros)

#                Multiplicacion

# numeroUno = int (input('Ingrese número a multiplicar: '))
# numeroDos = int(input('Por: '))

# def multiplicacion(numeroUno: int, numeroDos: int)->None:
#     resultado = 0
#     for i in range (0, numeroUno):
     
#         resultado = resultado + numeroDos

#     print(resultado)

# multiplicacion(numeroUno, numeroDos)       

#              Division

numeroUnoDiv = int (input('Ingrese número a dividir: '))
numeroDosDiv = int(input('Entre: '))

def division(numeroUnoDiv: int, numeroDosDiv: int)->None:
    resultado = 0

    numeroUnoDiv = numeroUnoDiv + numeroDosDiv

    if resultado >=0:
     
        resultado = resultado + 1
        numeroUnoDiv = numeroUnoDiv - numeroDosDiv

    print(resultado)

division(numeroUnoDiv, numeroDosDiv)  