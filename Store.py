class Store(object):
	def __init__(self):
		self.potion = 10;
		self.mega_potion = 20;
		self.weapon_attack =  5;
		self.weapon_defense= 2;
		self.cost = 100;
	def heal(self, hero):
		hero.health += self.potion;
		hero.gold -= self.cost;
	def mega_heal(self, hero):
		hero.health += self.mega_potion;
		hero.gold -= 200;
	def weapon(self, hero):
		hero.power += self.weapon_attack;
		hero.gold -= 200;
	def armor(self, hero):
		hero.defense += self.weapon_defense;
		hero.gold -= 200;

	def print_store_items(self):
		print("Choose an option")
		print("1. Heal (100gd)");
		print("2. Mega Heal (200gd)")
		print("3. Add Weapon (200gd)")
		print("4. Add Armor (200gd)")
		print("5. Nothing")
		print("6. Mana Potion");
		print("> ");
	def print_people_to_hire(self):
		print("1. Hire a Medic (300gd)");
		print("2. Hire a Buff Guy (400gd)");
		print("3. Hire a Ninja (500gd)");