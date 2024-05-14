class Solution(object):
  def smallestElementLargerThanTarget(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array or len(array) == 0: 
      return -1
    
    lo = 0
    hi = len(array) - 1
    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if array[mid] == target:
        lo = mid + 1
      elif array[mid] < target:
        lo = mid
      else:
        hi = mid

    if array[lo] > target: return lo
    if array[hi] > target: return hi

    return -1


sol = Solution()
test1 = [[1, 2, 3, 3.3, 3.4, 10], 3.3]
test2 = [[3.4, 10], 3]

res = sol.smallestElementLargerThanTarget(test1[0], test1[1])
print('index: ', res)

res = sol.smallestElementLargerThanTarget(test2[0], test2[1])
print('index: ', res)
