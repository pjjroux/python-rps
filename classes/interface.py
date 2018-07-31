from os import name, system

class Interface:
  """Handles all interface printing"""
  def __init__(self):
    pass

  def clear_screen(self):
    """Clears the screen"""
    if name == 'nt':   # Windows
      system('cls')
    else:             # MacOS/Linux
      system('clear')

  def print_continue(self):
    """Prints the continue screen to wait for input"""
    print('---------------------------------------------------------')
    print('[Enter] to continue')
    print('---------------------------------------------------------')
    input()

  def print_init_input_prompt(self):
    """Get the initial input"""
    print('---------------------------------------------------------')
    print('Start new game [Y/N]')
    print('---------------------------------------------------------')

  def print_farewell(self):
    """Print farewell message"""
    print('---------------------------------------------------------')
    print('                  Thanks for playing!')
    print('---------------------------------------------------------')

  def print_banner(self):
    """Print the game banner"""
    print('---------------------------------------------------------')
    print('  Welcome to Super Ultimate Battle Rock Paper Scissors!')
    print('---------------------------------------------------------')

  def print_initial_gap(self):
    """Print blank space when no ASCII art is present"""
    for i in range(12):
      print()
    
  def print_input_prompt(self):
    """Prints the prompt for user input"""
    print('---------------------------------------------------------')
    print('R: Rock|P: Paper|S: Scissors|X: Exit')
    print('---------------------------------------------------------')

  def print_play(self, round, result, user_play, user_wins, com_play, com_wins):
    """Prints ASCII art for the play"""
    """Print ASCII art"""
    print('                        ROUND #%d' % round)
    print()
    print('          USER                           COMPUTER')
    self.__print_content(user_play + com_play + '.txt')
    print()
    print('          WINS: %d                        WINS: %d' % (user_wins, com_wins))
    print()

  def __print_content(self, file_name):
    """Prints the content of a file"""
    file = open('resources/' + file_name, 'r')
    art = file.readlines()

    for line in art:
      print(line.rstrip('\n'))

  def print_end(self, user_wins, com_wins):
    """Print winner and farewell message"""
    if (user_wins > com_wins):
      self.__print_content('PLAYER_WINS.txt')
    elif (user_wins < com_wins):
      self.__print_content('COM_WINS.txt')
    else:
      self.__print_content('DRAW.txt')