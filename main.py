from classes.match import Match
from classes.user import User
from classes.com import Com
from classes.interface import Interface
from classes.db import Database

interface = Interface()
match = Match()
user = User()
com = Com()
db = Database()

def reset():
  """Resets wins and rounds"""
  match.reset_rounds()
  user.reset_wins()
  com.reset_wins()

def print_default():
  """Prints the default play area"""
  interface.clear_screen()
  interface.print_banner()

def start_new_round():
  """Starts a new round and sets input"""
  match.new_round()
  interface.print_input_prompt()
  user.set_play()
  com.set_play()

def main():
  """Main game loop"""
  global match, user, com

  print_default()
  interface.print_initial_gap()
  start_new_round()
  print_default()
  done = False

  while (user.get_play() != 'X' and not done):
    match.set_result(user.get_play(), com.get_play())

    if match.get_result() == 'User':
      user.win()
    elif match.get_result() == 'Com':
      com.win()

    interface.print_play(match.get_round(), match.get_result(), user.get_play(), user.get_wins(), com.get_play(), com.get_wins())
    match.save_log(user.get_play(), com.get_play())

    if match.get_round() == 3 or user.get_wins() == 2 or com.get_wins() == 2:
      # Store match data in database
      db.store_match_data(match.get_log())
      
      interface.print_continue()
      done = True
    else:
      start_new_round()
      print_default()

  interface.clear_screen()
  interface.print_banner()
  interface.print_end(user.get_wins(), com.get_wins())
  reset()

interface.clear_screen()
interface.print_banner()
interface.print_initial_gap()

init_inputs = ['Y', 'N']
interface.print_init_input_prompt()
init_input = input().upper()

while init_input != 'N':
  while (init_input not in init_inputs):
    init_input = input().upper()
  
  if (init_input != 'N'):
    main()
    interface.print_init_input_prompt()
    init_input = input().upper()

interface.clear_screen()
interface.print_farewell()
interface.print_initial_gap()
interface.print_continue()