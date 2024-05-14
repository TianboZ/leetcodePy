from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sanity check
        if not arr or len(arr) == 0:
            return 

        # (lo, hi) exluding
        lo = self.helper2(arr, x) 
        hi = lo + 1

        print(lo, hi)
        cnt = 0

        while cnt < k:
            if lo >= 0 and hi < len(arr):
                if abs( arr[lo] - x) <= abs( arr[hi] - x):
                    lo -= 1
                else:
                    hi += 1
            elif lo < 0:
                hi += 1
            else:
                lo -= 1

            cnt +=1

        return arr[lo + 1: hi]

    # find smallest element >= X
    def helper(self, arr, x):
        lo = 0
        hi = len(arr) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == x:
                hi = mid
            elif arr[mid] > x:
                hi = mid
            else:
                lo = mid

        return lo
      
    #  find larget element < x
    def helper2(self, arr, x):
        lo = 0
        hi = len(arr) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == x:
                hi = mid
            elif arr[mid] > x:
                hi = mid
            else:
                lo = mid

        if arr[hi] < x: return hi
        if arr[lo] < x: return lo
        return -1
        


sol =  Solution()
res = sol.findClosestElements([1,2,3,4,5], 4, 3)
print(res)