dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
from collections import deque

"""
DFS3
find all paths

time O(b^level)  = (4^(m*n))

TLE
"""
class Solution1:
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    self.dst = (destination[0], destination[1])
    visit = set()
    self.res = 10000
    self.dfs(start[0], start[1], maze, visit, 0)
    # build ans
    if self.res == 10000:
      return -1
    return self.res
  
  def dfs(self, r, c, maze, visit, cost):
    # base case

    # recursive rule
    # print((r, c))
    if (r, c) == self.dst:
      # print('cost: ', cost)
      self.res = min(self.res, cost)
      return
    
    visit.add((r,c))
    for dir in dirs:
      dr, dc = dir
      r2 = r
      c2 = c
      dis = 0
      # find next pos
      while self.isValid(r2 + dr, c2 + dc, maze) and maze[r2 + dr][c2 + dc] == 0:
        r2 += dr
        c2 += dc
        dis += 1
      if self.isValid(r2, c2, maze) and (r2, c2) not in visit:
        self.dfs(r2, c2, maze, visit, cost + dis)
    visit.remove((r, c))

  def isValid(self, r, c, maze):
    return  0<= r < len(maze) and 0 <= c < len(maze[0])


"""
dija

"""
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

from collections import deque
import heapq

class Solution2:
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    dst = (destination[0], destination[1])
    visit = {}  # key: (row, col). value: min cost
    
    # init
    minheap = [[0, start[0], start[1]]] # [cost from src, row, col]
    visit[(start[0], start[1])] = 0

    # terminate
    while minheap:
      print(1)
      # expand
      curr = heapq.heappop(minheap)
      cost, r, c = curr

      if (r, c) == dst:
        print(r, c, cost)
        return cost

      # generate
      for dr, dc in dirs:
        r2 = r
        c2 = c
        dis = 0
        while self.isValid(r2 + dr, c2 + dc, maze) and maze[r2 + dr][c2 + dc] == 0:
          r2 += dr
          c2 += dc
          dis += 1
        
        if not self.isValid(r2, c2, maze):
          continue

        costSum = dis + cost
        
        if (r2, c2) not in visit or costSum < visit[(r2, c2)]:
          visit[(r2, c2)] = costSum
          heapq.heappush(minheap, [costSum, r2, c2])
    return -1
  
  def isValid(self, r, c, maze):
    return  0<= r < len(maze) and 0 <= c < len(maze[0])