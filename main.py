from classes.Match import Match
from classes.Player import Player
from classes.COM import COM

match = Match()
player = Player()
com = COM()

match_stop = False
match.start_match()

player_input = input().upper()

while player_input != 'X':
    try:
        match.clear_screen()
        match.print_start()
        player_play = player.get_play(player_input)
        com_play = com.get_play()

        result = match.get_result(player_play,com_play)

        if result:
            player.win()
        elif not result:
            com.win()
 
        match.new_round()
        match.print_user_input()
        player_input = input().upper()
    except Exception as error:
        print(error)   
        match.print_user_input()
        player_input = input().upper()

input()
