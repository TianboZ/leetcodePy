"""
[[4,7], [10, 11], [13,15]]
each interval no overlap. given index, remove it from cover list, then return new interval

e.g.
remove index 2
4,5,6,7,10,11,13,14,15
    |
    2

[4,5], [7,7], [10, 11], [13,15]

"""

from typing import List


class Solution:
  def remove(self, ranges: List[List[int]], targetIdx: int):
    prev = -1
    for i, r in enumerate(ranges):
      diff = r[1] - r[0]

      leftIdx = prev + 1
      rightIdx = leftIdx + diff
      prev = rightIdx

      # case 1, diff == 0
      if diff == 0 and targetIdx == leftIdx:
        ranges.pop(i)
        break

      # case 2, targetindx == leftIdx
      if diff > 0 and targetIdx == leftIdx:
        print('case 2')
        r[0] = r[0] + 1
        break

      # case 3, targetindx == rightIdx
      if diff > 0 and targetIdx == rightIdx:
        print('case 3')
        r[1] = r[1] - 1
        break

      # case 4: leftIdx < targetidx < rightIdx
      if diff  > 0 and leftIdx < targetIdx < rightIdx:
        removeItemVal = r[0] + targetIdx - leftIdx
        leftrange = [r[0], removeItemVal - 1]
        rightrange = [removeItemVal + 1, r[1]]
        ranges.pop(i)
        ranges.insert(i, rightrange)
        ranges.insert(i, leftrange)

    return ranges

sol = Solution()
arr = sol.remove([[4,7], [10, 11], [13,15], [16, 16]], 8)
print(arr)
