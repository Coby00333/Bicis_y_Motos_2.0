import unittest 
from bicicle import Bicicleta

class TestBicicleta(unittest.TestCase):
    def setUp(self):
        self.bicicleta = Bicicleta("Orbea", "Alma", "Negro")  # Instancia un objeto Bicicleta para usar en los tests

    def test_acelerar(self):
        # Prueba el método acelerar para incrementar la velocidad correctamente
        self.bicicleta.acelerar(10)
        self.assertEqual(self.bicicleta.velocidad, 10)  # Comprueba que la velocidad sea 10 después de acelerar en 10 km/h

    def test_frenar(self):
        # Prueba el método frenar para reducir la velocidad correctamente
        self.bicicleta.velocidad = 10
        self.bicicleta.frenar(5)
        self.assertEqual(self.bicicleta.velocidad, 5)  # Comprueba que la velocidad sea 5 después de frenar en 5 km/h

        # Prueba que frenar detenga la bicicleta cuando la velocidad es menor que el decremento
        self.bicicleta.frenar(10)
        self.assertEqual(self.bicicleta.velocidad, 0)  # Comprueba que la velocidad sea 0 después de frenar en 10 km/h

    def test_str(self):
        # Prueba el método __str__ para asegurarse de que devuelve la cadena esperada
        expected_output = "Bicicleta Orbea Alma de color Negro, velocidad actual: 0 km/h"
        self.assertEqual(str(self.bicicleta), expected_output)  # Comprueba que la representación de cadena sea correcta

if __name__ == '__main__':
    unittest.main()  # Ejecuta los tests