class Board():
	dict_of_ships = {}
	
		
	def __init__(self, ship):
		self.matrix = []
		self.ship = ship
		self.previous_shot = []
		self.size = size
		
	def generate_board(self):
		for item in range(10):
			item = []
			self.matrix.append(item)
			for value in range(self.matrix):
				self.matrix[item][value] = None
		print(self.matrix)

	def position_ship(self, ship, start, end):
		start = input("Where would you like the start point of the ship?")
		end = input("Where would you like the end of the ship")

		if start not in self.matrix:
			print("you may not place your ship there")
		if end not in self.matrix:
			print("you may not place your ship there")

		dict_of_ships[ship] = self.size, start, end



		
	
	def get_inactive_ships(self):
		if Ship.is_sunk(self.ship):
			return True
		else: 
			return False
	def shots_fired(self, coordinates):
		if coordinates not in self.previous_shot:
			return True
		else: 
			return False


	
	def parse_coordinates(self, coordinates):
		alphabetdict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
		letter_of_coord = coordinates[0]
		number_of_coord = coordinates[1:] 
		if letter_of_coord not in alphabetdict:
			print("false coordinates mate, you got the letter wrong")
		if number_of_coord > 10 or number_of_coord < 1:
			print("false coordinates mate, you got your numbers wrong")

		letter_to_number_coord = alphabetdict[letter_of_coord]
		new_coord = (letter_to_number_coord, int(number_of_coord))
		return new_coord









def main():
	Board.generate_board()

if __name__ == '__main__':
	main()