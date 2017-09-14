class Hero(object):
	def __init__(self, name = "Tidus"):
		self.name = name;
		self.health = 10;
		self.power = 5;
		self.defense = 5;
		self.regular_pot = 5;
		self.increase_attack = 5;
		self.increase_defense = 2;
		self.gold = 400;
	def take_damage(self, damage):
		self.health -= damage;
	def cheer_for_hero(self):
		print("fight hard %s" %self.name);
	def is_alive(self):
		return self.health>0;
	def heal(self):
		self.health +=self.regular_pot;
		self.gold -=100;
	def weapon(self):
		self.power += self.increase_attack;
		self.gold -=200;
	def armor(self):
		self.defense += self.increase_defense;
		self.gold -=200;
	def increase_gold(self):
		self.gold += 100;
	def mega_heal(self):
		self.health *= self.regular_pot;
		self.gold -= 300;