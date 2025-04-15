#https://github.com/JuanCavallin/Lab10-JC-KG
#Partner 1: Juan Cavallin
#Partner 2: Kieran Galveston
import unittest
import calculator as c

class Test(unittest.TestCase):
    def setUp(self):
        self.c = c

    def test_add(self):
        self.assertEqual(self.c.add(9,10), 19)
        self.assertEqual(self.c.add(1, -2), -1)
    def test_subtract(self):
        self.assertEqual(self.c.sub(9, 10), -1)
        self.assertEqual(self.c.sub(-1, -1), 0)
    def test_divide_by_zerp(self):
        self.assertEqual(self.c.div(15, 0), 0)
        with self.assertRaises(ZeroDivisionError):
            self.c.div(0, 15)
    def test_logarithm(self):
        self.assertEqual(self.c.log(2, 8),3)
        self.assertEqual(self.c.log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            self.c.log(10, 1)
        with self.assertRaises(ValueError):
            self.c.log(-1, 9)
        with self.assertRaises(ValueError):
            self.c.log(0, 12)
if __name__ == "__main__":
    unittest.main()

