'''
classic
https://neetcode.io/problems/dijkstra

'''
import heapq
from typing import Dict, List

class Solution:
  # dedupe at generate
  def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # build grpah
    adj = {}
    for i in range(n):
        adj[i] = []
    
    for start, end, weight in edges:
        adj[start].append([end, weight])
    
    visit = {}
    heap = [[0, src]] # min heap    [total dis to node, node]
    visit[src] = 0

    while heap:
      # expand
      curr = heapq.heappop(heap)
      w1, n1 = curr

      # generate
      for n2, w2 in adj[n1]:
        dis = w1 + w2

        if n2 not in visit or dis < visit.get(n2):
          heapq.heappush(heap, [dis, n2])
          visit[n2] = dis

    for i in range(n):
      if  i not in visit:
        visit[i] = -1

    return visit

  # deduplicate at expansion
  def shortestPath2(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # build grpah
    adj = {}
    for i in range(n):
      adj[i] = []
    
    for start, end, weight in edges:
      adj[start].append([end, weight])
    
    visit = {}
    heap = [[0, src]] # min heap    [total dis to node, node]

    while heap:
      # expand
      curr = heapq.heappop(heap)
      w1, n1 = curr
      print('expand', curr)
      # deduplicate
      if n1 in visit:
        continue
      
      visit[n1] = w1

      # generate
      for n2, w2 in adj[n1]:
        dis = w1 + w2
        # each node can generate multi times
        heapq.heappush(heap, [dis, n2])

    for i in range(n):
      if i not in visit:
        visit[i] = -1

    return visit
      
# test
n=5
edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
src=0

sol = Solution()
res = sol.shortestPath(5, edges, src)
print(res)