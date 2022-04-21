from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		lo = 0
		hi = len(nums) - 1
		while (lo + 1 < hi):
			mid = lo + (hi - lo) // 2
			if nums[mid] == target:
				return mid
			if nums[mid] < target:
				lo = mid
			else:
				hi = mid

		if nums[lo] == target:
			return lo
		if nums[hi] == target:
			return hi
		return -1

sol = Solution()
res = sol.search([1, 2, 3, 4, 5], 2.4)
print(res)
