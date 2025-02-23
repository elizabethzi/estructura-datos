#Ejercicio 1

# def fibonacci(n, n1=0, n2=1, fibo = []):
#     if fibo is None:
#         fibo.append(n1, n2)  

#     if len(fibo) >= n: #mayor o igual a longitud de fibo
#         return fibo

#     fibo.append(n1 + n2) 
#     return fibonacci(n, n2, n1 + n2, fibo)  

# numero = 10  
# print(fibonacci(numero))

#Ejercicio 2

# def llenarArray(arr=None, contador=0):
#     if arr is None:
#         arr = []  

#     if contador == 5:  
#         return arr  

#     numero = int(input("Ingrese los datos del arreglo: "))
#     arr.append(numero)  
#     return llenarArray(arr, contador + 1)  

# def suma(arr, i=0):
#     if i == len(arr):  
#         return 0  
#     return arr[i] + suma(arr, i + 1)  


# datos = llenarArray()


# resultado = suma(datos)

# print(datos)
# print("Resultado:", resultado)

#Ejercicio 3

# numeroUno = int(input('Ingrese número a multiplicar: '))
# numeroDos = int(input('Por: '))

# def multiplicacion(numeroUno: int, numeroDos: int,resultado=0) -> int:
    
#     if numeroUno == 0:
#         return resultado
#     return multiplicacion(numeroUno - 1, numeroDos, resultado + numeroDos)  

# resultado = multiplicacion(numeroUno, numeroDos)
# print(resultado)

#Ejercicio 4

# def division(dividendo: int, divisor: int, contador=0) -> int:
#     if divisor == 0:
#         return print('No se divide por 0')  

#     if dividendo < divisor: 
#         return contador  
    
#     return division(dividendo - divisor, divisor, contador + 1)  


# dividendo = int(input("Dividendo: "))
# divisor = int(input("Divisor: "))


# resultado = division(dividendo, divisor)

# print(resultado)
