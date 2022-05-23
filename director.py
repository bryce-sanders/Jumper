from game import Game

class Director:

    def __init__(self):
        self.game = Game()

    def start_game(self):

        self.welcome_player()

        while self.game.guessed_wrong < 5:

            self.game.show_jumper()
            self.game.show_word()
            print("""
            """)
            self.make_guess()

    def welcome_player(self):
    # Welcome the player!
        print("\033[33m" + """
Welcome to Jumer! You must guess the letters of the secret word!
Don't get too many guesses wrong, or the jumper will run out of parachute!
""" + "\033[39m")

    def make_guess(self):

        alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        guess = input("Guess a letter [a - z]: ")

        if guess.upper() not in alphabet:

            print("You can only guess letters")

        else:

            if guess.upper() in self.game.guessed_letters:

                print(f"You already guessed '{guess.upper}'")

            else:

                pass