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
      seen = set()
      graph = self.get_graph(edges)
      return self.dfs(source, destination, seen, graph)

    def get_graph(self, edges: List[List[int]]):
      graph = {}
      for n1, n2 in edges:
        if graph.get(n1):
          graph.get(n1).append(n2)
        else:
          graph[n1] = [n2]
        
        if graph.get(n2):
          graph.get(n2).append(n1)
        else:
          graph[n2] = [n1]
      
      return graph

    def dfs(self, curr, end, seen, graph):
      # basecase
      if curr == end: 
        return True
      if curr in seen:
        return False

      # recursive rule
      seen.add(curr)
      for nei in graph.get(curr):
        res = self.dfs(nei, end, seen, graph)
        if res: 
          return True
      return False

    
sol = Solution()
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
sol.validPath(3, edges, source, destination)