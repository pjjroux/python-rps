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

  def clear_sceen(self):
    """Clears the screen"""
    if name == 'nt':  # Windows
      system('cls')
    else:             # Linux/MacOS
      system('clear')

  def print_initial_gap(self):
    """Print blank space when no ASCII art is present"""
    for i in range(12):
      print()

  def __print_content(self, file_name):
    """Prints the content of a file"""
    file = open('resources/' + file_name, 'r')
    art = file.readlines()

    for line in art:
      print(line.rstrip('\n'))

  def print_input_prompt(self):
    """Prints the prompt for user input"""
    print('---------------------------------------------------------')
    print('R: Rock|P: Paper|S: Scissors|X: Exit')
    print('---------------------------------------------------------')

  def get_round(self):
    """Returns the current round number"""
    return self.round

  def reset_rounds(self):
    """Reset the round counter"""
    self.round = 0

  def print_banner(self):
    """Print the game banner"""
    print('---------------------------------------------------------')
    print('  Welcome to Super Ultimate Battle Rock Paper Scissors!')
    print('---------------------------------------------------------')

  def print_play(self, result, user_play, user_wins, com_play, com_wins):
    """Prints ASCII art for the play"""
    """Print ASCII art"""
    print('                        ROUND #%d' % self.round)
    print()
    print('          USER                           COMPUTER')
    self.__print_content(user_play + com_play + '.txt')
    print()
    print('          WINS: %d                        WINS: %d' % (user_wins, com_wins))
    print()

  def print_end(self, user_wins, com_wins):
    """Print winner and farewell message"""
    if (user_wins > com_wins):
      self.__print_content('PLAYER_WINS.txt')
    elif (user_wins < com_wins):
      self.__print_content('COM_WINS.txt')
    else:
      self.__print_content('DRAW.txt')

  def print_farewell(self):
    """Print farewell message"""
    print()
    print('---------------------------------------------------------')
    print('                  Thanks for playing!')
    print('---------------------------------------------------------')

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
