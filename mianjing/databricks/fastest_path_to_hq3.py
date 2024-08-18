"""

10:57 - 11:22  

solution:
- bfs from start node
- each time take only one transporation
  - try all 4 differernt way

complexity:
time o(m * n)   m*n is grid size
space o(m * n)


"""

#                            ["Walk", "Bike", "Car", "Train"]
# Cost Matrix (Dollars/Block): [0,      1,      3,     2]
# Time Matrix (Minutes/Block): [3,      2,      1,     1]
# 1 = Walk, 2 = Bike, 3 = Car, 4 = Train

from collections import deque

cost = {
  '1': [3, 0], # [ time, cost]
  '2': [2, 1],
  '3': [1, 3],
  '4': [1, 2] 
}

grid = [
  ['3', '3', 'S', '2', 'X', 'X'],
  ['3', '1', '1', '2', 'X', '2'],
  ['3', '1', '1', '2', '2', '2'],
  ['3', '1', '1', '1', 'D', '3'],
  ['3', '3', '3', '3', '3', '4'],
  ['4', '4', '4', '4', '4', '4']
]

class Solution:
  def shortestPath(self, grid):
    m = len(grid)
    n = len(grid[0])
    x = -1
    y = -1

    # find start
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 'S':
          x = i
          y = j

    res = []
    for type in ['1', '2', '3' , '4']:
      dis = self.bfs(x, y, grid, type)
      print('type: ', type , 'dis: ', dis)
      if dis >= 0:
        time = cost[type][0] * dis
        _cost = cost[type][1] * dis
        res.append([ time, _cost, type ])

    # find min time type, if time same, compare cost
    res.sort()
    print(res)

  def bfs(self, i, j, grid, type):
    m = len(grid)
    n = len(grid[0])
    dirs = [ [1, 0],    [-1, 0],   [0, 1],   [0, -1] ]
    queue = deque([])
    visit = [[False for _ in range(n)] for _ in range(m)]
    
    # init bfs
    queue.append([i, j])
    visit[i][j] = True
    dis = 0

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand 
        curr = queue.popleft()
        x, y = curr

        # generate 
        for dir in dirs:
          dx, dy = dir
          x2 = x + dx
          y2 = y + dy

          if self.isValid(x2, y2, grid) and not visit[x2][y2]:
            if  grid[x2][y2] == type:
              queue.append([x2, y2])
              visit[x2][y2] = True
            if  grid[x2][y2] == 'D':
              return dis
      dis += 1  

    return -1

  def isValid(self, i, j, grid):
    m = len(grid)
    n = len(grid[0])
    return 0 <= i < m and 0 <= j < n
  
sol = Solution()
sol.shortestPath(grid)