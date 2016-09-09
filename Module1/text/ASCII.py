''' 
    ASCII to integers
    cblouin@dal.ca
'''

# Here is how you can convert integer and ASCII characters in Python

# Get input from console
mychar = "5"

# Ensures that it is only one charaacter long
mychar = mychar[0]

# Convert using a built-in function called "ord
mychar_code = ord(mychar)

# Print output
print("The character %s has ASCII code %d ."%(mychar, mychar_code))
