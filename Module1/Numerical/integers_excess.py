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


def DecodeExcess( x ):
    # Size of the integer
    nbits = len(x)
    
    # Find minimal value for this bit size
    minval = -1 * 2**(nbits-1)
    
    # Find offset by decoding the bit string
    offset = ConvertBitString( x )
    
    # Add the offset to the minval
    return minval + offset



# Testing area


# Define an excess string as the following string variable:
excess_int = '1001011'
print DecodeExcess( excess_int )
    
        
    
