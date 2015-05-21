'''
   Decimal to Hexadecimal conversion
   INFX 1615 - Module 1 - Data Encoding
   cblouin@dal.ca

   This is a hack of the Dec2Bin.py script (which is more simple)
'''
# import log from the math library
from math import log

# Defining a hexadecimal character alphabet (without the 0, for simplicity later on)
hex_alphabet = '0123456789ABCDEF'

# Setting parameters
decimal_value = 17

# The string that will be output
hex_string = ''

## Conversion
# Find the number of bits by its log in base 16 (and removing the digist after the . )
n_hex = int(log(decimal_value,16))
print ( "The value %d requires %d hexadecimal characters to encode. "%( decimal_value, n_hex ) )

# Reverse the string to go from lowest order to highest order bit
rev_string = hex_string[::-1]

# Temporary list of binary characters
temp = []
dval = decimal_value
for value in range( n_hex, -1, -1 ):
	# Value of the nth bit
	nth_value = 16**value

	# How many nth_value (from 0 to 15)
	n = int(dval / nth_value)

	# Actual character to write (taken from the alphabet defined above)
	nth_char = hex_alphabet[ n ]

	# There is a 1 in this position if the remaining value is larger than nth_bit
	if dval >= nth_value:
		# Yes, set to 1 and subtract nth_value
		temp.append( nth_char )
		dval = dval - nth_value * n
	else:
		# Nope, put a 0 here and move on
		temp.append( nth_char )

print ('Hex string for %d is %s'%( decimal_value, ''.join(temp) ))
