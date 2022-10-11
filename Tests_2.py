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

        def test_maximum(self):
            test_max = _max(line)
            self.assertEqual(test_max, max(line))

        def test_minimum(self):
            test_min = _min(line)
            self.assertEqual(test_min, min(line))

        def test_summa(self):
            test_sum = _sum(line)
            self.assertEqual(test_sum, sum(line))

        def test_multiply(self):
            test_mult = _mult(line)
            self.assertEqual(test_mult, reduce(lambda x, y: x * y, (line)))

        def test_del(self):
            test_delimost = _delimost(line)
            self.assertEqual(test_delimost, sum(line) % 3)
    else:
        pass



if __name__ == '__main__':
    unittest.main()
