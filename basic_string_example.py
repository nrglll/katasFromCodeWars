# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:29:17 2020

@author: Nurgul Aygun
"""

# =============================================================================
# Kata explanation:
# Write simple .camelCase method (camel_case function in PHP, CamelCase 
# in C# or camelCase in Java) for strings. All words must have their first 
# letter capitalized without spaces.
# 
# For instance:
# 
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord
# =============================================================================

def camel_case(string):
    return "".join(w.capitalize() for w in string.split())
    
# =============================================================================
# print(camel_case("hello case")) # HelloCase
# print(camel_case("camel case word")) # CamelCaseWord
# =============================================================================
