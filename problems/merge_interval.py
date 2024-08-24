from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x: x[0])
    merged = []

    for range in intervals:
      if not merged:
        merged.append(range)
      elif merged[-1][1] >= range[0]:
        old = merged.pop()
        merged.append([old[0], max(range[1], old[1])])
      else:
        merged.append(range)

    return merged