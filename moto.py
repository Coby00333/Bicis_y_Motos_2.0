from bicicle import Bicicleta
#clase moto hija de la clase bicicleta
class Moto(Bicicleta):
#Constructor de la clase moto
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
#informacion de la clase moto
    def __str__(self):
        return f"Moto {self.marca} {self.modelo} de color {self.color}, cilindrada: {self.cilindrada}cc, velocidad actual: {self.velocidad} km/h"

# Ejemplo de uso
#objeto moto1
moto1 = Moto("Honda", "CB500X", "Rojo", 500)
#llamando a los métodos de la clase
moto1.acelerar(20)
print(moto1)  # Salida: Moto Honda CB500X de color Rojo, cilindrada: 500cc, velocidad actual: 20 km/h

moto1.frenar(10)
print(moto1)  # Salida: Moto Honda CB500X de color Rojo, cilindrada: 500cc, velocidad actual: 10 km/h

moto1.frenar(20)
print(moto1)  # Salida: Moto Honda CB500X de color Rojo, cilindrada: 500cc, velocidad actual: 0 km/h

