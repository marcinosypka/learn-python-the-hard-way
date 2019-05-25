#this line prints a string literal
print('Mary had a little lamb.')
#this line prints a string literal
print("Its fleece was white as {}.".format('snow'))
#this line prints a string literal
print("And everywhere that Mary went.")
#this line firstly makes string which consists of 10 dots and then it prints it
print("." * 10) # what'd that do?

#this line assigns string value to variable named end1
end1 = "C"
#this line assigns sting value to variable named end2
end2 = "h"
#this line assigns sting value to variable named end3
end3 = "e"
#this line assigns string value to variable named end4
end4 = "e"
#this line assigns string value to variable named end5
end5 = "s"
#this line assigns string value to variable named end6
end6 = "e"
#this line assigns string value to variable named end7
end7 = "B"
#this line assigns string value to variable named end8
end8 = "u"
#this line assigns string value to variable named end9
end9 = "r"
#this line assigns string value to variable named end10
end10 = "g"
#this line assigns string value to variable named end11
end11 = "e"
#this line assigns string value to variable named end12
end12 = "r"

#watch that comma at the end. try removint it to see what happens
#this line concatenates string in variables end1 - end6, end prints them, it uses ' ' character as last character instead of default newline character
print(end1 + end2 + end3 + end4 +  end5 + end6, end=' ')
#this line concatenates variables from end7 to end12 and prints them
print(end7 + end8 + end9 + end10 + end11 + end12)
