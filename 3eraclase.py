####### Factoriales

# numero = 5
# resultado : int

# def factorial (n :int )->int:
#     resultado :int =1
#     for i in range (1, n+1):
#         resultado = resultado * i
#     return resultado
# print(factorial(numero))

#  ##################         While

# numero = 6

# def factorialWhile (n : int)->int:
#     res: int = 1
#     contador = 0

#     while contador <n:
#         contador = contador + 1
#         res = res * contador
#     return res
    
# print(factorialWhile(numero))    



# numero = 5
# def factoral(n:int) ->int:
#     if n == 1:
#         return n
#     return factoral(n-1) * n

# print(factoral(numero))   


# numeroUno :int = 0
# numeroDos :int = 1
# resultado = 0
fibo = list()

# fibo.append(numeroUno)
# fibo.append(numeroDos)

# for i in range(2, 10):
    
#     resultado = numeroUno + numeroDos
#     numeroUno=numeroDos
#     numeroDos = resultado

#     fibo.append(resultado)

# print(fibo, 'actualizado')

##### Recursion

def fibonacci (n:int)->int:
        
        if n==0:
            fibo.append(n)
            return 0
        elif n ==1:
            fibo.append(n)
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        

print(fibonacci(10-1))

