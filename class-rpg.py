import os
# import pygame
from Hero import Hero
from random import randint
from Store import Store;

from Goblin import Goblin
from Vampire import Vampire
# instantiate a hero object from the Hero Class
hero = Hero();
store = Store();
# pygame.init();
# screenX = 1080;
# screenY = 920;
# screen_size = (screenX, screenY);
# pygame_screen = pygame.display.set_mode(screen_size);
# pygame.display.set_caption("FF remake");
#make a list to hold all our monsters
monsters = []
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
		print("1. Heal");
		print("2. Mega Heal")
		print("3. Add Weapon")
		print("4. Add Armor")
		print("> ");
		us_input = raw_input();
		if(us_input == "1"):	
			store.heal(hero.health);
		elif(us_input == "2"):
			store.mega_heal(heao.health);
		elif(us_input == "3"):
			hero.weapon();
		elif(us_input == "4"):
			hero.armor();
		else:
			print("invaild input %s") % us_input
	elif(user_inp == "2"):
		pass;
	else:
		print("invaild input %s") % user_inp

# we need to loop through all the monsters 
for monster in monsters:
	while(monster.is_alive() and hero.is_alive()):
		# game is on
		os.system("clear");
		print "You have %d health and %d power and  %d defense %d mana." % (hero.health, hero.power, hero.defense, hero.mana);
		print "You have %d gold" %hero.gold;
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
			if(hero.mana > 0):
				print("Choose an option")
				print("1. Regular Attack")
				print("2. Spell Attack")
				user_input = raw_input("> ")
				if(user_input == "1"):
					monster.take_damage(hero.power);
				if(user_input == "2"):
					monster.take_spell_damage(hero.spell_power);
					hero.spell_power_cost();
			elif(hero.mana<0):
				print("Choose an option")
				print("1. Regular Attack")
				user_input = raw_input("> ")
				if(user_input == "1"):
					monster.take_damage(hero.power);

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
				store.heal(hero.health);
			elif(u_input == "2"):
				store.mega_heal(hero.health);
			elif(u_input == "3"):
				store.weapon(hero.power);
			elif(u_input == "4"):
				store.armor(hero.defense);
		else:
			print("invaild input %s") % user_input

		# goblins turn to attack !! only if he's still alive

		if(monster.is_alive() > 0):
			#just like the goblin, the hero should be changing its own stuff
			hero.take_damage(monster.power);


			print("the goblin hits you for %d damage" % monster.power);
			# goblin has attacked, now check to see if hero is still alive
			if(hero.is_alive() < 0):
				print("you haave been killed by the weak %s, shame on you" %monster.name);
		else:
			hero.increase_gold();



#work on adding a partner and fight multiple monsters at the same time
	#let the monster choose a random number and deals damage to whichever one.
#work on armor reduction to damage ratio
#work on adding a gold monster
#can add a heal mana option

