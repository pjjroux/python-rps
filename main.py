from classes.match import Match
from classes.user import User
from classes.com import Com

match = Match()
user = User()
com = Com()

def print_default():
  """Prints the default play area"""
  match.clear_sceen()
  match.print_banner()

def start_new_round():
  """Starts a new round and sets input"""
  match.new_round()
  user.set_play()
  com.set_play()

def main():
  """Main game loop"""
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

    if match.get_round() == 3 or user.get_wins() == 2 or com.get_wins() == 2:
      input('[Enter] to continue')
      done = True
    else:
      start_new_round()
      print_default()

  match.clear_sceen()
  match.print_end(user.get_wins(), com.get_wins())

main()
input('[Enter] to quit')
