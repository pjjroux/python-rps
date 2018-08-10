import requests

class ApiClient:
  """Handles all API-calls to insert/select data"""
  def __init__(self):
    self.match_key = None

  def set_match_key(self):
    req = requests.get(url = 'https://qkok.co.za/rps/auth.php')
    response = req.json()
    self.match_key = response['match_key']

  def get_match_key(self):
    return self.match_key

  def save_round(self, round_number, user_play, com_play, winner):
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