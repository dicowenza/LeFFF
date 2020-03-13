from .Features import *

class Value():

    def __init__(self, val):
        self.val = val
    
    def toString(self):
       if (isinstance(self.val, str)):
           return self.val
       elif (isinstance(self.val, (int, float, complex))):
           return str(self.val)
       else:
           return self.val.toString()
        
        