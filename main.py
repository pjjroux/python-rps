from classes.Player import Player
from classes.COM import COM

player = Player()
com = COM()

try:
    player_play = player.get_play(input('Rock, paper or scissor? ').upper())
    com_play = com.get_play()

    rules = {
        ('P','R') : True,
        ('P','S') : False,
        ('R','P') : False,
        ('R','S') : True,
        ('S','P') : True,
        ('S','R') : False
    }

    if (player_play, com_play) in rules:
        if rules[(player_play,com_play)]:
            player.win()
            print('Player wins! Score: ' + str(player.score))
        else:
            com.win()
            print('COM wins! Score: ' + str(com.score))     
    else:
        print('DRAW!')
except Exception as error:
    print(error)
    
