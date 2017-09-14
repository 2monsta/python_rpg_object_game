import os
from Hero import Hero
from random import randint
from Store import Store;

from Goblin import Goblin
from Vampire import Vampire
# instantiate a hero object from the Hero Class
hero = Hero();
gamestore = Store();
#make a list to hold all our monsters
monsters = []
#before the game start, lets ask the hero for his her name.
print "what is thy name, brave adventurer";
hero_name = raw_input("> ");
hero.name = hero_name;
hero.cheer_for_hero();


print("how many monster are you willing to fight, brave %s" %hero.name);
number_of_enemies = int(raw_input("> "));
for i in range(0, number_of_enemies):
	rand_num = randint(0, 1);
	if(rand_num == 1):
		monsters.append(Goblin());
	else:
		monsters.append(Vampire());
print(monsters);

# we need to loop through all the monsters 
for monster in monsters:
	while(monster.is_alive() and hero.is_alive()):
		# game is on
		os.system("clear");
		print "You have %d health and %d power and  %d defense." % (hero.health, hero.power, hero.defense);
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
				hero.heal();
			elif(u_input == "2"):
				hero.mega_heal();
			elif(u_input == "3"):
				hero.weapon();
			elif(u_input == "4"):
				hero.armor();
		else:
			print("invaild input %s") % user_input

		# goblins turn to attack !! only if he's still alive

		if(monster.health > 0):
			#hero.health -= goblin.power;
			#just like the goblin, the hero should be changing its own stuff
			hero.take_damage(monster.power);


			print("the goblin hits you for %d damage" % monster.power);
			# goblin has attacked, now check to see if hero is still alive
			if(hero.health < 0):
				print("you haave been killed by the weak %s, shame on you" %monster.name);
		else:
			hero.increase_gold();