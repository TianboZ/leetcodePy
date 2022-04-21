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
    i = 0
    
    while i < k:
      if lo >= 0 and hi < len(array) and abs(array[lo] - target) <= abs(array[hi] - target):
        lo -= 1
      elif lo >= 0 and hi < len(array) and abs(array[lo] - target) > abs(array[hi] - target):
        hi += 1
      elif lo < 0:
        hi += 1
      else:
        lo -= 1

      i += 1

    return array[lo + 1: hi]  
  
  def helper(self, array, target, k):
    lo = 0
    hi = len(array) - 1
    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if (array[mid]) == target:
        lo = mid
      elif (array[mid]) < target:
        lo = mid
      else:
        hi = mid

    return lo


sol = Solution()
res = sol.kClosest([1,2,3], 2.1, 2)
print(res)