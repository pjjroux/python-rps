from classes.match import Match
from classes.user import User
from classes.com import Com

match = Match()
user = User()
com = Com()

def reset():
  """Resets wins and rounds"""
  match.reset_rounds()
  user.reset_wins()
  com.reset_wins()

def print_default():
  """Prints the default play area"""
  match.clear_sceen()
  match.print_banner()

def start_new_round():
  """Starts a new round and sets input"""
  match.new_round()
  match.print_input_prompt()
  user.set_play()
  com.set_play()

def main():
  """Main game loop"""
  global match, user, com

  print_default()
  match.print_initial_gap()
  start_new_round()
  print_default()
  done = False

  while (user.get_play() != 'X' and not done):
    match.set_result(user.get_play(), com.get_play())

    if match.get_result() == 'User':
      user.win()
    elif match.get_result() == 'Com':
      com.win()

    match.print_play(match.get_result(), user.get_play(), user.get_wins(), com.get_play(), com.get_wins())
    match.save_log(user.get_play(), com.get_play())

    if match.get_round() == 3 or user.get_wins() == 2 or com.get_wins() == 2:
      print('---------------------------------------------------------')
      print('[Enter] to continue')
      print('---------------------------------------------------------')
      input()
      done = True
    else:
      start_new_round()
      print_default()

  match.clear_sceen()
  match.print_banner()
  match.print_end(user.get_wins(), com.get_wins())
  reset()

def print_init_input_prompt():
  """Get the initial input"""
  print('---------------------------------------------------------')
  print('Start new game [Y/N]')
  print('---------------------------------------------------------')

match.clear_sceen()
match.print_banner()
match.print_initial_gap()

init_inputs = ['Y', 'N']
print_init_input_prompt()
init_input = input().upper()

while init_input != 'N':
  while (init_input not in init_inputs):
    init_input = input().upper()
  
  if (init_input != 'N'):
    main()
    print_init_input_prompt()
    init_input = input().upper()

match.clear_sceen()
match.print_farewell()
input('[Enter] to exit')