import unittest

from reto_01 import Vector

class VectorTestCase(unittest.TestCase):

    def test_add(self):
        vector1 = Vector(3, 4)
        vector2 = Vector(6, 7)
        vector3 = vector1 + vector2
        self.assertEqual(vector3.x, 9)
        self.assertEqual(vector3.y, 11)

    def test_mul(self):
        vector = Vector(2, 4)
        result = 3 * vector
        self.assertEqual(result.x, 6)
        self.assertEqual(result.y, 12)


if __name__ == '__main__':
    unittest.main()
