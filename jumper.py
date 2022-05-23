class Jumper:

    def __init__(self):
        self.stage = ""

    def get_stage(self, wrong_guesses):

        if wrong_guesses == 0:
            self.stage = """
     _____
    /_____\\
    \     /
     \   /
       O
      /|\\
      / \\

"""
        elif wrong_guesses == 1:
            self.stage = """
 
    /_____\\
    \     /
     \   /
       O
      /|\\
      / \\

"""

        elif wrong_guesses == 2:
            self.stage = """

     _____
    \     /
     \   /
       O
      /|\\
      / \\

"""

        elif wrong_guesses == 3:
            self.stage = """


    \     /
     \   /
       O
      /|\\
      / \\

"""

        elif wrong_guesses == 4:
            self.stage = """



     \   /
       O
      /|\\
      / \\

"""

        elif wrong_guesses <= 5:
            self.stage = """




       X
      /|\\
      / \\

"""

        return self.stage