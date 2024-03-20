class Bicicleta:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        if self.velocidad >= decremento:
            self.velocidad -= decremento
        else:
            self.velocidad = 0

    def __str__(self):
        return f"Bicicleta {self.marca} {self.modelo} de color {self.color}, velocidad actual: {self.velocidad} km/h"

bicicleta1 = Bicicleta("Orbea", "Alma", "Negro")
bicicleta1.acelerar(10)
print(bicicleta1)  # Salida: Bicicleta Orbea Alma de color Negro, velocidad actual: 10 km/h
bicicleta1.frenar(5)
print(bicicleta1)  # Salida: Bicicleta Orbea Alma de color Negro, velocidad actual: 5 km/h
bicicleta1.frenar(10)
print(bicicleta1)  # Salida: Bicicleta Orbea Alma de color Negro, velocidad actual: 0 km/h


#-------------------------------------------------------------------



