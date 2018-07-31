class Player:
  """Class containing logic for any player"""
  def __init__(self):
    self.wins = 0
    self.play = ''

  def set_play(self):
    """Abstract method that sets the current play"""
    pass

  def get_play(self):
    """Returns the current play"""
    return self.play

  def win(self):
    """Increases the number of wins for aplayer"""
    self.wins += 1

  def get_wins(self):
    """Return the number of wins"""
    return self.wins

  def reset_wins(self):
    """Resets the win counter"""
    self.wins = 0
