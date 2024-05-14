"""
soluiton:
1. find largest element < target, say its index is i
2. then i + 1 is insert pos

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # sanity check
        if not nums or len(nums) == 0:
            return -1
        
        lo = 0
        hi = len(nums) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                hi = mid
            elif nums[mid] < target:
                lo = mid  
            else:
                hi = mid

        if nums[hi] < target: 
            return hi + 1

        if nums[lo] < target: 
            return lo + 1

        return 0
    