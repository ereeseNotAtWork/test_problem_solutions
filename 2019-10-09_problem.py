# -*- coding: utf-8 -*-
"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""

class Solution:
  def isValid(self, s):
    parenStackList = []
    parenList = ['(', ')', '{', '}', '[', ']']

    for char in s:
        if char in parenList:
            charIndex = parenList.index(char)
            if charIndex in [0, 2, 4]:
                parenStackList.append(char)
            else:
                if charIndex == 1:
                    matchIndex = 0
                elif charIndex == 3:
                    matchIndex = 2
                elif charIndex == 5:
                    matchIndex = 4

                if len(parenStackList) > 0 and parenStackList[-1] == parenList[matchIndex]:
                    parenStackList.remove(parenStackList[-1])
                elif len(parenStackList) > 0 and parenStackList[-1] != matchIndex:
                    return False
                
    if len(parenStackList) == 0:
        return True
    else:
        return False
        

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))