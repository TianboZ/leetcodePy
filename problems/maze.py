dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

class Solution:
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    self.dst = (destination[0], destination[1])
    visit = set()
    self.found = False
    self.dfs(start[0], start[1], maze, visit)
    return self.found
  
  def dfs(self, r, c, maze, visit):
    # base case
    if self.found:
      return

    # recursive rule
    # print((r, c))
    if (r, c) == self.dst:
      # print(r, c)
      self.found = True
      return
    
    visit.add((r,c))
    for dir in dirs:
      dr, dc = dir
      r2 = r
      c2 = c
      # find next pos
      while self.isValid(r2 + dr, c2 + dc, maze) and maze[r2 + dr][c2 + dc] == 0:
        r2 += dr
        c2 += dc
      if self.isValid(r2, c2, maze) and (r2, c2) not in visit:
        self.dfs(r2, c2, maze, visit)
    visit.remove((r, c))

  def isValid(self, r, c, maze):
    return  0<= r < len(maze) and 0 <= c < len(maze[0])