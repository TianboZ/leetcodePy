"""
r1       ----
r2   --   --   --

"""

class Solution:
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0
    res = []
    while i < len(firstList) and j < len(secondList):
      r1 = firstList[i]
      r2 = secondList[j]
      
      if r2[1] < r1[0]:
        j += 1
        continue

      if r2[0] > r1[1]:
        i += 1
        continue 

      # r1, r2 is overlap
      lo = max(r1[0], r2[0])
      hi = min(r1[1], r2[1])
      res.append([lo, hi])

      if r1[1] < r2[1]:
        i += 1
        continue
      elif r1[1] > r2[1]:
        j += 1
        continue
      else:
        i += 1
        j += 1

    return res