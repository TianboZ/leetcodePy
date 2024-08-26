import collections
import heapq

class Pair:
  def __init__(self, word, freq):
    self.w = word
    self.f = freq
  def __lt__(self, other):
    if self.f == other.f:
      return self.w > other.w
    return self.f < other.f

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    map = collections.Counter(words)
    minheap = []
    
    for w, freq in map.items():
      heapq.heappush(minheap, Pair(w, freq))
      if len(minheap) > k:
        heapq.heappop(minheap)
    
    # build ans
    res = []
    # minheap.sort(reverse=True)
    while minheap:
      item = heapq.heappop(minheap)
      res.append(item.w)
    res.reverse()
    
    return res
        