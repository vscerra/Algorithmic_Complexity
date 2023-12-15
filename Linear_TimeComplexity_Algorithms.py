# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:18:31 2023

@author: vscerra
"""
# These are some examples of common algorithms with a maximum time complexity of O(n)

#%% Linear Search

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

#%% Counting sort 

# Counting sort is a non-comparison based algorithm that's useful when the 
# input is known and relatively small

# In all below count_sorting cases, the space complexity is defined by the size 
# of the `count` variable, and ranges from n (size of input) to k (size of maximum value of arr) 
# leaving each with a space complexity of O(k)


# Sorting non-negative integers
def counting_sort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)
  for num in arr:
    count[num] += 1
  
  sorted_arr = []
  for i in range(len(count)):
    sorted_arr.extend([i] * count[i])
  
  return sorted_arr


my_list = [4, 2, 3, 1, 0, 4, 6, 1, 2, 5, 6]
sorted_list = counting_sort(my_list)
print(f'Original list is {my_list}')
print(f'Sorted by value, the list is now {sorted_list}')

# Example: Sort students by test score 
class Student: 
  def __init__(self, name, score):
    self.name = name
    self.score = score


def counting_sort_students(students):
  max_score = max(student.score for student in students)
  count = [0] * (max_score + 1)
  
  for student in students:
    count[student.score] += 1
  
  # Calculate the cumulative count
  for i in range(1, len(count)):
    count[i] += count[i-1]
    
  # Create the sorted array
  sorted_students = [None] * len(students)
  for student in reversed(students):
    index = count[student.score] - 1
    sorted_students[index] = student
    count[student.score] -= 1
  
  return sorted_students

students = [Student("Olive",100), Student("Newton", 95), Student("Nala", 89), Student("Marisol", 92), Student("Charles", 64), Student("Hajun", 85), Student("Roger", 57), Student("Dharm", 75)]
sorted_students = counting_sort_students(students)
print("Sorted students by score:")
for student in sorted_students:
    print(f"{student.name}: {student.score}")
    
   
# Sorting Characters in a string
# Given a string, sort the letters using a counting sort

def counting_sort_string(input_str):
  max_char = ord(max(input_str))
  count = [0] * (max_char + 1)
  
  for char in input_str:
    count[ord(char)] += 1
    
    sorted_str = ""
    for char in range(len(count)):
      sorted_str += chr(char) * count[char]
      
  return sorted_str

my_string = 'Veronica Emily Scerra'
sorted_string = counting_sort_string(my_string.lower())

print(f"Original string: {my_string}")
print(f"Sorted string: {sorted_string}")

#%% Merge Sort

# Merge sort algorithms sort arrays into ascending order

# Example 1, given an array, return that array in ascending order by splitting 
# into two halves, then working through both halves to create a sorted array

def merge_sort(arr):
    if len(arr) <= 1:
      return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else: 
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage:
my_list = [0, 4, 2, 3, 3, 5, 6, 9]

sorted_list = merge_sort(my_list)
print(f"Original array: {my_list}")
print(f"Sorted array: {sorted_list}")

# Example 2 Given an array, count how many inversions are necessary to sort the array

def count_inversions(arr):
  if len(arr) <= 1:
    return arr, 0
  
  mid = len(arr) // 2
  left, inv_left = count_inversions(arr[:mid])
  right, inv_right = count_inversions(arr[mid:])
  merged, inv_merged = merge_and_count(left, right)
  total_inversions = inv_left + inv_right + inv_merged
  return merged, total_inversions

def merge_and_count(left, right):
  result = []
  i = j = inversions = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else: 
      result.append(right[j])
      inversions += len(left) - i
      j += 1
      
  result.extend(left[i:])
  result.extend(right[j:])
  return result, inversions

# Example usage: 
my_list = [1, 0, 3, 0, 4, 2, 2, 6]
sorted_list, inversions = count_inversions(my_list)

print(f'Original array: {my_list}')
print(f'Sorted array: {sorted_list}')
print(f'Number of inversions necessary to sort list: {inversions}')

