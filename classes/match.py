from os import name, system

class Match:
  """Class handling match logic"""
  def __init__(self):
    self.round = 0
    self.result = ''
    self.log = []

  def save_log(self, user_play, com_play):
    """Saves round to log"""
    tmp_log = {
      'Round': self.get_round(),
      'User': user_play,
      'Com': com_play,
      'Result': self.get_result()
    }

    self.log.append(tmp_log)

  def get_log(self):
    """Returns the match log"""
    return self.log

  def new_round(self):
    """Starts a new round"""
    self.round += 1

  def get_round(self):
    """Returns the current round number"""
    return self.round

  def set_round(self, round):
    """Set the round for a returning player"""
    self.round = int(round)

  def reset_rounds(self):
    """Reset the round counter and match log"""
    self.round = 0
    self.tmp_log = {}
    
  def set_result(self, user_play, com_play):
    """Determine outcome of play"""
    rules = {
      ('P','R') : 'User',
      ('P','S') : 'Com',
      ('R','P') : 'Com',
      ('R','S') : 'User',
      ('S','P') : 'User',
      ('S','R') : 'Com'
    }

    if (user_play, com_play) in rules:
      self.result = rules[(user_play, com_play)]
    else:
      self.result = 'Draw'

  def get_result(self):
    """Returns the result"""
    return self.result
