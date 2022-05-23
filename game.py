from secret_word import SecretWord
from jumper import Jumper

class Game:

    def __init__(self):
        self.secret_word = SecretWord()
        self.guessed_letters = []
        self.guessed_wrong = 0
        self.jumper = Jumper()

    def show_word(self):

        # Print each letter in the word that has already been
        # guessed. Leave letters that have yet to be guessed
        # as '_'.
        print("The word is...")
        for letter in self.secret_word.word:
            if letter in self.guessed_letters:
                print(letter, end =" ")
            else:
                print("_", end =" ")

    def show_jumper(self):
        jumper = self.jumper.get_stage(self.guessed_wrong)
        print(jumper)
