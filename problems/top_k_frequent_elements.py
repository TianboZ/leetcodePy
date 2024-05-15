from typing import *
import heapq

"""
step1: 
count frequency

step2:
build a min-heap of size K


complexity:
time: O(n * log k)
space O(k)

"""
class Cell:
  def __init__(self, key, val):
    self.key = key
    self.val = val

  def __lt__(self, other):
    return self.val < other.val

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    map = {}
    for n in nums:
      freq = map.get(n, 0) + 1
      map[n] = freq
    
    pq = []  # min heap

    for key, val in map.items():
      heapq.heappush(pq, Cell(key, val))
      if len(pq) > k:
        heapq.heappop(pq)

    res = []
    for i in pq:
      res.append(i.key)
    
    return res

sol = Solution()

# test
res = sol.topKFrequent([1,2,3,2,2,2,2,2,2,1,1,1,1,3,4,4,5], 3)
print(res)

