import unittest
from simple_calculator import SimpleCalculator


class AddTestFunctions(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 20), 30) 
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(100, 40), 60)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 7), 35)

    def test_division(self):
        self.assertEqual(self.calc.divide(20, 4), 5)

if __name__ == "__main__":
    unittest.main()
