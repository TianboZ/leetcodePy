from collections import defaultdict
from typing import List
class Solution:
  def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    # sanity check
    if not relations:
      return max(time)
    
    # build graph
    adj = defaultdict(set)
    for a, b in relations:
      adj[b].add(a) # b depends on a
      if a not in adj:
        adj[a] = set()
    
    # build time map
    self.time = {}
    for i in range(len(time)):
      self.time[i+1] = time[i]

    # topo sort
    visit = {}
    self.cache = {}
    totalTime = 0
    for task in range(1, n+1):
      if task not in visit:
        cycle, time = self.dfs(task, adj, visit)
        if cycle:
          return -1
        print('task:', task, 'total time:', time)
        totalTime = max(time, totalTime)
    return totalTime

  # return [is_cycle, time]  
  # if cycle, true. time represent total time needed 
  def dfs(self, node, adj, visit):
    if visit.get(node) == 1:
      return [True, 0]
    if visit.get(node) == 2:
      return [False, self.cache[node]]

    # recursive rule
    visit[node] = 1
    maxtime = 0
    for nei in adj.get(node, []):
      hasCycle, time = self.dfs(nei, adj, visit)
      if hasCycle:
        return [True, 0]
      maxtime = max(maxtime, time)

    # mark visted
    visit[node] = 2
    self.cache[node] = self.time[node] + maxtime
    return [False, self.time[node] + maxtime]
