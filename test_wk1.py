import unittest

from wk1 import func1


class MyTestCase(unittest.TestCase):
    def test_fun1(self):
        test_num = func1(2, 1, 6)
        self.assertEqual(test_num, 5)


if __name__ == '__main__':
    unittest.main()
