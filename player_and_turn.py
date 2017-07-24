class Player:
	
	def __init__ (self, name, board):
		self.name = name
		self.board = board

	def get_name(self):
		
		return self.name	

	def get_board(self):
		
		return self.board

	def is_loser(self):
		'''
		checks if the player has lost
		to see if it should continue running
		by checking if all ships have been sunk?
		confused since this is kind of a one player game currently
		'''
		return self.board.count_active_ships() == 0


class Turn:	
	def __init__(self, board):
		self.player	= player
		self.board = board

	def get_target(self):
		'''
		player inputs coordinates
		then runs parse_coordinates?
		'''
		target = input('What tile would you like to attack:')
		return self.board.shot_fired(target)


	def run (self):
		'''
		uses the board class to run?
		sets up the turn by asking for the target
		'''
		result = None
		while result is None:
			result = self.get_target()


class Shot:
	def __init__(self, board)
		self.target = target
		self.valid = False
		



