# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:37:52 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# You are given a secret message you need to decipher. Here are the things 
# you need to know to decipher it:
# 
# For each word:
# 
# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces
# 
# Examples
# 
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'
# =============================================================================

import string

def decipher_this(text):
    deciphered_text = []
    for w in text.split():
        ascii_number = int(w.rstrip(string.ascii_letters))
        w = w.replace(str(ascii_number), chr(ascii_number))
        
        i = list(w)
        
        if len(i) <= 2:
            deciphered_text.append(w)
            
        else:
            i[1], i[-1] = i[-1], i[1]
            deciphered_text.append("".join(i))
            
    return " ".join(deciphered_text)
            

# =============================================================================
# print(decipher_this('72olle 103doo 100ya'))        
# print(decipher_this('72o'))     
# print(decipher_this('100'))       
# =============================================================================
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
