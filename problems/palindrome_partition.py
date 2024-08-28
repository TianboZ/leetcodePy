"""
soluiton:

recursion tree, for each index, 2 options, cut or not cut. if cut, check str[preCutIdx, currCutInx] if is palindrome

            a b b
            /\      
           a|bb     

           /   \
        a|b|b   a|bb



complexity:
n is string length

time O( n * 2^n)
space O(n)
"""
from typing import List


class Solution:
  def partition(self, s: str) -> List[List[str]]:
    path = [-1]
    res = []
    self.ans = []
    self.dfs(0, s, path, res)
    
    return self.ans
  # path records all cut index, i is index of string, res is array of substring
  def dfs(self, i, s, path, res):
    # base case
    if i == len(s):
      if path[-1] == len(s) - 1:
        # print(res)
        self.ans.append(list(res))
      return

    # recursive rule
    # case 1: cut at i
    prevIdx = path[-1] + 1
    # print('prevIdx:', prevIdx, 'i:', i)
    sub = s[prevIdx: i+1]
    # print(sub)
    if self.isP(sub):
      path.append(i)
      res.append(sub)
      self.dfs(i + 1, s, path, res)
      path.pop()
      res.pop()

    # case 2: not cut at i
    self.dfs(i + 1, s, path, res)

  def isP(self, s):
    return s == s[::-1]
        
        
# better, cleaner
class Solution2:
  def partition(self, s: str) -> List[List[str]]:
    cuts = [0]   # e.g. [0, 2, 4, .]  means substring[0, 1] and substring[2, 4]
    path = []
    self.ans = []
    self.dfs(0, s, cuts, path)
    
    return self.ans
  # path records all cuts index, i is index of string, path is array of substring
  def dfs(self, i, s, cuts, path):
    # print('i:',i)
    # baes case
    if i == len(s):
      # print('111')
      # print(cuts, path)
      self.ans.append(list(path))
      return

    # recursive rule
    prev = cuts[-1]
    for j in range(prev + 1, len(s) + 1):
      sub = s[prev:j]
      if not self.isP(sub):
        continue
      
      # print(sub)
      cuts.append(j)
      path.append(sub)
      self.dfs(j, s, cuts, path)
      cuts.pop()
      path.pop()

  def isP(self, s):
    return s == s[::-1]
      