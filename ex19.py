#this line defines function named cheese_and_crackers() with 2 parameters
def cheese_and_crackers(cheee_count, boxes_of_crackers):
	#this line prints f-string with cheese_count variable embedded
	print("You have {cheese_count} cheeses!")
	#this line prints f-string with boxes_of_crackers embedded
	print("You have {boxes_of_crackers} boxes of crackers!")
	#this line prints string
	print("Man that's enough for a party!")
	#this line prints a string
	print("Get a blanker.\n")

def my_function(arg1, arg2, arg3):
	print(arg1, arg2, arg3)

#this line prints a string
print("We can just give the function numbers directly:")
#this line calls a function cheese_and_crackers and passes 2 arguments value 20 and 30
cheese_and_crackers(20, 30)

#this line prints string literal
print("OR, we can use variables from our script:")
#this line assings int value 10 to variable
amount_of_cheese = 10
#this line assigns int value 50 to variable
amount_of_crackers = 50

#this line calls a function cheese_and_crackers and passes 2 parameters, 2 variables, amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this line prints string literal
print("We can even do math inside too:")
#this line calles a function cheese_and_crackers and passes 2 arguments, values which are calculated on the fly
cheese_and_crackers(10 + 20, 5 + 6)
#this line prints string literal
print("And we can combine the two, variables and math:")
#this line calls function cheese_and_crackers() and passes 2 arguments, variables 2 which are added int values
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

my_function("My ", " function", " call")
my_function("Antorher", "function", "call")
my_function("Call ", "number ", "three")
my_function("Call ", "number ", "four")
my_function("Some ", "random ", "text")
my_function("It's ", "quite ", "boring")
my_function("Blah ", "Blah ", "Blah")
my_function("I ", "guess ", "couple more times")
my_function("And ", "that's ", "it")
my_function("10th ", "call of ", "my function")

