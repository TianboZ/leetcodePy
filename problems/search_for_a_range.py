class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # sanity check
        if not nums or len(nums) == 0:
            return [-1, -1]

        lo = self.first(nums, target)
        hi = self.last(nums, target)

        return [lo, hi]

    def first(self, nums, target):
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

        if nums[lo] == target:
            return lo
        
        if nums[hi] == target:
            return hi
        
        return -1
        
    def last(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                lo = mid
            elif nums[mid] < target:
                lo = mid
            else:
                hi = mid
        
        if nums[hi] == target:
            return hi

        if nums[lo] == target:
            return lo
        
        return -1