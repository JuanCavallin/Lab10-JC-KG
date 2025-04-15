#https://github.com/JuanCavallin/Lab10-JC-KG
#Partner 1: Juan Cavallin
#Partner 2: Kieran Galveston
import unittest
import calculator as c

class Test(unittest.TestCase):
    def setUp(self):
        self.c = c

    def test_add(self):
        self.assertEqual(self.c.add(9, 10), 19)
        self.assertEqual(self.c.add(1, -2), -1)

    def test_subtract(self):
        self.assertEqual(self.c.sub(9, 10), -1)
        self.assertEqual(self.c.sub(-1, -1), 0)

    def test_divide_by_zerp(self):
        with self.assertRaises(ZeroDivisionError):
            self.c.div(0, 15)
        with self.assertRaises(ZeroDivisionError):
            self.c.div(0, 0)

    def test_logarithm(self):
        self.assertEqual(self.c.log(2, 8), 3)
        self.assertEqual(self.c.log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            self.c.log(10, 1)
        with self.assertRaises(ValueError):
            self.c.log(-1, 9)
        with self.assertRaises(ValueError):
            self.c.log(0, 12)

    def test_multiply(self):
        self.assertEqual(self.c.mul(3, 4), 12)
        self.assertEqual(self.c.mul(-2, 5), -10)
        self.assertEqual(self.c.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.c.div(2, 10), 5)
        self.assertEqual(self.c.div(3, -15), -5)
        with self.assertRaises(ZeroDivisionError):
            self.c.div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.c.logarithm(0, 10)
        with self.assertRaises(ValueError):
            self.c.logarithm(-3, 10)
        with self.assertRaises(ValueError):
            self.c.logarithm(10, 1)

    def test_hypotenuse(self):
        self.assertEqual(self.c.hypotenuse(3, 4), 5)
        self.assertEqual(self.c.hypotenuse(-3, -4), 5)

    def test_sqrt(self):
        self.assertEqual(self.c.square_root(25), 5)
        with self.assertRaises(ValueError):
            self.c.square_root(-1)

if __name__ == "__main__":
    unittest.main()
