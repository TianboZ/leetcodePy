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
from collections import defaultdict
class Solution:
  def alienOrder(self, words: List[str]) -> str:
    # get graph
    adj, valid = self.getGraph(words)
    if not valid:
      return ''
    
    # get all chars
    chars = set()
    for w in words:
      for c in w:
        chars.add(c)
    print(chars)
    
    # build ans
    visit = {}   # key: node, value: 1=visiting 2=visited
    path = []
    for c in chars:
      if c not in visit:
        if not self.dfs(c, adj, visit, path):
          return ''
    
    return ''.join(path)

  # return false if cycle 
  def dfs(self, node, adj, visit, path)->bool:
    # base case
    if visit.get(node) == 1:
      return False
    
    if visit.get(node) == 2:
      return True

    # recursive rule
    visit[node] = 1
    for nei in adj.get(node, []):
      if not self.dfs(nei, adj, visit, path):
        return False
    visit[node] = 2
    path.append(node)
    return True

  # return false if no valid graph
  def getGraph(self, words)->bool:
    adj = defaultdict(set)
    for i in range(len(words)):
      w1 = words[i]
      for j in range(i + 1,  len(words)):
        w2 = words[j]
        # comppare each char
        k = 0
        while k < len(w1) and k < len(w2):
          c1 = w1[k]   #  e.g. a < b represent as b: [a], b depends on a
          c2 = w2[k]
          if c1 != c2:
            adj[c2].add(c1)
            break
          k += 1
        if k == len(w2) and k < len(w1):
          return [adj, False]
    print(adj)
    return [adj, True]


# test
words = ["wrt","wrf","er","ett","rftt"]
sol = Solution()
res = sol.alienOrder(words)
print(res)