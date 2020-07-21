# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:52:52 2020

@author: Nurgul Aygun
"""

# =============================================================================
# Kata Explanation:
# Create a function which accepts one arbitrary string as an argument, and 
# return a string of length 26.
# 
# The objective is to set each of the 26 characters of the output string to 
# either '1' or '0' based on the fact whether the Nth letter of the alphabet 
# is present in the input (independent of its case).
# 
# So if an 'a' or an 'A' appears anywhere in the input string (any number of 
# times), set the first character of the output string to '1', otherwise to 
# '0'. if 'b' or 'B' appears in the string, set the second character to '1', 
# and so on for the rest of the alphabet.
# 
# For instance:
# 
# "a   **&  cZ"  =>  "10100000000000000000000001"
# =============================================================================
import string
   
def change(st):
    st_list = list(i for i in st.lower())
    alp = string.ascii_lowercase
    for i in alp:
        if i in st_list:
            alp = alp.replace(i, "1")
        else:
            alp = alp.replace(i, "0")
    return alp


# =============================================================================
# print(change("a   **&  cZ")) # answer should be "10100000000000000000000001"
# =============================================================================


















