import requests

class ApiClient:
  """Handles all API-calls to insert/select data"""
  def __init__(self):
    self.match_key = None

  def set_match_key(self):
    """Sets the match key for the current IP and retrieves the round number if one exists"""
    req = requests.get(url = 'https://qkok.co.za/rps/auth.php')
    response = req.json()
    self.match_key = response['match_key']
    self.round = response['round']

  def get_match_key(self):
    """Returns the match key for the current IP"""
    return self.match_key

  def get_round(self):
    """Returns the round number for the current IP"""
    return self.round

  def save_round(self, round_number, user_play, com_play, winner):
    """Saves the current round to the online DB"""
    params = {
      'match_key': self.match_key,
      'round_number': round_number,
      'user_play': user_play,
      'com_play': com_play,
      'winner': winner
    }

    req = requests.post(url = 'https://qkok.co.za/rps/insert_round.php', data = params)
    response = req.json()
    return response['return_status']
