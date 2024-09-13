"""
solution:
- run DFS, find one island, get all 1's position, say there are N positions
- run BFS, initial state N position, find shortest path to another island 
"""
from collections import deque
from typing import List

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def shortestBridge(self, grid: List[List[int]]) -> int:
    pos = []
    m = len(grid)
    n = len(grid[0])
    visit = set()
    pos = []
    
    flag = False
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1 and (i, j) and not flag:
          self.dfs(i, j, grid, visit, pos)
          flag = True
    
    # print(pos)
    
    res = self.bfs(pos, grid)
    # print(res)
    return res
    
  def bfs(self, pos, grid):
    # init
    queue = deque(pos)
    visit = set()
    dis = 0
    for p in pos:
      visit.add(p)
      
    # terminate 
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand 
        curr = queue.popleft()
        r, c = curr
        
        # generate
        for dr, dc in dirs:
          r2 = dr + r
          c2 = dc + c
          if self.isValid(r2, c2, grid) and (r2, c2) not in visit:
            if grid[r2][c2] == 0:
              queue.append((r2, c2))
              visit.add((r2, c2))
            if grid[r2][c2] == 1:
              return dis
        
      dis += 1
    
    return -1
  
  def dfs(self, r, c, grid, visit, pos):
    # base case
    
    # print(r, c)
    # recursive rule
    visit.add((r, c))
    pos.append((r, c))
    for dr, dc in dirs:
      r2 = dr + r
      c2 = dc + c
      if self.isValid(r2, c2, grid) and (r2, c2) not in visit and grid[r2][c2] == 1:
        self.dfs(r2, c2, grid, visit, pos)
    
  def isValid(self, r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
  
sol = Solution()
grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
sol.shortestBridge(grid)