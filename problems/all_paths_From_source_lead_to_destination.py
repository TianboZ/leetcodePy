'''
solution:
if has cycle, return false
since could have cycle, creat a hashset to record what nodes have been visited


'''

from typing import List


class Solution:
  def leadsToDestination(
    self, n: int, edges: List[List[int]], source: int, destination: int
  ) -> bool:
    visit = set()
    adj = {}
    self.getGraph(adj, edges)
    return self.dfs(source, adj, visit, destination)

  def getGraph(self, adj, edges):
    for a, b in edges:
      if adj.get(a):
        adj[a].append(b)
      else:
        adj[a] = [b]
    
  # return false if can't reach to target
  def dfs(self, node, adj, visit, target):
    # basecase
    if node in visit:
      return False

    if node not in adj:
      return False

    # recursive rule
    visit.add(node)
    for nei in adj.get(node):
      if not self.dfs(nei, adj, visit, target):
        return False
    visit.remove(node)
    return True

sol = Solution()
res = sol.leadsToDestination(4, [[0,1],[1,1]], 0, 1)
print(res)