import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        x_y_outputs = (
            (1, 2, 3), 
            (2, 3, 5), 
            (3, 4, 7))
        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(Calculadora().soma(x, y), output)



unittest.main()