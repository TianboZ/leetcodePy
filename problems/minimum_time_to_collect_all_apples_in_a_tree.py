"""
solution:
it is a graph problem

1. build adj list
2. traverse graph

"""

class Solution:
  def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    adj = {}
    # build adj
    for a, b in edges:
      if a not in adj:
        adj[a] = [b]
      else:
        adj[a].append(b)
      if b not in adj:
        adj[b] = [a]
      else:
        adj[b].append(a)

    visit = set()
    res = self.dfs(0, hasApple, adj, visit, -1)
    
    return res
  
  # return time needed for root's subtree
  def dfs(self, root, hasApple, adj, visit, prev) -> int:
    if root in visit:
      return 0

    visit.add(root)  
    currTime = 0

    for nei in adj.get(root, []):
      if nei == prev: 
        continue

      neiTime = self.dfs(nei, hasApple, adj, visit, root)
      if neiTime: 
        currTime  += neiTime + 2
      elif hasApple[nei]:
        currTime += 2
      
    return currTime