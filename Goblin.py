class Goblin(object):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6;
		self.power = 2;
	def take_damage(self, damage):
		self.health -= damage;
	def is_alive(self):
		return self.health > 0;
	def get_health(self):
		return self.health;
	def take_spell_damage(self, damage):
		self.health -= damage * 2;