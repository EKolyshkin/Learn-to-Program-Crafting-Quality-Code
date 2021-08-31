import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_1(self):
        '''Test a1.stock_price_summary with empty list.'''

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2(self):
        '''Test a1.stock_price_summary with single-item, threshold value list.'''

        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_3(self):
        '''Test a1.stock_price_summary with single-item, non-zero integer value list.'''

        actual = a1.stock_price_summary([3])
        expected = (3, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_4(self):
        '''Test a1.stock_price_summary with single-item, non-zero float value list.'''

        actual = a1.stock_price_summary([2.07])
        expected = (2.07, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_5(self):
        '''Test a1.stock_price_summary with multiple integer, negative start item list.'''

        actual = a1.stock_price_summary([-1, 5, 17])
        expected = (22, -1)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_6(self):
        '''Test a1.stock_price_summary with multiple float, negative start item list.'''

        actual = a1.stock_price_summary([-2.4, 1.3, -3.2])
        expected = (1.3, -5.6)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_7(self):
        '''Test a1.stock_price_summary with an even number of float and integer items.'''

        actual = a1.stock_price_summary([2, -0.5, 1.3, -3])
        expected = (3.3, -3.5)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
