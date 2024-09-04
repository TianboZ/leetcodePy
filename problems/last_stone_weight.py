import heapq
from typing import List

class Node:
  def __init__(self, val):
    self.val = val

  def __lt__(self, other):
    return self.val > other.val

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    # init maxheap
    maxheap = []
    for s in stones:
      maxheap.append(Node(s))
    heapq.heapify(maxheap)

    # terminate
    while len(maxheap) >= 2:
      s1 = heapq.heappop(maxheap).val
      s2 = heapq.heappop(maxheap).val

      if s1 != s2:
        heapq.heappush(maxheap, Node(abs(s1 - s2)))
    
    if maxheap:
      return maxheap[0].val
    return 0