# Import the necessary classes.
from secret_word import SecretWord
from jumper import Jumper

class Game:
    """
    The game that the player is currently playing.

    The responsibility of the Game is to have a SecretWord and
    a Jumper, to keep track of the letters that they player
    has guess, to keep track of the number of guesses that the
    player has gotten wrong, and whether or not the game is over.

    Attributes:
        secret_word: The SecretWord of this game.
        guessed_letters: The list of letters the player has
                         already guessed
        guessed_wrong: The number of letters the player has
                       guessed wrong.
        jumper: The Jumper of this game.
        game_over: A Boolean variable that tracks whether or
                   or not the game has ended.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        self.secret_word = SecretWord()
        self.guessed_letters = []
        self.guessed_wrong = 0
        self.jumper = Jumper()
        self.game_over = False

    def show_word(self):
        """
        Displays the current state of the secret word, with
        correctly guessed letters filled in.
        """

        # Keep track of how many letters are still left blank.
        letters_left = 0

        # Print each letter in the word that has already been
        # guessed. Leave letters that have yet to be guessed
        # as '_'.
        print("The word is...")
        for letter in self.secret_word.word:
            if letter in self.guessed_letters:
                print(letter, end =" ")
            else:
                print("_", end =" ")
                letters_left += 1
        
        # If there are no blank spaces left, the player
        # has won the game!
        if letters_left == 0:
            self.game_over = True
        

    def show_jumper(self):
        """
        Displays the current state of the jumper.
        """
        # Pass the Jumper the number of incorrect guesses
        # the player has made and then print the current
        # state of the jumper.
        jumper = self.jumper.get_stage(self.guessed_wrong)
        print(jumper)
