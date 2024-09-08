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

from collections import defaultdict
class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    self.total = len(tickets) + 1
    
    # build graph
    adj = defaultdict(list)
    for a, b in tickets:
      adj[a].append(b)
    for [k, v] in adj.items():
      v.sort()

    # build ans
    self.ans = None
    self.dfs('JFK', adj, [])
    return self.ans

  def dfs(self, node, adj, path):
    # base case
    if self.ans:
      return
        
    if not node:
      return

    # recursive rule
    path.append(node)

    if len(path) == self.total:
      print(path)
      self.ans = list(path)
      path.pop()
      return

    neis = adj.get(node, [])
    for i in range(len(neis)):
      nei = neis[i]
      if not nei:
        continue

      next = nei
      neis[i] = ''  # mark this ticket used
      self.dfs(next, adj, path)
      neis[i] = next # back tracking

    path.pop()

# test
sol = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res = sol.findItinerary(tickets)
print(res)
