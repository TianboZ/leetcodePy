class Solution(object):
  def longest(self, input, k):
    """
    input: string input, int k
    return: string
    """
    # write your solution here
    lo, hi = 0, 0
    window = {}
    cnt = 0
    size = 0
    res = ''
    
    while hi < len(input):
      # handle right
      c = input[hi]
      window[c] = window.get(c, 0) + 1

      # current window
      if len(window) == k:
        if hi - lo + 1 > size:
          size = hi - lo + 1
          res = input[lo: hi + 1]

      # handle left
      while len(window) > k:
        c = input[lo]
        window[c] -= 1
        if window[c] == 0:
          window.pop(c)
        lo += 1    
      hi += 1

    return res