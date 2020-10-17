from collections import Counter
import math

def import_dictionary(path_to_text):

    """Reads a .txt file and adds all the words in it to the dictionary.

    Args:
        path_to_text: The location of the txt file that contains valid words.

    Returns:
        The dictionary with new words added to it.
    """
    dictionary = []

    with open(path_to_text,'r') as file:
        for word in file.read().splitlines(): 
            dictionary.append(word)

    return dictionary

def get_shortest_word(licence_plates, dictionary):

	"""Finds the shortest word form a vocabulary that includes
		all the letters from a given licence plate.

    Args:
        licence_plates: A list of licence plates
        dictionary: The reference that will be used to form 
        	a vocabulary given the letters from a licence plate

    Returns:
        A list that contains the shortest words of all the licence plates
    """

	shortest_words_arr = []

	for licence in licence_plates:

		shortest_word = ""
		shortest_word_length = math.inf
		
		# Get the letters in licence
		licence_letters = [char for char in licence.lower() if char.isalpha()]

		# If there are no letters in licence
		if len(licence_letters) == 0:
			shortest_words_arr.append("")
			continue
		
		licence_hash = Counter(licence_letters)

		for word in dictionary:
			counter = 0 # Used to track whether the current word has all the letters in licence
			word_hash = Counter(word.lower())

			for key in licence_hash.keys():

				# If the number of occurence of a letter in licence is
				# greater than or equal to the number of occurence of a letter in word
				if word_hash.get(key, 0) >= licence_hash[key]:
					counter += 1

			# If all the letters in licence are in word AND 
			# if length of word == length of all letters in licence,
			# then the word is the shortest word, so break the loop
			# because there's no need to go through other words in dictionary
			if counter == len(licence_hash.keys()) and len(licence_letters) == len(word):
				shortest_word = word
				break

			# If the current word is shorter than the shortest_word_length
			if counter == len(licence_hash.keys()) and shortest_word_length > len(word):
				shortest_word_length = len(word)
				shortest_word = word

		# Append the shortest word that can be formed using the current licence plate
		shortest_words_arr.append(shortest_word)

	return shortest_words_arr
