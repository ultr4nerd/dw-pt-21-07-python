"""Usa funciones"""

import unittest
from unittest import mock
from aritmeticas import suma, multiplicacion


class PruebaAritmeticas(unittest.TestCase):
    # Unitaria
    def test_suma(self):
        resultado = suma(2, 4)
        self.assertEqual(resultado, 6)

    # Integración
    def test_multiplicacion__integration(self):
        resultado = multiplicacion(2, 4)
        self.assertEqual(resultado, 8)

    
    @mock.patch("aritmeticas.suma")
    def test_multiplicacion__unit(self, mock_suma):
        # Preparación de pruebas
        return_value = mock_suma.return_value
        calls = [
            mock.call(0, 2),
            mock.call(return_value, 2),
            mock.call(return_value, 2),
        ]

        # Ejecución
        multiplicacion(2, 3)

        # Evaluación
        self.assertEqual(mock_suma.call_count, 3)
        mock_suma.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
