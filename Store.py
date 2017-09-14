class Store(object):
	def __init__(self):
		self.potion = 10;
		self.mega_potion = 20;
		self.weapon_attack =  5;
		self.weapon_defense= 2;
	def heal(self, health):
		health += self.potion;
	def mega_heal(self, health):
		health += self.mega_potion;
	def weapon(self, power):
		power += self.weapon_attack;
	def armor(self, defense):
		defense += self.weapon_defense;