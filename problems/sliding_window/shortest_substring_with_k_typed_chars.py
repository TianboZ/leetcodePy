class Solution(object):
  def shortest(self, input, k):
    """
    input: string input, int k
    return: string
    """
    # write your solution here
    lo, hi = 0, 0
    window = {}
    size = 1000
    res = ''
    
    while hi < len(input):
      # handle right
      c = input[hi]
      window[c] = window.get(c, 0) + 1

      # handle left
      while len(window) == k:
        # current window
        if hi - lo + 1 < size:
          size = hi - lo + 1
          res = input[lo: hi + 1]

        c = input[lo]
        window[c] -= 1
        if window[c] == 0:
          window.pop(c)
        lo += 1    
      hi += 1

    return res