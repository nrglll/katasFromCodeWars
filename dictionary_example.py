# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:58:27 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
# 
# >>> d = Dictionary()
# 
# >>> d.newentry('Apple', 'A fruit that grows on trees')
# 
# >>> print(d.look('Apple'))
# A fruit that grows on trees
# 
# >>> print(d.look('Banana'))
# Can't find entry for Banana
# =============================================================================

class Dictionary():
    def __init__(self):
        self.dictionary = dict()
        
    def newentry(self, word, definition):
        self.dictionary[word] = definition
        
    def look(self, key):
        return self.dictionary.get(key, "Can't find entry for %s" %key)
        
d = Dictionary()

# =============================================================================
# d.newentry('Apple', 'A fruit that grows on trees')
# print(d.look('Apple'))    # A fruit that grows on trees
# print(d.look('Banana'))   # Can't find entry for Banana
# =============================================================================
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
