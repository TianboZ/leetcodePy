import heapq
from typing import Dict, List


"""
complexity:

time:
N nodes => N^2 edges

O(N^2 * log(N^2)) = O(N ^2 * log(N))

space:
O(N^2)

"""

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    adj = {}  # node: [[dis, node], [dis2, node2], ...]
    self.getGraph(adj, points)
    print(adj)
    
    # prim algo
    visit = set()
    cost = 0

    # initial
    heap = [[0, 0]] 
    print(heap)

    # terminate
    while heap:
      # expand
      curr = heapq.heappop(heap)
      print('expand, ', curr)
      dis, node = curr

      if node in visit:
        continue

      visit.add(node)  # mark visit when generating
      cost += dis

      if len(visit) == len(points):
        break

      # generate
      for nei in adj.get(node, []):
        dis2, node2  = nei
        heapq.heappush(heap, [dis2, node2])

    print('cost = ', cost)
    return cost
  
  def getGraph(self, adj: Dict, points):
    for i in range(len(points)):
      neis = []
      for j in range(len(points)):
        if i == j:
          continue
        
        dis = abs(points[i][0] - points[j][0] ) + abs(points[i][1] - points[j][1] ) 
        neis.append([dis, j])
      adj[i] = neis  




sol = Solution()
points =[[0,0],[2,2],[3,10],[5,2],[7,0]]
sol.minCostConnectPoints(points)