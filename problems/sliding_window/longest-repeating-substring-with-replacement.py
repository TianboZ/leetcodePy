class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    window = {}
    lo, hi = 0, 0
    maxSize = 0

    while hi < len(s):
      c = s[hi]
      window[c] = window.get(c, 0) + 1
      currSize = hi - lo + 1
      if currSize - max(window.values()) <= k:
        maxSize = max(maxSize, currSize)
      
      while hi - lo + 1 - max(window.values()) > k:
        c = s[lo]    
        if c in window:
          window[c] -= 1 
        lo += 1
      
      hi += 1
        
    return maxSize   