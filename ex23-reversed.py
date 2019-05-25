import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()
	print(line)
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	cooked_string = next_lang.decode('utf-8')
	raw_string = cooked_string.encode(encoding, errors)
	
	print(raw_string, "<===>", cooked_string)

languages = open("languages.txt", "rb")
main(languages, encoding, error)	
