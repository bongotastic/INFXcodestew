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

# A simple function to convert bit strings to number in base 10, modified to handle radix point
def ConvertRadixString( x ):
    # remove all 0 character padding
    x = x[ x.find('1') :]
    
    # Number of bits before the radix point
    nbit = x.find('.')
    
    # Delete the radix point
    x = x.replace('.','')

    # output
    out = 0.0
    
    # Iterate over each bit
    for position in range(len(x)):
        # Case 1: there is a 1 at that position
        if x[position] == '1':
            out += 2**(nbit-1)
            
        # In both cases, nbit must be decreased by one for the next position
        nbit -= 1
            
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


def Decode8bitFloat( x ):
    # Sign bit
    if x[0] == '1':
        sign = 1
    else:
        sign = -1
        
    # Extract exponent
    exponent_string = x[1:4]
    exponent_int = int(DecodeExcess( exponent_string ))
    
    # Extract the mantissa
    mantissa = x[4:]
    
    # Pad the mantissa with a bunch of 0 to the left
    mantissa = mantissa.rjust(8,'0')
    
    # Find where to add the radix
    radix = 4 + exponent_int
    
    # Reform the string to place the radix point
    mantissa = mantissa[:radix] + '.' + mantissa[radix:]
    
    # Convert the radix point value to a float
    output = ConvertRadixString( mantissa )
    
    return output
    


# Testing area
# Define 8bit float string as the following string variable:
float_string = '10111101'

print Decode8bitFloat( float_string )
    
        
    
