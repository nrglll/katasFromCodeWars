# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:44:33 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# Move the first letter of each word to the end of it, then add "ay" to 
# the end of the word. Leave punctuation marks untouched.
# 
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# =============================================================================

import string

def pig_it(text):
    new_words = []
    for w in text.split():
        if w[::] not in string.punctuation:
            new_words += [w[1::] + w[0] + "ay"]
        else:
            new_words += w
    return " ".join(new_words)
      
    
# =============================================================================
# print(pig_it('Panem et circenses')) # anemPay teay ircensescay
# print(pig_it('Hello world !')) # elloHay orldway !
# =============================================================================
