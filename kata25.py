# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:41:40 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Step 1: Create a function called encode() to replace all the lowercase 
# vowels in a given string with numbers according to the following pattern:
# 
# a -> 1
# 
# e -> 2
# 
# i -> 3
# 
# o -> 4
# 
# u -> 5
# 
# For example, encode("hello") would return "h2ll4" There is no need to worry 
# about uppercase vowels in this kata.
# 
# Step 2: Now create a function called decode() to turn the numbers back into 
# vowels according to the same pattern shown above.
# 
# For example, decode("h3 th2r2") would return "hi there"
# 
# For the sake of simplicity, you can assume that any numbers passed into the 
# function will correspond to vowels.
# =============================================================================

vowels_list = ["a", "e", "i", "o", "u"]


def encode(st):
    for i in st:
        if i in vowels_list:
            st = st.replace(i, str(vowels_list.index(i) + 1))
    return st
    
def decode(st):
    for i in st:
        try:
            if int(i) < (len(vowels_list) +1) :
                st = st.replace(i, vowels_list[int(i)-1])
        except ValueError:
            pass
    return st

# =============================================================================
# print(encode("hello"))
# print(decode("h2ll4"))
# =============================================================================

# %% trans solution
    
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

# =============================================================================
# print(encode("hello"))
# print(decode("h2ll4"))
# =============================================================================











