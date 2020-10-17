"""Tests for GetAhead+ Week 6, Car Plates Vocabulary"""

import unittest
from week6 import get_shortest_word

class CarPlatesVocabularyTest(unittest.TestCase):
	def test_example_1(self):

		licence_plates = ["RA 12345", "CE 678D9", "OT 9S10S"]
		dictionary = ["A", "ARC", "CAR", "CODE", "SORTING", "SORTER", "SORTS"]

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, ["ARC", "CODE", "SORTS"])


	def test_example_2(self):

		licence_plates = ["WR 98765", "TE 67890", "TR E1236"]
		dictionary = ["EAT", "EEL", "TOW", "TOWER", "WHERE"]

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, ["TOWER", "EAT", "TOWER"])

	def test_no_licences_in_licence_plates_arr_returns_empty_array(self):

		licence_plates = []
		dictionary = ["EAT", "EEL", "TOW", "TOWER", "WHERE"]

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, [])

	def test_licence_contains_only_numbers_returns_arr_with_empty_strings(self):
		
		licence_plates = ["45 12345", "RT 34534", "12 96103"]
		dictionary = ["A", "ARC", "CAR", "CODE", "SORTING", "SORTER", "SORTS"]

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, ["", "SORTS", ""])

	def test_dictionary_is_empty_returns_arr_with_empty_strings(self):

		licence_plates = ["RA 12345", "CE 678D9", "OT 9S10S"]
		dictionary = []

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, ["", "", ""])

	def test_no_words_can_be_formed_returns_arr_with_empty_string(self):

		licence_plates = ["ZA KJ239", "XY 345LF", "QX LKJ78"]
		dictionary = ["EAT", "EEL", "TOW", "TOWER", "WHERE"]

		shortest_words = get_shortest_word(licence_plates, dictionary)

		self.assertEqual(shortest_words, ["", "", ""])

if __name__ == '__main__':
	unittest.main()