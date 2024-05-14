from typing import List
from collections import deque

class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    visit = {}
    for node in range(len(graph)):
      if not node in visit: # easy goes wrong!
        res = self.dfs(node, graph, 1, visit)
        if not res:
          return False
        
    print(visit)
    return True
  
  # return false if not bipartite
  def dfs(self, curr, graph, color, visit):
    #  base case
    if visit.get(curr):
      return color == visit.get(curr)

    #  recursive rule
    visit[curr] = color
    for nei in graph[curr]:
      res = self.dfs(nei, graph, color * -1, visit)
      if not res: 
        return False
    
    return True

  # BFS
  def isBipartite2(self, graph: List[List[int]]) -> bool:
    visit = {}
    for node in range(len(graph)):
      if not node in visit:
        if not self.bfs(node, graph, visit, 1): 
          return False
    return True  
    
  # BFS traverse graph, mark color. if not bipartite, return false
  def bfs(self, curr, graph, visit, color):
    node = visit.get(curr)
    if node:
      return node == color

    q = deque([])
    q.append(curr)
    
    while not q:
      size = len(q)
      for i in range(size):
        tmp = q.popleft()
        visit[tmp] = color

        for nei in graph[tmp]:
          if visit[nei] and visit[nei] != color * -1:
            return False
          q.append(nei)

    return True  


  
# test
graph = [[1,3],[0,2],[1,3],[0,2]]
sol = Solution()
res = sol.isBipartite2(graph)
print(res)
