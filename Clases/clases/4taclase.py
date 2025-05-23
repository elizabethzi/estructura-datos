# # POO

# clase -> class
# metodo -> def
# atributo -> variable dentro de una classmethod


# # ############

# Herencia -> heredar atributos o caracteristicas de la clase padre


# ##########

# Metodos /atributos privados

# Metodos o atributos que son solo acreditados desde la misma clase o clase hija


# Protegidos

# Apuntadores


class Vehiculo:
    color: str
    marca: str
    modelo: str
    cilindraje: int
    numero_ruedas: int  
    combustible: int
    tipo_de_vehiculo: str

    def __init__(self, tipo_de_vehiculo: str, marca: str, combustible: int):
        self.marca = marca
        self.combustible = combustible
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.encendido = False

    def __str__(self) -> str:
        return f"Tipo de vehículo: {self.tipo_de_vehiculo}, Marca: {self.marca}, Combustible: {self.combustible} galones"

    def encenderVehiculo(self):
        if self.combustible <= 10:
            print(f"Combustible en {self.combustible}, es muy bajo, ve a recargar")
        elif self.combustible == 0:
            self.apagarVehiculo()
        else:
            self.encendido = True
            print("Vehículo encendido y listo para usar.")

    def acelerarVehiculo(self):
        if not self.encendido:
            print("El vehículo está apagado. Enciéndalo primero.")
            return
        if self.combustible <= 0:
            print("No hay combustible. No puede avanzar.")
            return
        
        while self.combustible > 0:
            self.combustible -= 1
            print(f"Nivel de combustible: {self.combustible} galones")
            if self.combustible <= 10:
                print("Advertencia: Nivel de combustible bajo. Debe ir a la gasolinera.")
            if self.combustible == 0:
                self.apagarVehiculo()
                break

    def apagarVehiculo(self):
        self.encendido = False
        print(f"Combustible en {self.combustible}, el vehículo se ha detenido.")


class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: int):
        super().__init__("Moto", marca, combustible)


class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: int):
        super().__init__("Carro", marca, combustible)


carro1 = Carro("Bolita", 11)
moto1 = Moto("Boxer", 0)


# print(moto1)
# moto1.encenderVehiculo()
# moto1.acelerarVehiculo()

print(carro1)
carro1.encenderVehiculo()
carro1.acelerarVehiculo()

   


# #Constructor

# def __init__(self):
#     pass




