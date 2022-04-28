import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      pq = [] # min heap
      
      for n in nums:
        heapq.heappush(pq, n)
        if len(pq) > k:
          heapq.heappop(pq)
      
      return pq[0]
