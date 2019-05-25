from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	try:
		how_much = int(choice)
	except ValueError:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
	while True:
		choice = input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you than slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your legs off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulu_room():
	print("Here you see the great evil Cthulu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head, or maybe try to cast a spell?:")
	choice = input("> ")
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	elif "cast a spell":
		portal_room()
	else:
		cthulu_room()


def portal_room():
	print("You entered the portal room, you see the seer")
	print("He says: Hello creature, I was expecting you")
	print("Here's a riddle for you, if you answer correctly")
	print("you will pass, else you will implode")
	print("And here's a riddle for you:")
	print("What's the result of 2 + 2 * 2")
	choice = input("> ")
	if choice == "6":
		print("Congratulations, this is correct answer, now I will teleport you to golden room")
		gold_room()
	else:
		dead("Ohh you poor creature, you should pay more attention to maths in school ! You're deadnow.") 

def dead(why):
	print(why, "Good job!")
	exit(0)


def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	choice = input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
