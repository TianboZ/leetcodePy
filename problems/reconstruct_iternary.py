"""
solution:
N = cities count
run DFS, depth limited to N, find all path
DFS terminate conditons: N round, all cities have visited

detail
1. build graph
2. DFS

complexity:
time: O(b ^ l) = O(N ^ N) 
space:O(N)
"""

from typing import List


class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    adj = {}
    self.getGraph(adj, tickets)
    path = []
    ans = []
    self.dfs('JFK', adj, path, len(tickets) + 1, ans)
    return ans[0]

  def dfs(self, node, adj, path, length, ans):
    # base case
    if ans:
      return    
    
    # recursive rule
    path.append(node)

    if len(path) == length:
      if not ans:
        ans.append(path.copy())
      return  

    neis = adj.get(node, [])
    for i, nei in enumerate(neis):
      if nei:
        ori = neis[i]
        neis[i] = '' # mark the path as visited
        self.dfs(nei, adj, path, length, ans)
        neis[i] = ori
    path.pop()

  def getGraph(self, adj, tickets):
    for t in tickets:
      src, end = t
      if src in adj:
        adj.get(src).append(end)
      else:
        neis = [end]
        adj[src] = neis
    for k, v in adj.items():
      v.sort()

# test
sol = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res = sol.findItinerary(tickets)
print(res)
