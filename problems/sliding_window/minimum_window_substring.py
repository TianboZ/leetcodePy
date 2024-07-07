from collections import Counter


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    tLen = len(t)
    sLen = len(s)
    if tLen > sLen:
      return ''
    
    tMap = Counter(t)
    print(tMap)
    match = 0
    lo, hi = 0, 0
    window = {}
    size = 1000
    res = ''
    
    while hi < sLen:
      # handle right
      c = s[hi]
      window[c] = window.get(c, 0) + 1
      if c in tMap and window[c] == tMap.get(c):
        match += 1
      
      # handle left
      while match == len(tMap):
        # check current window
        if hi - lo < size:
          size = hi - lo
          res = s[lo: hi + 1]
          print(res)

        # shrink left bound
        c = s[lo]
        if c in window:
          window[c] -= 1
          if window[c] < tMap[c]:
            match -= 1
      
        lo += 1
      
      hi += 1
    
    print(lo, hi)
    return res