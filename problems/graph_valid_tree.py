"""
a undirected graph is tree when
1. E = V - 1
2. connnected
3. no cycle

any 2 cases satisfy, it is a tree
"""

from typing import List

class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    adj = {}
    self.getGraph(adj, edges)
    cnt = 0 # connected areas
    visit = set()
    
    for node in range(n):
      if node not in visit:
        if self.checkCycle(node, None, adj, visit):
          return False
        else:
          cnt += 1
          if cnt > 1:
            return False  
      
    return True
  
  # return True if has cycle
  def checkCycle(self, node, prev, adj, visit: set):
    # base case
    if node in visit:
      return True

    # recursive rule
    visit.add(node)
    for nei in adj.get(node, []):
      if nei != prev and self.checkCycle(nei, node, adj, visit):
        return True
      
    return False

  def getGraph(self, adj, edges):
    for e in edges:
      a, b = e
      neis = adj.get(a, [])
      neis.append(b)
      adj[a] = neis

      neis = adj.get(b, [])
      neis.append(a)
      adj[b] = neis





