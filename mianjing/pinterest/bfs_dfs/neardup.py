"""
https://leetcode.com/discuss/interview-question/1593622/Pinterest-or-Phone-Screen-or-MLE

We have a neardup pipeline at Pinterest, which produces a mapping from every image to a list of up to k near-duplicate images, such as:
near_dups = {
"A": ["B", "I", "K"],
"B": ["A", "D"],
"C": ["E"],
"D": [],
"E": [],
"F": [],
"G": ["K"],
"I": [],
"K": [],
}
Given a mapping such as this one, form neardup clusters: collections of almost identical images.
In the example above, we would form the following groups: (A, B, D, I, G, K), (C, E), and (F).**

solution:
- build graph, undirected
- DFS traverse, find connected area

"""

graph = {
  "A": ["B", "I", "K"],
  "B": ["A", "D"],
  "C": ["E"],
  "D": [],
  "E": [],
  "F": [],
  "G": ["K"],
  "I": [],
  "K": [],
}

from collections import defaultdict
class Solution:
  def findConnectedClusters(self, graph):
    # build graph
    adj = defaultdict(set)
    for k, v in graph.items():
      print(k, v)
      if k not in adj:
        adj[k] = set()
      for nei in v:
        adj[k].add(nei)
        adj[nei].add(k)
    print(adj)

    # DFS traverse
    cnt = 0
    nodes = adj.keys()
    visit = set()
    for n in nodes:
      if n not in visit:
        path = []
        self.dfs(n, visit, adj, path)
        cnt += 1      
        print(path)
    print(cnt)
    
  def dfs(self, node, visit, adj, path):
    # base case
    if node in visit:
      return
    
    # recursive rule
    visit.add(node)
    path.append(node)
    for nei in adj.get(node):
      self.dfs(nei, visit, adj, path)
      
sol = Solution()
sol.findConnectedClusters(graph)
  