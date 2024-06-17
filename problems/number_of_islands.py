from collections import deque
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
    visit = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1" and not visit[i][j]:
          cnt += 1
          self.bfs(grid, visit, i, j, m, n)

    return cnt

  def bfs(self, grid, visit, i, j, m, n):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([])

    # inital
    queue.append([i, j])
    visit[i][j] = True

    # terminate
    while queue:
      # expand 
      curr = queue.popleft()
      i1, j1 = curr

      # generate
      for dx, dy in dir:
        i2 = i1 + dx
        j2 = j1 + dy
        if i2 >= 0 and i2 < m and j2 >= 0 and j2 < n and not visit[i2][j2] and grid[i2][j2] == "1":
          visit[i2][j2] = True
          queue.append([i2, j2])
    


