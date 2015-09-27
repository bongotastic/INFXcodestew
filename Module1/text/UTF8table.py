''' 
    ASCII to integers
    cblouin@dal.ca
'''

# Generate the full range of ASCII characters

# Header
print('dec\thex\tUTF\n'+'-'*25)

# Start of range
begin = 1280
end   = 2000

for code in range(begin,end):
    # Decimal code
    dec_code = code
    
    # hexadecimal score
    hex_code = hex(code)
    
    # Actual character
    character = unichr(code)
    
    print("%d\t%s\t%s"%(dec_code, hex_code, character))