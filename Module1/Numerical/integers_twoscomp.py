'''
   Decoding integers
'''

# Useful functions
import math

# A simple function to convert bit strings to number in base 10
def ConvertBitString( x ):
    # Length of the string
    nbit = len(x)
    
    # output
    out = 0
    
    # Reverse the string so the lowest order bit is at index 0
    x = x[::-1]
    
    # Iterate over each bit
    for i in range(len(x)):
        if x[i] == '1':
            out += 2**i
            
    # return the output
    return out


def DecodeTwosComp( x ):
    # Size of the integer
    nbits = len(x)
    
    
    
    # Case 1: A negative value has a 1 in the first position
    if x[0] == '1':
        # Find minimal value for this bit size
        minval = -1 * 2**(nbits-1)        

        # Remove the first bit
        x = x[1:]
        
        # compute the offset
        offset = ConvertBitString( x )
        
        # Compute actual value
        output = minval + offset
    # A positive value has a 0 in the first bit
    else:
        # Simply decode the binary string
        output = ConvertBitString( x )
    
    # return the results
    return output



# Testing area
# Define an excess string as the following string variable:
tc_int = '111'
print DecodeTwosComp( tc_int )
    
        
    
