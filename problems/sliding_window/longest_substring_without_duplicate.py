"""
solution:
non-fixed size sliding window

"""

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    lo, hi = 0, 0
    window = {}
    dup = 0
    size = 0
      
    while hi < len(s):
      # handle right
      c = s[hi]
      window[c] = window.get(c, 0) + 1
      if window[c] == 2:
        dup += 1

      # curent window
      if dup == 0:
        size = max(hi - lo + 1, size)
      
      while dup > 0:
        c = s[lo]
        if c in window:
          window[c] -= 1
          if window[c] == 1:
            dup -= 1
        lo += 1        
      hi += 1

    return size