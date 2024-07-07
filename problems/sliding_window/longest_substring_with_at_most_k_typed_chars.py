class Solution(object):
  def lengthOfLongestSubstringKDistinct(self, input, k):
    """
    input: string input, int k
    return: int
    """
    # write your solution here
    window = {}
    lo, hi = 0, 0
    size = 0

    while hi < len(input):
      c = input[hi]
      window[c] = window.get(c, 0) + 1
      
      if len(window) <= k:
        size = max(size, hi - lo + 1)

      while len(window) > k:
        c = input[lo]
        if c in window:
          window[c] -= 1
          if window[c] == 0:
            window.pop(c)
        lo +=1 
      
      hi += 1

    return size