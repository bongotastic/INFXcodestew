'''
   Binary to Decimal conversion
   INFX 1615 - Module 1 - Data Encoding
   cblouin@dal.ca
'''
# Setting parameters
# Enter a string of 0s and 1s
binary_string = '11010011'

## Conversion
# Find the number of bits in the string
n_bits = len(binary_string)

# Variable to store the result
result = 0

# Reverse the string to go from lowest order to highest order bit
rev_string = binary_string[::-1]

# looping over each bit in the string
for bit in range( n_bits ):
	# Compute the bit value at index bit
	bit_value = 2**bit

	# Add only if there is a 1 at this position
	if rev_string[bit] == '1':
		# Add bit_value to the result
		result = result + bit_value

		# print message
		print( "Bit #%d = 1, adding 2^%d so result = %d"%(bit+1, bit, result) )
	else:
		# print message stating that nothing is done
		print( "Bit #%d = 0, not adding anything to result"%(bit+1) )

# Print final result
print( '*'*50 + '\n' + '%s = %d'%( binary_string, result ) )