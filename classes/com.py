from classes.player import Player
from classes.api_client import ApiClient
from random import choice
import requests

class Com(Player):
  """The logic for the computer player"""
  def __init__(self):
    super().__init__()
    self.wins = 0
    self.plays = ['R', 'P', 'S']

  def set_play(self):
    """Randomly sets the computers current play"""
    self.play = choice(self.plays)

  def set_play_advanced(self, match_key):
    """Decide play by using user plays from historic data"""
    req = requests.get(url = f'https://qkok.co.za/rps/get_rounds.php?match_key={match_key}')
    response = req.json()
    if response['return_status']:
      rounds_played = response['count']
    else:
      rounds_played = 0

    # If the user has less than 10 rounds played use random choice
    if int(rounds_played) <= 10:
      self.set_play()
    else:
      req = requests.get(url = f'https://qkok.co.za/rps/get_plays.php?player=U&match_key={match_key}')
      response = req.json()
      if response['return_status']:
        plays = ''
        for play in response['plays']:
          plays += play['play']
         
        # Find pattern for last three moves excluding the last three moves recorded
        pattern = plays[-3:]
        pattern_index = plays.rfind(pattern, 0, len(plays) - 3)

        if pattern_index != -1:
          # Player is most likely to play the move previously played directly after the last three moves pattern
          # Set play as the choice that beats the user's play
          most_likely_play = plays[pattern_index+1]
          if most_likely_play == 'R':
            self.play = 'P'
          elif most_likely_play == 'P':
            self.play = 'S'
          elif most_likely_play == 'S':
            self.play = 'R'
        else:
          self.set_play()
      else:
        self.set_play()