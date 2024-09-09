from collections import deque
from typing import List

# BFS
class Solution(object):
  def numIslands(self, grid):
    """
    input: char[][] grid
    return: int
    """
    # write your solution here
    # sanity check
    if not grid or len(grid) == 0: 
      return 0
    
    m = len(grid)
    n = len(grid[0])
    cnt = 0 # cound connected areas
    visit = set()

    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1" and (i, j) not in visit:
          cnt += 1
          self.bfs(grid, visit, i, j, m, n)

    return cnt

  def bfs(self, grid, visit, i, j, m, n):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([])

    # inital
    queue.append([i, j])
    visit.add((i, j))

    # terminate
    while queue:
      # expand 
      curr = queue.popleft()
      i1, j1 = curr

      # generate
      for dx, dy in dir:
        i2 = i1 + dx
        j2 = j1 + dy
        if 0 <= i2 < m and 0<= j2 < n and (i2, j2) not in visit and grid[i2][j2] == "1":
          visit.add((i2, j2))
          queue.append([i2, j2])

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# DFS
class Solution2:
  def numIslands(self, grid: List[List[str]]) -> int:
    visit = set()
    m = len(grid)
    n = len(grid[0])
    cnt = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1' and (i, j) not in visit:
          self.dfs(i, j , grid, visit)
          cnt+=1
    return cnt
  
  def dfs(self, i, j, grid, visit):
    if (i, j) in visit:
      return
    
    visit.add((i, j))
    for dx, dy in dirs:
      i2 = i + dx
      j2 = j + dy
      if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] == '1':
        self.dfs(i2, j2, grid, visit)
