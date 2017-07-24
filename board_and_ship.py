class Board():
	dict_of_ships = {}
	
		
	def __init__(self):
		self.matrix = []
		self.ships = []
		self.previous_shots = set()
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
		start_coord = self.parse_coordinates(start)
		end_coord = self.parse_coordinates(end)
		
		
		dict_of_ships[ships] = self.size, start, end



	
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
		alphabetdict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
		letter_of_coord = coordinates[0]
		number_of_coord = coordinates[1:] 
		number_of_coord = int(number_of_coord) if number_of_coord.isdigit() else 0
		if letter_of_coord not in alphabetdict:
			print("false coordinates mate, you got the letter wrong")
		if number_of_coord > 10 or number_of_coord < 1:
			print("false coordinates mate, you got your numbers wrong")

		letter_to_number_coord = alphabetdict[letter_of_coord]
		return letter_to_number_coord, number_of_coord

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
		 # ships = [(5, "Aircraft carrier"),
   #                (4, "Battleship"),
   #                (3, "Submarine"),
   #                (3, "Cruiser"),
   #                (2, "Patrol boat")]
		return self.size

	def hit_taken(self):
		self.hitcount += 1








def main():
	Board.generate_board()

if __name__ == '__main__':
	main()