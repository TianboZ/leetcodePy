"""
solution:
DFS find all path, TLE

complexity:
branch = 4
level = m * n

time O(brancn^level) = O(4 ^ (m*n))
space O(m * n)
"""
from collections import deque
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
solution2:
BFS
新思想 !!! each state is combination of (row, col) and blocks used 

"""

class Solution2:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    # init
    visit = set()
    queue = deque([(0, 0, 0)])  # (row, col, blocks)
    visit.add((0, 0, 0)) # (row, col, blocks)  !!! each state is combination of (row, col) and blocks used 
    dis = 0
    
    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand 
        curr = queue.popleft()
        r, c, blocks = curr

        # hit dst
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
          print(dis)
          return dis

        # generate
        for dir in dirs:
          dr, dc = dir
          r2 = dr + r
          c2 = dc + c
          if self.isValid(r2, c2, grid):
            # if block
            if grid[r2][c2] == 1 and blocks < k and (r2, c2, blocks + 1) not in visit:
              queue.append((r2, c2, blocks + 1))
              visit.add((r2, c2, blocks + 1))
            
            # not block
            elif grid[r2][c2] == 0 and (r2, c2, blocks) not in visit:
              queue.append((r2, c2, blocks))
              visit.add((r2, c2, blocks))
      dis += 1  

    return -1
        
  def isValid(self, i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])
  

  
