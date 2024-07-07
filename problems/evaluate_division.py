"""
solution:
a -> b -> c
  2     3  

a  <-  b  <-  c
   1/2   1/3

- build graph
- BFS traverse graph, src is equation[0], target node is equation[1]

"""

class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj = {}
    self.getAdj(equations, adj, values)
    print(adj)
    res = []
    
    for q in queries:
      ans = (self.bfs(q[0], q[1], adj))
      print(ans)
      res.append(ans)
    return res

  def bfs(self, src, target, adj):
    if src not in adj or target not in adj:
      # can not finish calucale
      return -1
    
    # initialize
    queue = deque([ [src, 1] ])  # node is [node, current cost to this node]
    visit = set()
    visit.add(src)

    # terminate
    while queue:
      # expand 
      curr = queue.popleft()
      n, cost = curr

      if n == target:
        return cost
      
      # generate
      for nei in adj.get(n, []):
        n2, cost2 = nei
        if n2 in visit:
          continue
        queue.append([n2, cost2 * cost])
        visit.add(n2)

    return -1
  
  def getAdj(self, e, adj, values):
    for i in range(len(e)):
      a, b = e[i]
      v = values[i]
      if a not in adj:
        adj[a] = [[b, v]]
      else:
        adj[a].append([b, v])

      if b not in adj:
        adj[b] = [[a, 1/v]]
      else:
        adj[b].append([a, 1/v])

    