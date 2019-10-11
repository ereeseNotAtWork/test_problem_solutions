#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.
"""

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    start_index = -1
    end_index = -1
    counter = 0
    for value in arr:
        if value == x:
            if start_index == -1:
                start_index = counter
        elif value != x and start_index >= 0 and end_index == -1:
            end_index = counter - 1
        counter += 1
    return [start_index, end_index]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]