'''
   Decoding integers
'''

# Useful functions
import math

# A simple function to convert radix bit strings to number in base 10
def ConvertBitString( x ):
    # Length of the string
    nbit = len(x)
    
    # Has radix?
    if x.find('.') !- -1:
        # Remove one for the radix character
        nbit = nbit - 1
        
        # output
        output = 0.0
        
    
