'''
solution:
1. for each E, run BFS to find shortest path to all empty cell, record the value 
2. for each empty cell, if it can be reached from all E, then calculate the sum, find global smallest value 
  2.1 cost matrix is 2D array, each cell is [cost1, cost2, ...]
  2.2 iterante cost matrix find smallest one with total cost

complexity:
m is matrx row; n is matrix column; e is # of equip

time: O(m*n*e)
space: O(m*n)

'''
from collections import deque
from math import e
class Solution(object):
  E = 'E'
  C = 'C'
  O = 'O'

  def putChair(self, gym):
    """
    input: char[][] gym
    return: Integer[]
    """
    # write your solution here
    m = len(gym)
    n = len(gym[0])
    e_cnt = 0
    res = [-1, -1]
    min_cost = 1000000
    
    # cost matrix
    cost_matrix = [[[] for i in range(n)] for j in range(m)] # each cell is array of cost that from differernt E[]
    
    # count total E
    for i in range(m):
      for j in range(n):
        if gym[i][j] == self.E:
          e_cnt += 1
          self.bfs(i, j, m, n, gym, cost_matrix)
        
    # find global smallest cost cell
    for i in range(m):
      for j in range(n):
        costs = cost_matrix[i][j]
        if len(costs) == e_cnt and e_cnt > 0:
          if sum(costs) < min_cost:
            min_cost = sum(costs)
            res = [i ,j]

    return res
  
  def bfs(self, i, j, m, n, gym, cost_matrix):
    dir = ((1, 0), (-1, 0), (0, 1), (0, -1))
    queue = deque([])
    visit = set()

    # initial
    queue.append([i, j])
    visit.add(str([i, j])) # mark visit
    dis = 0

    # terminate
    while queue:
      size = len(queue)
      
      for i in range(size):
        # expand
        i1, j1 = queue.popleft()
        if gym[i1][j1] == self.C:
          cost_matrix[i1][j1].append(dis)

        # generate
        for dx, dy in dir:
          i2 = i1 + dx
          j2 = j1 + dy
          
          if i2 < 0 or i2 == m or j2 < 0 or j2 == n:
            continue
          
          if str([i2, j2]) in visit: 
            continue
          
          if gym[i2][j2] == self.C or gym[i2][j2] == self.E:
            queue.append([i2, j2])
            visit.add(str([i2, j2]))

      dis += 1
      

# test 
sol = Solution()
gym = [['E', 'O', 'C'], ['C', 'E', 'C'], ['C', 'C', 'C']]
res = sol.putChair(gym)
print(res)