import heapq
from typing import List

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    minheap = [] # min heap
    
    for n in nums:
      heapq.heappush(minheap, n)
      if len(minheap) > k:
        heapq.heappop(minheap)
    
    return minheap[0]
