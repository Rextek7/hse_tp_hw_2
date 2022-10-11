from Homework_2 import _max
from Homework_2 import _min
from Homework_2 import _sum
from Homework_2 import _mult
from Homework_2 import _delimost
from Homework_2 import line
import os
import unittest
from functools import reduce


class TestCase(unittest.TestCase):

    if os.stat('Numbers.txt').st_size != 0:

        def test_01_maximum(self):
            test_max = _max(line)
            self.assertEqual(test_max, max(line))

        def test_02_minimum(self):
            test_min = _min(line)
            self.assertEqual(test_min, min(line))

        def test_03_summa(self):
            test_sum = _sum(line)
            self.assertEqual(test_sum, sum(line))

        def test_04_multiply(self):
            test_mult = _mult(line)
            self.assertEqual(test_mult, reduce(lambda x, y: x * y, (line)))

        def test_05_del(self):
            test_delimost = _delimost(line)
            self.assertEqual(test_delimost, sum(line) % 3)
    else:
        def test_02_min_on_empty_file(self):
            self.assertIsNone(_min(line))

        def test_01_max_on_empty_file(self):
            self.assertIsNone(_max(line))

        def test_03_summ_on_empty_file(self):
            self.assertIsNone(_sum(line))

        def test_04_mult_on_empty_file(self):
            self.assertIsNone(_mult(line))

        def test_05_del_on_empty_file(self):
            self.assertIsNone(_delimost(line))



if __name__ == '__main__':
    unittest.main()
