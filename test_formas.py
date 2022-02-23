import unittest
from formas import Circulo, Forma

class TestFormas(unittest.TestCase):
    def test_clase_forma_existe(self):
        f = Forma()
        self.assertIsNotNone(f)

    def test_nombre_forma(self):
        f = Forma()
        self.assertEqual(f.__str__(),'Forma')

class TestCirculo(unittest.TestCase):
    def test_clase_circulo_existe(self):
        c = Circulo()
        self.assertIsNotNone(c)