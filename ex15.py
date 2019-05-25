#this line imports argv object from sys module
from sys import argv

#this line unpacks filename from argv object, it uses _ to unpack script filename and note store it enywhere
_, filename = argv

#this line opens file with filename stored in filename variable, it uses default parameters such as 'rt' mode
txt = open(filename)

#this line uses f-string literals to print string with embedded value of filename variable
print(f"Here's your file {filename}:")
#this line reads whole file and prints the results
print(txt.read())

#this line prints a string
print("Type the filename again:")
#this line prompts for filename
file_again = input("> ")
#this line opens file with filename stored in file_again variable
txt_again = open(file_again)

#this line reads file and then prints it
print(txt_again.read())
txt.close()
txt_again.close()
