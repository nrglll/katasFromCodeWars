# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:18:02 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# 
# Tower block is represented as *
# 
# Python: return a list;
# JavaScript: returns an Array;
# C#: returns a string[];
# PHP: returns an array;
# C++: returns a vector<string>;
# Haskell: returns a [String];
# Ruby: returns an Array;
# Lua: returns a Table;
# Have fun!
# 
# for example, a tower of 3 floors looks like below
# 
# [
#   '  *  ', 
#   ' *** ', 
#   '*****'
# ]
# and a tower of 6 floors looks like below
# 
# [
#   '     *     ', 
#   '    ***    ', 
#   '   *****   ', 
#   '  *******  ', 
#   ' ********* ', 
#   '***********'
# ]
# 
# =============================================================================

def tower_builder(n_floors):
    final_list = []
    space_number = n_floors -1
    for n in range(1, n_floors+1):
        final_list.append((" "*(space_number) + "*"*(2*n-1) + " "*(space_number)))
        space_number += -1
        
    return final_list

# =============================================================================
# print(tower_builder(5))
# =============================================================================

































