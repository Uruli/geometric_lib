import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):

        a, b, c = 5, 4, 3

        result = area(a, b, c)

        self.assertEqual(result, 6)
    
    def test_perimeter(self):
        a, b, c = 5, 4, 3

        result = perimeter (a, b, c)

        self.assertEqual(result,12)

if __name__ == '__main__':
    unittest.main()