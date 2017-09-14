from Main_Character import Main_Character
class Hero(Main_Character):
	def __init__(self, name = "Tidus"):
		super(Hero, self).__init__(name);
		self.gold = 400;
	def cheer_for_hero(self):
		print("fight hard %s" %self.name);
	def increase_gold(self, amount):
		self.gold += amount;
	def decrease_gold(self, amount):
		self.gold -= amount;