class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    if len(array) == 0:
      return -1

    lo = 0; hi = len(array) - 1
    while lo + 1 < hi:
      mid  = lo + (hi - lo) // 2
      if array[mid] == target:
        return mid
      if array[mid] < target:
        lo = mid
      else:
        hi = mid
    
    # post process
    return lo if abs(target - array[lo]) < abs(target - array[hi]) else hi
