"""
solution:
DFS find all path

complexity:
branch = 4
level = m * n

time O(brancn^level) = O(4 ^ (m*n))
space O(m * n)
"""
from typing import List

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    self.k = k
    self.res = 1000
    
    # traverse grid, DFS
    visit = set()
    self.dfs(0, 0, grid, visit, 0, [])

    # result
    if self.res == 1000:
      return -1
    
    return self.res
  
  def dfs(self, i, j, grid, visit, obsCnt, path):
    # base case

    # recursive rule
    visit.add((i, j))
    path.append((i, j))
    
    # arrive dst 
    if i == len(grid) - 1 and  j == len(grid[0]) - 1:
      # print(path, len(path))
      self.res = min(self.res, len(path) - 1)
      visit.remove((i, j))
      path.pop()
      return

    for dir in dirs:
      dx, dy = dir
      i2 = i + dx
      j2 = j + dy
      if self.isValid(i2, j2, grid) and (i2, j2) not in visit: 
        if grid[i2][j2] == 1:
          # if obstacle
          if obsCnt < self.k:
            self.dfs(i2, j2, grid, visit, obsCnt + 1, path)
        else:
          self.dfs(i2, j2, grid, visit, obsCnt, path)

    visit.remove((i, j))
    path.pop()
        
  def isValid(self, i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])
  
  
  
  """
solution:
DFS find all path

complexity:
branch = 4
level = m * n

time O(brancn^level) = O(4 ^ (m*n))
space O(m * n)
"""

class Solution2:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
  
