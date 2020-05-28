# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:25:21 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Write a method that takes one argument as name and then greets that name, 
# capitalized and ends with an exclamation point.
# 
# Example:
# 
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"
# =============================================================================


def greet(name): 
    return "Hello " + "".join(name.split()).title() + "!"

# =============================================================================
# print(greet("nurgul"))
# =============================================================================
