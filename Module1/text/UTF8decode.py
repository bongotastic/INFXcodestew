''' UTF-8 Decoding
    cblouin@dal.ca
'''

# Some string to decode (keep only one uncommented)
#s = '00100110'
s = '111010011010101110101011'


# Case 1: ASCII character
if s[0] == '0':
    # Do a simple ASCII conversion
    # Step 1: from binary to integer using int in base 2
    myint = int(s, 2)
    
    # Fetch the correct ASCII character
    mychar = chr(myint)
    
    print ('The ASCII character for %s is "%s"'%(s, mychar))
    
else:
    # OK, we have a larger value and need to unpack the data
    # Step 1: how many 1 in the first byte? Can be done by looking for the first 0
    char_length = s.find('0')
    
    if char_length == 1:
        print('Character %s is not a valid UTF-8 character.'%(s))
        exit()
    
    # Step 2: fetch the whole character by picking the first 8 * byte numbers
    mychar = s[:8*char_length]
    
    # Step 3: Create a data bit string
    data = ''
    
    # Step 4: split into bytes
    mybytes = []
    for i in range(0, len(mychar), 8):
        mybytes.append(mychar[i:i+8])
        
    print('Byte breakdown: ')
    for i in range(len(mybytes)):
        # Get byte from list
        bt = mybytes[i]
        
        print(bt)
        
        # First byte?
        if i == 0:
            # remove the lead bits
            data = bt[ char_length + 1 : ]
            
        # Other bytes (skip the first two characters)
        else:
            data = data + bt[2:]
    
    # Print data
    print('Data after removing the structural bits is %s'%(data))
    
    # Convert to integer
    char_int = int(data, 2)
    print('Data as an integer: %d'%(char_int))
    
    # Print as unicode
    print( unichr(char_int ))