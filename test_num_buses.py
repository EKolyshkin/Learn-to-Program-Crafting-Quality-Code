import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_1(self):
        '''Test a1.num_buses with minimum acceptable value.'''

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_2(self):
        '''Test a1.num_buses with minimum non-zero value.'''

        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_3(self):
        '''Test a1.num_buses with threshold value.'''

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_4(self):
        '''Test a1.num_buses with above threshold value.'''

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_5(self):
        '''Test a1.num_buses with minimum plural output value.'''

        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
