from classes.player import Player

class User(Player):
  """The logic for the human player"""
  def __init__(self):
    super().__init__()
    self.plays = ['R', 'P', 'S', 'X']

  def set_play(self):
    """Gets input from user and sets the current play"""
    play = input().upper()

    while (play not in self.plays):
        play = input().upper()
    
    self.play = play
