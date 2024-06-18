from typing import List

'''
solution:
DFS to find target node
graph traversal 

compleixty:
V: # of nodes
E: # of edges

time
O(V + E)

space
1. graph: O(V + E)
2. recursion: O(V)
3. visited array: O(V)
4. total: O(V + E)

'''

class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    visit = set()
    adj = {}
    graph = self.getGraph(edges, adj)
    return self.dfs(source, destination, visit, graph)

  def getGraph(self, edges: List[List[int]], adj):
    for n1, n2 in edges:
      if adj.get(n1):
        adj.get(n1).append(n2)
      else:
        adj[n1] = [n2]
      
      if adj.get(n2):
        adj.get(n2).append(n1)
      else:
        adj[n2] = [n1]
    
    return adj

  # return true if find the node
  def dfs(self, curr, end, visit, graph)->bool:
    # basecase
    if curr == end: 
      return True
    if curr in visit:
      return False

    # recursive rule
    visit.add(curr)
    for nei in graph.get(curr):
      res = self.dfs(nei, end, visit, graph)
      if res: 
        return True
    return False

    
sol = Solution()
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
sol.validPath(3, edges, source, destination)