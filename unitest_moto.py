import unittest
from moto import Moto  # Importa la clase Moto desde el módulo moto

class TestMoto(unittest.TestCase):
    def setUp(self):
        self.moto = Moto("Honda", "CB500X", "Rojo", 500)  # Instancia un objeto Moto para usar en los tests

    def test_acelerar(self):
        # Prueba el método acelerar para incrementar la velocidad correctamente
        self.moto.acelerar(20)
        self.assertEqual(self.moto.velocidad, 20)  # Comprueba que la velocidad sea 20 después de acelerar en 20 km/h

    def test_frenar(self):
        # Prueba el método frenar para reducir la velocidad correctamente
        self.moto.velocidad = 20
        self.moto.frenar(10)
        self.assertEqual(self.moto.velocidad, 10)  # Comprueba que la velocidad sea 10 después de frenar en 10 km/h

        # Prueba que frenar detenga la moto cuando la velocidad es menor que el decremento
        self.moto.frenar(20)
        self.assertEqual(self.moto.velocidad, 0)  # Comprueba que la velocidad sea 0 después de frenar en 20 km/h

    def test_str(self):
        # Prueba el método __str__ para asegurarse de que devuelve la cadena esperada
        expected_output = "Moto Honda CB500X de color Rojo, cilindrada: 500cc, velocidad actual: 0 km/h"
        self.assertEqual(str(self.moto), expected_output)  # Comprueba que la representación de cadena sea correcta

if __name__ == '__main__':
    unittest.main()  # Ejecuta los tests
