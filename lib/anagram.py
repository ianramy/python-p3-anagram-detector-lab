# your code goes here!
class Anagram:
    def __init__(self, word):
        """
        Initializes the Anagram instance with a word.

        :param word: The word to find anagrams for.
        """
        self.word = word.lower()  # Store the word in lowercase for case-insensitive comparison

    def match(self, words):
        """
        Finds all anagrams of the initialized word from a list of words.

        :param words: A list of words to check for anagrams.
        :return: A list of words that are anagrams of the initialized word.
        """
        sorted_word = sorted(self.word)
        return [word for word in words if sorted(word.lower()) == sorted_word]
