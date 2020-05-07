# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:36:47 2020

@author: asus
"""

def validate_pin(pin):

        
    if len(pin) == 4 or len(pin) == 6:
        try:
            int(pin) == int
            
            if int(pin)<0:
                return False
            else: 
                return True
        except: 
            return False
        
    else:
        return False
    
print(validate_pin("+98476"))