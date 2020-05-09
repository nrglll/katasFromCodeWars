# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:45:41 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# You are given an array (which will have a length of at least 3, 
# but could be very large) containing integers. The array is either entirely 
# comprised of odd integers or entirely comprised of even integers 
# except for a single integer N. Write a method that takes the array as 
# an argument and returns this "outlier" N.
# =============================================================================

def find_outlier(integers):
    o = list(i for i in integers if i%2 != 0) 
    e = list(i for i in integers if i%2 == 0)       
    if len(o) == 1:
        return o[0]
    elif len(e) == 1: 
        return e[0]
   