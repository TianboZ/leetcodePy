from typing import List

"""
solution:
1. build graph. for each word, compare it with all words after it
2. run DFS to get topo order. if detect cycle, then no topo order


complexity:
time
N = # of words
M = avg length of word

1. build graph: O(N^2 * M)
2. topo: O(V + E)

space
"""
class Solution:
  def alienOrder(self, words: List[str]) -> str:
    adj = {}
    visit = {} # <node, state>  state=1: visiting  state=2: visited
    path = []

    # build graph
    if not self.getGraph(adj, words):
      return ""
    print(adj)
    chars = adj.keys()
    print(chars)
    
    # topo 
    for c in chars:
      if c not in visit:
        if not self.topo(c, adj, visit, path):
          return ""

    print(path)
    res = "".join(path)
    return res
  
  # return false if detect cycle
  def topo(self, node, adj, visit, path: list) -> bool:
    # base case
    if visit.get(node) == 1: 
      return False # cycle found
    if visit.get(node) == 2: 
      return True

    # recursive rule
    visit[node] = 1
    for nei in adj.get(node, []):
      if not self.topo(nei, adj, visit, path):
        return False

    visit[node] = 2
    path.append(node)
    return True

  def getGraph(self, adj: dict, words: list[str]) -> bool:
    n = len(words)

    for i in range(n):
      w1 = words[i]
      for char in w1:
        if char not in adj:
          adj[char] = []
      j = i + 1
      if j < n:
        w2 = words[j]
        # compare char in w1, w2
        k = 0
        while k < len(w1) and k < len(w2):
          if w1[k] == w2[k]:
            k += 1
          else:
            c1 = w1[k]
            c2 = w2[k]  # c2 -> c1, c2 depends on c1
            neis = adj.get(c2, [])
            neis.append(c1)
            adj[c2] = neis
            break
        if k == len(w2) and k < len(w1):
          return False
        
    return True


# test
words = ["wrt","wrf","er","ett","rftt"]
sol = Solution()
res = sol.alienOrder(words)
print(res)