import random

adjectives = ["luxuriant","sticky", "glamorous","direful","lackadaisical","nonstop","hungry","abounding","half","stale","tawdry"]
nouns = [
		"chocolate", "cricketer", "defender", "earrings",
		 "founde", "jackfruit", "lip", "perfection", 
		 "quarter", "sun", "dildo"
		]


def pick_number():
	while True:
		number = input("> ")
		try:
			number = int(number)
			if number < 0 or number > 10:
				print("this number is not within range 0 and 10, please try again.")
			else:
				break
		except:
			print("This is not a valid number, try again")
	return number

print("Hi, welcome to nickname generator, pick a number (from 0 to 10):")
first_number = pick_number()
print("Now pick another number:")
second_number = pick_number()
random_number = random.randrange(10,99,1)

nick = f"{adjectives[first_number]}_{nouns[second_number]}{random_number}"

print(f"Your nick is: {nick}")
