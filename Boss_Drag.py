from Character import Character
class Boss_Drag(Character):
	def __init__(self):
		super(Boss_Drag, self).__init__("Spirit Dragon", 100, 10);
		self.sp_attack_power = 20;
	def sp_attack(self, hero):
		hero.health -= self.sp_attack_power;