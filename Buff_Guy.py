from Character import Character
from Main_Character import Main_Character
from Hero import Hero
class Buff_Guy(Hero):
	def __init__(self, name = "Buff Guy"):
		super(Buff_Guy, self).__init__(name);
		self.power = 7;
	#when the user chooses, buff guy does 50 damage to the monster
	def power_hit(self, monster):
		monster.health -= self.power * 2;
