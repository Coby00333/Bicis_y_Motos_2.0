class Moto:

    def __init__(self, marca, modelo, color, cilindrada):
        # Atributos protegidos
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._cilindrada = cilindrada
        self.velocidad = 0

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_cilindrada(self):
        return self._cilindrada

    def set_cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def __str__(self):
        return f"""
        Moto:
            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}
            Cilindrada: {self._cilindrada}cc
            Velocidad actual: {self.velocidad} km/h
        """

moto = Moto("Yamaha", "R2", "Azul", 1500)


print(moto) 

