from typing import List


class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    adj = {}
    self.getGraph(adj, edges)
    visit = set()
    cnt = 0
    for node in range(n):
      if node not in visit:
        self.dfs(node, adj, visit)
        cnt += 1
    return cnt
  
  def dfs(self, node, adj, visit):
    # base case
    if node in visit:
      return
    
    # recursive rule
    visit.add(node)
    for nei in adj.get(node, []):
      self.dfs(nei, adj, visit)

  def getGraph(self, adj, edges):
    for e in edges:
      a, b = e
      if a in adj:
        adj.get(a).append(b)
      else:
        adj[a] = [b]
      if b in adj:
        adj.get(b).append(a)
      else:
        adj[b] = [a]