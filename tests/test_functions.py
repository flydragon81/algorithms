import unittest
from functions import find_smallest_number
from functions import find_biggest_number


class FindSmallestNumberTest(unittest.TestCase):
    def test(self):
        data = [1, 5, 6, 15, 7, 55, -40]
        idx = find_smallest_number(data)
        self.assertEqual(6, idx)

        data = [1, 5, 6, -150, 7, 55, -40]
        idx = find_smallest_number(data)
        self.assertEqual(3, idx)
        self.assertEqual(-150, data[idx])


class FindBiggestNumberTest(unittest.TestCase):
    def test(self):
        data = [1, 5, 6, 15, 7, 55, -40]
        idx = find_biggest_number(data)
        self.assertEqual(5, idx)

        data = [1, 5, 6, -150, 77, 155, -40]
        idx = find_biggest_number(data)
        self.assertEqual(5, idx)
        self.assertEqual(155, data[idx])
