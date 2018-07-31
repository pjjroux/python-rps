from classes.player import Player

class User(Player):
  """The logic for the human player"""
  def __init__(self):
    super().__init__()
    self.plays = ['R', 'P', 'S', 'X']

  def __print_input_prompt(self):
    """Prompts the user for input"""
    print()
    print('R: Rock|P: Paper|S: Scissors|X: Exit')

  def set_play(self):
    """Gets input from user and sets the current play"""
    self.__print_input_prompt()
    play = input().upper()

    while (play not in self.plays):
        self.__print_input_prompt()
        play = input().upper()
    
    self.play = play
