# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:02:41 2020

@author: asus
"""

def to_jaden_case(string):
    return " ".join(w.capitalize() for w in string.split())
    

a = to_jaden_case("Ali ata bak.")
print(a)
