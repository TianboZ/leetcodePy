class Solution(object):
    def binarySearch(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        # sanity check
        if (not array) or len(array) == 0:
            return -1

        lo = 0
        hi = len(array) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if array[mid] == target:
                return mid
            if array[mid] > target:
                hi = mid
            else:
                lo = mid

        if array[lo] == target:
            return lo
        if array[hi] == target:
            return hi
        return -1


sol = Solution()
res = sol.binarySearch([1, 2, 3, 4, 5], 2.4)
print(res)
