"""
solution:
topological sort problem
- build dependency graph
- for each node, run DFS(topo sort)
  - `visit` map to record each node status, key is node, value is status. e.g. 0=visiting, 1=visited
  - `depth` map to record each node max depth 

complexity:
time
n is # of nodes, m is edges 
O(n + m)

space
O(n + m)

"""
import collections
class Solution:
  def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    adj = collections.defaultdict(list)
    for a, b in relations:
      adj[b].append(a)

    visit = {}
    depth = {}
    self.res = -1
    
    for node in range(1, n + 1):
      if node not in visit:
        cycle, level = self.dfs(node, adj, visit, depth)
        if cycle:
          return -1
        
        self.res = max(self.res, level)
    # print(depth)
    return self.res
  
  # return ture if find cycle
  def dfs(self, node, adj, visit, depth)->[bool, int]:
    # base case
    if visit.get(node) == 0:
      return [True, 0]
    if visit.get(node) == 1:
      return [False, depth[node]]

    # recursive rule
    visit[node] = 0 # visiting
    localMax = 0
    for nei in adj.get(node, []):
      cycle, level = self.dfs(nei, adj, visit, depth)
      if cycle: 
        return [True, 0]
      localMax = max(localMax, level)

    visit[node] = 1 # visited
    depth[node] = localMax + 1
    return [False, localMax + 1]
        