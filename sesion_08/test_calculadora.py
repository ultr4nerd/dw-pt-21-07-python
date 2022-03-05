"""Usa clases"""

import unittest
from unittest import mock
from calculadora import Calculadora


class PruebaCalculadora(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configura algo al INICIO de TODAS las pruebas (una vez por clase)
        pass

    @classmethod
    def tearDownClass(cls):
        # Configura algo al FINAL de TODAS las pruebas (una vez por clase)
        pass

    def setUp(self):
        # Configurar la prueba al INICIO de cada prueba (una vez por prueba)
        self.calculadora = Calculadora()

    def tearDown(self):
        # Configurar la prueba al FINAL de cada prueba (una vez por prueba)
        pass

    # Unitaria
    def test_suma(self):
        resultado = self.calculadora.suma(2, 4)
        self.assertEqual(resultado, 6)

    # Unitaria
    def test_multiplicacion__unit(self):
        # Preparación de pruebas
        self.calculadora.suma = mock.Mock()
        return_value = self.calculadora.suma.return_value
        calls = [
            mock.call(0, 2),
            mock.call(return_value, 2),
            mock.call(return_value, 2),
        ]

        # Ejecución
        self.calculadora.multiplicacion(2, 3)

        # Evaluación
        self.assertEqual(self.calculadora.suma.call_count, 3)
        self.calculadora.suma.assert_has_calls(calls)

    # Integración
    def test_multiplicacion__integration(self):
        resultado = self.calculadora.multiplicacion(2, 4)
        self.assertEqual(resultado, 8)

    @unittest.skip
    def test_resta(self):
        resultado = self.calculadora.resta(6, 2)
        self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
