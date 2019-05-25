backslash_sequence = "This is backslash: \\"
quotes_sequence = "This is single quote: \', this is double quote: \""
tabs_sequence = "Here is a tab between '|' characters: |\t| and here is vertival tab: \v"
LF_CR_sequence = "linefeed: \n: carriage return: \r"
backspace_sequence = "I put, 5 'x' and then used 2 backspace escape sequence and put 2 'y': xxxxx\b\byy"
octal_hex_sequence= "character with octal value 444: \444, character with hex value fff: \xff"
unicode_sequence = "cross in unicode(16 bit hex): \u2670, in unicode(32 bit hex): \U00002670, unicode WEST SYRIAC CROSS: \N{WEST SYRIAC CROSS}"
formfeed_sequence = "this is a formfeed\fused in a string"
complex_sequence = '''
this is complex\fsequence using \t some of already learned\nescape\tsequences\\
I put here some quotes \' \" \" \' and backslashes \\\\\\ and maybe some unicode values
like cross \N{WEST SYRIAC CROSS}" and maybe vertical tabs \v to make things more interestring and I will end all of this with null character with hex code \\x00: \x00 and I will insert some values with format() method for example here: {} and here {}.
'''
print(backslash_sequence)
print(quotes_sequence)
print(tabs_sequence)
print(LF_CR_sequence)
print(backspace_sequence)
print(octal_hex_sequence)
print(unicode_sequence)
print(formfeed_sequence)
print(complex_sequence.format("first value","second value"))
