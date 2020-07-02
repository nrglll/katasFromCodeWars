# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:01:50 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# The number 45 is the first integer in having this interesting property: 
#     the sum of the number with its reversed is divisible by the difference 
#     between them(absolute Value).
# 
# 45 + 54 = 99 
# abs(45 - 54) = 9
# 99 is divisible by 9.
# The first terms of this special sequence are :
# 
# n        a(n)
# 1        45
# 2        54
# 3        495
# 4        594
# Make the function sum_dif_rev()(sumDivRef in JavaScript and CoffeeScript), 
# that receives n, the ordinal number of the term and may give us, the value 
# of the term of the sequence.
# 
# sum_dif_rev(n) -----> a(n)
# Let's see some cases:
# 
# sum_dif_rev(1) -----> 45
# sum_dif_rev(3) -----> 495
# Important: All the integers that its reversed has leading zeroes should be 
# discarded: ex: 1890 its reversed is 981 ("0981")
# 
# Your code will be tested up to the first 65 terms, so you should think to 
# optimize it as much as you can.
# 
# (Hint: I memoize, you memoize, he memoizes, ......they (of course) memoize)
# 
# Happy coding!!
# =============================================================================

def memoize_sum_dif(f):
    memory = {}
    
    def inner(n):
        if n not in memory:
            memory[n] = f(n)
        return memory[n]
    return inner
    
    
@memoize_sum_dif
def sum_dif_rev(n):
    
    if n == 1: return 45
    
    num = sum_dif_rev(n-1)
    
    while True:
        num = num+1
        if str(num)[::-1][0] == "0" or abs(num - int(str(num)[::-1])) == 0 :
            continue
        if (num + int(str(num)[::-1]))%abs(num - int(str(num)[::-1])) == 0:
            break              
    return num

 
    
# =============================================================================
# print(sum_dif_rev(3))
# =============================================================================


























