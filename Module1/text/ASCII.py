''' 
    ASCII to integers
    cblouin@dal.ca
'''

# Here is how you can convert integer and ASCII characters in Python

# Get input from console
mychar = raw_input("Enter one character: ")

# Ensures that it is only one charaacter long
mychar = mychar[0]

# Convert
mychar_code = ord(mychar)

# Print output
print("The character %s has ASCII code %d ."%(mychar, mychar_code))