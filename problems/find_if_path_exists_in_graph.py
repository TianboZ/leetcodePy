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
import collections
class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    visit = set()
    
    # build adj graph
    adj = collections.defaultdict(list)
    for a, b in edges:
      adj[a].append(b)
      adj[b].append(a)
    
    # tarverse graph
    return self.dfs(source, destination, visit, adj)


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