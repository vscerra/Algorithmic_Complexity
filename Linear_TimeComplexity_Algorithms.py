# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:18:31 2023

@author: vscerra
"""
# These are some examples of common algorithms with time complexity of O(n) in 
# the worst case scenario. 

# For each of these, the space complexity is O(1) or 
# O(k) as written (k <= n), as additional space is only needed to hold i, 
# element, and target in memory at any given time, and does not scale with the 
# size of the input


# Finding an element in an unsorted list

my_list = [3, 1, 4, -1, 5, 9, 2, 6, 5, 3, 5]
target_element = 3

# This implementation searches and returns the first occurrence of the target element in the array

def linear_search(arr, target):
  for i, element in enumerate(arr):
    if element == target:
      return i
  return -1

position_of_target = linear_search(my_list, target_element)
print(f'The position of {target_element} is {position_of_target}')

# if you wanted to search for all occurrences of a target element in an array instead of only the first one

def linear_search_all(arr, target):
  positions = []
  for i,element in enumerate(arr):
    if element == target:
      positions.append(i)
  return positions if positions else -1

positions_of_targets = linear_search_all(my_list, target_element)
print(f'The positions of all occurrences of {target_element} are {positions_of_targets}')


# Finding minimum or maximum elements in an unsorted list

def find_minimum(arr):
  if not arr: 
    return None
  minimum = arr[0]
  for element in arr:
    if element < minimum:
      minimum = element
  return minimum

min_element = find_minimum(my_list)
print(f'The minimum element in my_list is {min_element}')

# How to count occurrences of an element in an unsorted list

def count_occurrences(arr, target):
  count = 0
  for i, element in enumerate(arr):
    if element == target:
      count +=1
  return count

occurrences = count_occurrences(my_list, target_element)
print(f'{target_element} occurs {occurrences} times in my_list')