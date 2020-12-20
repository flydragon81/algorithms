import unittest
from functions import find_smallest, find_biggest, average_number, bubble_sort, insertion_sort


class FindSmallestTest(unittest.TestCase):
    def test(self):
        data = [1, 5, 6, 15, 7, 55, -40]
        idx = find_smallest(data)
        self.assertEqual(6, idx)

        data = [1, 5, 6, -150, 7, 55, -40]
        idx = find_smallest(data)
        self.assertEqual(3, idx)
        self.assertEqual(-150, data[idx])


class FindBiggestNumberTest(unittest.TestCase):
    def test(self):
        data = [1, 5, 6, 15, 7, 55, -40]
        idx = find_biggest(data)
        self.assertEqual(5, idx)

        data = [1, 5, 6, -150, 77, 155, -40]
        idx = find_biggest(data)
        self.assertEqual(5, idx)
        self.assertEqual(155, data[idx])


class AverageNumberTest(unittest.TestCase):
    def test(self):
        data = [6, 8, 10, 17, 14]
        avg = average_number(data)
        self.assertEqual(11, avg)


class BubbleSortTest(unittest.TestCase):
    def test(self):
        data = [3, 2, 7, 4, 9]
        result = bubble_sort(data)
        self.assertEqual([2, 3, 4, 7, 9], result)

        result = bubble_sort(data, False)
        self.assertEqual([9, 7, 4, 3, 2], result)


class InsectSortTest(unittest.TestCase):
    def test(self):
        data = [3, 2, 7, 4, 9]
        result = insertion_sort(data)
        self.assertEqual([2, 3, 4, 7, 9], result)

        result = insertion_sort(data, False)
        self.assertEqual([9, 7, 4, 3, 2], result)
