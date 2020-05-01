"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""

import unittest


def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_dict = dict()
    for movie_length in movie_lengths:
        if movie_dict.get(movie_length) is not None:
            movie_dict[movie_length] += 1
        else:
            movie_dict[movie_length] = 1

    for i in range(len(movie_lengths)):
        movie_dict[movie_lengths[i]] -= 1
        if i != 0:
            movie_dict[movie_lengths[i-1]] += 1
        print(movie_dict)
        print(flight_length-movie_lengths[i])
        if flight_length-movie_lengths[i] > 0 and movie_dict.get(flight_length-movie_lengths[i]) != 0:
            return True
    return False





# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)










# Solution
# def can_two_movies_fill_flight(movie_lengths, flight_length):
#     # Movie lengths we've seen so far
#     movie_lengths_seen = set()
#
#     for first_movie_length in movie_lengths:
#         matching_second_movie_length = flight_length - first_movie_length
#         if matching_second_movie_length in movie_lengths_seen:
#             return True
#         movie_lengths_seen.add(first_movie_length)
#
#     # We never found a match, so return False
#     return False

