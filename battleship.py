class Player:
	
	def __init__ (self, board):
		self.player = None
		self.board = None

	def get_name(self):
		'''
		help set up the game
		'''

		name = input('Hello player, welcome to Battleship! What is your name:').strip()
			print("Let's begin!")
		
		self.player = Player(name)
		
		self.board = Board(self.player)	

	def get_board(self):
		'''
		get player's board from the board class
		'''

	def is_loser(self):
		'''
		checks if the player has lost
		to see if it should continue running
		by checking if all ships have been sunk?
		confused since this is kind of a one player game currently
		'''


class Turn:	
	def __init__(self, board):
		self.player	= player
		self.board = board

	def get_target(self):
		'''
		player inputs coordinates
		then runs parse_coordinates?
		'''
		input('What tile would you like to attack:')
		self.board.parse_coordinates()


	def run (self):
		'''
		uses the board class to run?
		sets up the turn by asking for the target
		'''
		while self.player.is_loser() is False:
			self.get_target()
