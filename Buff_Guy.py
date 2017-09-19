from Character import Character;
class Buff_Guy(Character):
	def __init__(self):
		super(Buff_Guy, self).__init__("Buff_Guy", 0, 50);
	#when the user chooses, buff guy does 50 damage to the monster
	def power_hit(self, monster):
		monster.health -= self.power;
