# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:26:27 2020

@author: Nurgul Aygun
"""

# =============================================================================
# Kata Explaination:
# Welcome. In this kata, you are asked to square every digit of a number.
# 
# For example, if we run 9119 through the function, 811181 will come out, 
# because 92 is 81 and 12 is 1.
# 
# Note: The function accepts an integer and returns an integer    
# =============================================================================

def square_digits(num):
    return int("".join(str(int(i)**2) for i in str(num)))

    
# =============================================================================
# print(square_digits(725))
# =============================================================================

  
       
    
