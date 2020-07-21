# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:36:47 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# You probably know the "like" system from Facebook and other pages. People can
# "like" blog posts, pictures or other items. We want to create the text that should 
# be displayed next to such an item.
# 
# Implement a function likes :: [String] -> String, which must take in input array, 
# containing the names of people who like an item. It must return 
# the display text as shown in the examples:
# 
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in and 2 others simply increases.
# =============================================================================


def likes(names):
    l = len(names)
    if l == 1: return "{} likes this".format(names[0])
    elif l == 2: return "{} and {} like this".format(names[0], names[1])
    elif l == 3: return "{}, {} and {} like this".format(names[0], names[1], names[2])
    elif l > 3:  return "{}, {} and {} others like this".format(names[0], names[1], (l-2))
    else: return "no one likes this"

# =============================================================================
# print(likes(["elif", "ahmet", "mehmet", "veli"]))
# =============================================================================

        
        
