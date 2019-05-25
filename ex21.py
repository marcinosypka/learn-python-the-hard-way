def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#simpler approach to puzzle
div = divide(iq, 2)
mul = multiply(weight, div)
sub = subtract(height, mul)
add_res = add(age, sub)

print("That becomes: ", what, "Can you do it by hand?")
print(f"And here's the puzzle solved in simpler approach {add_res}")

new_formula = divide(10, add(15, multiply(22, divide(8, multiply(12, subtract(20,iq))))))
print(f"And here's the new formula result: {new_formula}")
print("And here's another one: {}".format(add(subtract(24,1023), divide(34, 100))))
