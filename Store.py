class Store(object):
	def __init__(self):
		self.potion = 10;
		self.mega_potion = 20;
		self.weapon_attack =  5;
		self.weapon_defense= 2;
		self.cost = 100;
	def heal(self, hero):
		hero.health += self.potion;
		hero.gold -= self.cost;
	def mega_heal(self, hero):
		hero.health += self.mega_potion;
		hero.gold -= 200;
	def weapon(self, hero):
		hero.power += self.weapon_attack;
		hero.gold -= 200;
	def armor(self, hero):
		hero.defense += self.weapon_defense;
		hero.gold -= 200;