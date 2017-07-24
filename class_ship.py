class Ship:
	
	def __init__(self,hitcount,length,name):
		self.hitcount = []
		self.display_name = display_name
        self.length = length
        self.name = name




	def is_sunk(self, hitcount):
		if self.hitcount == 0:
			return True
		else:
			return False 



	def sunk_message(self, display_name):
		return "your ship, {} has sunk".format(display_name)


	def get_size(self, length, display_name):
		 ships = [(5, "Aircraft carrier"),
                  (4, "Battleship"),
                  (3, "Submarine"),
                  (3, "Cruiser"),
                  (2, "Patrol boat")]
        return ships






