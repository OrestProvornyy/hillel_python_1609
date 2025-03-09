
import unittest


# def sum_2_numbers(a, b):
#     return a + b
#
#
class MyTest(unittest.TestCase):

    def test_compare_2_lists_with_dicts(self):
        expected_list = [
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'QA1'
            },
            {
                'Name': 'Den',
                'Age': 26,
                'Position': 'QA'
            },
        ]

        actual_list = [
            {
                'Name': 'Ivan',
                'Age': 25,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'AQA'
            },
            {
                'Name': 'Den',
                'Age': 30,
                'Position': 'QA'
            },
        ]
        assert self.assertEqual(actual_list, expected_list)
#     self.assertNotEqual(actual_list, expected_list)
#
#
# def test_almost_equal(self):
#     self.assertAlmostEqual(5, 7, delta=3)  # 7 between 5-3 and 5+3
#

if __name__ == '__main__':
    unittest.main()
