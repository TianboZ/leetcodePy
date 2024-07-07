class Solution(object):
  def shortestWordDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    # write your solution here
    self.arr = words
    lo, hi = 0, 0
    window = {}
    minsize = 100
    
    while hi < len(self.arr):
      # handle right
      s = self.arr[hi]
      window[s] = window.get(s, 0) + 1

      if word1 == word2:
        while word1 in window  and window[word1] > 1:
          size = hi - lo
          if size < minsize:
            minsize = size

          # handle left
          s = self.arr[lo]
          window[s] -= 1
          if window[s] == 0:
            window.pop(s)

          lo += 1
        
      else:
        while word1 in window and word2 in window:
          # current window
          size = hi - lo
          if size < minsize:
            minsize = size

          # handle left
          s = self.arr[lo]
          window[s] -= 1
          if window[s] == 0:
            window.pop(s)

          lo += 1
      hi += 1
    return minsize
      