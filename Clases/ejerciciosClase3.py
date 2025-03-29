class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        return f"{self.nombre} está trabajando en el departamento de {self.departamento}."


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo  # Lista de empleados

    def trabajar(self):
        return f"{self.nombre} está supervisando un equipo de {len(self.equipo)} empleados."


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        return f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}."


class FiguraGeometrica:
    def calcular_area(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergético):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergético = consumoEnergético

    def encender(self):
        return f"El electrodoméstico {self.marca} {self.modelo} está encendido."


class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergético, capacidad):
        super().__init__(marca, modelo, consumoEnergético)
        self.capacidad = capacidad

    def encender(self):
        return f"La lavadora {self.marca} inicia el ciclo de lavado con capacidad de {self.capacidad} kg."


class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergético, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergético)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        return f"El refrigerador {self.marca} está regulando la temperatura." if self.tieneCongelador else f"El refrigerador {self.marca} está enfriando sin congelador."


class Usuario:
    def __init__(self, nombreDeUsuario, contraseña):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña

    def iniciar_sesion(self, usuario, contraseña):
        return "Inicio de sesión exitoso" if usuario == self.nombreDeUsuario and contraseña == self.contraseña else "Credenciales incorrectas."


class Administrador(Usuario):
    def gestionar_usuarios(self):
        return "Gestionando usuarios..."


class Cliente(Usuario):
    def realizar_compra(self):
        return "Realizando compra..."


# Pruebas de impresión
empleado1 = Empleado("Juan", 50000, "Recursos Humanos")
gerente1 = Gerente("Ana", 70000, "Ventas", ["Pedro", "Luis"])
desarrollador1 = Desarrollador("Carlos", 60000, "IT", "Python")

print(empleado1.trabajar())
print(gerente1.trabajar())
print(desarrollador1.trabajar())

triangulo1 = Triangulo(10, 5)
cuadrado1 = Cuadrado(4)
print(f"Área del triángulo: {triangulo1.calcular_area()}")
print(f"Área del cuadrado: {cuadrado1.calcular_area()}")

lavadora1 = Lavadora("LG", "T200", "Bajo", 7)
refrigerador1 = Refrigerador("Samsung", "Frost", "Medio", True)
print(lavadora1.encender())
print(refrigerador1.encender())

usuario1 = Usuario("usuario123", "pass123")
administrador1 = Administrador("admin", "adminpass")
cliente1 = Cliente("cliente1", "clientePass")
print(usuario1.iniciar_sesion("usuario123", "pass123"))
print(administrador1.gestionar_usuarios())
print(cliente1.realizar_compra())
