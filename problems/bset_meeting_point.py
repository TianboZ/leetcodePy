from collections import deque
'''
solution:
1. for each home, run BFS, to find shortest path to all other cells
2. for each empty space, it stores array of distance from differernt people's home
3. find the smallest cell. total cost for that cell is: sum([d1, d2, d3....])

complexity
'''

class Solution(object):
  def minTotalDistance(self, grid):
    """
    input: int[][] grid
    return: int
    """
    # sanity check
    if not grid or not grid[0]: return 0
    
    m = len(grid)
    n = len(grid[0])
    res = []
    min_val = 10000
    home_cnt = 0
    costmatrix = [[ [] for _ in range(n)] for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          home_cnt += 1 
          self.bfs(i, j, grid, m, n, costmatrix)
    # find smallest sum
    for i in range(m):
      for j in range(n):
        costs = costmatrix[i][j]
        if costs and len(costs) == home_cnt:
          total = sum(costs)
          min_val = min(min_val, total)
    
    if min_val == 10000: return 0
    return min_val
    # write your solution here
  def bfs( self, i, j, grid, m, n, costmatrix):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit = [[False for _ in range(n)] for _ in range(m)]
    queue = deque([])
    dis = 0
    
    # initial 
    queue.append([i, j])
    visit[i][j] = True

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        i1 = curr[0]
        j1 = curr[1]
        costmatrix[i1][j1].append(dis)

        # generate
        for [dx, dy] in dir:
          i2 = dx + i1
          j2 = dy + j1

          if i2 < 0 or j2 < 0 or i2 == m or j2 == n:
            continue
          
          if not visit[i2][j2]:
            queue.append([i2, j2])
            visit[i2][j2] = True
      
      dis += 1
