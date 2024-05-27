from collections import deque

class Solution(object):
  def putChair(self, gym):
    """
    input: char[][] gym
    return: Integer[]
    """
    # write your solution here
    m = len(gym)
    n = len(gym[0])
    costmatrix = [[[] for _ in range(n) ] for _ in range(m)]
    ecnt = 0 # E count
    mincost = 1000000
    res = [-1, -1]

    for i in range(m):
      for j in range(n):
        if gym[i][j] == 'E':
          self.bfs(i, j, m, n, gym, costmatrix)
          ecnt += 1

    for i in range(m):
      for j in range(n):
        if ecnt == len(costmatrix[i][j]):
          cost  = sum(costmatrix[i][j])
          if cost < mincost:
            mincost = cost
            res = [i, j]
    
    return res

  def bfs(self, i, j, m, n, gym, costmatrix):
    dir = [(1, 0), (-1, 0), (0 ,1), (0, -1)]
    queue = deque([])
    visit =  [[False for _ in range(n) ] for _ in range(m)]
    print(1)
    print(visit)
    print(2)
    # initial
    queue.append([i, j])
    visit[i][j] = True
    dis = 0

    while queue:
      size = len(queue)
      for _ in range(size):
        # expand
        curr = queue.popleft()
        i1, j1 = curr
        print('curr', curr)
        costmatrix[i1][j1].append(dis)
        
        # generate
        for dx, dy in dir:
          i2 = i1 + dx
          j2 = j1 + dy

          if i2 < 0 or i2 == m or j2 < 0 or j2 == n:
            continue
          
          print('new cor', i2, j2, 'm, n', m, n)
          if not visit[i2][j2]:
            queue.append([i2, j2])
            visit[i2][j2] = True
      
      dis += 1


sol = Solution(
)
gym2 = [['E', '', ''], ['', 'E', ''], ['', '', 'E']]
gym = [[["E","E"," ","E","E"],["E"," ","E","E"," "],[" ","E"," "," ","E"],["E"," "," ","E"," "],["E"," "," "," ","E"]]]
res = sol.putChair(gym2)
# print(res)