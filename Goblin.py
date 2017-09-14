#get the super (parent) class
from Character import Character
#make goblin a subclass of Character
class Goblin(Character):
	def __init__(self):
		super(Goblin, self).__init__("Goblin", 6, 2)