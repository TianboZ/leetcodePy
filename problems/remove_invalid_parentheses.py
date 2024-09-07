"""
solution:
for each char, add or not add

complexity:
time O(2^n)
space O(N)
"""

class Solution:
  def removeInvalidParentheses(self, s: str) -> List[str]:
    path  = []
    self.res = set()
    self.size = 0
    self.dfs(0, s, 0, 0, path)
    # print(self.res)
    return list(self.res)
  
  # left: record ( count
  # right: record ) count 
  def dfs(self, i, s, left, right, path):
    # base case
    if i == len(s):
      if left == right:
        if left > self.size:
          # new global max
          self.size = left
          self.res.clear()
          self.res.add(''.join(path))
        elif left == self.size:
          self.res.add(''.join(path))
      return 

    # recursive rule
    c = s[i]

    # c is character
    if c != '(' and c != ')':
      path.append(c)
      self.dfs(i + 1, s, left, right, path)
      path.pop()
      return
    
    # case 1: keep c
    if c == '(':
      path.append(c)
      self.dfs(i + 1, s, left + 1, right, path)
      path.pop()
    else:
      # ')
      if left > right:
        path.append(c)
        self.dfs(i + 1, s, left, right + 1, path)
        path.pop()

    # case 2: not keep c
    self.dfs(i + 1, s, left, right, path)

        