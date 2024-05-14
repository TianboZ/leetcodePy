"""
step1: binary search, find larget nubmer this is <= target
step: two pointers, move 
"""

class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    lo = self.helper(array, target, k)
    hi = lo + 1
    cnt = 0
    res = []

    while cnt < k and cnt < len(array):
      if lo >= 0 and hi < len(array): 
        if abs(array[lo] - target) <= abs(array[hi] - target):
          res.append(array[lo])
          lo -= 1
        else:
          res.append(array[hi])
          hi += 1
      elif lo < 0:
        res.append(array[hi])
        hi += 1
      else :
        res.append(array[lo])
        lo -= 1

      cnt += 1

    return res
    # return array[lo + 1: hi]  
  
  # find smallest element that >= target
  def helper(self, array, target, k):
    lo = 0
    hi = len(array) - 1
    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if (array[mid]) == target:
        hi = mid
      elif (array[mid]) < target:
        lo = mid
      else:
        hi = mid

    return lo


sol = Solution()
res = sol.kClosest([1,2,3], 2.1, 5)
print(res)