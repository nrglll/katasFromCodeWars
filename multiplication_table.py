# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:08:03 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Your task, is to create NxN multiplication table, of size 
# provided in parameter.
# 
# for example, when given size is 3:
# 
# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
# =============================================================================

def multiplication_table(size):
    first = []
    for n in range(1, size+1):
        first.append([elem*n for elem in list(range(1, size+1))])
    return first

# =============================================================================
# print(multiplication_table(5))
# =============================================================================

#%% best
    
def multiplication_table(size):
    return [[n*m for n in range(1, size+1)] for m in range(1, size+1)]


# =============================================================================
# print(multiplication_table(5))
# =============================================================================
















