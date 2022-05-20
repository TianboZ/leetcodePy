from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        
        while fast < len(nums):
          if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
          else:
            fast += 1
        
        print(slow)
        for i in range(slow, len(nums)):
          nums[i] = 0
        return nums

sol = Solution()
res = sol.moveZeroes([1,2,3,0,0,0,32])
print(res)