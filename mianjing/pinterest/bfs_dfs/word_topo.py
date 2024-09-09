"""
given 
["a>b", "b>c", "c>d"]

"""

import collections


class Solution:
  def findWord(self, arr):
    # build graph
    adj = collections.defaultdict(set)
    for ele in arr:
      c1, c2 = ele.split(">")
      print(c1, c2)   # a>b  c1>c2  ->  c2: c1 means c2 depends on c1
      adj[c2].add(c1)
      if c1 not in adj:
        adj[c1] = set()
    print(adj)

    # topo order
    nodes = adj.keys()
    visit = {}  # key: node, value: status  1 == visiting  2 == visited
    path = []
    for n in nodes:
      if n not in visit:
        if self.dfs(n, adj, visit, path):
          print('cycle!')
          return ''
    print(path)
    
  # topo order, return True if cycle
  def dfs(self, node, adj, visit, path)->bool:
    # baes case
    if visit.get(node) == 1:
      return True
    if visit.get(node) == 2:
      return False
    
    # recursive rule
    visit[node] = 1
    for nei in adj.get(node, []):
      if self.dfs(nei, adj, visit, path):
        return True
    visit[node] = 2
    path.append(node)
    return False



# test
sol = Solution()
words = ['g>r', 'r>e', 'e>a', 'a>t']
sol.findWord(words)