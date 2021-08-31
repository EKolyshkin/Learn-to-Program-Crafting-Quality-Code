import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_1(self):
        '''Test a1.swap_k with empty list.'''

        L = []
        a1.swap_k(L, 0)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_2(self):
        '''Test a1.swap_k with single-item list.'''

        L = [1]
        a1.swap_k(L, 0)
        expected = [1]
        self.assertEqual(L, expected)

    def test_swap_k_3(self):
        '''Test a1.swap_k with minimum swappable even list.'''

        L = [1, 2]
        a1.swap_k(L, 1)
        expected = [2, 1]
        self.assertEqual(L, expected)

    def test_swap_k_4(self):
        '''Test a1.swap_k with minimum swappable odd list.'''

        L = [1, 2, 3]
        a1.swap_k(L, 1)
        expected = [3, 2, 1]
        self.assertEqual(L, expected)

    def test_swap_k_5(self):
        '''Test a1.swap_k with minimum swappable even list where peculiarity is shown.'''

        L = [1, 2, 3, 4]
        a1.swap_k(L, 2)
        expected = [3, 4, 1, 2]
        self.assertEqual(L, expected)

    def test_swap_k_6(self):
        '''Test a1.swap_k with minimum swappable odd list where peculiarity is shown.'''

        L = [1, 2, 3, 4, 5]
        a1.swap_k(L, 2)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(L, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
