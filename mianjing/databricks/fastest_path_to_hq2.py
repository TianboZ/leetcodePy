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
#                            ["Walk", "Bike", "Car", "Train"]
# Cost Matrix (Dollars/Block): [0,      1,      3,     2]
# Time Matrix (Minutes/Block): [3,      2,      1,     1]
# 1 = Walk, 2 = Bike, 3 = Car, 4 = Train


from collections import deque
from unittest import result


cost = {
  '1': [0, 3], # [cost, time]
  '2': [1, 2],
  '3': [3, 1],
  '4': [2, 1]
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
  def findTranspotation(self, grid):
    modes = ['1', '2', '3', '4']
    results = [] # []
    for mode in modes:
      res = self.bfs(mode, grid)
      print(res)
      if res == -1:
        continue
      results.append([cost[mode][1] * res, cost[mode][0] * res, mode])
    
    results.sort()
    print(results)
    print('fatest transpotation is:', results[0][2], 'cost is:', results[0][1])
    return results[0][2]

  def bfs(self, mode, grid):
    m = len(grid)
    n = len(grid[0])
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # find start point
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 'S':
          start = [i, j]
    
    visit = [[ False for _ in range(n)] for _ in range(m)]
    queue = deque([])

    # init
    dis = 0
    i = start[0]
    j = start[1]
    visit[i][j] = True
    queue.append([i, j])

    # terminate
    while queue:
      size = len(queue)
      for _ in range(size):
        # expand 
        x, y = queue.popleft()
        if grid[x][y] == 'D':
          return dis - 1

        # generate
        for dx, dy in dir:
          x2 = x + dx
          y2 = y + dy

          if 0 <= x2 < m and 0 <= y2 < n and not visit[x2][y2]:
            if grid[x2][y2] == mode or grid[x2][y2] == 'D':
              queue.append([x2, y2])
              visit[x2][y2] = True

      dis += 1  

    return -1


sol = Solution()
sol.findTranspotation(grid)