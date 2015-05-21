'''
   Decimal to Radix point binary conversion
   INFX 1615 - Module 1 - Data Encoding
   cblouin@dal.ca

   A simpler script is found at Dec2Bin.py, this approximate floating point numbers
'''
# import log from the math library
from math import log

# Setting parameters
decimal_value = 2.56

# The string that will be output
binary_string = ''

## Conversion
# Find the number of bits by its log in base 2 (and removing the digist after the . )
n_bits = int(log(decimal_value,2))
print ( "The value %d requires %d bits to encode. "%( decimal_value, n_bits ) )

# Reverse the string to go from lowest order to highest order bit
rev_string = binary_string[::-1]

# Temporary list of binary characters, maximum precision of 9 binary characters after the radix point
temp = []
dval = decimal_value
for value in range( n_bits, -10, -1 ):
	# Value of the nth bit
	nth_bit = 2**value

	# There is a 1 in this position if the remaining value is larger than nth_bit
	if dval >= nth_bit:
		# Yes, set to 1 and subtract nth_value
		temp.append( '1' )
		dval = dval - nth_bit
	else:
		# Nope, put a 0 here and move on
		temp.append( '0' )

	# Time to insert the radix point IF value is 0
	if value == 0:
		temp.append( '.' )

print ('Binary string for %d is %s'%( decimal_value, ''.join(temp) ))
