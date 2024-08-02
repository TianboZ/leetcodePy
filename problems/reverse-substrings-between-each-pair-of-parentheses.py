"""
solution:
use stack 

complexity:
time O(n^2)
space O(n)
"""

class Solution:
  def reverseParentheses(self, s: str) -> str:
    stack = []
    for c in s:
      if c == ')':
        reverse = []
        while stack[-1] != '(':
          reverse.append(stack.pop())
        stack.pop() # pop (
        for r in reverse:
          stack.append(r)
      else:
        stack.append(c)
    # print(stack)
    return ''.join(stack)