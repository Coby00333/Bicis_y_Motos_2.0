class Moto:

    def __init__(self, marca, modelo, color, cilindrada):
        self.__marca = marca  # Atributo ahora privado
        self.__modelo = modelo  # Atributo ahora privado
        self.__color = color  # Atributo ahora privado
        self.__cilindrada = cilindrada  # Atributo ahora privado
        self.velocidad = 0

    def __str__(self):
         # No se puede acceder directamente desde fuera de la clase
        return f"""
        Moto:
            Marca: {self.__marca} 
            Modelo: {self.__modelo} 
            Color: {self.__color}  
            Cilindrada: {self.__cilindrada}cc  
            Velocidad actual: {self.velocidad} km/h
        """

    # Métodos para acceder y modificar los atributos privados (getters y setters)

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

