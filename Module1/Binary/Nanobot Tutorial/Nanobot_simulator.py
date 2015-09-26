'''
   Nanobot simulator
   
   Modify the Interpret state method to program the nanobot
   
   cblouin@dal.ca
'''

class Nanobot_Wheel:

    def __init__(self, engine_id):
        # Wheel Id
        self.engine_id = engine_id
        
        # What state the wheel is in. Either FF, F, N, R, FR
        self.state = 'N'
    
    def Receive(self, message):
        pass
    
    def Engine(self, engine_id, action):
        '''
            Engage engine with id engine_id to perform the following 
        '''
        pass