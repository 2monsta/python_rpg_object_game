import os
from Hero import Hero
from random import randint
from Store import Store;
from Medic import Medic;

from Goblin import Goblin
from Vampire import Vampire
# instantiate a hero object from the Hero Class
hero = Hero();
store = Store();
medic = Medic();
monsters = []
heros = []
heros.append(hero);
longstring = """

			   
 \ \    / /__| |__ ___ _ __  ___  | _ \ |__ _ _  _ ___ _ _ 
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ / _` | || / -_) '_|
   \_/\_/\___|_\__\___/_|_|_\___| |_| |_\__,_|\_, \___|_|  
											  |__/              
			
"""
print(longstring);
#before the game start, lets ask the hero for his her name.
print "what is thy name, brave adventurer";
hero_name = raw_input("> ");
hero.name = hero_name;
hero.cheer_for_hero();

#generate number of monster to put in the list of monsters
print("how many monster are you willing to fight, brave %s" %hero.name);
number_of_enemies = int(raw_input("> "));
for i in range(0, number_of_enemies):
	rand_num = randint(0, 1);
	if(rand_num == 1):
		monsters.append(Goblin());
	else:
		monsters.append(Vampire());


#a chance to stop before entering battle
print("Do you want to shop before going into battle? (Y or N) ");
is_battle = raw_input("> ");
if(is_battle == "Y"):
	print "What do you want to do?"
	print "1. store";
	print "2. do nothing"
	user_inp = raw_input("> ");
	if(user_inp == "1"):
		print("You have %d gold" % hero.gold);
		print("Choose an option")
		print("1. Heal (100gd)");
		print("2. Mega Heal (200gd)")
		print("3. Add Weapon (200gd)")
		print("4. Add Armor (200gd)")
		print("> ");
		us_input = raw_input();
		if(us_input == "1"):
	#===========================NOT HEALING	
			store.heal(hero.health);
			print(hero.health);
		elif(us_input == "2"):
			store.mega_heal(hero.health);
		elif(us_input == "3"):
			store.weapon(hero.power)
		elif(us_input == "4"):
			store.armor(hero.defense);
		else:
			print("invaild input %s") % us_input
	elif(user_inp == "2"):
		pass;
	else:
		print("invaild input %s") % user_inp


print("Do you want to hire someone to take this journey with you? (Y or N)")
user_input = raw_input("> ")
if(user_input == "Y"):
	print("1. Hire a Medic (300gd)");
	print("2. Hire a Buff Guy (400gd)");
	print("3. Hire a Ninja (500gd)");
	user_input = raw_input("> ");
	if(user_input == "1"):
		hero.decrease_gold(300);
		heros.append(medic);
	elif(user_input=="2"):
		hero.decrease_gold(400);
	elif(user_input == "3"):
		hero.decrease_gold(500);


# we need to loop through all the monsters 
for monster in monsters:
	while(monster.is_alive() and hero.is_alive()):
		# game is on
		os.system("clear");
		for i in range(0, len(heros)):
			print("%s is attacking!" % heros[i].name);
			print "You have %d health and %d power and  %d defense %d mana." % (heros[i].health, heros[i].power, heros[i].defense, heros[i].mana);
			print "You have %d gold" %heros[i].gold;
			print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
			print "What do you want to do?"
			print "1. fight %s" % monster.name
			print "2. do nothing"
			print "3. flee"
			print "4. store";
			print "> "
			user_input = raw_input()
			if(user_input == "1"):
			# 	User has choosen to attack
			# 	take away health from the goblin base on hero power
			# the goblin class should be managing the goblin's health
			# the hero is giong to do hero.power damage to the goblin
				if(heros[i].mana > 0):
					print("Choose an option")
					print("1. Regular Attack")
					print("2. Spell Attack")
					if(heros[i].name == "Medic"):
						print("3. Heal");
						print("4. Heal_Others");
						user_input = raw_input("> ");
			#Heal's himself
						if(user_input == "3"):
							medic.heal();
			#heal's main hero
						elif(user_input == "4"):
		#============================NOT HEALING OTHERS
							medic.heal_other(hero.health);
					else:
						user_input = raw_input("> ")
					if(user_input == "1"):
						monster.take_damage(heros[i].power);
					if(user_input == "2"):
						monster.take_spell_damage(heros[i].spell_power);
						heros[i].spell_power_cost();
				elif(heros[i].mana<0):
					print("Choose an option")
					print("1. Regular Attack")
					user_input = raw_input("> ")
					if(user_input == "1"):
						monster.take_damage(heros[i].power);

			elif(user_input == "2"):
				# hero is going to stand there like an idoit
				pass
			elif(user_input == "3"):
				print("Goodbye coward, you remind me of Goober");
				break; # call break to end the while loop
			elif(user_input=="4"):
				print("Choose an option")
				print("1. Heal");
				print("2. Mega Heal")
				print("3. Add Weapon")
				print("4. Add Armor")
				print("> ");
				u_input = raw_input();
				if(u_input == "1"):
					store.heal(heros[i].health);
				elif(u_input == "2"):
					store.mega_heal(heros[i].health);
				elif(u_input == "3"):
					store.weapon(heros[i].power);
				elif(u_input == "4"):
					store.armor(heros[i].defense);
			else:
				print("invaild input %s") % user_input
			# goblins turn to attack !! only if he's still alive
		if(monster.is_alive() > 0):
			random_number = randint(0,2);
			if(random_number == 0):
			#just like the goblin, the hero should be changing its own stuff
				heros[0].take_damage(monster.power);
			else:
				heros[1].take_damage(monster.power);
			print("the goblin hits you for %d damage" % monster.power);
			# goblin has attacked, now check to see if hero is still alive
			if(hero.is_alive() < 0):
				print("you haave been killed by the weak %s, shame on you" %monster.name);
		else:
			hero.increase_gold();

		print(hero.health)
		print(medic.health);

#work on armor reduction to damage ratio
#work on adding a gold monster
#can add a heal mana option'
#make sure mage heal itself
	#
#make sure store heals the person
	#make sure to minus gold


