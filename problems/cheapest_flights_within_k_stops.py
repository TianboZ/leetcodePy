from typing import List
import heapq

'''

sol1:
BFS or DFS


sol2:
dijkstra
'''
  
class Solution:
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
      cost1, city1, stops1 = curr
      print('expand: ', [cost1, city1, stops1], 'k=', k)  # we expand same node multiple times because optimial solution may not we want!

      if stops1 > k + 1:
        continue
      
      if city1 == dst and stops1 - 1 <= k:
        print('res: ', [cost1, city1, stops1], 'k=', k, 'stops1=', stops1)
        return cost1

      # generate
      neis = adj.get(city1)
      if neis:
        for nei in neis:
          city2, cost2 = nei
          heapq.heappush(heap, [cost1 + cost2, city2, stops1 + 1])
      
    return -1 

# test
sol  = Solution()
res = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
print(res)