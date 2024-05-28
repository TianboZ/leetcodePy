'''
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
'''

from typing import List


class Solution:
  #Function to detect cycle in a directed graph.
  def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
    visit = {} # <node: status>   1: visiting, 2: visited
    for n in range(V):
      if n not in visit and self.dfs(n, visit, adj):
        return True
    return False
  
  def dfs(self, node, visit, adj):
    # base case
    if visit.get(node) == 1:
      return True
    if visit.get(node) == 2:
      return False
    
    visit[node] = 1
    for nei in adj[node]:
      if self.dfs(nei, visit, adj):
        return True
    visit[node] = 2
    return False

