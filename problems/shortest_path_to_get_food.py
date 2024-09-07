from collections import deque

class Solution:
  def getFood(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    visit = set()
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dis = 0
    queue = deque([])

    for r in range(m):
      for c in range(n):
        if grid[r][c] == '*':
          # init
          queue.append((r, c))
          visit.add((r, c))
        
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand 
        curr = queue.popleft()
        r, c = curr
        # print(curr)
        
        if grid[r][c] == '#':
          # find food
          return dis
        
        # generate
        for dir in dirs:
          dr, dc = dir
          r2 = r + dr
          c2 = c + dc

          if self.isValid(r2, c2, grid) and (r2, c2) not in visit:
            if grid[r2][c2] == 'O' or grid[r2][c2] =='#':
              visit.add((r2, c2))
              queue.append((r2, c2))
      dis += 1

    # not reachable to food
    return -1

  def isValid(self, r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])