'''
Fastest Route to Databricks HQ
You live in San Francisco city and want to minimize your commute time to the Databricks HQ.
Given a 2D matrix of the San Francisco grid and the time as well as cost matrix of all the available transportation
modes, return the fastest mode of transportation. If there are multiple such modes then return one with the least cost.
Rules:
1. The input grid represents the city blocks, so the commuter is only allowed to travel along the horizontal and vertical axes.
Diagonal traversal is not permitted.
2. The commuter can only move to the neighboring cells with the same transportation mode.
Sample Input:
2D Grid:              Legend:
|3|3|S|2|X|X|         X = Roadblock
|3|1|1|2|X|2|         S = Source
|3|1|1|2|2|2|         D = Destination
|3|1|1|1|D|3|         1 = Walk, 2 = Bike, 3 = Car, 4 = Train
|3|3|3|3|3|4|
|4|4|4|4|4|4|
Transportation Modes:        ["Walk", "Bike", "Car", "Train"]
Cost Matrix (Dollars/Block): [0,      1,      3,     2]
Time Matrix (Minutes/Block): [3,      2,      1,     1]
NOTE: In this example, we are only counting the blocks between 'S' and 'D' to compute the minimum time & dollar cost.
Sample Output: Bike
*/
/*
walk:  minTime, dollar ?
[0,2], [1,2], .... [3,4] 4 steps minTime: 4 * 3 = 12, cost: 4 * 0 = 0
bike: [0,2], [0,3], ... 4 stpes.  minTime: 4 * 2 = 8, cost: 4 * 1 =4
car:  ...
train: ...
for each transportation:
  bfs to find num of blocks
  if cannot reach to desti, ignore this type
  els:
    update minTime, minCost
o(m*n) time
o(m*n) space
   0 1 2 3 4 5
0 |3|3|S|2|X|X|
1 |3|1|1|2|X|2|
2 |3|1|1|2|2|2|
3 |3|1‍‌‌‍‌‍‍‍‍‍‌‍‌‌‌‌‌‌|1|1|D|3|
4 |3|3|3|3|3|4|
5 |4|4|4|4|4|4|
grid = {
  {'3', '3', 'S', '2', 'X', 'X'},
  {'3', '1', '1', '2', 'X', '2'},
  {'3', '1', '1', '2', '2', '2'},
  {'3', '1', '1', '1', 'D', '3'},
  {'3', '3', '3', '3', '3', '4'},
  {'4', '4', '4', '4', '4', '4'}
};
cost_matrix = {0, 1, 3, 2};
time_matrix = {3, 2, 1, 1};

'''

from ast import mod
from collections import deque

class Solution:
  def shortestPath(self, grid):
    m = len(grid)
    n = len(grid[0])
    start = []
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 'S':
          start = [i ,j]
    
    res = []  # [[time, cost, mode], [] ]
    map = {
      '1': [0, 3],  # cost, time
      '2': [1, 2],
      '3': [3, 1],
      '4': [2, 1]
    }
    for mode in ['1', '2', '3', '4']:
      visit = [[False for _ in range(n)] for _ in range(m)]
      dis = self.bfs(grid, m, n, visit, start[0], start[1], mode)
      print('dis', dis)
      if dis > 0:
        time = map[mode][1] * dis
        cost = map[mode][0] * dis
        res.append([time, cost, mode])

    res.sort()
    print(res[0])
    print(res)
  
  def bfs(self, grid, m, n, visit, i, j, mode):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dis = 0
    # init
    queue = deque([])
    queue.append([i, j])
    visit[i][j] = True
    
    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        # print(curr)
        x, y = curr

        if grid[x][y] == 'D':
          return dis

        # terminate
        for dx, dy in dir:
          x2 = dx + x
          y2 = dy + y
          if 0 <= x2 < m and 0 <= y2 < n:
            if  grid[x2][y2] == 'D':
              return dis + 1
            if grid[x2][y2] == mode and not visit[x2][y2]:
              visit[x2][y2] = True
              queue.append([x2, y2])
      dis += 1

    return -1

sol = Solution()
grid = [
  ['3', '3', 'S', '2', 'X', 'X'],
  ['3', '1', '1', '2', 'X', '2'],
  ['3', '1', '1', '2', '2', '2'],
  ['3', '1', '1', '1', 'D', '3'],
  ['3', '3', '3', '3', '3', '4'],
  ['4', '4', '4', '4', '4', '4']
]
sol.shortestPath(grid)
