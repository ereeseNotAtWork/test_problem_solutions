#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:00:39 2019

@author: evanreese
"""

class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
      i = 0
      j = 1
      palindromeList = []
      for i in range(0,len(s)):
          jstart = i+1
          for j in range(jstart,len(s)+1):
              checkString = s[i:j]
              if checkString == checkString[::-1]:
                  palindromeList.append(checkString)
      return max(palindromeList, key=len)
  
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar