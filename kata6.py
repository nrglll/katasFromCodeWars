# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:01:35 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation: 
# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.
# 
# It should remove all values from list a, which are present in list b.
# 
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# 
# array_diff([1,2,2,2,3],[2]) == [1,3]
# =============================================================================

def array_diff(a, b):
    return list(i for i in a if i not in b)
    
        
# =============================================================================
# print(array_diff([-6, -14, -9, 4, -19, 14, 3, -17, 8, -8],[6, 4]))
# =============================================================================
