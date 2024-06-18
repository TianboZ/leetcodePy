"""
solution:
run BFS
inital condition: all rot oranges

time: O(M*N)
space: O(M*N)
"""
from collections import deque
import queue
from typing import List

ROT = 2
FRESH = 1
EMPTY = 0
DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    queue = deque([])
    m = len(grid)
    n = len(grid[0])
    freshCnt = 0
    # inital, add all rot oranges to queue
    for i in range(m):
      for j in range(n):
        if grid[i][j] == ROT:
          queue.append([i, j])
        if grid[i][j] == FRESH:
          freshCnt += 1
    
    level = 0

    # sanity check
    if freshCnt == 0:
      return 0
    
    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        curr = queue.popleft()
        x, y = curr

        for dx, dy in DIR:
          x2 = x + dx
          y2 = y + dy
          if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n:
            if grid[x2][y2] == FRESH:
              grid[x2][y2] = ROT
              queue.append([x2, y2])
              freshCnt -= -1
      level += 1 
    
    if freshCnt > 0:
      return -1
    
    return level - 1 

