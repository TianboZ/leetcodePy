from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] >= nums[lo]:
        if nums[lo] <= target < nums[mid]:
          hi = mid
        else: 
          lo = mid
      else:
        if nums[mid] < target <= nums[hi]:
          lo = mid
        else: 
          hi = mid
    
    if nums[lo] == target:
      return lo
    
    if nums[hi] == target:
      return hi
    return -1
        

sol = Solution()
arr3 = [5,6,7,1,2,3,4]
arr= [1, 0, 1, 1]
print(sol.search(arr, 1))