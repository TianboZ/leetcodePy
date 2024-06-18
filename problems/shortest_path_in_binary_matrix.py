"""
solution:
run BFS from top-left, target node is bottom-right
time: O(V + E) = O(N^2)
space: O(V)

"""
from typing import List


DIR = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    # sanity check
    if not grid:
      return -1
    if grid[0][0] != 0:
      return -1

    n = len(grid)
    queue = deque([])
    visit = [[False for _ in range(n)] for _ in range(n)]
    level = 0
    
    # initial
    queue.append([0, 0])
    visit[0][0] = True

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        x, y = curr

        if x == n - 1 and y == n - 1:
          return level + 1

        # generate
        for dx, dy in DIR:
          x2 = x + dx
          y2 = y + dy

          if 0<= x2 < n and 0<= y2 < n and grid[x2][y2] == 0 and not visit[x2][y2]:
            visit[x2][y2] = True
            queue.append([x2, y2])

      level += 1  
    
    return -1
        