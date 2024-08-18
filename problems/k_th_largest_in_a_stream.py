"""
maintain size K minheap

"""
from typing import List
import heapq

class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.k  = k
    # self.nums = nums
    self.minheap = nums
    heapq.heapify(self.minheap)
    while len(self.minheap) > k:
      heapq.heappop(self.minheap)
        

  def add(self, val: int) -> int:
    heapq.heappush(self.minheap, val)
    while len(self.minheap) > self.k:
      heapq.heappop(self.minheap)
    
    if self.minheap:
      return self.minheap[0]

    return -1