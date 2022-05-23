import random

class SecretWord:

    def __init__(self):
        self.word = ""

    def pick_word(self):
        word_list = ["summer", "heat", "pool", "sunny", "relax"]
        self.word =  random.choice(word_list)

    def get_word(self):
        return self.word