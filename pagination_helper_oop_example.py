# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:11:29 2020

@author: Nurgul Aygun
"""


# =============================================================================
# Kata explanation:
# For this exercise you will be strengthening your page-fu mastery. You will
# complete the PaginationHelper class, which is a utility class helpful for 
# querying paging information related to an array.
# 
# The class is designed to take in an array of values and an integer 
# indicating how many items will be allowed per each page. The types of values
#  contained within the collection/array are not relevant.
# 
# The following are some examples of how this class is used:
# 
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count # should == 2
# helper.item_count # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid
# 
# # page_ndex takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative ind
# =============================================================================
    
# TODO: complete this class

import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page      
      self.number_of_pages = math.ceil(len(collection)/items_per_page)
      
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
      
  
  # returns the number of pages
  def page_count(self):
      return self.number_of_pages
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      
      if page_index >= 0 and page_index <= (self.number_of_pages-1):
    
        if page_index == (self.number_of_pages-1):
            return len(self.collection) % self.items_per_page
        else:
            return self.items_per_page
        
      else:
          return -1
      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      
      if len(self.collection) > 0 and (len(self.collection)-1) >= item_index:
          
          if item_index > 0:
              return (math.ceil(item_index/self.items_per_page)-1)
          elif item_index == 0:
              return 0
          else:
              return -1
          
      else: 
          return -1
      
# =============================================================================
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# =============================================================================


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
