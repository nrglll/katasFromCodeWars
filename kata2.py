# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:26:27 2020

@author: asus
"""

def square_digits(num):
    return int("".join(str(int(i)**2) for i in str(num)))

    
print(square_digits(725))

  
       
    
