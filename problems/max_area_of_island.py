from typing import List


DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
    m = len(grid)
    n = len(grid[0])
    maxarea = 0
    
    for r in range(m):
      for c in range(n):
        if grid[r][c] == 1:
          self.cnt = 0
          self.dfs(grid, r, c)
          maxarea = max(maxarea, self.cnt)
  
    return maxarea

  def dfs(self, grid, x, y):
    # base case

    # recursive rule
    self.cnt += 1
    grid[x][y] = 0

    for dir in DIRS:
      dx, dy = dir
      x2 = dx + x
      y2 = dy + y

      if self.isValid(x2, y2, grid) and grid[x2][y2] == 1:
        self.dfs(grid, x2, y2)

  def isValid(self, x, y, grid):
    return  0<= x < len(grid) and 0 <= y < len(grid[0])