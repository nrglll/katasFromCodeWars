# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:52:07 2020

@author: Nurgul Aygun
"""

# =============================================================================
# Kata explanation:
# Take an input string and return a string that is made up of the 
# number of occurences of each english letter in the input followed 
# by that letter, sorted alphabetically. The output string shouldn't 
# contain chars missing from input (chars with 0 occurence); leave them out.
# 
# An empty string, or one with no letters, should return an empty string.
# 
# Notes:
# 
# the input will always be valid;
# treat letters as case-insensitive
# Examples
# "This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
# ""                          ==>  ""
# "555"                       ==>  ""
# =============================================================================
# 1013 ms

def string_letter_count(s):
    final = []
    if s == "":
        return ""
    else:    
        for i in sorted(list(s.lower())):
             if i.isalpha() and i not in final:
                    n=1
                    final.append(str(n))
                    final.append(i)
             elif i.isalpha() and i in final: 
                    n = n +1
                    final[-2] = str(n)
        return "".join(final)



# =============================================================================
# print(string_letter_count("This is a test sentence.")) # "1a1c4e1h2i2n4s4t"
# =============================================================================


# %% refactor version 910 ms

def string_letter_count(s):
    return "".join(str(s.count(i.lower()) + s.count(i.upper()))+i for i in sorted(set(s.lower())) if i.isalpha())


# =============================================================================
# print(string_letter_count("This is a test sentence.")) # "1a1c4e1h2i2n4s4t"
# =============================================================================













