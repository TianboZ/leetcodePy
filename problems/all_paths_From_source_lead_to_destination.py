'''
solution1:
based on DFS3, find all paths
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


solution2:
based on DFS2, find all reachable nodes

time
O(V + E)

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


class Solution2:
  def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adj = {}
    self.getGraph2(adj, edges)
    visit = {} # node: status     1: visiting.  2: visited
    return self.dfs2(source, visit, destination, adj)

  # return true if from node, all paths lead to dst
  def dfs2(self, node, visit: dict, dst, adj: dict)->bool:  
    # base case
    if visit.get(node) == 1: # detect cycle
      return False 

    if visit.get(node) == 2: # visited
      return True
    
    # leaf node
    neis = adj.get(node, [])
    if not neis:
      return node == dst

    # recursive rule
    visit[node] = 1
    
    for nei in neis:
      res = self.dfs2(nei, visit, dst, adj)
      if not res: return False

    visit[node] = 2
    return True
  
  def getGraph2(self, adj: dict, edges):
    for a, b in edges:
      neis = adj.get(a, [])
      neis.append(b)
      adj[a] = neis

sol = Solution2()
res = sol.leadsToDestination(4, [[0,1],[1,1]], 0, 1)
print(res)