class Vampire(object):
	def __init__(self):
		self.name = "Vampire"
		self.health = 15;
		self.power = 4;
	def take_damage(self, damage):
		self.health -= damage;
	def get_health(self):
		return self.health;
	def is_alive(self):
		return self.health>0;