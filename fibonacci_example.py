# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:34:57 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# 
# The drawing shows 6 squares the sides of which have a length of 
# 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters 
# of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80
# 
# Could you give the sum of the perimeters of all the squares in a 
# rectangle when there are n + 1 squares disposed in the same manner 
# as in the drawing:
# 
# Hint: See Fibonacci sequence #Ref: http://oeis.org/A000045
# 
# The function perimeter has for parameter n where n + 1 is the 
# number of squares (they are numbered from 0 to n) and returns the 
# total perimeter of all the squares.
# =============================================================================

def perimeter(n):
    fibonacci = 1
    list_of_fibonacci = [0, 1]
    while len(list_of_fibonacci) <= (2 + n) :
        fibonacci = list_of_fibonacci[-2] + fibonacci
        list_of_fibonacci.append(fibonacci)
        if len(list_of_fibonacci) == (2 + n):
            break
    return sum(i for i in list_of_fibonacci)*4

# =============================================================================
# print(perimeter(8))
# =============================================================================
    

    
    
