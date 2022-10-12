import Homework_2
import os
import unittest
from functools import reduce


class TestCase(unittest.TestCase):

    if os.stat('Numbers.txt').st_size != 0:

        def test_01_maximum(self):
            test_max = Homework_2._max(Homework_2.line)
            self.assertEqual(test_max, max(Homework_2.line))

        def test_02_minimum(self):
            test_min = Homework_2._min(Homework_2.line)
            self.assertEqual(test_min, min(Homework_2.line))

        def test_03_summa(self):
            test_sum = Homework_2._sum(Homework_2.line)
            self.assertEqual(test_sum, sum(Homework_2.line))

        def test_04_multiply(self):
            test_mult = Homework_2._mult(Homework_2.line)
            self.assertEqual(test_mult, reduce(lambda x, y: x * y, (Homework_2.line)))

        def test_05_del(self):
            test_delimost = Homework_2._delimost(Homework_2.line)
            self.assertEqual(test_delimost, sum(Homework_2.line) % 3)
    else:
        def test_02_min_on_empty_file(self):
            self.assertIsNone(Homework_2._min(Homework_2.line))

        def test_01_max_on_empty_file(self):
            self.assertIsNone(Homework_2._max(Homework_2.line))

        def test_03_summ_on_empty_file(self):
            self.assertIsNone(Homework_2._sum(Homework_2.line))

        def test_04_mult_on_empty_file(self):
            self.assertIsNone(Homework_2._mult(Homework_2.line))

        def test_05_del_on_empty_file(self):
            self.assertIsNone(Homework_2._delimost(Homework_2.line))



if __name__ == '__main__':
    unittest.main()
