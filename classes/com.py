from classes.player import Player
from random import choice

class Com(Player):
  """The logic for the computer player"""
  def __init__(self):
    super().__init__()
    self.wins = 0
    self.plays = ['R', 'P', 'S']

  def set_play(self):
    """Randomly sets the computers current play"""
    self.play = choice(self.plays)
