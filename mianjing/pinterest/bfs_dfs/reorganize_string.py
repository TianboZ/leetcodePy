"""
question:
given arr = [a, a, a, b, b, c, c..], 相邻不一样
LC 767


solution:
- find freq of each char
- sort them by freq, and use most freq char to build string
  - repeatly do this, until all chars are used 

a: 4
b: 2
c: 1
"""
from collections import Counter
import heapq

class Solution:
  def reorganizeString(self, s: str) -> str:
    maxheap = []
    map = Counter(s)
    for k, v in map.items():
      maxheap.append([-v, k])  # [freq, value]
    heapq.heapify(maxheap)
    res = []

    # terminate 
    while maxheap:
      curr1 = heapq.heappop(maxheap)
      freq1, val1 = curr1
      
      if not res or res[-1] != val1:
        # prev char is diff from current one
        res.append(val1)
        if freq1 + 1 != 0:
          heapq.heappush(maxheap, [freq1 + 1, val1])
      else:
        # try next most freq char
        if not maxheap:
          # return '' # invalid 
          break # invalid, then we find longest valid part
        
        curr2 = heapq.heappop(maxheap)
        freq2, val2 = curr2
        
        res.append(val2)
        if freq2 + 1 != 0:
          heapq.heappush(maxheap, [freq2 + 1, val2])
          
        # add curr1 back to heap
        heapq.heappush(maxheap, curr1)
    
    print(res)
    return ''.join(res)
      
  
sol = Solution()
res = sol.reorganizeString('aabbbb')
print(res)