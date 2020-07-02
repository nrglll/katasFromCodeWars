# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:10:48 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
#     
# This kata focuses on the Numpy python package and you can 
# read up on the Numpy array manipulation functions here: 
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-manipulation.html
# 
# You will get two integers N and M. You must return an array 
# with two sub-arrays with numbers in ranges [0, N / 2) and [N / 2, N) 
# respectively, each of them being rotated M times.
# 
# reorder(10, 1)   =>  [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
# reorder(10, 3)   =>  [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
# reorder(10, 97)  =>  [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
# =============================================================================

import numpy as np

def reorder(a, b):
    first = np.arange(0, int(a/2))
    first_array = np.hstack((first[-int((b%(a/2))):], first[:int(((a/2) - (b%(a/2))))]))
    second = np.arange(int(a/2), int(a))
    second_array = np.hstack((second[-int((b%(a/2))):], second[:int(((a/2) - (b%(a/2))))]))
    if (b%(a/2)) == 0:  
        return [first, second]
    return [list(first_array), list(second_array)]


# =============================================================================
# print(reorder(10, 1))   # [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
# print(reorder(10, 3))   # [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
# print(reorder(10, 97))  # [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
# =============================================================================


#%% solution with lists

def reorder(a, b):

    first = list(range(0, int(a/2)))
    x = first[-int((b%(a/2))):] + first[:int(((a/2) - (b%(a/2))))]
    second = list(range(int(a/2), int(a)))
    y = second[-int((b%(a/2))):] + second[:int(((a/2) - (b%(a/2))))]

    if (b%(a/2)) == 0:  
        return [first, second]
    
    return [x, y]

# =============================================================================
# print(reorder(10, 1))   # [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
# print(reorder(10, 3))   # [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
# print(reorder(10, 97))  # [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
# =============================================================================

# %% best practise
    
import numpy as np

def reorder(a, b):
    return np.roll(np.arange(a).reshape(2, -1), b, 1).tolist()

# =============================================================================
# print(reorder(10, 1))   # [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]]
# print(reorder(10, 3))   # [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]]
# print(reorder(10, 97))  # [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]]
# =============================================================================










