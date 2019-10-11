#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Here is the function signature as a starting point (in Python):

"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    counter = 0
    carry_over = 0
    output = 0
    while l1:
        l1_val = l1.val
        l2_val = l2.val
        tmp = l1_val + l2_val + carry_over
        if tmp > 9:
            carry_over = 1
            output = tmp - 10
        elif tmp <= 9:
            carry_over = 0
            output = tmp
        if counter == 0:
            l3 = ListNode(output)
        elif counter == 1:
            l3.next = ListNode(output)
        elif counter == 2:
            l3.next.next = ListNode(output)
            
        l1 = l1.next
        l2 = l2.next
        counter += 1
    return l3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val),
  result = result.next
# 7 0 8