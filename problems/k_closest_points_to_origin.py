import heapq
from typing import List


class Cell:
  def __init__(self, v, cor):
    self.v = v
    self.cor = cor

  def __lt__(self, other):
    return self.v > other.v
  
class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = [] # max heap
    res = []

    for p in points:
      dis = p[0] ** 2 + p[1] ** 2
      heapq.heappush(heap, Cell(dis, p))

      if len(heap) > k:
        heapq.heappop(heap)
    
    while heap:
      res.append(heapq.heappop(heap).cor)
    
    return res

sol = Solution()
res = sol.kClosest([[3,3],[5,-1],[-2,4]], 2)
print(res)

