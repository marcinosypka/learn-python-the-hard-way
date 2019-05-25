print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	bear = input("> ")
	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away.")

elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Your body survuves powered by a mind of jello.")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
elif door == "3":
	print("You entered shops with vinyls, what do you do ?")
	print("1. Go to jazz section.")
	print("2. Go to rock music section.")
	section = input("> ")
	if section == "1":
		print("You pick up miles davis record, the strange man enters the shop and starts shooting, you end up injured in hospital")
	elif section == "2":
		print("You couldn't find anything intresting and you leave the shop")
	else:
		print("""You stumble into strange man, he injects something into your arm, you wake up on your bed, this was only a dream""")
else:
	print("You stumble around and fall on a knife and die. Good job!")
