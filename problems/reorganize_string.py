from collections import Counter
import heapq


class Solution:
  def reorganizeString(self, s: str) -> str:
    maxheap = []
    map = Counter(s)
    for k, v in map.items():
      maxheap.append([-v, k])  # [freq, value]
    heapq.heapify(maxheap)
    prev = None #  [freq, value]
    res = []

    while maxheap or prev:
      # terminate 
      if prev and not maxheap:
        return ""
      
      curr = heapq.heappop(maxheap)
      # add prev item back to heap right after pop 
      if prev:
        heapq.heappush(maxheap, prev)
        prev = None
      
      cnt, val = curr
      cnt += 1 # decreament freq 
      res.append(val)

      if cnt:
        prev = [cnt, val]
    return ''.join(res)
  
sol = Solution()
res = sol.reorganizeString('aab')
print(res)