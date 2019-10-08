# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    i = 0
    j = 1
    substringsList = []
    for letter in s:
        if j == (len(s)):
            j += 1
            substringsList.append(s[i:j])
        elif s[j] == letter and j != len(s):
            substringsList.append(s[i:j])
            i = j
        
        j += 1
    return len(max(substringsList, key=len))
        

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10