# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:10:22 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# I thank yvonne-liu for the idea and for the example tests :)
# 
# Description:
# Encrypt this!
# 
# You want to create secret messages which can be deciphered by the Decipher 
# this! kata. Here are the conditions:
# 
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"
# =============================================================================

def encrypt_this(text):
    encrypted_text = []
    for i in text.split():
        w = i.strip()
        if len(w) == 0:
            return encrypted_text.append("")
        elif len(w) == 1:
            encrypted_text.append(str(ord(w[0])))
        elif len(w) == 2:
            encrypted_text.append(str(ord(w[0])) + w[-1])
        elif len(w) == 3:
            encrypted_text.append(str(ord(w[0])) + w[-1] +  w[1])
        else:
            encrypted_text.append(str(ord(w[0])) + w[-1] + w[2:-1] + w[1])
            
    return " ".join(encrypted_text)
        
# =============================================================================
# print(encrypt_this("Hello world"))
# print(encrypt_this(""))
# print(encrypt_this("A"))
# =============================================================================

# %% Second option (best)

def encrypt_this(text):
    encrypted_text = []
    
    for i in text.split():
        w = list(i)
        w[0] = str(ord(w[0]))
        if len(w) >2:
            w[1], w[-1] = w[-1], w[1]
        encrypted_text.append("".join(w))
    return " ".join(encrypted_text)
        
       
# =============================================================================
# print(encrypt_this("Hello world"))
# print(encrypt_this(""))
# print(encrypt_this("A"))
# =============================================================================












