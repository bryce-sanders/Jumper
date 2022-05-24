class Jumper:
  """
  The person with the parachute.

  The responsibility of the Jumper is to visually keep track
  of how many time the user has made a wrong guess. The more
  wrong guesses the player has made, the less parachute the
  Jumper will display.

  Attributes:
    stage: The visual appearance of the Jumper.

  """
  def __init__(self):
    """
    Construct the object with necessary attributes.
    """
    self.__stage = ""

  def get_stage(self, wrong_guesses):
    """
    With the number of guesses that the player has gussed wrong,
    decide and return the correct stage of the jumper.
    """
    # Decide which stage is correct with the wrong_guesses
    # number provided.
    if wrong_guesses == 0:
      self.__stage = """
     _____
    /_____\\
    \     /
     \   /
       O
      /|\\
      / \\

"""
    elif wrong_guesses == 1:
      self.__stage = """
 
    /_____\\
    \     /
     \   /
       O
      /|\\
      / \\

"""

    elif wrong_guesses == 2:
      self.__stage = """

     _____
    \     /
     \   /
       O
      /|\\
      / \\

"""

    elif wrong_guesses == 3:
      self.__stage = """


    \     /
     \   /
       O
      /|\\
      / \\

"""

    elif wrong_guesses == 4:
      self.__stage = """



     \   /
       O
      /|\\
      / \\

"""

    elif wrong_guesses <= 5:
      self.__stage = """




       X
      /|\\
      / \\

"""
    # Return the stage of the Jumper.
    return self.__stage

  def show_jumper(self, guessed_wrong):
        """
        Displays the current state of the jumper.
        """
        # Pass the Jumper the number of incorrect guesses
        # the player has made and then print the current
        # state of the jumper.
        self.stage = self.get_stage(guessed_wrong)
        print(self.stage)
