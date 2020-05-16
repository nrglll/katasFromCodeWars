# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:38:29 2020

@author: Nurgul Aygun
"""

# ============================================================================= 
# Kata explanation:
# Write a function that when given a URL as a string, parses out just the 
# domain name and returns it as a string. For example:
# 
# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
# =============================================================================

def domain_name(url):
    
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

# =============================================================================
# print(domain_name("http://google.co.jp"))
# print(domain_name("https://www.zombie-bites.com"))
# =============================================================================
