import unittest
from simple_calculator import SimpleCalculator


class AddTestFunctions(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_add_numbers(self):
        self.assertEqual(self.calc.add(10, 20), 30) 
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    def test_subtract_numbers(self):
        self.assertEqual(self.calc.subtract(100, 40), 60)

    def test_multiply_numbers(self):
        self.assertEqual(self.calc.multiply(5, 7), 35)

if __name__ == "__main__":
    unittest.main()
