class Store(object):
	def __init__(self):
		self.weapon = 5;
		self.armor = 5;
	def increase_attack(self, power):
		power += self.weapon;
