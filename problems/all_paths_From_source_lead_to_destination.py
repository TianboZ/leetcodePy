'''
solution:
find all paths from src, check the end node is target

optimization:
graph like this, can use memo for node 4
    1
  /  \
  2   3
  \  /
   4       
/ \ \ \
5 6  7 8
...

complexity:
time
worst case: O(branch ^ level) = O(V ^ V)

space
O(V)



'''

from typing import List

class Solution:
  def leadsToDestination(
    self, n: int, edges: List[List[int]], source: int, destination: int
  ) -> bool:
    visit = set()
    adj = {}
    path = []
    self.getGraph(adj, edges)
    memo = {}
    return self.dfs(source, adj, visit, destination, memo)

  def getGraph(self, adj, edges):
    for a, b in edges:
      if adj.get(a):
        adj[a].append(b)
      else:
        adj[a] = [b]
    
  # return false if end node !== target
  def dfs(self, node, adj, visit, target, memo)->bool:
    # basecase
    if node in visit:
      return False # cycle! 
    
    if node not in adj or len(adj.get(node, [])) == 0:
      # reach end
      return node == target

    if node in memo:
      return memo.get(node)
    
    # recursive rule
    visit.add(node)
    for nei in adj.get(node, []):
      if not self.dfs(nei, adj, visit, target, memo):
        memo[nei] = True
        return False
    visit.remove(node)
    memo[node] = True
    return True


sol = Solution()
res = sol.leadsToDestination(4, [[0,1],[1,1]], 0, 1)
print(res)