# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import es_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_par(self):
        assert es_par(4)
        assert not(es_par(7))
        assert es_par(12)
        assert es_par(8)

