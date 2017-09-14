#this is our super parent class
class Character(object):
	def __init__(self, name, health, power):
		self.name = name;
		self.health = health;
		self.power = power;
	def take_damage(self, damage):
		self.health -= damage;
	def get_health(self):
		return self.health;
	def is_alive(self):
		return self.health>0;
	def take_spell_damage(self, damage):
		self.health -= damage * 2;