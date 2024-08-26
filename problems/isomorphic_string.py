class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t): 
      return False
    
    map = {}
    map2 = {}
    
    for i in range(len(s)):
      c = s[i]
      c2 = t[i]

      if (c not in map) and (c2 not in map2):
        map[c] = c2
        map2[c2] = c
      elif map.get(c) != c2 or map2.get(c2) != c:
        return False

    return True
