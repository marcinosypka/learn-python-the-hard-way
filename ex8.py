#this line assigns string with 4 curly braces pairs to variable named formatter
formatter = "{} {} {} {}"

#this line inserts passed values to format method, creates new string and prints it
print(formatter.format(1,2,3,4))
#this line insert passed values to format string and then creates new string and prints it
print(formatter.format("one", "two", "three", "four"))
#this line passes bool values to format method called on formatter variable and then prints it
print(formatter.format(True, False, False, True))
#this line passes formatter variable four times to format method and then it prints it
print(formatter.format(formatter, formatter, formatter, formatter))
#this line passes four string literals to format string and then it prints it
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))
