import unittest

from sudoku import new_locate

class MyTestCase(unittest.TestCase):
    def test_fun(self):
        test_num=new_locate(5,8,0,0)
        self.assertEqual(test_num,(0,0,0,0))


if __name__ == '__main__':
    unittest.main()
