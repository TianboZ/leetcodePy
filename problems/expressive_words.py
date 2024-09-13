from typing import List


class Solution:
  def expressiveWords(self, s: str, words: List[str]) -> int:
    cnt = 0
    for w in words:
      if self.check(s, w):
        cnt += 1
        
    print(cnt)
    return cnt
  
  # w1 is source, w2 is query word. return True if w2 is stretchy
  def check(self, w1, w2)->bool:
    i = 0
    j = 0
    while i < len(w1) and j < len(w2):
      c1 = w1[i]
      c2 = w2[j]
      if c1 != c2:
        return False

      # find continues same char of w1
      m = i + 1
      while m < len(w1) and w1[m] == c1:
        m += 1
      size1 = m - i
      
      n = j + 1
      while n < len(w2) and w2[n] == c1:
        n += 1
      size2 = n - j
      
      # compare size1 and size2
      if size1 > size2 and size1 < 3:
        return False
      
      if size2 > size1:
        return False
      
      # increment i, j
      i = m
      j = n
    
    return i == len(w1) and j == len(w2)

sol = Solution()
s = "heeellooo"
words = ["hello", "hi", "helo"]
sol.expressiveWords(s, words)