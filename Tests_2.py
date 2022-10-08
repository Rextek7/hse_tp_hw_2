import Homework_2
import unittest
from functools import reduce


class TestCase(unittest.TestCase):

    def test_maximum(self):
        test_max = Homework_2._max(Homework_2.line)
        self.assertEqual(test_max, max(Homework_2.line))

    def test_minimum(self):
        test_min = Homework_2._min(len(Homework_2.line))
        self.assertEqual(test_min, min(Homework_2.line))

    def test_summa(self):
        test_sum = Homework_2._sum(Homework_2.line)
        self.assertEqual(test_sum, sum(Homework_2.line))

    def test_multiply(self):
        test_mult = Homework_2._mult(Homework_2.line)
        self.assertEqual(test_mult, reduce(lambda x, y: x * y, (Homework_2.line)))

    def test_del(self):
        test_delimost = Homework_2._delimost(Homework_2.line)
        self.assertEqual(test_delimost, sum(Homework_2.line) % 3)


if __name__ == '__main__':
    unittest.main()
