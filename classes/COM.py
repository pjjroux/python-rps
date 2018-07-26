from classes.Player import Player

import random

class COM(Player):
    """ AI player in the RPS game. COM have the following properties:
    
        score: An integer tracking number of games won
        played: A string representing the play made by the player (R = Rock, P = Paper, S = Scissor)
    """
    
    def get_play(self):
        """ Return a string containing R/P/S for the played property. """
        com_options = ('R', 'P', 'S')
        return random.choice(com_options)

