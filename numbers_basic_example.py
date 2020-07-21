# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:34:19 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Finish the solution so that it returns the sum of all the 
# multiples of 3 or 5 below the number passed in.
# 
# Note: If the number is a multiple of both 3 and 5, only count it once.
# =============================================================================

def solution(number):
    numbers = range(1, number)
    l = []
    for n in numbers:
        if n % 3 == 0 or n % 5 == 0: l.append(n)
    return sum(l)
        
# =============================================================================
# print(solution(10))
# =============================================================================
