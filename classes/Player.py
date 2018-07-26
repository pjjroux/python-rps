class Player(object):
    """ A player in the RPS game. Players have the following properties:
    
        score: An integer tracking number of games won
        played: A string representing the play made by the player (R = Rock, P = Paper, S = Scissor)
    """

    
    def __init__(self):
        """ Return a Player object with a score of 0 and no play. """
        self.score = 0
        self.played = ''

        
    def get_play(self, player_input):
        """ Return a string containing R/P/S for the played property. """
        try:
            player_options = {
                'ROCK': 'R',
                'R': 'R',
                'PAPER': 'P',
                'P': 'P',
                'SCISSOR': 'S',
                'S': 'S',
            }
            return player_options[player_input]
        except KeyError:
            print("Player: Invalid player input")


    def win(self):
        """ Add 1 to the score property representing a win for the Player """
        self.score += 1


