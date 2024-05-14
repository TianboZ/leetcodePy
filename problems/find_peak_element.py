'''
this solution just find any peak, if there are multiple peaks, like moutain, they 
not able to find them all
'''

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: 
            return -1
        lo = 0
        hi = len(nums) - 1

        while lo + 1< hi:
            mid = lo + (hi - lo) //2
            if nums[mid] == nums[mid - 1]:
                lo = mid
            elif nums[mid] > nums[mid - 1]:
                lo = mid
            else:
                hi = mid

        return lo if nums[lo] > nums[hi] else hi