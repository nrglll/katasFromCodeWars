# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:50:22 2020

@author: Nurgul Aygun
"""
# =============================================================================
# Kata explanation:
# You know how sometimes you write the the same word twice in a sentence, 
# but then don't notice that it happened? For example, you've been distracted 
# for a second. Did you notice that *"the"* is doubled in the first sentence 
# of this description?
# 
# As as aS you can see, it's not easy to spot those errors, especially if 
# words differ in case, like *"as"* at the beginning of the sentence.
# 
# Write a function that counts the number of sections repeating the same 
# word (case insensitive). The occurence of two or more equal words next 
# after each other count as one.
# 
# Example:
# 
# "dog cat"                 --> 0
# "dog DOG cat"             --> 1
# "apple dog cat"           --> 0
# "pineapple apple dog cat" --> 0
# "apple     apple dog cat" --> 1
# "apple dog apple dog cat" --> 0
# "dog dog DOG dog dog dog" --> 1
# "dog dog dog dog cat cat" --> 2
# "cat cat dog dog cat cat" --> 3
# =============================================================================
def count_adjacent_pairs(st): 
    words = st.split()
    repeat = 0
    check = list()
    for i in range(0,len(words)-1):
        if words[i].lower() in check: pass
        else:
            check *=0 #clear elements in list but not change list type. If I use .clear() it change type as NoneType.
            if words[i].lower() == words[i+1].lower():
                repeat = repeat +1
                check.append(words[i].lower())
    return repeat

        

# =============================================================================
# print(count_adjacent_pairs("dog cat"))                   #--> 0
# print(count_adjacent_pairs("dog DOG cat"))               #--> 1
# print(count_adjacent_pairs("apple dog cat"))             #--> 0
# print(count_adjacent_pairs("pineapple apple dog cat"))   #--> 0
# print(count_adjacent_pairs("apple     apple dog cat"))   #--> 1
# print(count_adjacent_pairs("apple dog apple dog cat"))   #--> 0
# print(count_adjacent_pairs("dog dog DOG dog dog dog"))   #--> 1
# print(count_adjacent_pairs("dog dog dog dog cat cat"))   #--> 2
# print(count_adjacent_pairs("cat cat dog dog cat cat"))   #--> 3
# =============================================================================
















































