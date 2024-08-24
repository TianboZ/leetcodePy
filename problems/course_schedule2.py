from typing import List
import collections

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # build adj list
    adj = collections.defaultdict(list)
    for p in prerequisites:
      a, b = p
      adj[a].append(b)

    visit = {} # <course, state>   state=1: visting   state=2: visited
    
    path = []
    
    for c in range(numCourses):
      if (c not in visit):
        if not self.topo(adj, visit, c, path):
          return []
    return path

  # return false if has cycle
  def topo(self, adj, visit, node, path) -> bool:
    #  base case
    if visit.get(node) == 1:
      # cycle
      return False
    if visit.get(node) == 2:
      return True

    # recursive rule
    visit[node] = 1   # visiting
    for nei in adj.get(node, []):
      if not self.topo(adj, visit, nei, path):
        return False
    visit[node] = 2    # visiting
    path.append(node)
    return True

        