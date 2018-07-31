from classes.player import Player

class User(Player):
  """The logic for the human player"""
  def __init__(self):
    super().__init__()
    self.plays = ['R', 'P', 'S', 'X']

  def __get_input(self):
    """Prompts the user for input"""
    return input('R: Rock|P: Paper|S: Scissors|X: Exit\n').upper()

  def set_play(self):
    """Gets input from user and sets the current play"""
    play = self.__get_input()

    while (play not in self.plays):
        play = self.__get_input()
    
    self.play = play
