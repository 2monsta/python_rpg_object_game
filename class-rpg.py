import os
from Hero import Hero
from random import randint
from Store import Store
from Medic import Medic
from Gold_Monster import Gold_Monster
from Boss_Drag import Boss_Drag
from Buff_Guy import Buff_Guy

from Goblin import Goblin
from Vampire import Vampire
# instantiate a hero object from the Hero Class
hero = Hero()
store = Store()
medic = Medic()
gold_monster = Gold_Monster()
boss_dragon = Boss_Drag()
buff_guy = Buff_Guy()
monsters = []
heros = []
heros.append(hero)
longstring = """

			   
 \ \    / /__| |__ ___ _ __  ___  | _ \ |__ _ _  _ ___ _ _ 
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ / _` | || / -_) '_|
   \_/\_/\___|_\__\___/_|_|_\___| |_| |_\__,_|\_, \___|_|  
											  |__/              
			
"""
print longstring
#==========================================ADD A STORY==============================
story_string = """
The goal of this game is to reach 10,000 gold. 
Monster's will keep coming at you! Beware of the Dragon!

"""

print(story_string)
#before the game start, lets ask the hero for his her name.
print "what is thy name, brave adventurer"
hero_name = raw_input("> ")
hero.name = hero_name
hero.cheer_for_hero()

#generate number of monster to put in the list of monsters
# print("how many monster are you willing to fight, brave %s" %hero.name);
# number_of_enemies = int(raw_input("> "));
# for i in range(0, number_of_enemies):
# 	rand_num = randint(0, 3);
# 	if(rand_num == 1):
# 		monsters.append(Goblin());
# 	elif(rand_num == 2):
# 		monsters.append(Vampire());
# 	elif(rand_num == 0):
# 		monsters.append(Gold_Monster());
# #Appending a final boss monster!!
# monsters.insert(-1, boss_dragon);
monsters.append(Goblin());

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
		store.print_store_items();
		us_input = raw_input();
		if(us_input == "1"):
			#before i was using a part of hero's data, which got changed but just not reflected in the hero object
			#now if i pass in the hero object, and change 
			store.heal(hero);
			if(hero.health > 20):
				hero.health = 20;
		elif(us_input == "2"):
			store.mega_heal(hero);
			if(hero.health > 20):
				hero.health = 20;
		elif(us_input == "3"):
			store.weapon(hero)
		elif(us_input == "4"):
			store.armor(hero);
		elif(us_input == "5"):
			pass;
		elif us_input == "6":
			hero.mana += 10;
		else:
			print("invaild input %s") % us_input
	elif(user_inp == "2"):
		pass;
	else:
		print("invaild input %s") % user_inp


print("Do you want to hire someone to take this journey with you? (Y or N)")
user_input = raw_input("> ")
if(user_input == "Y"):
	store.print_people_to_hire();
	user_input = raw_input("> ");
	if(user_input == "1"):
		hero.decrease_gold(300);
		heros.append(medic);
	elif(user_input=="2"):
		hero.decrease_gold(400);
		heros.append(buff_guy);
	elif(user_input == "3"):
		hero.decrease_gold(500);
	else:
		print("invaild input %s") % user_input
is_battle = True;
# we need to loop through all the monsters 
for monster in monsters:
	while(monster.is_alive() and hero.is_alive() and is_battle == True):
		# game is on
		rand_num = randint(0, 9);
		if(rand_num == 1 or rand_num == 3 or rand_num == 5):
			monsters.append(Goblin());
		elif(rand_num == 4 or rand_num == 6 or rand_num == 8):
			monsters.append(Vampire());
		elif(rand_num == 0 or rand_num == 2):
			monsters.append(Gold_Monster());
		elif(rand_num == 7):
			monsters.append(Boss_Drag());
		#================================IMPLEMENT the user to use buff guy
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
							if(medic.health > 20):
								medic.health = 20;
			#heal's main hero
						elif(user_input == "4"):
							medic.heal_other(hero);
							if(hero.health > 20):
								hero.health = 20;
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
				else:
					print("invaild input %s") % user_input

			elif(user_input == "2"):
				pass
			elif(user_input == "3"):
				print("Goodbye coward, you remind me of Goober");
				is_battle = False; # call break to end the while loop
				break;
			elif(user_input=="4"):
				store.print_store_items();
				us_input = raw_input();
				if(us_input == "1"):
					store.heal(heros[i]);
					if(heros[i].health > 20):
						heros[i].health = 20;
				elif(us_input == "2"):
					store.mega_heal(heros[i]);
					if(heros[i].health > 20):
						heros[i].health = 20;
				elif(us_input == "3"):
					store.weapon(heros[i]);
				elif(us_input == "4"):
					store.armor(heros[i]);
			else:
				print("invaild input %s") % user_input
			# goblins turn to attack !! only if he's still alive

	#=========================Testing Final Boss's sp attack=========================
		if(monster.is_alive() > 0):
			r_num = randint(0,3)
			if(monster.name == "Spirit Dragon"):
				if(r_num == 3):
					monster.sp_attack(hero);
				else:
					hero.take_damage(monster.power);
			random_number = randint(0,2);
			for i in range(0, len(heros)):
				if(random_number == 0):
				#just like the goblin, the hero should be changing its own stuff
					heros[i].take_damage(monster.power);
					print("the goblin hits you for %d damage" % monster.power);
				elif(random_number==1):
					heros[i].take_damage(monster.power);
					print("the %s hits you for %d damage" %(monster.name, monster.power));
				# goblin has attacked, now check to see if hero is still alive
			if(hero.is_alive() < 0):
				print("you haave been killed by the weak %s, shame on you" %monster.name);
		else:
			#increase the hero's gold after defeating monster
			if(monster.name == "Gold_Monster"):
				hero.increase_gold(300);
			elif(monster.name == "Vampire"):
				hero.increase_gold(200);
			elif(monster.name =="Boss_Drag"):
				her.increase_gold(500);
				print("You have the option to hire a someone to fight along side you!");
				store.print_people_to_hire();
			else:
				hero.increase_gold(100);

		print(hero.health)
		print(medic.health);


	#Buff guy's special attack if choosen, the user can choose to use buff guy to attk
	#to do 50 damage

	#work on armor reduction to damage ratio
	#can add a heal mana option'
	#Weapon class to extend weapon list to power up power
	#have t1 +5, t2+7, t3+10 weapons
	#armor class to extend defnse power
	#add new characters and able to hire only after defeating a spirit dragon
	#have a print class that just prints some ofthese lines



