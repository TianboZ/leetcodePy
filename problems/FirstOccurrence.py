class Solution(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if (not array) or len(array) == 0:
      return -1

    lo = 0; hi = len(array) - 1;
    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if target == array[mid]:
        hi = mid
      elif target < array[mid]:
        hi = mid
      else:
        lo = mid

    if array[lo] == target:
      return lo

    if array[hi] == target:
      return hi
    
    return -1