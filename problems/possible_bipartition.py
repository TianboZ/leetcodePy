from collections import defaultdict

class Solution:
  def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    nodes = set()
    visit = {} # key: node, value: 1 or -1
    # build graph
    adj = defaultdict(set)
    for a, b in dislikes:
      adj[a].add(b)
      adj[b].add(a)
      nodes.add(a)
      nodes.add(b)

    # traverse graph
    for n in nodes:
      if n not in visit:
        if not self.dfs(n, adj, visit, 1):
          return False
    
    return True

  # if not bipartite, return False
  def dfs(self, node, adj, visit, flag):
    # base case
    if visit.get(node) == flag * -1:
      return False
    
    if visit.get(node) == flag:
      return True

    # recursive rule
    visit[node] = flag
    for nei in adj.get(node, []):
      if not self.dfs(nei, adj, visit, flag * -1):
        return False
    
    return True
