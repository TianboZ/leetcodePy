from typing import List


dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]

class Solution:
  def numDistinctIslands(self, grid: List[List[int]]) -> int:
    m =  len(grid) 
    n =  len(grid[0])
    visit = set()
    
    res = set()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1 and (i, j) not in visit:
          path = []
          self.dfs(i, j, i, j, grid, visit, path)
          print(''.join(path))
          res.add(''.join(path))
    
    return len(res)
  
  # r0, c0 is initial pos
  def dfs(self, r0, c0, r, c, grid, visit, path):
    # base case
    
    # recursive rule
    visit.add((r, c))
    path.append(str(r-r0) + ',' + str(c - c0) + '/')
    for dr, dc in dirs:
      r2 = r + dr
      c2 = c + dc
      if self.isValid(r2, c2, grid) and (r2, c2) not in visit and grid[r2][c2] == 1:
        self.dfs(r0, c0, r2, c2, grid, visit, path)

  def isValid(self, r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])      