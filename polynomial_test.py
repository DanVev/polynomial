import unittest
from polynomial import Polynomial


class Polynomial_test(unittest.TestCase):
    def setUp(self):
        self.a = Polynomial([1, 2, 3])
        self.b = Polynomial([-3, 0])
        self.c = Polynomial([0, 2, -1])

    def test_init(self):
        with self.assertRaises(ValueError):
            Polynomial([])
        self.assertEqual(Polynomial([1, 2, 3]).coeffs, [1, 2, 3])
        self.assertEqual(Polynomial([-3, 0]).coeffs, [-3, 0])
        self.assertEqual(Polynomial([0, 2, -1]).coeffs, [2, -1])

    def test_len(self):
        self.assertEqual(len(self.a), 3)
        self.assertEqual(len(self.c), 2)

    def test_eq(self):
        self.assertTrue(self.a == self.a)
        self.assertFalse(self.b == self.c)
        self.assertFalse(self.a == self.c)

    def test_not_eq(self):
        with self.assertRaises(TypeError):
            self.a == " "
        self.assertFalse(self.a != self.a)
        self.assertTrue(self.b != self.c)

    def test_add(self):
        with self.assertRaises(TypeError):
            self.a + " "
        self.assertEqual((self.a + 1).coeffs, [1, 2, 4])
        self.assertEqual((1 + self.a).coeffs, [1, 2, 4])
        self.assertEqual((self.a + self.b).coeffs, [1, -1, 3])
        self.assertEqual((self.b + self.c).coeffs, [-1, -1])
        self.assertEqual((self.b + Polynomial([3, 3])).coeffs, [3])

    def test_mul(self):
        with self.assertRaises(TypeError):
            self.a * " "
        self.assertEqual(-1 * self.a, self.a * -1)
        self.assertEqual((-1 * self.a).coeffs, [-1, -2, -3])
        self.assertEqual((self.a * self.b).coeffs, [-3, -6, -9, 0])
        self.assertEqual((self.b * self.c).coeffs, [-6, 3, 0])

    def test_sub(self):
        with self.assertRaises(TypeError):
            self.a - " "
        self.assertEqual((self.a - 1).coeffs, [1, 2, 2])
        self.assertEqual((self.a - self.b).coeffs, [1, 5, 3])
        self.assertEqual((self.b - self.c).coeffs, [-5, 1])

    def test_str(self):
        self.assertEqual(str(self.a), "x^2+2x+3")
        self.assertEqual(str(self.b), "-3x")
        self.assertEqual(str(self.c), "2x-1")
        self.assertEqual(str(Polynomial([0])), "0")

    def test_input_fails(self):
        with self.assertRaises(ValueError):
            p = Polynomial([])
        with self.assertRaises(ValueError):
            p = Polynomial('abc')
            c = p + 1
        with self.assertRaises(ValueError):
            p = Polynomial((1.0, 1.3))

        with self.assertRaises(ValueError):
            p = Polynomial({1.0, 1.3})

        with self.assertRaises(TypeError):
            d = self.a + 'asb'
        with self.assertRaises(TypeError):
            e = 'asb' + self.a
        with self.assertRaises(TypeError):
            self.a * 'asdc'

    def test_repr(self):
        self.assertEqual(repr(self.a), 'Polynomial([1, 2, 3])')
        self.assertEqual(repr(self.c), 'Polynomial([2, -1])')
