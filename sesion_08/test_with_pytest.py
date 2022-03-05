"""Usa funciones"""

from unittest.mock import patch, call

import pytest

from aritmeticas import suma, multiplicacion


@pytest.fixture
def resultado_integracion():
    return 8


@pytest.mark.parametrize("first, second, result", [
    (0, 1, 1),
    (1, 0, 1),
    (2, 3, 5),
])
def test_suma(first, second, result):
    resultado = suma(first, second)
    assert resultado == result


def test_multiplicacion__integration(resultado_integracion):
    resultado = multiplicacion(2, 4)
    assert resultado == resultado_integracion


@patch("aritmeticas.suma")
def test_multiplicacion__unit(mock_suma):
    # Preparación de pruebas
    return_value = mock_suma.return_value
    calls = [
        call(0, 2),
        call(return_value, 2),
        call(return_value, 2),
    ]

    # Ejecución
    multiplicacion(2, 3)

    # Evaluación
    assert mock_suma.call_count == 3
    mock_suma.assert_has_calls(calls)
