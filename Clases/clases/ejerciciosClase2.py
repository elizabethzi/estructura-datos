class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}."


class CuentaBancaria:
    def __init__(self, titular, saldo, numeroDeCuenta):
        self.titular = titular  # Objeto Persona
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta
    
    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Nuevo saldo: {self.saldo}"
    
    def retirar(self, monto):
        if monto > self.saldo:
            return "Fondos insuficientes."
        self.saldo -= monto
        return f"Retiro exitoso. Nuevo saldo: {self.saldo}"
    
    def consultarSaldo(self):
        return f"Saldo disponible: {self.saldo}"


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio


class Libro:
    def __init__(self, titulo, autor, genero, anioPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anioPublicacion = anioPublicacion
    
    def mostrarDetalles(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.anioPublicacion}"


class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
    
    def reproducir(self):
        return f"Reproduciendo: {self.titulo} de {self.artista}..."


class Producto:
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible
    
    def calcularTotal(self, cantidad):
        if cantidad > self.cantidadDisponible:
            return "Stock insuficiente."
        return f"Total a pagar: {self.precio * cantidad}"


class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    
    def calcular_promedio(self):
        if not self.calificaciones:
            return "No hay calificaciones."
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def esta_aprobado(self):
        return "Aprobado" if self.calcular_promedio() >= 6 else "Reprobado"
    



# Crear una persona
persona1 = Persona("Juan", 30, "Masculino")
print(persona1.presentarse())

# Crear una cuenta bancaria
cuenta1 = CuentaBancaria(persona1, 1000, "123456789")
print(cuenta1.depositar(500))
print(cuenta1.retirar(200))
print(cuenta1.consultarSaldo())

# Crear un rectángulo
rectangulo1 = Rectangulo(10, 5)
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")

# Crear un círculo
circulo1 = Circulo(7)
print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Circunferencia del círculo: {circulo1.calcular_circunferencia()}")

# Crear un libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
print(libro1.mostrarDetalles())

# Crear una canción
cancion1 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "5:55")
print(cancion1.reproducir())

# Crear un producto
producto1 = Producto("Laptop", 1200, 5)
print(producto1.calcularTotal(2))

# Crear un estudiante
estudiante1 = Estudiante("Ana", 20, "Matemáticas")
estudiante1.agregar_calificacion(8)
estudiante1.agregar_calificacion(9)
print(f"Promedio: {estudiante1.calcular_promedio()}")
print(f"Estado: {estudiante1.esta_aprobado()}")
