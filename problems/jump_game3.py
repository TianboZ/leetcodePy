from typing import List


class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    self.found = False
    visit = set()
    self.dfs(start, arr, visit)
    
    return self.found
  
  def dfs(self, i, arr, visit):
    # base case
    if self.found:
      return 
    if i < 0 or i >= len(arr):
      return 
    if i in visit:
      return

    # recursive rule
    if arr[i] == 0:
      self.found = True
      return 

    visit.add(i)
    left = i - arr[i]
    self.dfs(left, arr, visit)
    right = i + arr[i]
    self.dfs(right, arr, visit)
    visit.remove(i)

        