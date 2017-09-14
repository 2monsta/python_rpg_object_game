class Main_Character(object):
	def __init__(self, name = "Cloud"):
		self.name = name;
		self.health = 20;
		self.power = 5;
		self.spell_power = 3;
		self.defense = 5;
		self.mana = 10;	
	def take_damage(self, damage):
		self.health -= damage;
	def is_alive(self):
		return self.health>0;
	def spell_power_cost(self):
		self.mana -=2;
	def take_spell_damage(self, damage):
		self.health -= damage * 2;