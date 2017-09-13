import os
from Hero import Hero

from Goblin import Goblin

# instantiate a hero object from the Hero Class
hero = Hero();
goblin = Goblin();


while(goblin.health > 0 and hero.health > 0):
	# game is on
	os.system("clear");
	print "You have %d health and %d power." % (hero.health, hero.power)
	print "The goblin has %d health and %d power." % (goblin.health, goblin.power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> ",
	user_input = raw_input()
	if(user_input == "1"):
	# 	User has choosen to attack
	# 	take away health from the goblin base on hero power
		#goblin_health -= hero_power;
	# the goblin class should be managing the goblin's health
	# the hero is giong to do hero.power damage to the goblin
		goblin.take_damage(hero.power);
	elif(user_input == "2"):
		# hero is going to stand there like an idoit
		pass
	elif(user_input == "3"):
		print("Goodbye coward, you remind me of Goober");
		break; # call break to end the while loop
	else:
		print("invaild input %s") % user_input

	# goblins turn to attack !! only if he's still alive

	if(goblin.health > 0):
		#hero.health -= goblin.power;
		#just like the goblin, the hero should be changing its own stuff
		hero.take_damage(goblin.power);

		print("the goblin hits you for %d damage" % goblin.power);
		# goblin has attacked, now check to see if hero is still alive
		if(hero.health < 0):
			print("you haave been killed by the weak goblin, shame on you");