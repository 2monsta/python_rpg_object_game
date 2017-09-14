from Main_Character import Main_Character
from Hero import Hero;
class Medic(Hero):
	def __init__(self, name ="Medic"):
		super(Medic,self).__init__(name);
	def heal(self):
		self.health += 10;
		self.mana -=4;
	def heal_other(self, health):
		health += 10;
		self.mana -=4;