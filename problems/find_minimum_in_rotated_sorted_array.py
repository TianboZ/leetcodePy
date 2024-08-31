class Solution:
  def findMin(self, nums: List[int]) -> int:
    lo = 0 
    hi = len(nums) - 1

    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2

      # not rotated
      if nums[lo] < nums[mid] < nums[hi]:
        return nums[lo]

      # rotated 
      if nums[mid] > nums[lo]:
        lo = mid
      else:
        hi = mid

    if nums[lo] < nums[hi]:
      return nums[lo]

    return nums[hi]