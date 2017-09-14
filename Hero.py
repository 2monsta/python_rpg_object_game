class Hero(object):
	def __init__(self, name = "Tidus"):
		self.name = name;
		self.health = 20;
		self.power = 5;
		self.spell_power = 3;
		self.defense = 5;
		self.mana = 10;	
	def take_damage(self, damage):
		self.health -= damage;
	def cheer_for_hero(self):
		print("fight hard %s" %self.name);
	def is_alive(self):
		return self.health>0;
	def increase_gold(self):
		self.gold += 100;
	def spell_power_cost(self):
		self.mana -=2;