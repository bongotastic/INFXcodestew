''' State calculator

    Determine the number of bits necessary to encode a defined number of states. Ut then determines the number of stats unused for this 
    bit allocation. 
    
    cblouin@dal.ca
'''

# Ask the user how many states should be encoded.
n_state = int(raw_input("How many different values must be encodable: "))

# Compute the minimum number of bits to encode this number, it is essentionally the integer that is at least equal or larger 
# to the log in base 2 of n_state
import math
log2_of_n = math.log(n_state, 2)

print("The log in base 2 of %d is %f. \n"%(n_state, log2_of_n))

# number of bits is the smallest integer larger than log2_of_n
n_bits = math.ceil(log2_of_n)

print("This means that it takes %d states can be encoded in %d bits. \n"%(n_state, n_bits))

# wasted states 
wasted_states = 2**n_bits - n_state

print('Leaving %d states unused.'%(wasted_states))