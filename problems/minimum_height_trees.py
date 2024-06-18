from ast import Tuple
from collections import deque
from typing import Dict, List

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # sanity check
    if not edges: return [0]
    
    adj = {}
    self.getGraph(edges, adj)

    leaf, _ = self.bfs(0, adj)
    leaf2, map = self.bfs(leaf, adj)

    maxLevel = max(map.keys())
    # print(maxLevel)
    # print(map)
    res = []
    if maxLevel % 2 != 0:
      res.append(map[maxLevel // 2][0])
      res.append(map[maxLevel // 2 + 1][0])
    else:
      res.append(map[maxLevel // 2][0])

    print(res)
    res.sort()
    return res

  def bfs(self, node, adj)->tuple[int, dict]:
    visit = set()
    queue = deque([])
    level = 0
    leaf = None
    map = {}

    # initial
    queue.append(node)
    visit.add(node)

    # terminate
    while queue:
      size  = len(queue)
      for i in range(size):
        # expand
        curr  = queue.popleft()
        leaf = curr
        res = map.get(level, [])
        res.append(curr)
        map[level] = res
        # print(curr)
        
        # generate
        for nei in adj.get(curr, []):
          if nei not in visit:
            queue.append(nei)
            visit.add(nei)
      
      level += 1
      
    print(map)
    print(leaf)
    return [leaf, map]
  
  def getGraph(self, edges, adj):
    for e in edges:
      a, b = e
      neis = adj.get(a, [])
      neis.append(b)
      adj[a] = neis

      neis = adj.get(b, [])
      neis.append(a)
      adj[b] = neis

        

sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
sol.findMinHeightTrees(n, edges)