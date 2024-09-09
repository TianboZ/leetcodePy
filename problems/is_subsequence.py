"""
solution:
- iterate t, compare each char with s[index]
- if ==, then index += 1
- when index == len(s), s is subsequence of t

"""
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
      return True
    i = 0 # record s index
    for c in t:
      if s[i] == c:
        i += 1
        if i == len(s):
          return True
    
    return i == len(s)


        