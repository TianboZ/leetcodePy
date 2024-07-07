from collections import Counter
from typing import List


class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    sLen = len(s)
    pLen = len(p)
    pMap = Counter(p)
    # print('pmap', pMap)
    fast = 0
    slow = 0
    window = {} # record elements in window, [slow, fast]
    res = []
    
    if pLen > sLen:
      return []
    
    
    while fast < sLen:
      # handle right
      curr = s[fast]
      window[curr] = window.get(curr, 0) + 1

      # handle left
      if fast - slow >= pLen:
        tmp = s[slow]
        if window.get(tmp) == 1:
          window.pop(tmp) 
        if tmp in window and window.get(tmp) > 1:
          window[tmp] = window[tmp] - 1
        slow += 1

      # check window
      print('pmap', pMap, 'window', window )
      if window == pMap:
        res.append(fast - pLen + 1)

      fast += 1 

    print(res)
    return res
  
sol = Solution()
sol.findAnagrams("abcabcdsadbca", "abc")