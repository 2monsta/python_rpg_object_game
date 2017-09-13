class Hero(object):
	def __init__(self, name = "incongnito"):
		self.name = name;
		self.health = 10;
		self.power = 5;
	def take_damage(self, damage):
		self.health -= damage;