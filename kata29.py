# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:14:30 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
#     
# You need to write regex that will validate a password to make sure it 
# meets the following criteria:
# 
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.
# =============================================================================

#%% regular expression


regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"

# =============================================================================
# (
#     '^'            # start line
#     '(?=.*\d)'     # must contain one digit from 0-9
#     '(?=.*[a-z])'  # must contain one lowercase characters
#     '(?=.*[A-Z])'  # must contain one uppercase characters
#     '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
#     '{6,}'         # length at least 6 chars
#     '$'            # end line
# )
# 
# =============================================================================









































