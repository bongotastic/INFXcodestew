# Binary to Decimal

S = '1101'
n = len(S)

total = 0

# Iterate over each position in the string (where i is in turn from 0 to n
for i in range(0,n):
    # Find the power of two value for position i
    powervalue = (n - 1) - i 

    # Add to total if the i^th bit is a 1 
    if S[i] == '1':
        total = total + 2 ** powervalue

# Show the results on screen
print total
