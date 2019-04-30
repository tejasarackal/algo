import unittest
import bit_manipulation.insertion as e


class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(e.insertion(m = 100000000, n = 11011, i = 2, j = 6), 101101100)


if __name__ == '__main__':
    unittest.main()

