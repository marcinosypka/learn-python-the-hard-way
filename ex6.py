#this line assigns value 10 of type int to variable named types_of_people
types_of_people = 10
#this line assigns f-string value to variable named x, it also puts value types_of_people inside f-string
x = f"There are {types_of_people} types of people."

#this line assigns string value to variable named binary
binary = "binary"
#this line assings string value to variable named do_not
do_not = "don't"
#this line assings f-string value to variable named y, it also puts value of variables binary and do_not inside f-string
y = f"Those who know {binary} and those who {do_not}."

#this line prints variable x
print(x)
#this line prints variable y
print(y)

#this line prints f-string which contains x variable
print(f"I said: {x}")
#this line prints f-string which contains y variable
print(f"I also said: '{y}'")

#this line assings B: bool value False to variable named hilarious
hilarious = False
#this line assings string to variable named joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

#this line prints joke_evaluation variable with inserted hilarious variable value with .format() method
print(joke_evaluation.format(hilarious))

#this line assigns string to variable named w
w = "This is the left side of..."

#this line assigns string to variable named e
e = "a string with a right side."

#this line prints concatenated w and e strings 
print(w + e)
