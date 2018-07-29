class Match(object):
	""" Represents the Match played over three rounds and controls input and output.

		round_count: And integer tracking round number
		match_result: A string representing the match winner (Player/COM)
	"""
	
	def __init__(self):
		""" Return a Match object with a round_count of 0 """
		self.round_count = 0

	def print_initial_gap(self):
		"""Print blank space when no ASCII art is present"""
		for i in range(11):
			print()

		print('---------------------------------------------------------')

	def start_match(self):
		""" Print welcome message and start first round """
		self.clear_screen()
		self.print_start()
		self.print_initial_gap()
		self.new_round()
		self.print_user_input()

	def new_round(self):
		self.round_count += 1

	def get_result(self, player_play, com_play):
		""" Determine outcome of play and return:

		True = Player wins
		False = COM wins
		-1    = Draw
		"""

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
				outcome = 'Player'
			else:
				outcome = 'COM'

			result = rules[(player_play,com_play)]
		else:
			outcome = 'DRAW'
			result = -1

		self.print_play(outcome, player_play, com_play)
		return result

	def print_user_input(self):
		print()
		print('Round:')
		print()
		print('R: Rock | P: Paper | S: Scissors | X: Exit')


	def print_start(self):
		print('---------------------------------------------------------')
		print('  Welcome to Super Ultimate Battle Rock Paper Scissors!')
		print('---------------------------------------------------------')

	def print_play(self, outcome, player_play, com_play):
		print()
		self.print_art(player_play, com_play)
		print()
		print('Winner: ' + outcome)
		print()
		print('---------------------------------------------------------')
	
	def print_art(self, player_play, com_play):
		print('          PLAYER                         COMPUTER')

		file_name = player_play + com_play + '.txt'
		file = open('resources/' + file_name, 'r')
		art = file.readlines()

		for line in art:
			print(line.rstrip('\n'))
	
	def clear_screen(self):
		import os

		if (os.name == 'nt'):
			os.system('cls')
		else:
			os.system('clear')