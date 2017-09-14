from Character import Character
class Gold_Monster(Character):
	def __init__(self):
		super(Gold_Monster, self).__init__("Gold_Monster", 50, 2);
		self.gold = 300;
