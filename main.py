from classes.Match import Match
from classes.Player import Player
from classes.COM import COM

match = Match()
player = Player()
com = COM()

try:
    match_stop = False
    match.start_match()

    player_input = input().upper()

    player_play = player.get_play(player_input)
    com_play = com.get_play()

    result = match.get_result(player_play,com_play)

    if result:
        player.win()
    elif not result:
        com.win()
    
    input()
except Exception as error:
    print(error)   
