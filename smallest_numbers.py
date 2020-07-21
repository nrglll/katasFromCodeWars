# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:33:16 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Create a function that returns the sum of the two lowest positive numbers 
# given an array of minimum 4 positive integers. No floats or non-positive 
# integers will be passed.
# 
# For example, when an array is passed like [19, 5, 42, 2, 77], 
# the output should be 7.
# 
# [10, 343445353, 3453445, 3453545353453] should return 3453455.
# =============================================================================

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
    
# =============================================================================
# print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
# =============================================================================
