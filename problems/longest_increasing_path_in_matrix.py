"""
solution:
complexity:
time: O(V + E) = O(m * n)
space O(m * n)
"""
from typing import List


dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    res = 1
    self.cache = {}
    for i in range(m):
      for j in range(n):
        visit = set()
        longest = self.dfs(i, j, matrix, visit)
        print(longest)
        res = max(res, longest)
    
    return res

  # return longest increasing path from [i, j] position
  def dfs(self, r, c, grid, visit)->int:
    # base case
    if (r, c) in self.cache:
      return self.cache[(r, c)]
    
    if (r, c) in visit:
      return 

    # recursive rule
    visit.add((r, c))
    localmax = 0
    for dx, dy in dirs:
      r2 = r + dx
      c2 = c + dy

      if self.isValid(r2, c2, grid) and (r2, c2) not in visit and grid[r2][c2] > grid[r][c]:
        longest = self.dfs(r2, c2, grid, visit)
        localmax = max(localmax, longest)
    visit.remove((r, c))
    self.cache[(r, c)] = 1 + localmax
    return 1 + localmax

  def isValid(self, i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])
    