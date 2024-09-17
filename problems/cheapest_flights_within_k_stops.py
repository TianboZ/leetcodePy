from typing import List
import heapq

  
"""
solution1:
depth limited DFS

"""
from collections import defaultdict
import math
class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    self.src = src
    self.dst = dst
    # build graph
    adj = defaultdict(list)
    for ticket in flights:
      a, b, cost  = ticket
      adj[a].append([b, cost])
    
    # traverse graph
    visit = set()
    self.k = k
    self.res = math.inf
    self.dfs(src, adj, [], visit)

    if self.res == math.inf:
      return -1
    return self.res

  def dfs(self, node, adj, path, visit):
    # base case
    if node in visit:
      return
    
    if len(path) > self.k + 1:
      # over max depth limited
      return
    
    # recursive rule
    visit.add(node)

    if node == self.dst:
      # find destination
      print(path)
      visit.remove(node)
      # update global min cost
      self.res = min(self.res, sum(path))
      return

    for nei in adj.get(node, []):
      next, cost = nei
      path.append(cost)
      self.dfs(next, adj, path, visit)
      path.pop() # back tracking

    visit.remove(node) # back tracking

'''
sol2:
dijkstra
'''
class Solution2:
  # TLE, no dedup
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # build graph
    adj = {}
    for start, end, p in flights:
      neis = adj.get(start, [])
      adj[start] = neis
      neis.append([end, p])  # [city, cost]

    # initial
    heap = [] # min heap
    heapq.heappush(heap, [0, src, 0])  # [cost, city, stops]
  
    # terminate
    while heap:
      # expand
      curr = heapq.heappop(heap)
      cost1, n1, stops1 = curr
      print('expand: ', [cost1, n1, stops1], 'k=', k)  # we expand same node multiple times because optimial solution may not we want!

      if stops1 > k + 1:
        continue
      
      if n1 == dst and stops1 - 1 <= k:
        print('res: ', [cost1, n1, stops1], 'k=', k, 'stops1=', stops1)
        return cost1

      # generate
      neis = adj.get(n1)
      if neis:
        for nei in neis:
          n2, cost2 = nei
          heapq.heappush(heap, [cost1 + cost2, n2, stops1 + 1])
      
    return -1 

  # with dedup
  def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # build graph
    adj = defaultdict(list)
    for a, b, nextCost in flights:
      adj[a].append([b, nextCost]) # <node, [ [n2, cost2], [n3, cost3]... ]>
    visit = {} # <(node, stop), min cost to this node>
    
    # init
    minheap = [[0, src, 0]] # [cost, node, stops]
    visit[(src, 0)] = 0
    
    # terminate
    while minheap:
      # expand
      curr = heapq.heappop(minheap)
      cost1, n1, stops1 = curr

      if n1 == dst and stops1 - 1 <= k:
        return cost1
      
      # If we've made more than k stops, skip this path
      if stops1 > k:
        continue
      
      # generate
      for nei in adj.get(n1, []):
        n2, cost2 = nei
        nextCost = cost1 + cost2
        nextStop = stops1 + 1
        if (n2, nextStop) not in visit or nextCost < visit[(n2, nextStop)] :
          visit[(n2, nextStop)] = nextCost
          heapq.heappush(minheap, [nextCost, n2, nextStop])
        
    return -1

# test
sol  = Solution2()
res = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
print(res)