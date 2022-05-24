# Import the necessary classes.
from game import Game

class Director:
    """
    The Director that will help you play Jumper.

    The responsibility of the Director is to facilitate the game
    of Jumper. The class has all of the member functions necessary
    to run the game.

    Attributes:
        game: The Game that the Director has and will facilitate.

    """
    def __init__(self):
        """
        Construct the object with necessary attributes.
        """
        self.__game = Game()

    def start_game(self):
        """
        Starts the gameplay loop. If the player wins or loses and would
        like to play again, the player will start the loop over with a
        new game.
        """
        # Welcome the player!
        print("\033[33m" + """
Welcome to Jumer! You must guess the letters of the secret word!
Don't get too many guesses wrong, or the jumper will run out of parachute!
""" + "\033[39m")

        # Print the initial Jumper and show how many letters are
        # in the secret word.
        self.__game.show_jumper()
        self.__game.show_word()
        print("""
        """)

        # Begin the gameplay loop. While the player has not completed
        # the word or guessed wrong too many times, continue this loop.
        while not self.__game.game_over:

            # Prompt the player to make a guess.
            self.make_guess()

            # Display the current state of the secret word and the jumper.
            self.__game.show_jumper()
            self.__game.show_word()
            print("""
            """)

            # Check if the player is out of guesses.
            if self.__game.guessed_wrong >= 5:
                self.__game.game_over = True



        # If the player has lost, inform them and ask if they would like to
        # play again.
        if self.__game.guessed_wrong >= 5:
            print("\033[31m" + "You lost the game!" + "\033[39m")
            self.play_again()

        # If the player has won, congratulate them and ask if they would like
        # to play again.
        else:
            print("\033[32m" + "You won the game!" + "\033[39m")
            self.play_again()

    def make_guess(self):
        """
        Prompt the user to make a guess. If they don't guess a valid letter,
        inform the player and prompt them again.
        """
        # Create a list to keep track of each letter in the alphabet.
        alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        # Prompt the player to guess a letter.
        guess = input("Guess a letter [a - z]: ")

        # Check if the guess the player entered is valid. If not, prompt
        # them again.
        if guess.upper() not in alphabet:

            print("\033[31m" + "#=== You can only guess single letters ===#" + "\033[39m")

        else:

            # Check if the player has already guessed the letter that they entered.
            if guess.upper() in self.__game.guessed_letters:

                print("\033[31m" + f"#=== You already guessed '{guess.upper()}' ===#" + "\033[39m")

            else:

                # If the letter the player guessed is not in the secret word, inform
                # the player and add to their 'guessed_wrong' count. Add the guessed
                # letter to the 'guessed_letters' list.
                if guess.upper() not in self.__game.secret_word._word:
                    print("\033[31m" + f"'{guess.upper()}' is not in the word!" + "\033[39m")
                    self.__game.guessed_wrong += 1
                    self.__game.guessed_letters.append(guess.upper())
                
                # If the letter the player guessed is in the secret word, inform
                # the player. Add the guessed letter to the 'guessed_letters' list.
                else:
                    print("\033[32m" + f"'{guess.upper()}' is in the word!" + "\033[39m")
                    self.__game.guessed_letters.append(guess.upper())

    def play_again(self):
        """
        Asks the player if they want to start a new game.
        """
        # Prompt the user for an answer.
        choice = input("Would you like to play again? [y / n] ")

        # If the user enters 'Y', refresh the director's 'game' atribute
        # and start the gameplay loop over.
        if choice.upper() == "Y":
            self.__game = Game()
            self.start_game()
        
        # If the user enters 'N', thank the user for playing and
        # end the program.
        elif choice.upper() == "N":
            print("\033[33m" + """
Okay! Thanks for playing!
""" + "\033[39m")
            quit()

        # If the user enters an invalid response, inform them, and prompt
        # them for a new answer.
        else:
            print("\033[31m" + "#=== Invalid Response, Please Try Again ===#" + "\033[39m")
            self.play_again()
