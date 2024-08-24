"""
soluiton:
- build reversed graph
- for each node, run DFS to find all ancestor 

complexity:
n is # of nodes, m is edges array length

- time 
build graph: O(m)
DFS traverse graph: O(V + E) = O(n + m)
total = m +  n * (n + m) = m + n^2 + mn = O(m*n + n^2)

- space
build graph: O(m + n)


"""
import collections
class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    adj = collections.defaultdict(list)
    res = []
    
    # build reversed graph
    for e in edges:
      a, b = e
      adj[b].append(a)
    
    # iterate each node
    for node in range(n):
      orders = []  # need to remove last one
      visit = set()
      self.dfs(node, adj, visit, orders)
      # print(orders)
      orders.pop()
      orders.sort()
      res.append(orders)

    return res
  def dfs(self, node, adj, visit, orders):
    # base case
    if node in visit:
      return

    # recursive rule
    visit.add(node)
    for nei in adj.get(node, []):
      self.dfs(nei, adj, visit, orders)
    
    orders.append(node)