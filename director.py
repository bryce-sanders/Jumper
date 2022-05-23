from game import Game

class Director:

    def __init__(self):
        self.game = Game()

    def start_game(self):

        self.welcome_player()

        self.game.show_jumper()
        self.game.show_word()
        print("""
        """)

        while not self.game.game_over:

            self.make_guess()

            self.game.show_jumper()
            self.game.show_word()
            print("""
            """)
            if self.game.guessed_wrong >= 5:
                self.game.game_over = True

        self.game.show_jumper()
        self.game.show_word()
        print("""
        """)

        if self.game.guessed_wrong >= 5:
            print("\033[31m" + "You lost the game!" + "\033[39m")
            self.play_again()
        else:
            print("\033[32m" + "You won the game!" + "\033[39m")
            self.play_again()

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

            print("\033[31m" + "#=== You can only guess letters ===#" + "\033[39m")

        else:

            if guess.upper() in self.game.guessed_letters:

                print("\033[31m" + f"#=== You already guessed '{guess.upper()}' ===#" + "\033[39m")

            else:

                if guess.upper() not in self.game.secret_word.word:
                    print("\033[31m" + f"'{guess.upper()}' is not in the word!" + "\033[39m")
                    self.game.guessed_wrong += 1
                    self.game.guessed_letters.append(guess.upper())
                else:
                    print("\033[32m" + f"'{guess.upper()}' is in the word!" + "\033[39m")
                    self.game.guessed_letters.append(guess.upper())

    def play_again(self):
        choice = input("Would you like to play again? [y / n] ")

        if choice.upper() == "Y":
            self.game = Game()
            self.start_game()
        elif choice.upper() == "N":
            print("\033[33m" + """
Okay! Thanks for playing!
""" + "\033[39m")
            quit()
        else:
            print("\033[31m" + "#=== Invalid Response, Please Try Again ===#" + "\033[39m")
            self.play_again()
