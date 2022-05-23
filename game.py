from secret_word import SecretWord

class Game:

    def __init__(self):
        self.secret_word = SecretWord()

game = Game()

print(f"The Word is : {game.secret_word}")