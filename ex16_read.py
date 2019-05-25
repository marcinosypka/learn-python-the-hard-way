from sys import argv

_, filename = argv

txt = open(filename)
print(f"This is the file {filename} you just opened:")
print(txt.read())
