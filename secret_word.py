import random

class SecretWord:

    def __init__(self):
        self.word = self.get_word()

    def get_word(self):
        word_list = ["summer", "heat", "pool", "sunny", "relax"]
        self.word =  random.choice(word_list)
        return self.word.upper()
