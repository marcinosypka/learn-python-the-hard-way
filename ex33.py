from sys import argv

def get_numbers(n, inc):
	i = 0
	numbers = []
	while i < n:
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + inc
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers

def get_numbers_fl(n, inc):
	numbers = []
	for i in range(0, n, inc):		
		print(f"At the top i is {i}")
		numbers.append(i)
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers

_, n, inc = argv
n = int(n)
inc = int(inc)
numbers = get_numbers_fl(n, inc)
print("The numbers: ")

for num in numbers:
	print(num)
