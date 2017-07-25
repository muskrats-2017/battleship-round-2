class Board():
		
	def __init__(self):
		self.matrix = self.generate_board()
		self.ships = []
		self.previous_shots = set()
		
	def generate_board(self):
		matrix = []
		for item in range(10):
			matrix.append([])
			for value in range(10):
				matrix[item].append(None)
		return matrix

	def position_ship(self, ship):
		'''
		Given coords, will the ship even fit there

		'''
		
		start = input("Where would you like the start point of the ship?").strip()
		end = input("Where would you like the end of the ship?").strip()
		start_coord = self.parse_coordinates(start)
		end_coord = self.parse_coordinates(end)
		
		if start_coord[0] == end_coord[0]:
			if start_coord[1] > end_coord[1]:
				start_coord, end_coord = end_coord, start_coord
			if ship.get_size() == (abs(start_coord[1] - end_coord[1]) +1):
				
				sequence = ( (start_coord[0], row) for row in range(start_coord[1], end_coord[1]+1) )
				if self.ship_position_check(ship, sequence):
					return True
		elif start_coord[1] == end_coord[1]:
			if start_coord[0] > end_coord[0]:
				start_coord, end_coord = end_coord, start_coord

			if ship.get_size() == (abs(start_coord[0] - end_coord[0]) +1):
				
				sequence = ( (col, start_coord[1]) for col in range(start_coord[0], end_coord[0]+1) )
				if self.ship_position_check(ship, sequence):
					return True

		print(start_coord)
		print(end_coord)
		return False

		
	
	def	ship_position_check(self, ship, sequence):
		#takes ship, start, and end and returns true or false
		#position_ship(ship)
		valid_coordinates = []
		for col, row in sequence:
			if self.matrix[row][col] is not None:
				return False
			else:
				valid_coordinates.append((col, row))

		for col, row in valid_coordinates:
			self.matrix[row][col] = ship

		self.ships.append(ship)

		return True

	
	def count_active_ships(self):
		counter = 0
		for ship in self.ships:
			if not ship.is_sunk():
				counter += 1

		return counter

		
			
	




	def shots_fired(self, coordinates):
		coordinates = self.parse_coordinates(coordinates)
		if coordinates not in self.previous_shot:
			return True
		else: 
			return False


	
	def parse_coordinates(self, coordinates):
		alphabetdict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
		letter_of_coord = coordinates[0]
		number_of_coord = coordinates[1:] 
		number_of_coord = int(number_of_coord) if number_of_coord.isdigit() else 0
		if letter_of_coord not in alphabetdict:
			print("false coordinates mate, you got the letter wrong")
		if number_of_coord > 10 or number_of_coord < 1:
			print("false coordinates mate, you got your numbers wrong")

		letter_to_number_coord = alphabetdict[letter_of_coord]
		return letter_to_number_coord, number_of_coord - 1

class Ship:
	
	def __init__(self, size, display_name):
		self.hitcount = 0
		self.display_name = display_name
		self.size = size
		




	def is_sunk(self):
		if self.hitcount == self.size:
			return True
		else:
			return False 



	def sunk_message(self):
		return "your ship, {} has sunk".format(self.display_name)


	def get_size(self):
		return self.size

	def hit_taken(self):
		self.hitcount += 1








def main():
	board = Board()
	board.generate_board()

if __name__ == '__main__':
	main()