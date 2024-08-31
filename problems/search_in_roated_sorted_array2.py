from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo + 1 < hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] == target:
        return mid
      
      if nums[mid] == nums[hi]:
        hi -= 1
        continue
      
      if nums[mid] >= nums[lo]:
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
arr3 = [5,6,7,1,1,1,1,1,1,2,2,2,2,2,3,4]
print(sol.search(arr3, 1))