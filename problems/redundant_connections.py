import collections
from typing import List

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    adj = collections.defaultdict(set)
    
    for a, b in edges:
      visit = set()
      if a in adj and b in adj:
        if self.dfs(a, b, visit, adj):
          return [a, b]
      adj[a].add(b)  
      adj[b].add(a)  
    
    return []
  
  # return true if find target
  def dfs(self, node, target, visit, adj)->bool:
    if node in visit:
      return False
    
    visit.add(node)
    if node == target:
      return True
    
    for nei in adj.get(node, []):
      if self.dfs(nei, target, visit, adj):
        return True
    
    return False
        