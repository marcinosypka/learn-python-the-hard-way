#this line imports argv from sys module
from sys import argv

#this line unpacks argv to script and input_file variables, it expects that argv contains 2 arguments
script, input_file = argv

#this line defindes function print_all() which takes one argument
def print_all(f):
#this line reads contents of a file to string and prints it
	print(f.read())

#this line defines function rewind() which takes one parameter
def rewind(f):
#this line calls method seek() with argument 0 on variable f, which means it set current file possition to the beggining 
	f.seek(0)

#this lines defines a function print_a_line which takes 2 arguments
def print_a_line(line_count, f):
#this line reads one line from file and then prints line_count variable and the line currently read
	print(line_count, f.readline(), end="")
#this line opens a file with a name stored in input_file variable and assigns the file object to current_file variable
current_file = open(input_file)
#this line prints a string
print("First let's print the whole file:\n")
#this line calls a function print_all() and passes current_file as argument
print_all(current_file)

#this line prints a string
print("Now let's rewind, kind of like a tape.")

#this line calls a function rewind() with current_file variable as argument
rewind(current_file)

#this line prints a string
print("Let's print three lines:")

#this line assigns integer value 1 to variable current_line
current_line = 1
#this line calls a function print_a_line() and passes current_line and current_variable as parameters
print(f"urrent_line is equal to: {current_line}")
print_a_line(current_line, current_file)

#this line increments value of current_line variable
current_line += 1
print(f"current_line is equal to: {current_line}")
#this line calls function print_a_line with parameters current_line and current_file
print_a_line(current_line, current_file)

#this line increments value of current_line variable
current_line += 1
print(f"current_line is equal to: {current_line}")
#this line calls a function print_a_line() and passes current_line and current_file as parameters
print_a_line(current_line, current_file)
