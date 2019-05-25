#this line assigns int value to people variable
people = 30
#this line assigns int value to cars variable
cars = 30
#this line assigns int value to trucks variable
trucks = 30

#this line starts compound statemet, if statemets executes suite below if satement after if is true
if cars > people:
#this line belongs to suite started by if above, prints a string to terminal
	print("We should take the cars.")
#this line starts elif statement, if statement after elif is true suite below is executed, it has to be put after if compound statement
elif cars < people:
#this line belongs to suite started by elif, it prints string to terminal
	print("We should not take the cars.")
#this line starts a compound statement, if if statement and all elif statements above are false then else suite is executed
else:
#this line belongs to else suite, it prints string to terminal
	print("We can't decide.")
#this line starts if statement
if trucks > cars:
#this line prints string to terminal if if statement is true
	print("That's too many trucks.")
#this line starts elif statement
elif trucks < cars:
#this line prints string to terminal if elif statement is true
	print("Maybe we could take the trucks.")
#this line starts else statement
else:
#this line prints string to terminal if all elifs and if above is false
	print("We still can't decide")
#this line starts if statement
if people > trucks or not people > cars * 2 :
#this line prints string to terminal if if statement above is true
	print("Alright, let's just take the trucks.")
#this line starts else statement
else:
#this line prints string to terminal if all elifs and if statement above is false
	print("Fine, let's stay home than.")
