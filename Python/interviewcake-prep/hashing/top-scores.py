"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    if len(unsorted_scores) == 0:
        return []

    min_arr = min(unsorted_scores)
    max_arr = max(unsorted_scores)
    res = list()
    ctr_dict = dict()
    for i in range(min_arr, max_arr+1):
        ctr_dict[i] = 0
    for i in unsorted_scores:
        ctr_dict[i] += 1

    for i in range(max_arr,min_arr-1,-1):
        if ctr_dict[i] > 0:
           for _ in range(ctr_dict[i]):
               res.append(i)

    return res


















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)