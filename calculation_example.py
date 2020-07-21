# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:16:07 2020

@author: Nurgul Aygun
"""

# =============================================================================
# Kata explanation:
# This time we want to write calculations using functions and get the results. 
# Let's have a look at some examples:
# 
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
# 
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: 
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner 
# function represents the right operand
# Divison should be integer division. For example, this should 
# return 2, not 2.666666...:
# eight(divided_by(three()))
# =============================================================================
      
def calc(x, y):
    if x[-1] == "+":
        return int(y + x[0]) 
    elif x[-1] == "-":
        return int(y - x[0])
    elif x[-1] == "*":
        return int(y * x[0])
    elif x[-1] == "/":
        return int(y / x[0])
    
def zero(n = None): 
    if n == None:
        return 0
    return calc(n, 0)
        
def one(n = None):
    if n == None:
        return 1
    return calc(n, 1)
       
def two(n = None): 
    if n == None:
        return 2
    return calc(n, 2)

def three(n = None):
    if n == None:
        return 3
    return calc(n, 3)

def four(n = None):  
    if n == None:
        return 4
    return calc(n, 4)

def five(n = None): 
    if n == None:
        return 5
    return calc(n, 5)

def six(n = None):  
    if n == None:
        return 6
    return calc(n, 6)

def seven(n = None): 
    if n == None:
        return 7
    return calc(n, 7)

def eight(n = None): 
    if n == None:
        return 8
    return calc(n, 8)

def nine(n = None):  
    if n == None:
        return 9
    return calc(n, 9)

def plus(a, b=None): return (a, "+") 
def minus(a, b=None): return (a, "-") 
def times(a, b=None): return (a, "*") 
def divided_by(a, b=None):  return (a, "/") 
    
# =============================================================================
# print(seven(times(five())))
# =============================================================================

    
    
    
    
    
    
