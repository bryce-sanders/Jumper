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
    self.stage = ""

  def get_stage(self, wrong_guesses):
    """
    With the number of guesses that the player has gussed wrong,
    decide and return the correct stage of the jumper.
    """
    # Decide which stage is correct with the wrong_guesses
    # number provided.
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
    # Return the stage of the Jumper.
    return self.stage