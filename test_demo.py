import unittest

from demo import compare

class MyTestCase(unittest.TestCase):

    def test_compare(self):
        test_min = compare(1, 2)
        self.assertEqual(test_min, 1)



if __name__ == '__main__':
    unittest.main()
