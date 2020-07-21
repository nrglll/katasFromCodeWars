# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:48:00 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata Explanation:
# There is enough money available on ATM in nominal value 10, 20, 50, 
# 100, 200 and 500 dollars.
# 
# You are given money in nominal value of n with 1<=n<=1500.
# 
# Try to find minimal number of notes that must be used to repay in dollars, 
# or output -1 if it is impossible.
# =============================================================================

def solve(n):
    money = [500, 200, 100, 50, 20, 10]
    notes = 0
    if n <= 1500 and n > 0 and n%10 == 0:
        for i in money: 
            notes += int(n/i)
            n = n%i
        return notes
    else: return -1
    
# =============================================================================
# print(solve(770))
# =============================================================================
