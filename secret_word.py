# Import the necessary libraries.
import random

class SecretWord:
    """
    A secret word that the player has to guess.

    The responsibility of the SecretWord is to select and store the
    word that the player has to guess.

    Attributes:
        __word: The secret word. Cannot be accessed outside of
                this class.
        guessed_letters: The list of letters the player has
                         already guessed
        letters_left: Keeps track of how many letters are left blank in
                      the SecretWord.
        guessed_wrong: The number of letters the player has
                       guessed wrong.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        self.__word = self.get_word()
        self.guessed_letters = []
        self.letters_left = 0
        self.guessed_wrong = 0

    def get_word(self):
        """
        Selects and returns a random word from the list.
        """
        # Create the list of words that will be picked from.
        word_list = ["summer", "heat", "pool", "sunny", "relax"]

        # Select and return a random word from the list.
        return random.choice(word_list).upper()

    def show_word(self):
        """
        Displays the current state of the secret word, with
        correctly guessed letters filled in.
        """

        # Reset 'letters_left' attribute to 0 in order to get
        # a fresh count.
        self.letters_left = 0

        # Print each letter in the word that has already been
        # guessed. Leave letters that have yet to be guessed
        # as '_'.
        print("The word is...")
        for letter in self.__word:
            if letter in self.guessed_letters:
                print(letter, end =" ")
            else:
                print("_", end =" ")
                self.letters_left += 1

    def check_guess(self, guess):

        # Check if the player has already guessed the letter that
        # they entered.
        if guess.upper() in self.guessed_letters:

            print("\033[33m" + f"#=== You already guessed '{guess.upper()}' ===#" + "\033[39m")

        # Else...
        else:

            # If the letter the player guessed is not in the secret word, inform
            # the player and add to their 'guessed_wrong' count. Add
            # the guessed letter to the 'guessed_letters' list.
            if guess.upper() not in self.__word:
                    print("\033[31m" + f"'{guess.upper()}' is not in the word!" + "\033[39m")
                    self.guessed_wrong += 1
                    self.guessed_letters.append(guess.upper())
                
            # If the letter the player guessed is in the secret word,
            # inform the player. Add the guessed letter to the 
            # 'guessed_letters' list.
            else:
                print("\033[32m" + f"'{guess.upper()}' is in the word!" + "\033[39m")
                self.guessed_letters.append(guess.upper())
