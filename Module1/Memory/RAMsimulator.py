''' RAM simulator
    cblouin@dal.ca
'''

# Create a RAM object type using a class
class RAMstick:
    def __init__(self, max_size):
        # Actual storage structure
        self.stick = [None]*max_size
        
    def Read(self, address, lenght):
        ''' Reads and concatenate cells from address to address+length
        '''
        # Convert hex address to dec index
        decimal_start_address = int(address,16)
        
        # Create an output string
        output = []
        
        # Scan the stick
        for i in range(decimal_start_address,decimal_start_address+lenght):
            output.append( self.stick[i] )
            
        return output
        
    def Write(self, text, address):
        '''
            Write each characters into a ram cell.
        '''
        # Make sure that it can write text to RAM
        decimal_start_address = int(address,16)
        
        # How long is the text
        text_length = len(text)
        
        # address of the last cell to write to
        decimal_end_address = decimal_start_address + text_length
        
        # Check that the write operation can be completed
        if decimal_end_address >= len(self.stick):
            raise "Memory overflow by %d bytes."%(decimal_end_address-(len(self.stick)))
        
        # Perform the write, one byte at the time
        for character_index in range(len(text)):
            # Where to write
            byte_address = decimal_start_address + character_index
            
            # What to write
            character = text[character_index]
            
            # Do the deed
            self.stick[byte_address] = character  
            
    def PrettyPrint(self):
        ''' Display the content of the RAM stick
        '''
        # Header
        print('Address\tContent')
        
        for i in range(len(self.stick)):
            # Hex address
            Hx = hex(i)
            
            # Content
            content = self.stick[i]
            
            #print to screen
            print('%s\t%s'%(str(Hx), content))
            


if __name__ == "__main__":
    # Create a RAM stick with 20 cells
    RAM = RAMstick(20)
    
    # Print the content after 
    RAM.PrettyPrint()    
    
    print("What you see abov is an empty sequence of 20 memory cells")
    raw_input('Press enter to Write "Hello" starting at memory cell 0X5')

    # Write something starting at cell 0x5
    RAM.Write('Hello', '0X5')
    
    # Print the content after 
    RAM.PrettyPrint()
    
    raw_input('Press enter to read 10 cells starting at memory address 0X3')
    print(RAM.Read('0X3', 10))  
    
    # Write something starting at cell 0x5
    raw_input('Press enter to overwrite memory cell 0X5 from "H" to "J"')
    RAM.Write('J', '0X5')  
    
    # Print the content after 
    RAM.PrettyPrint()    