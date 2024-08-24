
"""
solution:
map, key is course, value is status, 1: visited, 0: visiting

"""

import collections
from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build adj graph
    adj = collections.defaultdict(list)
    for p in prerequisites:
      a, b = p
      adj[a].append(b)
    
    print(adj)
    visit = {}  # key is course, value is status, 0 is visiting, 1 is visited

    for course in range(numCourses):
      if course not in visit:
        res = self.dfs(course, visit, adj)
        # print(visit)
        if not res:
          return False

    return True

  # return false if has cycle
  def dfs(self, node, visit, adj)->bool:
    # base case
    if visit.get(node) == 0:
      return False
    
    if visit.get(node) == 1:
      return True

    # recursive rule
    visit[node] = 0  # visiting 
    for nei in adj.get(node, []):
      if not self.dfs(nei, visit, adj):
        return False
    
    visit[node] = 1   # visited
    return True
        