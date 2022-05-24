# Import the necessary libraries.
import random

class SecretWord:
    """
    A secret word that the player has to guess.

    The responsibility of the SecretWord is to select and store the
    word that the player has to guess.

    Attributes:
        word: The secret word.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        self._word = self.get_word()

    def get_word(self):
        """
        Selects and returns a random word from the list.
        """
        # Create the list of words that will be picked from.
        word_list = ["summer", "heat", "pool", "sunny", "relax"]

        # Select and return a random word from the list.
        return random.choice(word_list).upper()
