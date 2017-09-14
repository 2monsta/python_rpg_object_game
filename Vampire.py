class Vampire(object):
	def __init__(self):
		self.name = "Vampire"
		self.health = 15;
		self.power = 3;
	def take_damage(self, damage):
		self.health -= damage;
	def get_health(self):
		return self.health;
	def is_alive(self):
		return self.health>0;
	def take_spell_damage(self, damage):
		self.health = self.health - (damage * 2);