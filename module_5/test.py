target = __import__('mysum.py')
sum = target.sum

import unittest

from mysum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == "__main_":
    unittest.main()