# this is a procedural apprach to a text based rpg game
# the hero is ging to fight a goblin
# the hero will have the option to:
# 1) fight the goblin
# 2) do nothing( the goblin will still attack the hero)
# 3) run away
import os

hero_health = 10;
hero_power = 10;
goblin_health = 6;
goblin_power = 2;

# run the game as long as both characters have health
while(goblin_health > 0 and hero_health > 0):
	# game is on
	os.system("clear");
	print "You have %d health and %d power." % (hero_health, hero_power)
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
	print "What do you want to do?"
	print "1. fight goblin"
	print "2. do nothing"
	print "3. flee"
	print "> ",
	user_input = raw_input()
	if(user_input == "1"):
	# 	User has choosen to attack
	# 	take away health from the goblin base on hero power
		goblin_health -= hero_power;
	elif(user_input == "2"):
		# hero is going to stand there like an idoit
		pass
	elif(user_input == "3"):
		print("Goodbye coward, you remind me of Goober");
		break; # call break to end the while loop
	else:
		print("invaild input %s") % user_input

	# goblins turn to attack !! only if he's still alive

	if(goblin_health > 0):
		hero_health -= goblin_power;
		print("the goblin hits you for %d damage" % goblin_power);
		# goblin has attacked, now check to see if hero is still alive
		if(hero_health < 0):
			print("you haave been killed by the weak goblin, shame on you");