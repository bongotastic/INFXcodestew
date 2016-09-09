''' 
    ASCII to integers
    cblouin@dal.ca
'''

# Generate the full range of ASCII characters

# Header
print('dec\thex\tASCII\n'+'-'*25)

for ascii_code in range(0,128):
    # Decimal index
    dec_code = ascii_code
    
    # hexadecimal index
    hex_code = hex(ascii_code)
    
    # Printable character
    ascii = chr(ascii_code)
    
    print("%d\t%s\t%s"%(dec_code, hex_code, ascii))