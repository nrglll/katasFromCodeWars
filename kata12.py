# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:02:38 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# You have an array of numbers.
# Your task is to sort ascending odd numbers 
# but even numbers must be on their places.
# 
# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.
# 
# Example
# 
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
# =============================================================================

def sort_array(source_array):
    n = -1
    odd_list = sorted(list(o for o in source_array if not o %2 == 0))
    for index, item in enumerate(source_array):
        if not item %2 == 0:
            n += 1
            source_array[index] = odd_list[n]
    return source_array

# =============================================================================
# print(sort_array([5, 3, 2, 8, 1, 4]))  #should return [1, 3, 2, 8, 5, 4]
# =============================================================================

















